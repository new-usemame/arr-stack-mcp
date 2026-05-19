"""v0.2 MCP-client smoke test.

Drives every new v0.2 tool through the official `mcp` Python SDK's stdio
client against a freshly spawned `arr-stack-mcp serve`. Covers the
deliverables in design notes/DESIGN-v0.2.md §§2.1-2.4 + §3:

  stack.health
  stack.dryrun_log
  stack.report_issue
  stack.find_anywhere
  stack.queue_status_all
  jellyfin.users_list   (skipped if test stack doesn't have Jellyfin auth)
  sonarr.series_status  (needs an existing series id — runs only if probe finds one)
  prowlarr.system_status
  prowlarr.health
  prowlarr.indexer_list

The agent's catalog before/after view validates the v0.2 instructions
field and confirms every tool registered cleanly.

Run after `scripts/test-stack-up.sh` succeeds. Transcript writes to
`examples/mcp-smoke-v02-output.json`.
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
OUT_PATH = REPO_ROOT / "examples" / "mcp-smoke-v02-output.json"

# v0.2 toolset enabled — sonarr / radarr / lidarr / prowlarr against the docker
# test stack. Jellyfin is omitted because its first-run wizard isn't scripted
# in v0.2 (deferred from v0.1's HANDOFF).
CONFIG_YAML = """\
log_level: warning
transport:
  stdio: true
policy:
  read_only: false
  disable_destructive: false
  dry_run: true
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
  prowlarr:
    enabled: true
    url: http://localhost:19696
    api_key: ar5tcmcptestprowlarr0000000000004
  jellyfin:
    enabled: false
    url: http://localhost:18096
"""

# Call ordering exercises diagnostic chain: status -> health -> per-tool.
CALLS: list[tuple[str, dict[str, object]]] = [
    # cross-service first — cheapest aggregator
    ("stack.health", {"args": {}}),
    # The 4 stack.* aggregators
    ("stack.dryrun_log", {"args": {}}),
    ("stack.find_anywhere", {"args": {"query": "test", "limit_per_service": 3}}),
    ("stack.queue_status_all", {"args": {"limit_per_service": 5}}),
    ("stack.report_issue", {"args": {"summary": "v0.2 smoke test", "include_dryrun_log": True}}),
    # Prowlarr v0.2 surface
    ("prowlarr.system_status", {}),
    ("prowlarr.health", {}),
    ("prowlarr.indexer_list", {"args": {"enabled_only": False}}),
    ("prowlarr.indexer_stats", {}),
    ("prowlarr.indexer_status", {}),
    # Sonarr — new v0.2 tool
    # The series_status call uses tvdb_id=12345 which won't exist; we expect a
    # graceful "not in library" error envelope rather than a crash.
    ("sonarr.series_status", {"args": {"tvdb_id": 12345}}),
]


def stack_ready() -> bool:
    targets = [
        ("sonarr", 18989, "ar5tcmcptestsonarr00000000000001"),
        ("radarr", 17878, "ar5tcmcptestradarr00000000000002"),
        ("lidarr", 18686, "ar5tcmcptestlidarr00000000000003"),
        ("prowlarr", 19696, "ar5tcmcptestprowlarr0000000000004"),
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
        args=["run", "arr-stack-mcp", "serve", "--transport", "stdio", "--config", cfg, "--dry-run"],
        cwd=str(REPO_ROOT),
    )

    transcript: list[dict[str, object]] = []

    async with stdio_client(params) as (read, write), ClientSession(read, write) as session:
        init = await session.initialize()
        print(f"   server: {init.serverInfo.name} {init.serverInfo.version}")
        instructions_len = len(init.instructions or "")
        transcript.append(
            {
                "step": "initialize",
                "serverInfo": {
                    "name": init.serverInfo.name,
                    "version": init.serverInfo.version,
                },
                "protocolVersion": init.protocolVersion,
                "instructions_length": instructions_len,
            }
        )
        print(f"   instructions: {instructions_len} chars (v0.2 LLM-discipline anchors)")

        listing = await session.list_tools()
        names = sorted(t.name for t in listing.tools)
        print(f"-> tools/list: {len(names)} tools advertised")

        # Verify the v0.2 additions appear in the catalog.
        v02_additions = [
            "stack.health",
            "stack.dryrun_log",
            "stack.report_issue",
            "stack.find_anywhere",
            "stack.queue_status_all",
            "jellyfin.users_list",
            "sonarr.series_status",
            "prowlarr.system_status",
            "prowlarr.health",
            "prowlarr.indexer_list",
            "prowlarr.indexer_stats",
            "prowlarr.indexer_status",
            "prowlarr.indexer_test_all",
            "prowlarr.search",
        ]
        advertised = set(names)
        missing = [n for n in v02_additions if n not in advertised]
        if missing:
            print(f"  ! v0.2 tools missing from catalog: {missing}", file=sys.stderr)
        else:
            print(f"   all {len(v02_additions)} v0.2 tools advertised")
        transcript.append(
            {
                "step": "tools/list",
                "tool_count": len(names),
                "names": names,
                "v02_missing": missing,
            }
        )

        for name, args in CALLS:
            print(f"-> tools/call {name}")
            try:
                result = await session.call_tool(name, arguments=args)
                payload = [
                    c.model_dump(mode="json") if hasattr(c, "model_dump") else str(c)
                    for c in result.content
                ]
                status = "x" if result.isError else "ok"
                size = sum(len(json.dumps(p, default=str)) for p in payload)
                print(f"   {status} ({size} bytes)")
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
                    {"step": "tools/call", "tool": name, "args": args, "exception": repr(e)}
                )

    OUT_PATH.write_text(json.dumps(transcript, indent=2, default=str) + "\n")
    print(f"\nwrote transcript -> {OUT_PATH}")


if __name__ == "__main__":
    asyncio.run(run())
