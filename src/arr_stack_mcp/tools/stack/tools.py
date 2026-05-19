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
    ReportIssueInput,
    ReportIssueResult,
    StackHealthInput,
    StackHealthResult,
    StackHealthService,
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
        name="stack.health",
        description=(
            "Probe every enabled service's `*.system_status` in parallel and return a compact "
            "reachability matrix. Each row has `name`, `enabled`, `reachable`, `version` (when "
            "reachable), and `error` (when not). `overall_ok` is True iff every enabled service is "
            "reachable AND reported a version. Use this first when diagnosing 'is something broken?' "
            "before drilling into any one service. Read-only."
        ),
    )
    async def stack_health(_args: StackHealthInput) -> StackHealthResult:
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
