"""Prowlarr curated tool layer.

Seven tools land in v0.2: system_status, health, indexer_list,
indexer_stats, indexer_status, indexer_test_all, search. The full
upstream surface (93 paths) is wider than this; the v0.2 cut is the
subset that's workflow-relevant for diagnosing + searching, deliberately
excluding destructive operations (delete indexer, system restart) since
those are operator-decisions that belong in the Prowlarr web UI.

See notes/DESIGN-v0.2.md §2.1.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import structlog

from arr_stack_mcp.errors import ToolError
from arr_stack_mcp.generated.prowlarr.api.health import get_api_v1_health
from arr_stack_mcp.generated.prowlarr.api.indexer import (
    get_api_v1_indexer,
    post_api_v1_indexer_testall,
)
from arr_stack_mcp.generated.prowlarr.api.indexer_stats import get_api_v1_indexerstats
from arr_stack_mcp.generated.prowlarr.api.indexer_status import get_api_v1_indexerstatus
from arr_stack_mcp.generated.prowlarr.api.search import get_api_v1_search
from arr_stack_mcp.generated.prowlarr.api.system import get_api_v1_system_status
from arr_stack_mcp.policy import Tag
from arr_stack_mcp.tools.prowlarr._client import make_prowlarr_client
from arr_stack_mcp.tools.prowlarr._models import (
    HealthIssue,
    HealthResult,
    IndexerInput,
    IndexerListResult,
    IndexerStatsResult,
    IndexerStatsRow,
    IndexerStatusResult,
    IndexerStatusRow,
    IndexerSummary,
    SearchInput,
    SearchRelease,
    SearchResult,
    StatusResult,
    SystemStatus,
    TestAllInput,
    TestAllResult,
    TestAllRow,
)

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import ServiceConfig
    from arr_stack_mcp.policy import Policy


log = structlog.get_logger(__name__)
_SERVICE = "prowlarr"


def register_all(mcp: FastMCP, svc: ServiceConfig, policy: Policy) -> None:
    """Register every Prowlarr tool on the given MCP server.

    Pattern matches the other arrs: build the generated client once, register
    decorated handlers as closures over `client` + `svc` + `policy`. Tools
    that mutate state are skipped at registration when `--read-only` or
    `--disable-destructive` is active.
    """
    client = make_prowlarr_client(svc)
    base_url = str(svc.url).rstrip("/")

    @mcp.tool(
        name="prowlarr.system_status",
        description=(
            "Prowlarr system status (version, branch, runtime, instance name). Use first when "
            "diagnosing any Prowlarr problem to confirm reachability and learn the API version. "
            "Returns a compact dict."
        ),
    )
    async def prowlarr_system_status() -> StatusResult:
        policy.check("prowlarr.system_status", Tag.READ)
        result = await get_api_v1_system_status.asyncio(client=client)
        if result is None:
            raise ToolError(message=f"{_SERVICE}.system_status: empty response from {base_url}")
        return StatusResult(
            url=base_url,
            status=SystemStatus(
                version=str(getattr(result, "version", "") or ""),
                branch=_safe_str(getattr(result, "branch", None)),
                runtime_version=_safe_str(getattr(result, "runtime_version", None)),
                is_production=_safe_bool(getattr(result, "is_production", None)),
                is_admin=_safe_bool(getattr(result, "is_admin", None)),
                is_docker=_safe_bool(getattr(result, "is_docker", None)),
                start_time=_safe_dt(getattr(result, "start_time", None)),
                instance_name=_safe_str(getattr(result, "instance_name", None)),
            ),
        )

    @mcp.tool(
        name="prowlarr.health",
        description=(
            "Prowlarr health-check issues. Returns the list of warnings / errors Prowlarr reports "
            "(misconfigured indexers, missing categories, unreachable services, etc.). An empty list "
            "is the all-clear. Each issue carries `source`, `type` (notice / warning / error), "
            "`message`, and a `wiki_url` link with the upstream explanation."
        ),
    )
    async def prowlarr_health() -> HealthResult:
        policy.check("prowlarr.health", Tag.READ)
        issues_raw = await get_api_v1_health.asyncio(client=client)
        if not isinstance(issues_raw, list):
            return HealthResult(count=0, issues=[])
        items = [_health_to_issue(h) for h in issues_raw]
        return HealthResult(count=len(items), issues=items)

    @mcp.tool(
        name="prowlarr.indexer_list",
        description=(
            "List configured Prowlarr indexers. Returns id, name, implementation (Newznab / Torznab / "
            "Cardigann / specific tracker), protocol (usenet / torrent), priority, enable state, and "
            "tags. Pass `enabled_only=true` to filter out disabled indexers."
        ),
    )
    async def prowlarr_indexer_list(args: IndexerInput) -> IndexerListResult:
        policy.check("prowlarr.indexer_list", Tag.READ)
        rows = await get_api_v1_indexer.asyncio(client=client)
        if not isinstance(rows, list):
            return IndexerListResult(count=0, items=[])
        items = [_indexer_to_summary(r) for r in rows]
        if args.enabled_only:
            items = [it for it in items if it.enable]
        return IndexerListResult(count=len(items), items=items)

    @mcp.tool(
        name="prowlarr.indexer_stats",
        description=(
            "Per-indexer query / grab / failure counts and average response time. Use when "
            "diagnosing why a download isn't being found — a high `num_failed_queries` on the "
            "responsible indexer points at the cause."
        ),
    )
    async def prowlarr_indexer_stats() -> IndexerStatsResult:
        policy.check("prowlarr.indexer_stats", Tag.READ)
        page = await get_api_v1_indexerstats.asyncio(client=client)
        if page is None:
            return IndexerStatsResult(count=0, items=[])
        rows_raw = getattr(page, "indexers", None)
        if not isinstance(rows_raw, list):
            return IndexerStatsResult(count=0, items=[])
        items = [_stats_to_row(r) for r in rows_raw]
        return IndexerStatsResult(count=len(items), items=items)

    @mcp.tool(
        name="prowlarr.indexer_status",
        description=(
            "List indexers currently in a failing state. Each row has `indexer_id`, `disabled_till` "
            "(when Prowlarr will retry), `most_recent_failure`, and `initial_failure`. An empty list "
            "is the all-clear; failing indexers here explain a high `num_failed_queries` from "
            "`prowlarr.indexer_stats`."
        ),
    )
    async def prowlarr_indexer_status() -> IndexerStatusResult:
        policy.check("prowlarr.indexer_status", Tag.READ)
        rows = await get_api_v1_indexerstatus.asyncio(client=client)
        if not isinstance(rows, list):
            return IndexerStatusResult(count=0, items=[])
        items = [_status_to_row(r) for r in rows]
        return IndexerStatusResult(count=len(items), items=items)

    @mcp.tool(
        name="prowlarr.indexer_test_all",
        description=(
            "Trigger Prowlarr's test-every-indexer probe. Returns one row per indexer with "
            "`is_valid` and any `validation_failures`. WRITE: triggers test queries against every "
            "configured indexer, rate-limited at the upstream side. Useful as a 'is my indexer set "
            "working?' diagnostic after configuration changes."
        ),
    )
    async def prowlarr_indexer_test_all(args: TestAllInput) -> TestAllResult:
        del args  # FastMCP rejects underscore-prefixed param names; the input is empty by design.
        policy.check("prowlarr.indexer_test_all", Tag.WRITE)
        resp = await post_api_v1_indexer_testall.asyncio_detailed(client=client)
        # The endpoint returns a JSON array on 200. The generated thin client
        # surfaces it via `resp.parsed`; on some Prowlarr versions the parsed
        # shape lands as a list of dicts. Coerce defensively.
        body = getattr(resp, "parsed", None)
        if not isinstance(body, list):
            return TestAllResult(count=0, pass_count=0, fail_count=0, items=[])
        items = [_testall_to_row(r) for r in body]
        pass_count = sum(1 for r in items if r.is_valid)
        fail_count = len(items) - pass_count
        return TestAllResult(
            count=len(items),
            pass_count=pass_count,
            fail_count=fail_count,
            items=items,
        )

    @mcp.tool(
        name="prowlarr.search",
        description=(
            "Search Prowlarr-aggregated indexers for release candidates. Returns title, indexer, "
            "size, age, seeders / leechers, and category ids. Tagged READ — Prowlarr just queries; "
            "the agent does NOT act on release titles directly. To actually grab a release, use "
            "`sonarr.series_add` / `radarr.movie_add` / `lidarr.artist_add` with the catalog id "
            "(TVDB / TMDB / MusicBrainz), not the release title from this result."
        ),
    )
    async def prowlarr_search(args: SearchInput) -> SearchResult:
        policy.check("prowlarr.search", Tag.READ)
        rows = await get_api_v1_search.asyncio(
            client=client,
            query=args.query,
            indexer_ids=args.indexer_ids or [],
            categories=args.categories or [],
            type_=args.search_type,
            limit=args.limit,
        )
        if not isinstance(rows, list):
            return SearchResult(query=args.query, count=0, items=[])
        items = [_release_to_compact(r) for r in rows[: args.limit]]
        return SearchResult(query=args.query, count=len(items), items=items)

    log.info(
        "prowlarr.tools registered",
        url=base_url,
        read_only=policy.read_only,
        disable_destructive=policy.disable_destructive,
    )


# ---------- projection helpers ----------


def _health_to_issue(h: object) -> HealthIssue:
    type_raw = getattr(h, "type_", None) or getattr(h, "type", None)
    return HealthIssue(
        source=_safe_str(getattr(h, "source", None)),
        type=_safe_str(type_raw),
        message=str(getattr(h, "message", "") or "<unknown>"),
        wiki_url=_safe_str(getattr(h, "wiki_url", None)),
    )


def _indexer_to_summary(r: object) -> IndexerSummary:
    tags_raw = getattr(r, "tags", None)
    tags = [int(t) for t in tags_raw] if isinstance(tags_raw, list) else []
    return IndexerSummary(
        id=int(getattr(r, "id", 0) or 0),
        name=str(getattr(r, "name", "") or "<unknown>"),
        implementation=_safe_str(getattr(r, "implementation", None)),
        protocol=_safe_str(getattr(r, "protocol", None)),
        priority=_safe_int(getattr(r, "priority", None)),
        enable=bool(getattr(r, "enable", False)),
        tags=tags,
    )


def _stats_to_row(r: object) -> IndexerStatsRow:
    return IndexerStatsRow(
        indexer_id=int(getattr(r, "indexer_id", 0) or 0),
        indexer_name=str(getattr(r, "indexer_name", "") or "<unknown>"),
        num_queries=int(getattr(r, "number_of_queries", 0) or 0),
        num_grabs=int(getattr(r, "number_of_grabs", 0) or 0),
        num_rss_queries=int(getattr(r, "number_of_rss_queries", 0) or 0),
        num_auth_queries=int(getattr(r, "number_of_auth_queries", 0) or 0),
        num_failed_queries=int(getattr(r, "number_of_failed_queries", 0) or 0),
        num_failed_grabs=int(getattr(r, "number_of_failed_grabs", 0) or 0),
        num_failed_rss_queries=int(getattr(r, "number_of_failed_rss_queries", 0) or 0),
        num_failed_auth_queries=int(getattr(r, "number_of_failed_auth_queries", 0) or 0),
        average_response_time=int(getattr(r, "average_response_time", 0) or 0),
    )


def _status_to_row(r: object) -> IndexerStatusRow:
    return IndexerStatusRow(
        indexer_id=int(getattr(r, "indexer_id", 0) or 0),
        disabled_till=_safe_dt(getattr(r, "disabled_till", None)),
        most_recent_failure=_safe_dt(getattr(r, "most_recent_failure", None)),
        initial_failure=_safe_dt(getattr(r, "initial_failure", None)),
    )


def _testall_to_row(r: object) -> TestAllRow:
    failures_raw = getattr(r, "validation_failures", None)
    if isinstance(failures_raw, list):
        failures = [str(getattr(f, "error_message", f) or "") for f in failures_raw]
    elif isinstance(r, dict) and isinstance(r.get("validationFailures"), list):
        failures = [str(f.get("errorMessage", "")) for f in r["validationFailures"]]
    else:
        failures = []
    if isinstance(r, dict):
        return TestAllRow(
            indexer_id=int(r.get("id", 0) or 0),
            is_valid=bool(r.get("isValid", False)),
            validation_failures=failures,
        )
    return TestAllRow(
        indexer_id=int(getattr(r, "id", 0) or 0),
        is_valid=bool(getattr(r, "is_valid", False)),
        validation_failures=failures,
    )


def _release_to_compact(r: object) -> SearchRelease:
    return SearchRelease(
        title=str(getattr(r, "title", "") or "<unknown>"),
        indexer=_safe_str(getattr(r, "indexer", None)),
        indexer_id=_safe_int(getattr(r, "indexer_id", None)),
        size=_safe_int(getattr(r, "size", None)),
        age_minutes=_safe_int(getattr(r, "age_minutes", None)) or _safe_int(getattr(r, "age", None)),
        seeders=_safe_int(getattr(r, "seeders", None)),
        leechers=_safe_int(getattr(r, "leechers", None)),
        categories=_categories(getattr(r, "categories", None)),
        protocol=_safe_str(getattr(r, "protocol", None)),
    )


def _categories(v: object) -> list[int]:
    if not isinstance(v, list):
        return []
    out: list[int] = []
    for c in v:
        cid = _safe_int(getattr(c, "id", None)) if not isinstance(c, int) else c
        if cid is not None:
            out.append(cid)
    return out


# ---------- shared safe-coerce helpers ----------


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


def _safe_bool(v: object) -> bool | None:
    if v is None:
        return None
    if isinstance(v, bool):
        return v
    return None


def _safe_dt(v: object) -> str | None:
    if v is None:
        return None
    if hasattr(v, "isoformat"):
        return v.isoformat()  # type: ignore[no-any-return]
    s = str(v)
    if s == "UNSET":
        return None
    return s
