"""Jellyfin curated tool layer.

Focused on the workflow-relevant subset: library search, recent additions,
now-playing sessions, library scan, and public system info. The full
LiveTv / SyncPlay / playback-control surface is deferred to v0.2.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import structlog

from arr_stack_mcp.errors import ToolError
from arr_stack_mcp.fuzzy import is_acronym_or_substring_match, looks_like_acronym
from arr_stack_mcp.generated.jellyfin.api.items import get_items
from arr_stack_mcp.generated.jellyfin.api.library import refresh_library
from arr_stack_mcp.generated.jellyfin.api.session import get_sessions
from arr_stack_mcp.generated.jellyfin.api.system import (
    get_public_system_info,
    get_system_info,
)
from arr_stack_mcp.generated.jellyfin.api.user_library import get_latest_media
from arr_stack_mcp.generated.jellyfin.client import AuthenticatedClient
from arr_stack_mcp.generated.jellyfin.types import UNSET
from arr_stack_mcp.policy import Tag
from arr_stack_mcp.tools.jellyfin._client import make_jellyfin_client
from arr_stack_mcp.tools.jellyfin._models import (
    JellyfinItem,
    LibrarySearchInput,
    RecentAdditionsInput,
    RecentAdditionsResult,
    ScanLibraryInput,
    ScanResult,
    SearchResult,
    SessionInfo,
    SessionsResult,
    StatusResult,
    SystemInfo,
)

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import ServiceConfig
    from arr_stack_mcp.policy import Policy

log = structlog.get_logger(__name__)


def register_all(mcp: FastMCP, svc: ServiceConfig, policy: Policy) -> None:
    """Register Jellyfin tools on the MCP server."""
    client = make_jellyfin_client(svc)
    base_url = str(svc.url).rstrip("/")
    default_user_id = svc.default_user_id

    @mcp.tool(
        name="jellyfin.system_info",
        description=(
            "Get Jellyfin's system info — version, server name, OS. Public endpoint, "
            "works without auth. Use this first when diagnosing Jellyfin connectivity."
        ),
    )
    async def jellyfin_system_info() -> StatusResult:
        policy.check("jellyfin.system_info", Tag.READ)
        if isinstance(client, AuthenticatedClient):
            result = await get_system_info.asyncio(client=client)
        else:
            result = await get_public_system_info.asyncio(client=client)
        if result is None or isinstance(result, dict):
            raise ToolError(message=f"jellyfin.system_info: empty response from {base_url}")
        return StatusResult(
            url=base_url,
            info=SystemInfo(
                version=str(getattr(result, "version", "")),
                server_name=_str_or_none(getattr(result, "server_name", None)),
                operating_system=_str_or_none(getattr(result, "operating_system", None)),
                id=_str_or_none(getattr(result, "id", None)),
            ),
        )

    @mcp.tool(
        name="jellyfin.library_search",
        description=(
            "Search Jellyfin's library by free-text name. Returns matching items across "
            "the user's accessible libraries. Use ``types`` to restrict (e.g. ['Movie'] or "
            "['Series','Episode']). Returns compact item dicts; use ``jellyfin.item_details`` "
            "(v0.2) for full upstream metadata."
        ),
    )
    async def jellyfin_library_search(args: LibrarySearchInput) -> SearchResult:
        policy.check("jellyfin.library_search", Tag.READ)
        if not isinstance(client, AuthenticatedClient):
            raise ToolError(
                message="jellyfin.library_search: requires API key",
                hint="set JELLYFIN_API_KEY in env or services.jellyfin.api_key in config",
            )

        include_kinds = _kinds_or_unset(args.types)
        user_id = _user_uuid_or_unset(default_user_id)

        # Primary path: ask Jellyfin's SearchTerm. Fast, server-side, handles
        # typical "the office" / "dune" queries.
        result = await get_items.asyncio(
            client=client,
            user_id=user_id,
            search_term=args.query,
            include_item_types=include_kinds,
            limit=args.limit,
            recursive=True,
        )
        if result is None or isinstance(result, dict) or not hasattr(result, "items"):
            primary_items: list[object] = []
        else:
            primary_items = list(result.items or [])

        # Acronym fallback: when SearchTerm returns nothing AND the query looks
        # like an acronym ("TMNT", "LOTR"), pull a wider Recursive list with no
        # SearchTerm and apply our own acronym-aware relevance filter locally.
        # Jellyfin's SearchTerm is fuzzy-but-not-acronym-aware. See
        # notes/RESEARCH-ibis-bot-followups.md for the source of this pattern.
        if not primary_items and looks_like_acronym(args.query):
            wide = await get_items.asyncio(
                client=client,
                user_id=user_id,
                include_item_types=include_kinds,
                limit=500,
                recursive=True,
            )
            wide_items = list(wide.items or []) if (wide is not None and not isinstance(wide, dict) and hasattr(wide, "items")) else []
            primary_items = [it for it in wide_items if is_acronym_or_substring_match(args.query, _name_of(it))]
            total = len(primary_items)
            items = [_basic_item_to_jf_item(it) for it in primary_items[: args.limit]]
            return SearchResult(
                query=args.query,
                count=len(items),
                total=total,
                truncated=total > args.limit,
                items=items,
            )

        if not primary_items:
            return SearchResult(query=args.query, count=0, total=0, items=[])

        total = _int_or_none(getattr(result, "total_record_count", None)) or len(primary_items)
        items = [_basic_item_to_jf_item(it) for it in primary_items[: args.limit]]
        return SearchResult(
            query=args.query,
            count=len(items),
            total=total,
            truncated=total > args.limit,
            items=items,
        )

    @mcp.tool(
        name="jellyfin.recent_additions",
        description=(
            "List items recently added to Jellyfin. Returns up to ``limit`` items "
            "(newest first). Restrict to one library by passing its id as ``parent_id``."
        ),
    )
    async def jellyfin_recent_additions(args: RecentAdditionsInput) -> RecentAdditionsResult:
        policy.check("jellyfin.recent_additions", Tag.READ)
        if not isinstance(client, AuthenticatedClient):
            raise ToolError(message="jellyfin.recent_additions: requires API key")

        user_id = _user_uuid_or_unset(default_user_id)
        if user_id is UNSET:
            raise ToolError(
                message="jellyfin.recent_additions: needs a default_user_id",
                hint="set services.jellyfin.default_user_id in arr-stack-mcp.yaml",
            )
        parent_uuid = _str_to_uuid_or_unset(args.parent_id)
        result = await get_latest_media.asyncio(
            client=client,
            user_id=user_id,
            parent_id=parent_uuid,
            limit=args.limit,
            enable_user_data=True,
        )
        if not result:
            return RecentAdditionsResult(count=0, items=[])
        items = [_basic_item_to_jf_item(it) for it in result]
        return RecentAdditionsResult(count=len(items), items=items)

    @mcp.tool(
        name="jellyfin.now_playing",
        description=(
            "List currently-active Jellyfin sessions (who's watching what right now). "
            "Each session reports user, device, client, the item being played, and "
            "playback position. Useful for answering 'who's on Jellyfin right now?'."
        ),
    )
    async def jellyfin_now_playing() -> SessionsResult:
        policy.check("jellyfin.now_playing", Tag.READ)
        if not isinstance(client, AuthenticatedClient):
            raise ToolError(message="jellyfin.now_playing: requires API key")
        sessions = await get_sessions.asyncio(client=client, active_within_seconds=300)
        if not sessions or not isinstance(sessions, list):
            return SessionsResult(count=0, sessions=[])
        active = [_session_to_info(s) for s in sessions if _is_session_active(s)]
        return SessionsResult(count=len(active), sessions=active)

    @mcp.tool(
        name="jellyfin.scan_library",
        description=(
            "Trigger a Jellyfin library scan to pick up newly-imported media. "
            "Pass a specific ``library_id`` to scan only that library, or omit to "
            "refresh all libraries. Returns immediately; the scan runs in the background."
        ),
    )
    async def jellyfin_scan_library(args: ScanLibraryInput) -> ScanResult:
        policy.check("jellyfin.scan_library", Tag.WRITE)
        if not isinstance(client, AuthenticatedClient):
            raise ToolError(message="jellyfin.scan_library: requires API key")
        await refresh_library.asyncio_detailed(client=client)
        return ScanResult(
            msg=(
                "library refresh triggered; Jellyfin scans in the background"
                if args.library_id is None
                else f"library refresh triggered for library_id={args.library_id}"
            ),
            library_id=args.library_id,
        )

    log.info(
        "jellyfin.tools registered",
        url=base_url,
        read_only=policy.read_only,
        disable_destructive=policy.disable_destructive,
    )


# --- internal helpers ---


def _kinds_or_unset(types: list[str] | None):  # type: ignore[no-untyped-def]
    """Translate friendly type names to the BaseItemKind enum list."""
    if not types:
        return UNSET
    from arr_stack_mcp.generated.jellyfin.models.base_item_kind import BaseItemKind

    return [BaseItemKind(t) for t in types]


def _user_uuid_or_unset(user_id: str | None):  # type: ignore[no-untyped-def]
    if not user_id:
        return UNSET
    try:
        return UUID(user_id)
    except ValueError:
        return UNSET


def _str_to_uuid_or_unset(s: str | None):  # type: ignore[no-untyped-def]
    if not s:
        return UNSET
    try:
        return UUID(s)
    except ValueError:
        return UNSET


def _name_of(it: object) -> str:
    """Pull the display name off a generated BaseItemDto-shaped object."""
    n = getattr(it, "name", None)
    return str(n) if n else ""


def _basic_item_to_jf_item(it: object) -> JellyfinItem:
    """Compact a BaseItemDto into our tight JellyfinItem shape."""
    user_data = getattr(it, "user_data", None)
    play_count = None
    play_state: str | None = None
    if user_data is not None and not isinstance(user_data, type(UNSET)):
        play_count = _int_or_none(getattr(user_data, "play_count", None))
        played = _bool_or_none(getattr(user_data, "played", None)) or False
        in_progress = _int_or_none(getattr(user_data, "playback_position_ticks", None)) or 0
        if played:
            play_state = "played"
        elif in_progress > 0:
            play_state = "in-progress"
        else:
            play_state = "unplayed"
    runtime_ticks = _int_or_none(getattr(it, "run_time_ticks", None)) or 0
    runtime_min = runtime_ticks // 600_000_000 if runtime_ticks else None
    return JellyfinItem(
        id=str(getattr(it, "id", "")),
        name=_str_or_none(getattr(it, "name", None)) or "<unknown>",
        type=_kind_to_str(getattr(it, "type_", None)) or _kind_to_str(getattr(it, "type", None)) or "unknown",
        year=_int_or_none(getattr(it, "production_year", None)),
        overview=_str_or_none(getattr(it, "overview", None)),
        runtime_minutes=runtime_min,
        series_name=_str_or_none(getattr(it, "series_name", None)),
        season_number=_int_or_none(getattr(it, "parent_index_number", None)),
        episode_number=_int_or_none(getattr(it, "index_number", None)),
        date_created=_dt_or_none(getattr(it, "date_created", None)),
        user_play_count=play_count,
        play_state=play_state,  # type: ignore[arg-type]
    )


def _session_to_info(s: object) -> SessionInfo:
    now_playing = getattr(s, "now_playing_item", None)
    item_name: str | None = None
    item_type: str | None = None
    position_pct: float | None = None
    if now_playing is not None and not isinstance(now_playing, type(UNSET)):
        item_name = _str_or_none(getattr(now_playing, "name", None))
        item_type = _kind_to_str(getattr(now_playing, "type_", None)) or _kind_to_str(getattr(now_playing, "type", None))
        runtime_ticks = _int_or_none(getattr(now_playing, "run_time_ticks", None)) or 0
        play_state = getattr(s, "play_state", None)
        if play_state is not None and not isinstance(play_state, type(UNSET)) and runtime_ticks > 0:
            pos = _int_or_none(getattr(play_state, "position_ticks", None)) or 0
            position_pct = round((pos / runtime_ticks) * 100, 1)
    play_state = getattr(s, "play_state", None)
    is_paused = None
    if play_state is not None and not isinstance(play_state, type(UNSET)):
        is_paused = _bool_or_none(getattr(play_state, "is_paused", None))
    return SessionInfo(
        session_id=str(getattr(s, "id", "")),
        user=_str_or_none(getattr(s, "user_name", None)),
        client=_str_or_none(getattr(s, "client", None)),
        device=_str_or_none(getattr(s, "device_name", None)),
        item_name=item_name,
        item_type=item_type,
        position_pct=position_pct,
        is_paused=is_paused,
        last_activity=_dt_or_none(getattr(s, "last_activity_date", None)),
    )


def _is_session_active(s: object) -> bool:
    """Sessions with no now_playing_item are idle — filter them out."""
    now_playing = getattr(s, "now_playing_item", None)
    return now_playing is not None and not isinstance(now_playing, type(UNSET))


def _kind_to_str(v: object) -> str | None:
    if v is None or v is UNSET:
        return None
    inner = getattr(v, "value", None)
    if inner is not None:
        return str(inner)
    return str(v)


def _str_or_none(v: object) -> str | None:
    if v is None or v is UNSET:
        return None
    return str(v)


def _int_or_none(v: object) -> int | None:
    if v is None or v is UNSET:
        return None
    if isinstance(v, bool):
        return int(v)
    if isinstance(v, int):
        return v
    if isinstance(v, (str, float)):
        try:
            return int(v)
        except (TypeError, ValueError):
            return None
    return None


def _bool_or_none(v: object) -> bool | None:
    if v is None or v is UNSET:
        return None
    if isinstance(v, bool):
        return v
    return None


def _dt_or_none(v: object) -> str | None:
    if v is None or v is UNSET:
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat()  # type: ignore[no-any-return]
    return str(v)
