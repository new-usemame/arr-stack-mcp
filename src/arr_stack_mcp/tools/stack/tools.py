"""Cross-service `stack.*` toolset.

These tools span services rather than belonging to one. They're registered
unconditionally — the dispatch-time wiring lives in `server.build_server`,
not in `_register_service` (which is keyed on per-upstream service names).

See notes/DESIGN-v0.2.md §2.2.
"""

from __future__ import annotations

import asyncio
import urllib.parse
from typing import TYPE_CHECKING

import structlog

from arr_stack_mcp.policy import Tag
from arr_stack_mcp.tools.stack._models import (
    DryRunEntry,
    DryRunLogInput,
    DryRunLogResult,
    FindAnywhereInput,
    FindAnywhereResult,
    FindAnywhereSourceResult,
    QueueStatusAllInput,
    QueueStatusAllResult,
    QueueStatusAllSource,
    ReportIssueInput,
    ReportIssueResult,
    StackFoundItem,
    StackHealthInput,
    StackHealthResult,
    StackHealthService,
    StackQueueItem,
)

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import Config, ServiceConfig
    from arr_stack_mcp.policy import Policy

log = structlog.get_logger(__name__)


# GitHub repo the stack.report_issue tool prefills against. Hardcoded — this
# is the operator's source-of-truth project URL and changes don't belong in
# user-facing config.
_REPO_SLUG: str = "new-usemame/arr-stack-mcp"


def register_all(mcp: FastMCP, cfg: Config, policy: Policy) -> None:
    """Register every `stack.*` tool. Always called from `server.build_server`."""

    @mcp.tool(
        name="stack.dryrun_log",
        description=(
            "Read the in-memory ring buffer of would-have-fired mutations recorded when `--dry-run` "
            "is active. Each entry names the tool, the wall-clock timestamp, and the intended payload. "
            "Use this after a dry-run plan-and-execute cycle to show the user what WOULD have happened. "
            "Buffer is per-process, capped at 200 entries, lossy on the older end. Returns empty when "
            "the server is not running with `--dry-run` (the buffer is only written to when dry-run is on)."
        ),
    )
    async def stack_dryrun_log(args: DryRunLogInput) -> DryRunLogResult:
        policy.check("stack.dryrun_log", Tag.READ)
        raw = policy.dryrun_log(limit=args.limit)
        entries: list[DryRunEntry] = []
        for e in raw:
            payload_raw = e.get("payload")
            payload: dict[str, object] | None = payload_raw if isinstance(payload_raw, dict) else None
            entries.append(
                DryRunEntry(
                    tool_name=str(e.get("tool_name", "")),
                    recorded_at=float(e.get("recorded_at", 0.0)),  # type: ignore[arg-type]
                    payload=payload,
                )
            )
        return DryRunLogResult(count=len(entries), entries=entries)

    @mcp.tool(
        name="stack.report_issue",
        description=(
            "Compose a pre-filled GitHub issue URL the user can post upstream when a tool errors in "
            "a way that isn't explained by the error envelope. Returns a click-to-create URL with the "
            "summary as the title and the detail (plus optional dry-run-log excerpt) as the body. "
            "Does NOT auto-submit — surface the URL to the user, who decides. Use this only when the "
            "user explicitly asks to file a bug or when an `upstream_bad_request` / generated-client "
            "deserialization error suggests the schema has drifted."
        ),
    )
    async def stack_report_issue(args: ReportIssueInput) -> ReportIssueResult:
        policy.check("stack.report_issue", Tag.READ)
        body = _compose_issue_body(args, policy)
        params = {"title": args.summary, "body": body}
        url = f"https://github.com/{_REPO_SLUG}/issues/new?" + urllib.parse.urlencode(params)
        return ReportIssueResult(url=url, repo=_REPO_SLUG)

    @mcp.tool(
        name="stack.find_anywhere",
        description=(
            "Fan a free-text query across every enabled arr / Jellyfin library in parallel and "
            "return a merged result list. Each row carries `source` (which service it came from), "
            "the stable id within that source, a title, year, and type. Use when the user's intent "
            "spans services ('where is X?', 'do we have X?'). For service-specific searches, call "
            "`*.search` on that service directly. Read-only; honors per-service errors gracefully "
            "(a single service failure does not fail the whole result)."
        ),
    )
    async def stack_find_anywhere(args: FindAnywhereInput) -> FindAnywhereResult:
        policy.check("stack.find_anywhere", Tag.READ)
        sources = await _gather_find_anywhere(cfg, args.query, args.limit_per_service)
        total = sum(s.count for s in sources)
        return FindAnywhereResult(query=args.query, total_count=total, sources=sources)

    @mcp.tool(
        name="stack.queue_status_all",
        description=(
            "Aggregate the active download / grab queue across Sonarr, Radarr, and Lidarr. Returns "
            "a list per source with normalized queue rows (`source`, `queue_id`, `entity_id`, "
            "`title`, `status`, `progress_pct`, `size`, `size_left`). Use to answer 'what's "
            "downloading right now?'. Jellyfin is omitted (it has no download queue concept). "
            "Read-only; per-service failures appear as `error` on the source row."
        ),
    )
    async def stack_queue_status_all(args: QueueStatusAllInput) -> QueueStatusAllResult:
        policy.check("stack.queue_status_all", Tag.READ)
        sources = await _gather_queue_status_all(cfg, args.limit_per_service)
        total = sum(s.count for s in sources)
        return QueueStatusAllResult(total_count=total, sources=sources)

    @mcp.tool(
        name="stack.health",
        description=(
            "Probe every enabled service's `*.system_status` in parallel and return a compact "
            "reachability matrix. Each row has `name`, `enabled`, `reachable`, `version` (when "
            "reachable), and `error` (when not). `overall_ok` is True iff every enabled service is "
            "reachable AND reported a version. Use this first when diagnosing 'is something broken?' "
            "before drilling into any one service. Read-only."
        ),
    )
    async def stack_health(args: StackHealthInput) -> StackHealthResult:
        del args  # FastMCP rejects underscore-prefixed param names; the input is empty by design.
        policy.check("stack.health", Tag.READ)
        rows = await _gather_health(cfg)
        overall = all(r.reachable and r.version is not None for r in rows if r.enabled)
        return StackHealthResult(overall_ok=overall, services=rows)

    log.info("stack.tools registered")


# ---------- internals ----------


def _compose_issue_body(args: ReportIssueInput, policy: Policy) -> str:
    """Build the prefilled body. Plain markdown, tone-grepped (no marketing intensifiers)."""
    parts: list[str] = []
    parts.append("Filed via `stack.report_issue` from arr-stack-mcp.")
    if args.detail:
        parts.append("")
        parts.append("**Detail:**")
        parts.append("")
        parts.append(args.detail.strip())
    if args.include_dryrun_log:
        entries = policy.dryrun_log(limit=20)
        if entries:
            parts.append("")
            parts.append("**Last 20 dry-run log entries:**")
            parts.append("")
            parts.append("```json")
            import json

            parts.append(json.dumps(entries, indent=2, default=str))
            parts.append("```")
    return "\n".join(parts)


async def _gather_health(cfg: Config) -> list[StackHealthService]:
    """Call `system_status` on every enabled service in parallel, project to StackHealthService rows.

    Disabled services appear with `enabled=False, reachable=False, version=None, error=None` so the
    operator can see at a glance which services are configured out.
    """
    rows: list[StackHealthService] = []
    enabled_probes: list[tuple[str, asyncio.Task[tuple[bool, str | None, str | None]]]] = []

    for name, svc in cfg.services.items():
        if not svc.enabled:
            rows.append(StackHealthService(name=name, enabled=False, reachable=False))
            continue
        # Launch the probe; gather later so all run concurrently.
        enabled_probes.append((name, asyncio.create_task(_probe_one_service(svc))))

    for name, task in enabled_probes:
        reachable, version, error = await task
        rows.append(
            StackHealthService(
                name=name,
                enabled=True,
                reachable=reachable,
                version=version,
                error=error,
            )
        )
    # Sort alphabetically so the matrix is stable across calls.
    rows.sort(key=lambda r: r.name)
    return rows


_PROBE_DISPATCH: dict[
    str,
    object,  # the value is a callable; using object to dodge the generic-bound dance
] = {}  # filled lazily below; see _build_dispatch


def _build_dispatch() -> dict[str, object]:
    """Lazy-build the service-name -> probe-function map. Avoids the long if/elif chain that triggered PLR0911."""
    return {
        "sonarr": _probe_sonarr,
        "radarr": _probe_radarr,
        "lidarr": _probe_lidarr,
        "prowlarr": _probe_prowlarr,
        "jellyfin": _probe_jellyfin,
    }


async def _probe_one_service(svc: ServiceConfig) -> tuple[bool, str | None, str | None]:
    """Best-effort system_status probe.

    Returns `(reachable, version, error)`. Dispatches by service name to
    the matching generated system-status function. Errors from the
    generated layer surface as a string for the LLM to interpret.
    """
    if not _PROBE_DISPATCH:
        _PROBE_DISPATCH.update(_build_dispatch())
    fn = _PROBE_DISPATCH.get(svc.name)
    if fn is None:
        return False, None, f"unknown service: {svc.name!r}"
    try:
        return await fn(svc)  # type: ignore[operator, no-any-return]
    except Exception as exc:
        return False, None, f"{type(exc).__name__}: {exc}"


async def _probe_sonarr(svc: ServiceConfig) -> tuple[bool, str | None, str | None]:
    from arr_stack_mcp.generated.sonarr.api.system import get_api_v3_system_status as fn
    from arr_stack_mcp.tools.sonarr._client import make_sonarr_client

    client = make_sonarr_client(svc)
    result = await fn.asyncio(client=client)
    if result is None:
        return False, None, "empty response"
    return True, str(getattr(result, "version", "") or ""), None


async def _probe_radarr(svc: ServiceConfig) -> tuple[bool, str | None, str | None]:
    from arr_stack_mcp.generated.radarr.api.system import get_api_v3_system_status as fn
    from arr_stack_mcp.tools.radarr._client import make_radarr_client

    client = make_radarr_client(svc)
    result = await fn.asyncio(client=client)
    if result is None:
        return False, None, "empty response"
    return True, str(getattr(result, "version", "") or ""), None


async def _probe_lidarr(svc: ServiceConfig) -> tuple[bool, str | None, str | None]:
    from arr_stack_mcp.generated.lidarr.api.system import get_api_v1_system_status as fn
    from arr_stack_mcp.tools.lidarr._client import make_lidarr_client

    client = make_lidarr_client(svc)
    result = await fn.asyncio(client=client)
    if result is None:
        return False, None, "empty response"
    return True, str(getattr(result, "version", "") or ""), None


async def _probe_prowlarr(svc: ServiceConfig) -> tuple[bool, str | None, str | None]:
    # Prowlarr generated client lives at arr_stack_mcp.generated.prowlarr — the v0.2 Prowlarr toolset
    # will use this same constructor. Available now via the v0.1.0 client scaffold.
    from arr_stack_mcp.generated.prowlarr.api.system import get_api_v1_system_status as fn
    from arr_stack_mcp.tools.prowlarr._client import make_prowlarr_client

    client = make_prowlarr_client(svc)
    result = await fn.asyncio(client=client)
    if result is None:
        return False, None, "empty response"
    return True, str(getattr(result, "version", "") or ""), None


async def _probe_jellyfin(svc: ServiceConfig) -> tuple[bool, str | None, str | None]:
    from arr_stack_mcp.generated.jellyfin.api.system import (
        get_public_system_info,
        get_system_info,
    )
    from arr_stack_mcp.generated.jellyfin.client import AuthenticatedClient
    from arr_stack_mcp.tools.jellyfin._client import make_jellyfin_client

    client = make_jellyfin_client(svc)
    if isinstance(client, AuthenticatedClient):
        result = await get_system_info.asyncio(client=client)
    else:
        result = await get_public_system_info.asyncio(client=client)
    if result is None or isinstance(result, dict):
        return False, None, "empty response"
    return True, str(getattr(result, "version", "") or ""), None


# ---------- find_anywhere ----------


async def _gather_find_anywhere(cfg: Config, query: str, limit: int) -> list[FindAnywhereSourceResult]:
    """Fan the query across every enabled arr + Jellyfin in parallel."""
    coros: dict[str, asyncio.Task[FindAnywhereSourceResult]] = {}
    for name, svc in cfg.services.items():
        if not svc.enabled:
            continue
        if name in {"sonarr", "radarr", "lidarr", "jellyfin"}:
            coros[name] = asyncio.create_task(_find_in_service(svc, query, limit))
    sources: list[FindAnywhereSourceResult] = []
    for name in sorted(coros.keys()):
        sources.append(await coros[name])
    return sources


async def _find_in_service(svc: ServiceConfig, query: str, limit: int) -> FindAnywhereSourceResult:
    """One service's per-library search, projected to StackFoundItem rows."""
    try:
        if svc.name == "sonarr":
            return await _find_sonarr(svc, query, limit)
        if svc.name == "radarr":
            return await _find_radarr(svc, query, limit)
        if svc.name == "lidarr":
            return await _find_lidarr(svc, query, limit)
        if svc.name == "jellyfin":
            return await _find_jellyfin(svc, query, limit)
    except Exception as exc:
        return FindAnywhereSourceResult(source=svc.name, count=0, items=[], error=f"{type(exc).__name__}: {exc}")
    return FindAnywhereSourceResult(source=svc.name, count=0, items=[], error=f"unknown service: {svc.name!r}")


async def _find_sonarr(svc: ServiceConfig, query: str, limit: int) -> FindAnywhereSourceResult:
    from arr_stack_mcp.fuzzy import is_acronym_or_substring_match, normalize, title_contains
    from arr_stack_mcp.generated.sonarr.api.series import get_api_v3_series
    from arr_stack_mcp.tools.sonarr._client import make_sonarr_client

    client = make_sonarr_client(svc)
    series = await get_api_v3_series.asyncio(client=client)
    if not series:
        return FindAnywhereSourceResult(source="sonarr", count=0, items=[])
    q_norm = normalize(query)
    matches: list[StackFoundItem] = []
    for s in series:
        title = str(getattr(s, "title", "") or "")
        if not (title_contains(title, query) or q_norm in normalize(title) or is_acronym_or_substring_match(query, title)):
            continue
        matches.append(
            StackFoundItem(
                source="sonarr",
                id=int(getattr(s, "id", 0) or 0),
                title=title,
                year=_safe_int(getattr(s, "year", None)),
                type="Series",
                external_id=_safe_str(getattr(s, "tvdb_id", None)),
            )
        )
        if len(matches) >= limit:
            break
    return FindAnywhereSourceResult(source="sonarr", count=len(matches), items=matches)


async def _find_radarr(svc: ServiceConfig, query: str, limit: int) -> FindAnywhereSourceResult:
    from arr_stack_mcp.fuzzy import is_acronym_or_substring_match, normalize, title_contains
    from arr_stack_mcp.generated.radarr.api.movie import get_api_v3_movie
    from arr_stack_mcp.tools.radarr._client import make_radarr_client

    client = make_radarr_client(svc)
    movies = await get_api_v3_movie.asyncio(client=client)
    if not movies:
        return FindAnywhereSourceResult(source="radarr", count=0, items=[])
    q_norm = normalize(query)
    matches: list[StackFoundItem] = []
    for m in movies:
        title = str(getattr(m, "title", "") or "")
        if not (title_contains(title, query) or q_norm in normalize(title) or is_acronym_or_substring_match(query, title)):
            continue
        matches.append(
            StackFoundItem(
                source="radarr",
                id=int(getattr(m, "id", 0) or 0),
                title=title,
                year=_safe_int(getattr(m, "year", None)),
                type="Movie",
                external_id=_safe_str(getattr(m, "tmdb_id", None)),
            )
        )
        if len(matches) >= limit:
            break
    return FindAnywhereSourceResult(source="radarr", count=len(matches), items=matches)


async def _find_lidarr(svc: ServiceConfig, query: str, limit: int) -> FindAnywhereSourceResult:
    from arr_stack_mcp.fuzzy import is_acronym_or_substring_match, normalize, title_contains
    from arr_stack_mcp.generated.lidarr.api.artist import get_api_v1_artist
    from arr_stack_mcp.tools.lidarr._client import make_lidarr_client

    client = make_lidarr_client(svc)
    artists = await get_api_v1_artist.asyncio(client=client)
    if not artists:
        return FindAnywhereSourceResult(source="lidarr", count=0, items=[])
    q_norm = normalize(query)
    matches: list[StackFoundItem] = []
    for a in artists:
        name = str(getattr(a, "artist_name", "") or "")
        if not (title_contains(name, query) or q_norm in normalize(name) or is_acronym_or_substring_match(query, name)):
            continue
        matches.append(
            StackFoundItem(
                source="lidarr",
                id=int(getattr(a, "id", 0) or 0),
                title=name,
                year=None,  # Lidarr artist has no canonical year
                type="MusicArtist",
                external_id=_safe_str(getattr(a, "foreign_artist_id", None)),
            )
        )
        if len(matches) >= limit:
            break
    return FindAnywhereSourceResult(source="lidarr", count=len(matches), items=matches)


async def _find_jellyfin(svc: ServiceConfig, query: str, limit: int) -> FindAnywhereSourceResult:
    from uuid import UUID

    from arr_stack_mcp.generated.jellyfin.api.items import get_items
    from arr_stack_mcp.generated.jellyfin.client import AuthenticatedClient
    from arr_stack_mcp.generated.jellyfin.types import UNSET, Unset
    from arr_stack_mcp.tools.jellyfin._client import make_jellyfin_client

    client = make_jellyfin_client(svc)
    if not isinstance(client, AuthenticatedClient):
        return FindAnywhereSourceResult(source="jellyfin", count=0, items=[], error="jellyfin requires API key")
    # default_user_id is optional config; when set we narrow to a UUID,
    # otherwise the upstream call uses UNSET (no user scoping).
    user_id: Unset | UUID = UNSET
    if svc.default_user_id:
        try:
            user_id = UUID(svc.default_user_id)
        except ValueError:
            user_id = UNSET
    result = await get_items.asyncio(
        client=client,
        user_id=user_id,
        search_term=query,
        limit=limit,
        recursive=True,
    )
    if result is None or isinstance(result, dict) or not hasattr(result, "items"):
        return FindAnywhereSourceResult(source="jellyfin", count=0, items=[])
    items_raw = list(result.items or [])
    matches = [
        StackFoundItem(
            source="jellyfin",
            id=str(getattr(it, "id", "") or ""),
            title=str(getattr(it, "name", "") or "<unknown>"),
            year=_safe_int(getattr(it, "production_year", None)),
            type=_safe_str(getattr(it, "type_", None) or getattr(it, "type", None)),
        )
        for it in items_raw
    ]
    return FindAnywhereSourceResult(source="jellyfin", count=len(matches), items=matches)


# ---------- queue_status_all ----------


async def _gather_queue_status_all(cfg: Config, limit: int) -> list[QueueStatusAllSource]:
    coros: dict[str, asyncio.Task[QueueStatusAllSource]] = {}
    for name, svc in cfg.services.items():
        if not svc.enabled:
            continue
        if name in {"sonarr", "radarr", "lidarr"}:
            coros[name] = asyncio.create_task(_queue_for_service(svc, limit))
    sources: list[QueueStatusAllSource] = []
    for name in sorted(coros.keys()):
        sources.append(await coros[name])
    return sources


async def _queue_for_service(svc: ServiceConfig, limit: int) -> QueueStatusAllSource:
    try:
        if svc.name == "sonarr":
            return await _queue_sonarr(svc, limit)
        if svc.name == "radarr":
            return await _queue_radarr(svc, limit)
        if svc.name == "lidarr":
            return await _queue_lidarr(svc, limit)
    except Exception as exc:
        return QueueStatusAllSource(source=svc.name, count=0, total=0, items=[], error=f"{type(exc).__name__}: {exc}")
    return QueueStatusAllSource(source=svc.name, count=0, total=0, items=[], error=f"unknown service: {svc.name!r}")


async def _queue_sonarr(svc: ServiceConfig, limit: int) -> QueueStatusAllSource:
    from arr_stack_mcp.generated.sonarr.api.queue import get_api_v3_queue
    from arr_stack_mcp.tools.sonarr._client import make_sonarr_client

    client = make_sonarr_client(svc)
    page = await get_api_v3_queue.asyncio(
        client=client,
        page=1,
        page_size=limit,
        include_series=True,
        include_episode=True,
    )
    return _project_arr_queue("sonarr", page, entity_attr="series_id")


async def _queue_radarr(svc: ServiceConfig, limit: int) -> QueueStatusAllSource:
    from arr_stack_mcp.generated.radarr.api.queue import get_api_v3_queue
    from arr_stack_mcp.tools.radarr._client import make_radarr_client

    client = make_radarr_client(svc)
    page = await get_api_v3_queue.asyncio(
        client=client,
        page=1,
        page_size=limit,
        include_movie=True,
    )
    return _project_arr_queue("radarr", page, entity_attr="movie_id")


async def _queue_lidarr(svc: ServiceConfig, limit: int) -> QueueStatusAllSource:
    from arr_stack_mcp.generated.lidarr.api.queue import get_api_v1_queue
    from arr_stack_mcp.tools.lidarr._client import make_lidarr_client

    client = make_lidarr_client(svc)
    page = await get_api_v1_queue.asyncio(
        client=client,
        page=1,
        page_size=limit,
        include_artist=True,
        include_album=True,
    )
    return _project_arr_queue("lidarr", page, entity_attr="artist_id")


def _project_arr_queue(source: str, page: object, *, entity_attr: str) -> QueueStatusAllSource:
    """Common projection from a Servarr `*.queue` page response into our normalized shape."""
    if page is None:
        return QueueStatusAllSource(source=source, count=0, total=0, items=[])
    records_attr = getattr(page, "records", None)
    if records_attr is None or not isinstance(records_attr, list):
        return QueueStatusAllSource(source=source, count=0, total=0, items=[])
    items: list[StackQueueItem] = []
    for r in records_attr:
        size = _safe_int(getattr(r, "size", None)) or 0
        size_left = _safe_int(getattr(r, "sizeleft", None)) or _safe_int(getattr(r, "size_left", None)) or 0
        progress = 0.0 if size == 0 else (1.0 - (size_left / size)) * 100.0
        items.append(
            StackQueueItem(
                source=source,
                queue_id=_safe_int(getattr(r, "id", None)) or 0,
                entity_id=_safe_int(getattr(r, entity_attr, None)),
                title=str(getattr(r, "title", "") or "<unknown>"),
                status=str(getattr(r, "status", "") or "unknown"),
                progress_pct=round(progress, 1),
                size=size,
                size_left=size_left,
                estimated_completion=_safe_dt(getattr(r, "estimated_completion_time", None)),
                download_client=_safe_str(getattr(r, "download_client", None)),
                protocol=_safe_str(getattr(r, "protocol", None)),
            )
        )
    total = _safe_int(getattr(page, "total_records", None)) or len(items)
    return QueueStatusAllSource(source=source, count=len(items), total=total, items=items)


# ---------- shared safe-coerce helpers ----------


def _safe_int(v: object) -> int | None:
    if v is None:
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


def _safe_str(v: object) -> str | None:
    if v is None:
        return None
    inner = getattr(v, "value", None)
    if inner is not None:
        return str(inner)
    s = str(v)
    if s == "UNSET":
        return None
    return s


def _safe_dt(v: object) -> str | None:
    if v is None:
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat()  # type: ignore[no-any-return]
    return str(v)
