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
) -> None:
    """Boot the MCP server. Pure orchestration; the per-service registration lives in arr_stack_mcp.tools.*."""
    cfg = load_config(config_path)
    policy = Policy.from_config(
        cfg.policy,
        read_only=read_only or cfg.policy.read_only,
        disable_destructive=disable_destructive or cfg.policy.disable_destructive,
    )
    mcp = build_server(cfg, policy)

    log.info(
        "starting",
        transport=transport,
        toolsets=sorted(s.name for s in _enabled_services(cfg)),
        read_only=policy.read_only,
        disable_destructive=policy.disable_destructive,
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

    Names the active services and the active risk-tolerance flags so the agent
    knows what's safe to call.
    """
    enabled = ", ".join(s.name for s in _enabled_services(cfg)) or "none"
    flags = []
    if cfg.policy.read_only:
        flags.append("read-only mode")
    if cfg.policy.disable_destructive:
        flags.append("destructive tools disabled")
    flag_str = f" ({'; '.join(flags)})" if flags else ""
    return (
        f"arr-stack-mcp gives you tools to query and control the user's *arr media stack and Jellyfin. "
        f"Active services: {enabled}{flag_str}. "
        f"Every destructive operation requires a confirm token. "
        f"Prefer `*.search` over `*.lookup_external` when the user asks about existing library content."
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
