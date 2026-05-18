"""PROWLARR tool surface. Registered with the MCP server when `services.prowlarr.enabled: true`."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import ServiceConfig
    from arr_stack_mcp.policy import Policy


def register(mcp: FastMCP, svc: ServiceConfig, policy: Policy) -> None:
    """Register every prowlarr tool on the given MCP server. Placeholder — Phase D fills this in."""
    from arr_stack_mcp.tools.prowlarr.tools import register_all

    register_all(mcp, svc, policy)
