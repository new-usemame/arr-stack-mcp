"""radarr MCP tools. Fully populated in Phase D once the curated layer design is locked in."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import ServiceConfig
    from arr_stack_mcp.policy import Policy


def register_all(mcp: FastMCP, svc: ServiceConfig, policy: Policy) -> None:
    """Phase D: register every radarr tool here."""
    # Intentionally empty until Phase D wires in the curated tools.
