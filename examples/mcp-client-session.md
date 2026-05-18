# MCP client live verification — v0.1.0

End-to-end exercise of the arr-stack-mcp v0.1.0 server through the official
MCP Python SDK's stdio client, against the dockerised test stack.

`examples/mcp-smoke.py` spawns `arr-stack-mcp serve --transport stdio`, walks
the full MCP handshake (`initialize` → `notifications/initialized` →
`tools/list` → N × `tools/call`), and writes the raw transcript to
`examples/mcp-smoke-output.json`.

## Reproducing

```
scripts/test-stack-up.sh        # boots Sonarr / Radarr / Lidarr / Prowlarr / Jellyfin
uv run python examples/mcp-smoke.py
```

The smoke script auto-skips if any test container isn't reachable.

## Recorded result

- Server: `arr-stack-mcp 1.27.1` (MCP SDK version reported by FastMCP)
- Protocol: `2025-11-25`
- Tools advertised: **23** (Sonarr 8, Radarr 8, Lidarr 7) — Jellyfin disabled in
  the test config because its first-run wizard hasn't been scripted yet
- Tool calls exercised:

| Tool | Outcome | Notes |
|---|---|---|
| `sonarr.system_status` | ok | version 4.0.16.2944, `is_docker=true` |
| `radarr.system_status` | ok | version 6.0.4.10291 |
| `lidarr.system_status` | ok | version 3.1.0.4875 |
| `sonarr.series_search` | ok | fresh container, empty library (count 0) |
| `radarr.movie_lookup`  | ok | real TMDB hits for "Dune" returned |

## What this verifies

- The MCP stdio JSON-RPC handshake works end-to-end against the published
  server entry point (`arr-stack-mcp serve --transport stdio`).
- The dotted tool naming (`sonarr.system_status`, etc.) survives the protocol
  encode/decode and reaches a real MCP client with the same names FastMCP
  registered them under.
- Three pillar verbs exercised: `*_status` (health), `*_search` (library
  read), `*_lookup` (external discovery returning TMDB live data).
- Pydantic input + output schemas round-trip through the MCP wire format.
- The full text payload of each response is in `mcp-smoke-output.json` for
  reviewer-side inspection.

## Known gap

Jellyfin tools (`jellyfin.system_info` etc.) aren't in this transcript. The
LinuxServer.io test container ships unconfigured; its first-run wizard
needs an HTTP scripted sequence to create an admin user and seed an API
key. That scripting is deferred to v0.2 along with the rest of the
Jellyfin write-path test coverage.
