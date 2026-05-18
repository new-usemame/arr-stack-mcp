"""End-to-end MCP-client smoke test.

Uses the official ``mcp`` Python SDK's stdio client to talk to a freshly
spawned ``arr-stack-mcp serve``. That's the same code path Claude Desktop
exercises — `mcp.client.stdio.stdio_client` is the canonical reference.

Run after ``scripts/test-stack-up.sh`` succeeds.
"""

from __future__ import annotations

import asyncio
import json
import sys
import tempfile
from pathlib import Path

import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = REPO_ROOT / "examples" / "mcp-smoke-output.json"

CONFIG_YAML = """\
log_level: warning
transport:
  stdio: true
policy:
  read_only: false
  disable_destructive: false
services:
  sonarr:
    enabled: true
    url: http://localhost:18989
    api_key: ar5tcmcptestsonarr00000000000001
  radarr:
    enabled: true
    url: http://localhost:17878
    api_key: ar5tcmcptestradarr00000000000002
  lidarr:
    enabled: true
    url: http://localhost:18686
    api_key: ar5tcmcptestlidarr00000000000003
  jellyfin:
    enabled: false
    url: http://localhost:18096
"""

CALLS: list[tuple[str, dict[str, object]]] = [
    ("sonarr.system_status", {}),
    ("radarr.system_status", {}),
    ("lidarr.system_status", {}),
    ("sonarr.series_search", {"args": {"query": "anything", "limit": 5}}),
    ("radarr.movie_lookup", {"args": {"query": "Dune", "limit": 3}}),
]


def stack_ready() -> bool:
    targets = [
        ("sonarr", 18989, "ar5tcmcptestsonarr00000000000001"),
        ("radarr", 17878, "ar5tcmcptestradarr00000000000002"),
        ("lidarr", 18686, "ar5tcmcptestlidarr00000000000003"),
    ]
    for name, port, key in targets:
        try:
            with httpx.Client(timeout=2.0) as c:
                r = c.get(f"http://localhost:{port}/ping", headers={"X-Api-Key": key})
            if r.status_code >= 500:
                print(f"  ! {name} returned {r.status_code}", file=sys.stderr)
                return False
        except httpx.HTTPError as e:
            print(f"  ! {name} unreachable on :{port} ({e})", file=sys.stderr)
            return False
    return True


async def run() -> None:
    if not stack_ready():
        print("test stack not healthy; run scripts/test-stack-up.sh first", file=sys.stderr)
        sys.exit(2)

    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        f.write(CONFIG_YAML)
        cfg = f.name

    print(f"-> spawning arr-stack-mcp serve --transport stdio --config {cfg}")
    params = StdioServerParameters(
        command="uv",
        args=["run", "arr-stack-mcp", "serve", "--transport", "stdio", "--config", cfg],
        cwd=str(REPO_ROOT),
    )

    transcript: list[dict[str, object]] = []

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            print(f"   server: {init.serverInfo.name} {init.serverInfo.version}")
            transcript.append(
                {
                    "step": "initialize",
                    "serverInfo": {
                        "name": init.serverInfo.name,
                        "version": init.serverInfo.version,
                    },
                    "protocolVersion": init.protocolVersion,
                }
            )

            listing = await session.list_tools()
            names = [t.name for t in listing.tools]
            print(f"-> tools/list: {len(names)} tools advertised")
            transcript.append({"step": "tools/list", "tool_count": len(names), "names": names})

            for name, args in CALLS:
                print(f"-> tools/call {name}")
                try:
                    result = await session.call_tool(name, arguments=args)
                    payload = [
                        c.model_dump(mode="json") if hasattr(c, "model_dump") else str(c)
                        for c in result.content
                    ]
                    if result.isError:
                        print(f"   x {payload!r}")
                    else:
                        print(f"   ok ({sum(len(json.dumps(p, default=str)) for p in payload)} bytes)")
                    transcript.append(
                        {
                            "step": "tools/call",
                            "tool": name,
                            "args": args,
                            "isError": result.isError,
                            "content": payload,
                        }
                    )
                except Exception as e:
                    print(f"   x exception: {e}")
                    transcript.append(
                        {
                            "step": "tools/call",
                            "tool": name,
                            "args": args,
                            "exception": repr(e),
                        }
                    )

    OUT_PATH.write_text(json.dumps(transcript, indent=2, default=str) + "\n")
    print(f"\nwrote transcript -> {OUT_PATH}")


if __name__ == "__main__":
    asyncio.run(run())
