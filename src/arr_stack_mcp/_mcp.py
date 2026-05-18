"""Single-file isolation of the upstream FastMCP import.

The MCP Python SDK migration notes mention a planned rename from `FastMCP` to
`MCPServer` at a future stable release. Keeping the import in one module limits
the blast radius of that rename to a one-line change here.
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

__all__ = ["FastMCP"]
