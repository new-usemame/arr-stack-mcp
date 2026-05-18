"""Lidarr curated tool layer. Mirrors Sonarr/Radarr at the artist + album grain."""

from __future__ import annotations

from typing import TYPE_CHECKING

import structlog

from arr_stack_mcp.errors import ToolError
from arr_stack_mcp.fuzzy import normalize
from arr_stack_mcp.generated.lidarr.api.album import get_api_v1_album
from arr_stack_mcp.generated.lidarr.api.artist import (
    delete_api_v1_artist_id,
    get_api_v1_artist,
    get_api_v1_artist_id,
    post_api_v1_artist,
)
from arr_stack_mcp.generated.lidarr.api.artist_lookup import get_api_v1_artist_lookup
from arr_stack_mcp.generated.lidarr.api.queue import get_api_v1_queue
from arr_stack_mcp.generated.lidarr.api.system import get_api_v1_system_status
from arr_stack_mcp.generated.lidarr.models import ArtistResource
from arr_stack_mcp.generated.lidarr.models.add_artist_options import AddArtistOptions
from arr_stack_mcp.generated.lidarr.types import UNSET
from arr_stack_mcp.policy import Tag, fingerprint
from arr_stack_mcp.tools.lidarr._client import make_lidarr_client
from arr_stack_mcp.tools.lidarr._models import (
    AddResult,
    AlbumsResult,
    AlbumSummary,
    ArtistAddInput,
    ArtistAlbumsInput,
    ArtistDeleteInput,
    ArtistLookupInput,
    ArtistSearchInput,
    ArtistSummary,
    DeletePlan,
    DeleteResult,
    LookupResult,
    QueueInput,
    QueueItem,
    QueueResult,
    SearchResult,
    StatusResult,
    SystemStatus,
)

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import ServiceConfig
    from arr_stack_mcp.policy import Policy

log = structlog.get_logger(__name__)


def register_all(mcp: FastMCP, svc: ServiceConfig, policy: Policy) -> None:
    """Register every Lidarr tool on the given MCP server."""
    client = make_lidarr_client(svc)
    base_url = str(svc.url).rstrip("/")

    @mcp.tool(
        name="lidarr.system_status",
        description=(
            "Get Lidarr's system status (version, branch, runtime). "
            "Use this first when diagnosing any Lidarr problem. Mirrors ``sonarr.system_status``."
        ),
    )
    async def lidarr_system_status() -> StatusResult:
        policy.check("lidarr.system_status", Tag.READ)
        result = await get_api_v1_system_status.asyncio(client=client)
        if result is None:
            raise ToolError(message=f"lidarr.system_status: empty response from {base_url}")
        return StatusResult(
            url=base_url,
            status=SystemStatus(
                version=str(result.version or ""),
                branch=_str_or_none(result.branch),
                runtime_version=_str_or_none(result.runtime_version),
                is_production=_bool_or_none(result.is_production),
                is_admin=_bool_or_none(result.is_admin),
                is_docker=_bool_or_none(result.is_docker),
                start_time=_dt_or_none(result.start_time),
                instance_name=_str_or_none(result.instance_name),
            ),
        )

    @mcp.tool(
        name="lidarr.artist_search",
        description=(
            "Search Lidarr's existing library (already-added artists) by free-text name. "
            "Returns ranked candidates with Lidarr ids and MusicBrainz ids. "
            "Use ``lidarr.artist_lookup`` to discover artists that AREN'T already added."
        ),
    )
    async def lidarr_artist_search(args: ArtistSearchInput) -> SearchResult:
        policy.check("lidarr.artist_search", Tag.READ)
        artists = await get_api_v1_artist.asyncio(client=client)
        if artists is None:
            return SearchResult(query=args.query, count=0, total=0, items=[])
        q_norm = normalize(args.query)
        matches: list[ArtistResource] = [a for a in artists if q_norm in normalize(_str_or_none(a.artist_name) or "")]
        total = len(matches)
        items = [_artist_to_summary(a) for a in matches[: args.limit]]
        return SearchResult(
            query=args.query,
            count=len(items),
            total=total,
            truncated=total > args.limit,
            items=items,
        )

    @mcp.tool(
        name="lidarr.artist_lookup",
        description=(
            "Search MusicBrainz through Lidarr to find artists that could be ADDED to the library. "
            "Each candidate's ``foreign_artist_id`` (the MusicBrainz mbid) is what "
            "``lidarr.artist_add`` expects."
        ),
    )
    async def lidarr_artist_lookup(args: ArtistLookupInput) -> LookupResult:
        policy.check("lidarr.artist_lookup", Tag.READ)
        results = await get_api_v1_artist_lookup.asyncio(client=client, term=args.query)
        if not results:
            return LookupResult(query=args.query, candidates=[])
        candidates = [_artist_to_summary(r) for r in results[: args.limit]]
        return LookupResult(query=args.query, candidates=candidates)

    @mcp.tool(
        name="lidarr.artist_albums",
        description=(
            "List every album under one Lidarr artist. Use this when the user asks "
            "'what albums do I have by X?' — find the artist via ``lidarr.artist_search`` first, "
            "then pass its ``lidarr_id`` here."
        ),
    )
    async def lidarr_artist_albums(args: ArtistAlbumsInput) -> AlbumsResult:
        policy.check("lidarr.artist_albums", Tag.READ)
        albums = await get_api_v1_album.asyncio(client=client, artist_id=args.lidarr_id)
        if not albums:
            return AlbumsResult(artist_lidarr_id=args.lidarr_id, count=0, items=[])
        if args.monitored_only:
            albums = [a for a in albums if _bool_or_none(a.monitored)]
        items = [_album_to_summary(a) for a in albums]
        return AlbumsResult(artist_lidarr_id=args.lidarr_id, count=len(items), items=items)

    @mcp.tool(
        name="lidarr.queue",
        description="List active Lidarr downloads with progress, ETA, and download client.",
    )
    async def lidarr_queue(args: QueueInput) -> QueueResult:
        policy.check("lidarr.queue", Tag.READ)
        page = await get_api_v1_queue.asyncio(
            client=client,
            page=1,
            page_size=args.limit,
            include_artist=True,
            include_album=True,
        )
        if page is None or page.records is None or isinstance(page.records, type(UNSET)):
            return QueueResult(count=0, total=0, items=[])
        records = list(page.records)  # type: ignore[arg-type]
        items = [_queue_record_to_item(r) for r in records]
        total = _int_or_none(page.total_records) or len(items)
        return QueueResult(count=len(items), total=total, items=items)

    @mcp.tool(
        name="lidarr.artist_add",
        description=(
            "Add a new artist to Lidarr by MusicBrainz id. Call ``lidarr.artist_lookup`` first "
            "to obtain the ``foreign_artist_id``. Omit ``quality_profile_id``, "
            "``metadata_profile_id``, and ``root_folder_path`` to use Lidarr's defaults. "
            "Idempotent on already-added artists."
        ),
    )
    async def lidarr_artist_add(args: ArtistAddInput) -> AddResult:
        policy.check("lidarr.artist_add", Tag.WRITE)

        # Lidarr's generated client expects a UUID for the mbid query param.
        from uuid import UUID

        try:
            mbid = UUID(args.foreign_artist_id)
        except ValueError as e:
            raise ToolError(
                message=f"lidarr.artist_add: invalid MusicBrainz id {args.foreign_artist_id!r}",
                hint="MusicBrainz ids are UUIDs (e.g. 5b11f4ce-a62d-471e-81fc-a69a8278c7da)",
            ) from e
        existing = await get_api_v1_artist.asyncio(client=client, mb_id=mbid)
        if existing:
            row = existing[0]
            lid = _int_or_none(row.id)
            if lid is not None:
                return AddResult(
                    lidarr_id=lid,
                    foreign_artist_id=args.foreign_artist_id,
                    name=_str_or_none(row.artist_name) or "<unknown>",
                    already_added=True,
                    msg=f"already in library as lidarr_id={lid}",
                )

        lookup = await get_api_v1_artist_lookup.asyncio(client=client, term=f"lidarr:{args.foreign_artist_id}")
        if not lookup:
            raise ToolError(
                message=(f"lidarr.artist_add: foreign_artist_id={args.foreign_artist_id} not found on MusicBrainz"),
                hint="call lidarr.artist_lookup with a name query first to confirm the mbid",
            )
        candidate = lookup[0]
        body = _build_add_body(candidate, args)
        added = await post_api_v1_artist.asyncio(client=client, body=body)
        if added is None:
            raise ToolError(
                message="lidarr.artist_add: Lidarr accepted the add but returned no payload",
                hint="check Lidarr's UI; the artist may still have been added",
            )
        lid = _int_or_none(added.id)
        return AddResult(
            lidarr_id=lid or 0,
            foreign_artist_id=args.foreign_artist_id,
            name=_str_or_none(added.artist_name) or "<unknown>",
            already_added=False,
            msg=f"added lidarr_id={lid}",
        )

    @mcp.tool(
        name="lidarr.artist_delete",
        description=(
            "Remove an artist from Lidarr. DESTRUCTIVE. First call without ``confirm_token`` "
            "returns a plan + token; second call with the token executes. ``delete_files=true`` "
            "also wipes files on disk."
        ),
    )
    async def lidarr_artist_delete(args: ArtistDeleteInput) -> DeletePlan | DeleteResult:
        policy.check("lidarr.artist_delete", Tag.DESTRUCTIVE)
        target = await get_api_v1_artist_id.asyncio(id=args.lidarr_id, client=client)
        if target is None:
            raise ToolError(
                message=f"lidarr: artist id {args.lidarr_id} not found",
                hint="call lidarr.artist_search to discover valid lidarr_id values",
            )
        target_summary = _artist_to_summary(target)
        fp = fingerprint(
            {
                "lidarr_id": args.lidarr_id,
                "delete_files": args.delete_files,
                "exclusion": args.add_import_list_exclusion,
            }
        )

        if args.confirm_token is None:
            token = policy.issue_token("lidarr.artist_delete", fp)
            files_msg = "AND delete files on disk" if args.delete_files else "keep files on disk"
            return DeletePlan(
                confirm_token=token,
                summary=(f"remove {target_summary.name!r} (lidarr_id={target_summary.lidarr_id}) from Lidarr; {files_msg}"),
                target=target_summary,
                expires_in_seconds=policy.confirm_token_ttl_seconds,
            )

        policy.consume_token("lidarr.artist_delete", fp, args.confirm_token)
        await delete_api_v1_artist_id.asyncio_detailed(
            id=args.lidarr_id,
            client=client,
            delete_files=args.delete_files,
            add_import_list_exclusion=args.add_import_list_exclusion,
        )
        return DeleteResult(
            deleted_lidarr_id=args.lidarr_id,
            name=target_summary.name,
            files_deleted=args.delete_files,
            msg=f"deleted lidarr_id={args.lidarr_id}",
        )

    log.info(
        "lidarr.tools registered",
        url=base_url,
        read_only=policy.read_only,
        disable_destructive=policy.disable_destructive,
    )


# --- internal helpers ---


def _build_add_body(candidate: ArtistResource, args: ArtistAddInput) -> ArtistResource:
    """Fill in the add-time fields the agent has authority over."""
    options = AddArtistOptions(
        monitor=_monitor_enum(args.monitor),
        search_for_missing_albums=args.search_for_missing_albums,
        monitored=True,
    )
    if args.quality_profile_id is not None:
        candidate.quality_profile_id = args.quality_profile_id
    if args.metadata_profile_id is not None:
        candidate.metadata_profile_id = args.metadata_profile_id
    if args.root_folder_path is not None:
        candidate.root_folder_path = args.root_folder_path
    candidate.monitored = True
    candidate.add_options = options
    return candidate


def _monitor_enum(monitor: str):  # type: ignore[no-untyped-def]
    """Translate friendly monitor string to the generated enum."""
    from arr_stack_mcp.generated.lidarr.models.monitor_types import MonitorTypes

    return MonitorTypes(monitor)


def _artist_to_summary(a: ArtistResource) -> ArtistSummary:
    stats = a.statistics
    album_count = None
    track_count = None
    track_file_count = None
    size_on_disk = None
    if stats is not None and not isinstance(stats, type(UNSET)):
        album_count = _int_or_none(getattr(stats, "album_count", None))
        track_count = _int_or_none(getattr(stats, "track_count", None))
        track_file_count = _int_or_none(getattr(stats, "track_file_count", None))
        size_on_disk = _int_or_none(getattr(stats, "size_on_disk", None))
    return ArtistSummary(
        lidarr_id=_int_or_none(a.id) or 0,
        foreign_artist_id=_str_or_none(a.foreign_artist_id),
        name=_str_or_none(a.artist_name) or "<unknown>",
        overview=_str_or_none(a.overview),
        status=_status_to_str(a.status),
        monitored=_bool_or_none(a.monitored) or False,
        album_count=album_count,
        track_count=track_count,
        track_file_count=track_file_count,
        size_on_disk=size_on_disk,
        path=_str_or_none(a.path),
    )


def _album_to_summary(a: object) -> AlbumSummary:
    artist = getattr(a, "artist", None)
    artist_name = None
    if artist is not None and not isinstance(artist, type(UNSET)):
        artist_name = _str_or_none(getattr(artist, "artist_name", None))
    stats = getattr(a, "statistics", None)
    track_count = None
    track_file_count = None
    if stats is not None and not isinstance(stats, type(UNSET)):
        track_count = _int_or_none(getattr(stats, "track_count", None))
        track_file_count = _int_or_none(getattr(stats, "track_file_count", None))
    return AlbumSummary(
        lidarr_id=_int_or_none(getattr(a, "id", None)) or 0,
        foreign_album_id=_str_or_none(getattr(a, "foreign_album_id", None)),
        title=_str_or_none(getattr(a, "title", None)) or "<unknown>",
        artist_name=artist_name,
        release_date=_dt_or_none(getattr(a, "release_date", None)),
        album_type=_str_or_none(getattr(a, "album_type", None)),
        monitored=_bool_or_none(getattr(a, "monitored", None)) or False,
        has_file=_bool_or_none(getattr(a, "any_release_ok", None)) or False,
        track_count=track_count,
        track_file_count=track_file_count,
    )


def _queue_record_to_item(r: object) -> QueueItem:
    title = _str_or_none(getattr(r, "title", None)) or "<unknown>"
    size = _int_or_none(getattr(r, "size", None)) or 0
    size_left = _int_or_none(getattr(r, "sizeleft", None)) or _int_or_none(getattr(r, "size_left", None)) or 0
    progress = 0.0 if size == 0 else (1.0 - (size_left / size)) * 100.0
    return QueueItem(
        queue_id=_int_or_none(getattr(r, "id", None)) or 0,
        artist_id=_int_or_none(getattr(r, "artist_id", None)),
        album_id=_int_or_none(getattr(r, "album_id", None)),
        title=title,
        status=_str_or_none(getattr(r, "status", None)) or "unknown",
        progress_pct=round(progress, 1),
        size=size,
        size_left=size_left,
        estimated_completion=_dt_or_none(getattr(r, "estimated_completion_time", None)),
        download_client=_str_or_none(getattr(r, "download_client", None)),
        protocol=_str_or_none(getattr(r, "protocol", None)),
    )


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


def _status_to_str(v: object) -> str | None:
    if v is None or v is UNSET:
        return None
    inner = getattr(v, "value", None)
    if inner is not None:
        return str(inner)
    return str(v)
