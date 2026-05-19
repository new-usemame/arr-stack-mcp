"""Cross-service `stack.*` composables.

Always registered (no per-service `enabled:` gate); the dispatch from
`server.build_server` happens after the per-service registration loop.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import Config
    from arr_stack_mcp.policy import Policy


def register(mcp: FastMCP, cfg: Config, policy: Policy) -> None:
    """Register every stack.* tool. Always called once from `server.build_server`."""
    from arr_stack_mcp.tools.stack.tools import register_all

    register_all(mcp, cfg, policy)
