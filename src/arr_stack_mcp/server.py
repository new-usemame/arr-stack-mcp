"""FastMCP entrypoint. Loads config, applies policy flags, registers enabled toolsets."""

from __future__ import annotations

from typing import TYPE_CHECKING

import structlog

from arr_stack_mcp._mcp import FastMCP
from arr_stack_mcp.config import Config, ServiceConfig, load_config
from arr_stack_mcp.policy import Policy

if TYPE_CHECKING:
    from collections.abc import Iterable

log = structlog.get_logger(__name__)


def run(
    *,
    config_path: str | None,
    transport: str,
    read_only: bool,
    disable_destructive: bool,
    dry_run: bool = False,
) -> None:
    """Boot the MCP server. Pure orchestration; the per-service registration lives in arr_stack_mcp.tools.*."""
    cfg = load_config(config_path)
    policy = Policy.from_config(
        cfg.policy,
        read_only=read_only or cfg.policy.read_only,
        disable_destructive=disable_destructive or cfg.policy.disable_destructive,
        dry_run=dry_run or cfg.policy.dry_run,
    )
    mcp = build_server(cfg, policy)

    log.info(
        "starting",
        transport=transport,
        toolsets=sorted(s.name for s in _enabled_services(cfg)),
        read_only=policy.read_only,
        disable_destructive=policy.disable_destructive,
        dry_run=policy.dry_run,
    )

    if transport == "stdio":
        mcp.run("stdio")
    elif transport in {"streamable-http", "http"}:
        mcp.run("streamable-http")
    else:
        raise ValueError(f"unknown transport: {transport!r}")


def build_server(cfg: Config, policy: Policy) -> FastMCP:
    """Construct the FastMCP server with every enabled toolset registered. Pulled out for testability."""
    mcp = FastMCP(name="arr-stack-mcp", instructions=_server_instructions(cfg))

    for svc in _enabled_services(cfg):
        _register_service(mcp, svc, cfg, policy)

    return mcp


def _server_instructions(cfg: Config) -> str:
    """Instructions string the MCP client passes to the agent at session start.

    Lifts LLM-facing discipline from ibis-bot's SYSTEM_PROMPT (output-discipline,
    confirm-token UX, disambiguation, error envelopes) minus the Matrix-specific
    bits. See notes/DESIGN-v0.2.md §1.1 for the porting rationale.
    """
    enabled = ", ".join(s.name for s in _enabled_services(cfg)) or "none"
    flags: list[str] = []
    if cfg.policy.read_only:
        flags.append("read-only mode")
    if cfg.policy.disable_destructive:
        flags.append("destructive tools disabled")
    flag_str = f" ({'; '.join(flags)})" if flags else ""
    # Implicit string concatenation inside the parenthesized return keeps each
    # source line under the 140-col ruff cap while preserving the on-wire
    # instructions text (no mid-paragraph line breaks).
    return (
        f"arr-stack-mcp exposes a unified tool surface for Sonarr, Radarr, Lidarr, Prowlarr, and Jellyfin."
        f" Active services: {enabled}{flag_str}.\n\n"
        "Result envelopes\n\n"
        "Every tool returns a self-describing pydantic envelope with `ok`, plus typed `items` / `count` /"
        " `total` / `candidates` fields as appropriate. Treat that envelope as the answer. Do not paraphrase"
        " its fields back to the user verbatim; your role is to interpret and act, not to re-render JSON.\n\n"
        "Confirm tokens for destructive operations\n\n"
        "Tools tagged DESTRUCTIVE (delete series / movies / artists / library items) follow a two-step"
        " pattern. The first call without `confirm_token` returns a plan envelope with `needs_confirm: true`,"
        " `confirm_token`, and a human-readable `summary`. The second call passes that same `confirm_token`"
        " and executes. Tokens are single-use, payload-bound, and expire after `confirm_token_ttl_seconds`"
        " (default 300s). The plan is already in the first envelope; you do not need to repeat the token to"
        " the user.\n\n"
        "Disambiguation\n\n"
        "When a lookup matches more than one library row, the server returns an `Ambiguous` error envelope"
        " with a `candidates` list, each carrying its stable id (`sonarr_id`, `radarr_id`, `lidarr_id`,"
        " `tvdb_id`, `tmdb_id`, `mbid`, Jellyfin item id). To pick one, retry the same tool with that id"
        " parameter (for example `sonarr_id=42`). Do not append fields to the original query string;"
        " appending the author or year to the title rarely matches what's in the library, while the id"
        " always does.\n\n"
        "Tool selection\n\n"
        "- `*.search` queries the existing library (already-added series / movies / artists / items)."
        " `*.lookup` (Sonarr / Radarr / Lidarr) queries the external catalog (TVDB / TMDB / MusicBrainz) for"
        " items the user could add. The id returned by `*.lookup` is what `*.add` requires. Idempotent add"
        " tools detect already-added by id and return `already_added: true`.\n"
        "- `*.system_status` is the cheapest read. Use it first when diagnosing connectivity or version"
        " concerns.\n"
        "- Prefer one bulk or aggregate call over N parallel per-service calls. Fanout fragments errors and"
        " multiplies token cost.\n\n"
        "Heuristics built into the server\n\n"
        "- Year tags embedded in titles (`Dune (2021)`, `BSG (2004)`, `TMNT (87)`) are extracted before the"
        " upstream lookup and re-applied as a year filter. Pass `year=N` for cleaner intent when the user"
        " explicitly named one.\n"
        "- Acronyms (`TMNT`, `LOTR`, `MCU`) resolve via initials when rapidfuzz's token-set ratio misses"
        " them. Jellyfin search falls back to a wider recursive scan automatically when the query looks like"
        " an acronym.\n\n"
        "Errors\n\n"
        "Each error envelope carries a `code` and a `hint`. `policy_denied` means the operator started the"
        " server with `--read-only` or `--disable-destructive`; the call shape is valid but the server gated"
        " it. Explain to the user; do not retry. `upstream_unavailable` means the underlying service did not"
        " respond; try `*.system_status` to verify reachability. `upstream_auth_failed` means the API key"
        " rotated or is wrong; the hint identifies the service. `confirm_required` means the two-step"
        " pattern was not honored; issue the first-call plan, then re-invoke with the token. `ambiguous`"
        " carries `candidates` per the disambiguation rule above.\n\n"
        "If a tool errors in a way you cannot explain, call `stack.report_issue` to capture the diagnostic"
        " context for the user to post upstream.\n"
    )


def _enabled_services(cfg: Config) -> Iterable[ServiceConfig]:
    """Iterate over services whose `enabled: true` flag is set."""
    return (svc for svc in cfg.services.values() if svc.enabled)


def _register_service(mcp: FastMCP, svc: ServiceConfig, cfg: Config, policy: Policy) -> None:
    """Dispatch to the per-service tool registration module."""
    # Deferred imports so a service that isn't enabled doesn't pay startup cost
    # for its generated client + tool module.
    match svc.name:
        case "sonarr":
            from arr_stack_mcp.tools.sonarr import register as register_sonarr

            register_sonarr(mcp, svc, policy)
        case "radarr":
            from arr_stack_mcp.tools.radarr import register as register_radarr

            register_radarr(mcp, svc, policy)
        case "lidarr":
            from arr_stack_mcp.tools.lidarr import register as register_lidarr

            register_lidarr(mcp, svc, policy)
        case "prowlarr":
            from arr_stack_mcp.tools.prowlarr import register as register_prowlarr

            register_prowlarr(mcp, svc, policy)
        case "jellyfin":
            from arr_stack_mcp.tools.jellyfin import register as register_jellyfin

            register_jellyfin(mcp, svc, policy)
        case other:
            raise ValueError(f"unknown service: {other!r}")
