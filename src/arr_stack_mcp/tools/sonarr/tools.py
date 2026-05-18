"""Sonarr curated tool layer.

Each tool wraps a small set of generated-client endpoints with an LLM-friendly
input schema, compact result envelope, and tag (read / write / destructive).

Tool naming uses dotted form (``sonarr.series_search``) per the design note in
``notes/RESEARCH-prior-art.md``. FastMCP accepts arbitrary strings as tool
names; the dots visually signal namespacing to the agent.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import structlog

from arr_stack_mcp.errors import Ambiguous, ToolError
from arr_stack_mcp.fuzzy import normalize, title_contains
from arr_stack_mcp.generated.sonarr.api.calendar import get_api_v3_calendar
from arr_stack_mcp.generated.sonarr.api.missing import get_api_v3_wanted_missing
from arr_stack_mcp.generated.sonarr.api.queue import get_api_v3_queue
from arr_stack_mcp.generated.sonarr.api.series import (
    delete_api_v3_series_id,
    get_api_v3_series,
    post_api_v3_series,
)
from arr_stack_mcp.generated.sonarr.api.series_lookup import get_api_v3_series_lookup
from arr_stack_mcp.generated.sonarr.api.system import get_api_v3_system_status
from arr_stack_mcp.generated.sonarr.models import SeriesResource
from arr_stack_mcp.generated.sonarr.models.add_series_options import AddSeriesOptions
from arr_stack_mcp.generated.sonarr.types import UNSET
from arr_stack_mcp.policy import Tag, fingerprint
from arr_stack_mcp.tools.sonarr._client import make_sonarr_client
from arr_stack_mcp.tools.sonarr._models import (
    AddResult,
    CalendarInput,
    CalendarItem,
    CalendarResult,
    DeletePlan,
    DeleteResult,
    LookupResult,
    MissingEpisode,
    MissingInput,
    MissingResult,
    QueueInput,
    QueueItem,
    QueueResult,
    SearchResult,
    SeriesAddInput,
    SeriesDeleteInput,
    SeriesLookupInput,
    SeriesSearchInput,
    SeriesSummary,
    StatusResult,
    SystemStatus,
)

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import ServiceConfig
    from arr_stack_mcp.policy import Policy

log = structlog.get_logger(__name__)


_SERVICE = "sonarr"


def register_all(mcp: FastMCP, svc: ServiceConfig, policy: Policy) -> None:
    """Register every Sonarr tool on the given MCP server.

    Tools that mutate state are skipped at registration time when ``--read-only``
    or ``--disable-destructive`` is active, so they never appear in the agent's
    catalogue.
    """
    client = make_sonarr_client(svc)
    base_url = str(svc.url).rstrip("/")

    # --- READ tools ---

    @mcp.tool(
        name="sonarr.system_status",
        description=(
            "Get Sonarr's system status (version, branch, runtime, instance name). "
            "Use this first when diagnosing any Sonarr problem to confirm the service "
            "is reachable and to learn the API version. Returns a compact dict — call "
            "``sonarr.health`` (v0.2) for a fuller health probe."
        ),
    )
    async def sonarr_system_status() -> StatusResult:
        policy.check("sonarr.system_status", Tag.READ)
        result = await get_api_v3_system_status.asyncio(client=client)
        if result is None:
            raise ToolError(message=f"{_SERVICE}.system_status: empty response from {base_url}")
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
        name="sonarr.series_search",
        description=(
            "Search Sonarr's existing library (already-added series) by free-text title. "
            "Returns ranked candidates with stable Sonarr ids and TVDB ids. Use this when "
            "the user asks 'do I have show X?' or 'what's in my library matching Y?'. "
            "Use ``sonarr.series_lookup`` instead to discover shows that AREN'T already added. "
            "When ``ambiguous: true`` is returned, follow up by passing the Sonarr id of "
            "the desired candidate to other tools."
        ),
    )
    async def sonarr_series_search(args: SeriesSearchInput) -> SearchResult:
        policy.check("sonarr.series_search", Tag.READ)
        series_list = await get_api_v3_series.asyncio(client=client)
        if series_list is None:
            return SearchResult(query=args.query, count=0, total=0, items=[])

        # Score series against the query. Use normalized title containment plus
        # optional year filter.
        q_norm = normalize(args.query)
        matches: list[SeriesResource] = []
        for s in series_list:
            title = _str_or_none(s.title) or ""
            if not title_contains(title, args.query) and q_norm not in normalize(title):
                continue
            if args.year is not None and _int_or_none(s.year) != args.year:
                continue
            matches.append(s)

        total = len(matches)
        truncated = total > args.limit
        items = [_series_to_summary(s) for s in matches[: args.limit]]
        return SearchResult(
            query=args.query,
            count=len(items),
            total=total,
            truncated=truncated,
            items=items,
        )

    @mcp.tool(
        name="sonarr.series_lookup",
        description=(
            "Search TVDB through Sonarr to discover series that could be ADDED to the library. "
            "Use this *before* ``sonarr.series_add`` — the ``tvdb_id`` field of each candidate "
            "is the value ``series_add`` requires. Each result includes ``already_added: bool`` "
            "so you can avoid duplicate-add attempts. For searching the current library, use "
            "``sonarr.series_search`` instead."
        ),
    )
    async def sonarr_series_lookup(args: SeriesLookupInput) -> LookupResult:
        policy.check("sonarr.series_lookup", Tag.READ)
        results = await get_api_v3_series_lookup.asyncio(client=client, term=args.query)
        if not results:
            return LookupResult(query=args.query, candidates=[])
        candidates = [_series_to_summary(r) for r in results[: args.limit]]
        return LookupResult(query=args.query, candidates=candidates)

    @mcp.tool(
        name="sonarr.queue",
        description=(
            "List active downloads in Sonarr's queue. Returns at most ``limit`` items "
            "with progress percentage, ETA, and download client. Use this to answer "
            "'what's downloading?' or to investigate stuck downloads."
        ),
    )
    async def sonarr_queue(args: QueueInput) -> QueueResult:
        policy.check("sonarr.queue", Tag.READ)
        page = await get_api_v3_queue.asyncio(
            client=client,
            page=1,
            page_size=args.limit,
            include_unknown_series_items=args.include_unknown_series,
            include_series=True,
            include_episode=True,
        )
        if page is None or page.records is None or isinstance(page.records, type(UNSET)):
            return QueueResult(count=0, total=0, items=[])
        records = list(page.records)  # type: ignore[arg-type]
        items = [_queue_record_to_item(r) for r in records]
        total = _int_or_none(page.total_records) or len(items)
        return QueueResult(count=len(items), total=total, items=items)

    @mcp.tool(
        name="sonarr.calendar",
        description=(
            "List upcoming or recently-aired episodes. Defaults to a 2-days-back + "
            "14-days-forward window suitable for 'what's airing this week?' queries. "
            "Set ``days_back=0`` to see only future episodes."
        ),
    )
    async def sonarr_calendar(args: CalendarInput) -> CalendarResult:
        policy.check("sonarr.calendar", Tag.READ)
        import datetime as _dt

        now = _dt.datetime.now(_dt.UTC)
        start = now - _dt.timedelta(days=args.days_back)
        end = now + _dt.timedelta(days=args.days_forward)
        episodes = await get_api_v3_calendar.asyncio(
            client=client,
            start=start,
            end=end,
            unmonitored=args.unmonitored,
            include_series=True,
            include_episode_file=True,
            include_episode_images=False,
        )
        if not episodes:
            return CalendarResult(count=0, items=[])
        items = [_episode_to_calendar(e) for e in episodes]
        return CalendarResult(count=len(items), items=items)

    @mcp.tool(
        name="sonarr.missing",
        description=(
            "List monitored episodes that have aired but aren't on disk. Useful for "
            "answering 'what am I missing?' or proactively triggering re-search. "
            "Returns the oldest-first up to ``limit``."
        ),
    )
    async def sonarr_missing(args: MissingInput) -> MissingResult:
        policy.check("sonarr.missing", Tag.READ)
        page = await get_api_v3_wanted_missing.asyncio(
            client=client,
            page=1,
            page_size=args.limit,
            sort_key="airDateUtc",
            sort_direction=UNSET,
            include_series=True,
            monitored=args.monitored_only,
        )
        if page is None or page.records is None or isinstance(page.records, type(UNSET)):
            return MissingResult(count=0, total=0, items=[])
        records = list(page.records)  # type: ignore[arg-type]
        items = [_episode_to_missing(e) for e in records]
        total = _int_or_none(page.total_records) or len(items)
        return MissingResult(count=len(items), total=total, items=items)

    # --- WRITE tools ---

    @mcp.tool(
        name="sonarr.series_add",
        description=(
            "Add a new series to Sonarr by TVDB id. Call ``sonarr.series_lookup`` first "
            "to obtain the ``tvdb_id``. Omit ``quality_profile_id`` and ``root_folder_path`` "
            "to use Sonarr's defaults (first profile, first root folder). Triggers an "
            "initial search for missing episodes unless ``search_for_missing_episodes=False``. "
            "Idempotent: if the series is already added, returns the existing id with "
            "``already_added: true`` rather than failing."
        ),
    )
    async def sonarr_series_add(args: SeriesAddInput) -> AddResult:
        policy.check("sonarr.series_add", Tag.WRITE)

        # Idempotency: check whether the series is already added.
        existing = await get_api_v3_series.asyncio(client=client, tvdb_id=args.tvdb_id)
        if existing:
            row = existing[0]
            sid = _int_or_none(row.id)
            if sid is not None:
                return AddResult(
                    sonarr_id=sid,
                    tvdb_id=args.tvdb_id,
                    title=_str_or_none(row.title) or "<unknown>",
                    already_added=True,
                    msg=f"already in library as sonarr_id={sid}",
                )

        # Look up the series on TVDB to get the metadata Sonarr needs to add it.
        lookup = await get_api_v3_series_lookup.asyncio(client=client, term=f"tvdb:{args.tvdb_id}")
        if not lookup:
            raise ToolError(
                message=f"sonarr.series_add: tvdb_id={args.tvdb_id} not found on TVDB",
                hint="call sonarr.series_lookup with a title query first to confirm the tvdb_id",
            )
        candidate = lookup[0]

        body = _build_add_body(candidate, args)
        added = await post_api_v3_series.asyncio(client=client, body=body)
        if added is None:
            raise ToolError(
                message="sonarr.series_add: Sonarr accepted the add but returned no payload",
                hint="check Sonarr's UI; the series may still have been added",
            )
        sid = _int_or_none(added.id)
        return AddResult(
            sonarr_id=sid or 0,
            tvdb_id=args.tvdb_id,
            title=_str_or_none(added.title) or "<unknown>",
            already_added=False,
            msg=f"added sonarr_id={sid}",
        )

    # --- DESTRUCTIVE tools ---

    @mcp.tool(
        name="sonarr.series_delete",
        description=(
            "Remove a series from Sonarr. DESTRUCTIVE. Call once WITHOUT ``confirm_token`` "
            "to receive a plan + token; the second call WITH the token executes the delete. "
            "Set ``delete_files=true`` to also remove files from disk (use with care). "
            "The token is single-use and expires after 5 minutes."
        ),
    )
    async def sonarr_series_delete(args: SeriesDeleteInput) -> DeletePlan | DeleteResult:
        policy.check("sonarr.series_delete", Tag.DESTRUCTIVE)

        # Resolve the target series so the plan is self-describing.
        target = await _get_series_by_id(client, args.sonarr_id)
        target_summary = _series_to_summary(target)

        fp = fingerprint(
            {
                "sonarr_id": args.sonarr_id,
                "delete_files": args.delete_files,
                "exclusion": args.add_import_list_exclusion,
            }
        )

        if args.confirm_token is None:
            token = policy.issue_token("sonarr.series_delete", fp)
            files_msg = "AND delete files on disk" if args.delete_files else "keep files on disk"
            return DeletePlan(
                confirm_token=token,
                summary=(f"remove {target_summary.title!r} (sonarr_id={target_summary.sonarr_id}) from Sonarr; {files_msg}"),
                target=target_summary,
                expires_in_seconds=policy.confirm_token_ttl_seconds,
            )

        # Execute path: validate the token, then delete.
        policy.consume_token("sonarr.series_delete", fp, args.confirm_token)
        await delete_api_v3_series_id.asyncio_detailed(
            id=args.sonarr_id,
            client=client,
            delete_files=args.delete_files,
            add_import_list_exclusion=args.add_import_list_exclusion,
        )
        return DeleteResult(
            deleted_sonarr_id=args.sonarr_id,
            title=target_summary.title,
            files_deleted=args.delete_files,
            msg=f"deleted sonarr_id={args.sonarr_id}",
        )

    log.info(
        "sonarr.tools registered",
        url=base_url,
        read_only=policy.read_only,
        disable_destructive=policy.disable_destructive,
    )


# --- internal helpers ---


async def _get_series_by_id(client: object, sonarr_id: int) -> SeriesResource:
    """Wrapper around the generated single-series GET to keep the call shape consistent.

    The generated function is `get_api_v3_series_id.asyncio(id=..., client=...)`;
    pulling it out here makes the tool body easier to read.
    """
    from arr_stack_mcp.generated.sonarr.api.series import get_api_v3_series_id

    result = await get_api_v3_series_id.asyncio(id=sonarr_id, client=client)  # type: ignore[arg-type]
    if result is None:
        raise ToolError(
            message=f"sonarr: series id {sonarr_id} not found",
            hint="call sonarr.series_search to discover valid sonarr_id values",
        )
    return result


def _build_add_body(candidate: SeriesResource, args: SeriesAddInput) -> SeriesResource:
    """Construct the SeriesResource POST body from a lookup candidate.

    Fills in quality profile, root folder, monitor options. The generated
    SeriesResource model carries every field from the lookup result; we
    overwrite only the ones the agent has authority over.
    """
    options = AddSeriesOptions(
        ignore_episodes_with_files=False,
        ignore_episodes_without_files=False,
        monitor=_monitor_to_enum(args.monitor),
        search_for_missing_episodes=args.search_for_missing_episodes,
        search_for_cutoff_unmet_episodes=False,
    )
    if args.quality_profile_id is not None:
        candidate.quality_profile_id = args.quality_profile_id
    if args.root_folder_path is not None:
        candidate.root_folder_path = args.root_folder_path
    candidate.monitored = True
    candidate.add_options = options
    return candidate


def _monitor_to_enum(monitor: str):  # type: ignore[no-untyped-def]
    """Translate the friendly monitor string to the generated enum.

    The Sonarr OpenAPI uses ``MonitorTypes`` with values like ``all``, ``future``,
    ``existing`` — case-insensitive. The generated enum lives at
    ``arr_stack_mcp.generated.sonarr.models.monitor_types``. Return type is left
    unannotated so the (excluded-from-mypy) generated module is the source of truth.
    """
    from arr_stack_mcp.generated.sonarr.models.monitor_types import MonitorTypes

    return MonitorTypes(monitor)


def _series_to_summary(s: SeriesResource) -> SeriesSummary:
    """Compact view of a SeriesResource — drops fields the LLM rarely needs."""
    stats = s.statistics
    episode_count = None
    episode_file_count = None
    size_on_disk = None
    if stats is not None and not isinstance(stats, type(UNSET)):
        episode_count = _int_or_none(getattr(stats, "episode_count", None))
        episode_file_count = _int_or_none(getattr(stats, "episode_file_count", None))
        size_on_disk = _int_or_none(getattr(stats, "size_on_disk", None))
    return SeriesSummary(
        sonarr_id=_int_or_none(s.id) or 0,
        tvdb_id=_int_or_none(s.tvdb_id),
        imdb_id=_str_or_none(s.imdb_id),
        title=_str_or_none(s.title) or "<unknown>",
        year=_int_or_none(s.year),
        status=_status_to_str(s.status),
        monitored=_bool_or_none(s.monitored) or False,
        episode_count=episode_count,
        episode_file_count=episode_file_count,
        size_on_disk=size_on_disk,
        path=_str_or_none(s.path),
    )


def _queue_record_to_item(r: object) -> QueueItem:
    """Map a QueueResource row to our compact QueueItem."""
    title = _str_or_none(getattr(r, "title", None)) or "<unknown>"
    size = _int_or_none(getattr(r, "size", None)) or 0
    size_left = _int_or_none(getattr(r, "sizeleft", None)) or _int_or_none(getattr(r, "size_left", None)) or 0
    progress = 0.0 if size == 0 else (1.0 - (size_left / size)) * 100.0
    return QueueItem(
        queue_id=_int_or_none(getattr(r, "id", None)) or 0,
        series_id=_int_or_none(getattr(r, "series_id", None)),
        episode_id=_int_or_none(getattr(r, "episode_id", None)),
        title=title,
        status=_str_or_none(getattr(r, "status", None)) or "unknown",
        tracked_status=_str_or_none(getattr(r, "tracked_download_status", None)),
        progress_pct=round(progress, 1),
        size=size,
        size_left=size_left,
        estimated_completion=_dt_or_none(getattr(r, "estimated_completion_time", None)),
        download_client=_str_or_none(getattr(r, "download_client", None)),
        protocol=_str_or_none(getattr(r, "protocol", None)),
    )


def _episode_to_calendar(e: object) -> CalendarItem:
    """Map an EpisodeResource to a CalendarItem."""
    return CalendarItem(
        series_id=_int_or_none(getattr(e, "series_id", None)) or 0,
        series_title=_episode_series_title(e),
        season_number=_int_or_none(getattr(e, "season_number", None)) or 0,
        episode_number=_int_or_none(getattr(e, "episode_number", None)) or 0,
        title=_str_or_none(getattr(e, "title", None)) or "<unknown>",
        air_date_utc=_dt_or_none(getattr(e, "air_date_utc", None)),
        has_file=_bool_or_none(getattr(e, "has_file", None)) or False,
        monitored=_bool_or_none(getattr(e, "monitored", None)) or False,
    )


def _episode_to_missing(e: object) -> MissingEpisode:
    return MissingEpisode(
        series_id=_int_or_none(getattr(e, "series_id", None)) or 0,
        series_title=_episode_series_title(e),
        season_number=_int_or_none(getattr(e, "season_number", None)) or 0,
        episode_number=_int_or_none(getattr(e, "episode_number", None)) or 0,
        title=_str_or_none(getattr(e, "title", None)) or "<unknown>",
        air_date_utc=_dt_or_none(getattr(e, "air_date_utc", None)),
    )


def _episode_series_title(e: object) -> str:
    """Pull the series title off the embedded series object the EpisodeResource carries."""
    series = getattr(e, "series", None)
    if series is None or series is UNSET:
        return "<unknown>"
    return _str_or_none(getattr(series, "title", None)) or "<unknown>"


# --- coercion helpers around the generated UNSET sentinel ---


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


# Silence the unused-import warning that ruff sometimes raises for `Ambiguous`
# even though it's part of the public error vocabulary surfaced from this module.
__all__ = ["Ambiguous", "register_all"]
