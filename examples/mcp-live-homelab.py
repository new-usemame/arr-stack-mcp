"""Live home-lab read-only sweep.

Drives arr-stack-mcp v0.1.0 against the operator's production stack
(teenyverse:8989/7878/8686, transcoder:8096) with ``policy.read_only: true``
hard-set so no tool tagged write or destructive can fire. Records the
transcript to ``examples/mcp-live-homelab-output.json``.

Run when v0.1.0 is published and the operator wants a real-data sanity
check. Does NOT touch torrent / VPN / download paths — only read endpoints.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import tempfile
from pathlib import Path

import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = REPO_ROOT / "examples" / "mcp-live-homelab-output.json"

CONFIG_YAML_TMPL = """\
log_level: warning
transport:
  stdio: true
policy:
  # Hard read-only: every tool tagged write or destructive is skipped at
  # registration. Even if the LLM tries to call series_add or movie_delete,
  # the server returns PolicyDenied without touching the upstream.
  read_only: true
  disable_destructive: true
services:
  sonarr:
    enabled: true
    url: https://teenyverse.lan:8989
    api_key: ${SONARR_API_KEY}
    verify_tls: false
  radarr:
    enabled: true
    url: https://teenyverse.lan:7878
    api_key: ${RADARR_API_KEY}
    verify_tls: false
  lidarr:
    enabled: true
    url: https://teenyverse.lan:8686
    api_key: ${LIDARR_API_KEY}
    verify_tls: false
  jellyfin:
    enabled: true
    url: http://transcoder.lan:8096
    api_key: ${JELLYFIN_API_KEY}
"""

# Read-only-only call set. No *_add, no *_delete, no scan_library.
CALLS: list[tuple[str, dict[str, object]]] = [
    ("sonarr.system_status", {}),
    ("radarr.system_status", {}),
    ("lidarr.system_status", {}),
    ("jellyfin.system_info", {}),
    ("sonarr.series_search", {"args": {"query": "the", "limit": 5}}),
    ("radarr.movie_search", {"args": {"query": "dune", "limit": 5}}),
    ("lidarr.artist_search", {"args": {"query": "the", "limit": 5}}),
    ("sonarr.queue", {"args": {"limit": 10}}),
    ("radarr.queue", {"args": {"limit": 10}}),
    ("sonarr.calendar", {"args": {"days_back": 3, "days_forward": 7}}),
]


def ping_live() -> bool:
    targets = [
        ("sonarr",   "https://teenyverse.lan:8989/ping",  os.environ.get("SONARR_API_KEY", "")),
        ("radarr",   "https://teenyverse.lan:7878/ping",  os.environ.get("RADARR_API_KEY", "")),
        ("lidarr",   "https://teenyverse.lan:8686/ping",  os.environ.get("LIDARR_API_KEY", "")),
        ("jellyfin", "http://transcoder.lan:8096/System/Info/Public", None),
    ]
    for name, url, key in targets:
        try:
            with httpx.Client(timeout=3.0, verify=False) as c:
                headers = {"X-Api-Key": key} if key else {}
                r = c.get(url, headers=headers)
            if r.status_code >= 500:
                print(f"  ! {name} returned {r.status_code}", file=sys.stderr)
                return False
        except httpx.HTTPError as e:
            print(f"  ! {name} unreachable ({e})", file=sys.stderr)
            return False
    return True


async def run() -> None:
    required = ["SONARR_API_KEY", "RADARR_API_KEY", "LIDARR_API_KEY", "JELLYFIN_API_KEY"]
    missing = [k for k in required if not os.environ.get(k)]
    if missing:
        print(f"missing env vars: {missing}", file=sys.stderr)
        sys.exit(2)

    if not ping_live():
        print("home lab not reachable", file=sys.stderr)
        sys.exit(2)

    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as f:
        f.write(CONFIG_YAML_TMPL)
        cfg = f.name

    print(f"-> spawning arr-stack-mcp serve --transport stdio (READ-ONLY against live homelab)")
    params = StdioServerParameters(
        command="uv",
        args=["run", "arr-stack-mcp", "serve", "--transport", "stdio", "--config", cfg],
        cwd=str(REPO_ROOT),
        env={**os.environ},
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
            print(f"-> tools/list: {len(names)} tools advertised (read-only filter applied)")
            transcript.append({"step": "tools/list", "tool_count": len(names), "names": names})

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
