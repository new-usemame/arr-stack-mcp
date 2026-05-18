"""Radarr curated tool layer. Mirrors Sonarr's shape, at the movie grain."""

from __future__ import annotations

from typing import TYPE_CHECKING

import structlog

from arr_stack_mcp.errors import ToolError
from arr_stack_mcp.fuzzy import normalize, title_contains
from arr_stack_mcp.generated.radarr.api.calendar import get_api_v3_calendar
from arr_stack_mcp.generated.radarr.api.missing import get_api_v3_wanted_missing
from arr_stack_mcp.generated.radarr.api.movie import (
    delete_api_v3_movie_id,
    get_api_v3_movie,
    get_api_v3_movie_id,
    post_api_v3_movie,
)
from arr_stack_mcp.generated.radarr.api.movie_lookup import get_api_v3_movie_lookup
from arr_stack_mcp.generated.radarr.api.queue import get_api_v3_queue
from arr_stack_mcp.generated.radarr.api.system import get_api_v3_system_status
from arr_stack_mcp.generated.radarr.models import MovieResource
from arr_stack_mcp.generated.radarr.models.add_movie_options import AddMovieOptions
from arr_stack_mcp.generated.radarr.types import UNSET
from arr_stack_mcp.policy import Tag, fingerprint
from arr_stack_mcp.tools.radarr._client import make_radarr_client
from arr_stack_mcp.tools.radarr._models import (
    AddResult,
    CalendarInput,
    CalendarItem,
    CalendarResult,
    DeletePlan,
    DeleteResult,
    LookupResult,
    MissingInput,
    MissingMovie,
    MissingResult,
    MovieAddInput,
    MovieDeleteInput,
    MovieLookupInput,
    MovieSearchInput,
    MovieSummary,
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
    """Register every Radarr tool on the given MCP server."""
    client = make_radarr_client(svc)
    base_url = str(svc.url).rstrip("/")

    @mcp.tool(
        name="radarr.system_status",
        description=(
            "Get Radarr's system status (version, branch, runtime, instance name). "
            "Use this first when diagnosing any Radarr problem. Mirrors ``sonarr.system_status``."
        ),
    )
    async def radarr_system_status() -> StatusResult:
        policy.check("radarr.system_status", Tag.READ)
        result = await get_api_v3_system_status.asyncio(client=client)
        if result is None:
            raise ToolError(message=f"radarr.system_status: empty response from {base_url}")
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
        name="radarr.movie_search",
        description=(
            "Search Radarr's existing library (already-added movies) by free-text title. "
            "Returns ranked candidates with stable Radarr ids and TMDB ids. Use when the "
            "user asks 'do I have movie X?'. For discovering movies that aren't yet added, "
            "use ``radarr.movie_lookup`` instead. ``year`` disambiguates remakes (Dune 1984 "
            "vs Dune 2021)."
        ),
    )
    async def radarr_movie_search(args: MovieSearchInput) -> SearchResult:
        policy.check("radarr.movie_search", Tag.READ)
        movies = await get_api_v3_movie.asyncio(client=client)
        if movies is None:
            return SearchResult(query=args.query, count=0, total=0, items=[])
        q_norm = normalize(args.query)
        matches: list[MovieResource] = []
        for m in movies:
            title = _str_or_none(m.title) or ""
            if not title_contains(title, args.query) and q_norm not in normalize(title):
                continue
            if args.year is not None and _int_or_none(m.year) != args.year:
                continue
            matches.append(m)
        total = len(matches)
        items = [_movie_to_summary(m) for m in matches[: args.limit]]
        return SearchResult(
            query=args.query,
            count=len(items),
            total=total,
            truncated=total > args.limit,
            items=items,
        )

    @mcp.tool(
        name="radarr.movie_lookup",
        description=(
            "Search TMDB through Radarr to find movies that could be ADDED. Each candidate's "
            "``tmdb_id`` is the input ``radarr.movie_add`` expects."
        ),
    )
    async def radarr_movie_lookup(args: MovieLookupInput) -> LookupResult:
        policy.check("radarr.movie_lookup", Tag.READ)
        results = await get_api_v3_movie_lookup.asyncio(client=client, term=args.query)
        if not results:
            return LookupResult(query=args.query, candidates=[])
        candidates = [_movie_to_summary(r) for r in results[: args.limit]]
        return LookupResult(query=args.query, candidates=candidates)

    @mcp.tool(
        name="radarr.queue",
        description="List active Radarr downloads with progress, ETA, and download client.",
    )
    async def radarr_queue(args: QueueInput) -> QueueResult:
        policy.check("radarr.queue", Tag.READ)
        page = await get_api_v3_queue.asyncio(
            client=client,
            page=1,
            page_size=args.limit,
            include_movie=True,
        )
        if page is None or page.records is None or isinstance(page.records, type(UNSET)):
            return QueueResult(count=0, total=0, items=[])
        records = list(page.records)  # type: ignore[arg-type]
        items = [_queue_record_to_item(r) for r in records]
        total = _int_or_none(page.total_records) or len(items)
        return QueueResult(count=len(items), total=total, items=items)

    @mcp.tool(
        name="radarr.calendar",
        description=(
            "List upcoming or recently-released movies. Window defaults to 2 days back and "
            "30 days forward, suitable for 'what's coming out this month?' queries."
        ),
    )
    async def radarr_calendar(args: CalendarInput) -> CalendarResult:
        policy.check("radarr.calendar", Tag.READ)
        import datetime as _dt

        now = _dt.datetime.now(_dt.UTC)
        start = now - _dt.timedelta(days=args.days_back)
        end = now + _dt.timedelta(days=args.days_forward)
        movies = await get_api_v3_calendar.asyncio(
            client=client,
            start=start,
            end=end,
            unmonitored=args.unmonitored,
        )
        if not movies:
            return CalendarResult(count=0, items=[])
        items = [_movie_to_calendar(m) for m in movies]
        return CalendarResult(count=len(items), items=items)

    @mcp.tool(
        name="radarr.missing",
        description="List monitored movies that are released but not on disk. Oldest-first.",
    )
    async def radarr_missing(args: MissingInput) -> MissingResult:
        policy.check("radarr.missing", Tag.READ)
        page = await get_api_v3_wanted_missing.asyncio(
            client=client,
            page=1,
            page_size=args.limit,
            sort_key="releaseDate",
            sort_direction=UNSET,
            monitored=args.monitored_only,
        )
        if page is None or page.records is None or isinstance(page.records, type(UNSET)):
            return MissingResult(count=0, total=0, items=[])
        records = list(page.records)  # type: ignore[arg-type]
        items = [_movie_to_missing(m) for m in records]
        total = _int_or_none(page.total_records) or len(items)
        return MissingResult(count=len(items), total=total, items=items)

    @mcp.tool(
        name="radarr.movie_add",
        description=(
            "Add a new movie to Radarr by TMDB id. Call ``radarr.movie_lookup`` first to "
            "obtain the ``tmdb_id``. Omit ``quality_profile_id`` and ``root_folder_path`` "
            "for Radarr defaults. Triggers an initial search unless ``search_for_movie=False``. "
            "Idempotent on already-added movies."
        ),
    )
    async def radarr_movie_add(args: MovieAddInput) -> AddResult:
        policy.check("radarr.movie_add", Tag.WRITE)
        existing = await get_api_v3_movie.asyncio(client=client, tmdb_id=args.tmdb_id)
        if existing:
            row = existing[0]
            rid = _int_or_none(row.id)
            if rid is not None:
                return AddResult(
                    radarr_id=rid,
                    tmdb_id=args.tmdb_id,
                    title=_str_or_none(row.title) or "<unknown>",
                    already_added=True,
                    msg=f"already in library as radarr_id={rid}",
                )

        lookup = await get_api_v3_movie_lookup.asyncio(client=client, term=f"tmdb:{args.tmdb_id}")
        if not lookup:
            raise ToolError(
                message=f"radarr.movie_add: tmdb_id={args.tmdb_id} not found on TMDB",
                hint="call radarr.movie_lookup with a title query first to confirm the tmdb_id",
            )
        candidate = lookup[0]
        body = _build_add_body(candidate, args)
        added = await post_api_v3_movie.asyncio(client=client, body=body)
        if added is None:
            raise ToolError(
                message="radarr.movie_add: Radarr accepted the add but returned no payload",
                hint="check Radarr's UI; the movie may still have been added",
            )
        rid = _int_or_none(added.id)
        return AddResult(
            radarr_id=rid or 0,
            tmdb_id=args.tmdb_id,
            title=_str_or_none(added.title) or "<unknown>",
            already_added=False,
            msg=f"added radarr_id={rid}",
        )

    @mcp.tool(
        name="radarr.movie_delete",
        description=(
            "Remove a movie from Radarr. DESTRUCTIVE. First call without ``confirm_token`` "
            "returns a plan + token; second call with the token executes. ``delete_files=true`` "
            "also wipes the file from disk. Token expires after 5 minutes."
        ),
    )
    async def radarr_movie_delete(args: MovieDeleteInput) -> DeletePlan | DeleteResult:
        policy.check("radarr.movie_delete", Tag.DESTRUCTIVE)
        target = await get_api_v3_movie_id.asyncio(id=args.radarr_id, client=client)
        if target is None:
            raise ToolError(
                message=f"radarr: movie id {args.radarr_id} not found",
                hint="call radarr.movie_search to discover valid radarr_id values",
            )
        target_summary = _movie_to_summary(target)
        fp = fingerprint(
            {
                "radarr_id": args.radarr_id,
                "delete_files": args.delete_files,
                "exclusion": args.add_import_list_exclusion,
            }
        )

        if args.confirm_token is None:
            token = policy.issue_token("radarr.movie_delete", fp)
            files_msg = "AND delete the file on disk" if args.delete_files else "keep file on disk"
            return DeletePlan(
                confirm_token=token,
                summary=(f"remove {target_summary.title!r} (radarr_id={target_summary.radarr_id}) from Radarr; {files_msg}"),
                target=target_summary,
                expires_in_seconds=policy.confirm_token_ttl_seconds,
            )

        policy.consume_token("radarr.movie_delete", fp, args.confirm_token)
        await delete_api_v3_movie_id.asyncio_detailed(
            id=args.radarr_id,
            client=client,
            delete_files=args.delete_files,
            add_import_exclusion=args.add_import_list_exclusion,
        )
        return DeleteResult(
            deleted_radarr_id=args.radarr_id,
            title=target_summary.title,
            files_deleted=args.delete_files,
            msg=f"deleted radarr_id={args.radarr_id}",
        )

    log.info(
        "radarr.tools registered",
        url=base_url,
        read_only=policy.read_only,
        disable_destructive=policy.disable_destructive,
    )


# --- internal helpers ---


def _build_add_body(candidate: MovieResource, args: MovieAddInput) -> MovieResource:
    """Fill in the add-time fields the agent has authority over."""
    from arr_stack_mcp.generated.radarr.models.movie_status_type import MovieStatusType

    options = AddMovieOptions(
        ignore_episodes_with_files=False,
        ignore_episodes_without_files=False,
        monitor=_monitor_enum(),  # type: ignore[no-untyped-call]
        search_for_movie=args.search_for_movie,
        add_method=_add_method_enum(),  # type: ignore[no-untyped-call]
    )
    if args.quality_profile_id is not None:
        candidate.quality_profile_id = args.quality_profile_id
    if args.root_folder_path is not None:
        candidate.root_folder_path = args.root_folder_path
    candidate.monitored = args.monitored
    candidate.minimum_availability = MovieStatusType(args.minimum_availability)
    candidate.add_options = options
    return candidate


def _monitor_enum():  # type: ignore[no-untyped-def]
    """Default to monitoring the movie itself (not extras)."""
    from arr_stack_mcp.generated.radarr.models.monitor_types import MonitorTypes

    return MonitorTypes("movieOnly")


def _add_method_enum():  # type: ignore[no-untyped-def]
    """Sensible default add-method."""
    from arr_stack_mcp.generated.radarr.models.add_movie_method import AddMovieMethod

    return AddMovieMethod("manual")


def _movie_to_summary(m: MovieResource) -> MovieSummary:
    return MovieSummary(
        radarr_id=_int_or_none(m.id) or 0,
        tmdb_id=_int_or_none(m.tmdb_id),
        imdb_id=_str_or_none(m.imdb_id),
        title=_str_or_none(m.title) or "<unknown>",
        year=_int_or_none(m.year),
        status=_status_to_str(m.status),
        monitored=_bool_or_none(m.monitored) or False,
        has_file=_bool_or_none(m.has_file) or False,
        size_on_disk=_int_or_none(m.size_on_disk),
        runtime_minutes=_int_or_none(m.runtime),
        certification=_str_or_none(m.certification),
        path=_str_or_none(m.path),
        in_cinemas=_dt_or_none(m.in_cinemas),
        digital_release=_dt_or_none(m.digital_release),
    )


def _movie_to_calendar(m: MovieResource) -> CalendarItem:
    return CalendarItem(
        movie_id=_int_or_none(m.id) or 0,
        title=_str_or_none(m.title) or "<unknown>",
        year=_int_or_none(m.year),
        in_cinemas=_dt_or_none(m.in_cinemas),
        digital_release=_dt_or_none(m.digital_release),
        physical_release=_dt_or_none(m.physical_release),
        has_file=_bool_or_none(m.has_file) or False,
        monitored=_bool_or_none(m.monitored) or False,
    )


def _movie_to_missing(m: MovieResource) -> MissingMovie:
    return MissingMovie(
        movie_id=_int_or_none(m.id) or 0,
        title=_str_or_none(m.title) or "<unknown>",
        year=_int_or_none(m.year),
        in_cinemas=_dt_or_none(m.in_cinemas),
        digital_release=_dt_or_none(m.digital_release),
    )


def _queue_record_to_item(r: object) -> QueueItem:
    title = _str_or_none(getattr(r, "title", None)) or "<unknown>"
    size = _int_or_none(getattr(r, "size", None)) or 0
    size_left = _int_or_none(getattr(r, "sizeleft", None)) or _int_or_none(getattr(r, "size_left", None)) or 0
    progress = 0.0 if size == 0 else (1.0 - (size_left / size)) * 100.0
    return QueueItem(
        queue_id=_int_or_none(getattr(r, "id", None)) or 0,
        movie_id=_int_or_none(getattr(r, "movie_id", None)),
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
