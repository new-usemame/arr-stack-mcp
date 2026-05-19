# arr-stack-mcp

A Model Context Protocol server that exposes Sonarr, Radarr, Lidarr, and Jellyfin to any MCP client (Claude Desktop, Claude Code, n8n, ibis-bot, custom agents) through a hand-curated tool layer written for LLM consumption.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)

## What this gives an agent

28 curated tools split across four services:

| Service | Tools | Highlights |
|---|---|---|
| Sonarr | 8 | series search, TVDB lookup, queue, calendar, missing episodes, add/delete |
| Radarr | 8 | movie search, TMDB lookup, queue, calendar, missing, add/delete |
| Lidarr | 7 | artist + album search, MusicBrainz lookup, queue, add/delete |
| Jellyfin | 5 | library search, recent additions, now-playing sessions, library scan |

Every tool:

- Has a description written for an agent's decision-making, not for human docs.
- Pins its input and output with Pydantic v2, so the MCP catalogue carries strict JSON Schema.
- Returns a compact, self-describing envelope (`ok`, `query`, `count`, `total`, `items`).
- Translates upstream HTTP errors into structured `ToolError` envelopes with self-suggesting hints.
- Destructive operations require a two-call confirm-token flow.

## Quickstart

### uvx (one-shot)

```
uvx arr-stack-mcp serve --transport stdio
```

### Docker

```
docker run --rm -i \
  -e SONARR_URL=http://host.docker.internal:8989 \
  -e SONARR_API_KEY=$SONARR_API_KEY \
  -e RADARR_URL=http://host.docker.internal:7878 \
  -e RADARR_API_KEY=$RADARR_API_KEY \
  -e LIDARR_URL=http://host.docker.internal:8686 \
  -e LIDARR_API_KEY=$LIDARR_API_KEY \
  -e JELLYFIN_URL=http://host.docker.internal:8096 \
  -e JELLYFIN_API_KEY=$JELLYFIN_API_KEY \
  ghcr.io/new-usemame/arr-stack-mcp:0.1.0
```

### Local development (uv)

```
git clone https://github.com/new-usemame/arr-stack-mcp
cd arr-stack-mcp
uv sync
uv run arr-stack-mcp init           # writes a starter arr-stack-mcp.yaml
uv run arr-stack-mcp serve          # boots stdio MCP server
```

### Claude Desktop config

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS, or `%APPDATA%\Claude\claude_desktop_config.json` on Windows:

```json
{
  "mcpServers": {
    "arr-stack": {
      "command": "uvx",
      "args": ["arr-stack-mcp", "serve"],
      "env": {
        "SONARR_URL": "http://localhost:8989",
        "SONARR_API_KEY": "...",
        "RADARR_URL": "http://localhost:7878",
        "RADARR_API_KEY": "...",
        "LIDARR_URL": "http://localhost:8686",
        "LIDARR_API_KEY": "...",
        "JELLYFIN_URL": "http://localhost:8096",
        "JELLYFIN_API_KEY": "..."
      }
    }
  }
}
```

## Config reference

`arr-stack-mcp init` writes a starter `arr-stack-mcp.yaml`. Every secret can also be supplied via env var. Inline expansion of `${VAR}` and `${VAR:-default}` is supported.

```yaml
log_level: info

transport:
  stdio: true
  http_enabled: false
  http_host: 127.0.0.1
  http_port: 8080

policy:
  read_only: false
  disable_destructive: false
  confirm_token_ttl_seconds: 300

services:
  sonarr:
    enabled: true
    url: http://localhost:8989
    api_key: ${SONARR_API_KEY}
    verify_tls: true
    timeout_seconds: 30
  radarr:
    enabled: true
    url: http://localhost:7878
    api_key: ${RADARR_API_KEY}
  lidarr:
    enabled: true
    url: http://localhost:8686
    api_key: ${LIDARR_API_KEY}
  jellyfin:
    enabled: true
    url: http://localhost:8096
    api_key: ${JELLYFIN_API_KEY}
    default_user_id: 4f8b6d2e-3a9c-4f1d-9c2a-1b3c5d7e9f01
```

### Runtime flags

| Flag | Env | Effect |
|---|---|---|
| `--read-only` | `ARRSTACK_READ_ONLY=true` | Skip every tool tagged `write` or `destructive` at registration. |
| `--disable-destructive` | `ARRSTACK_DISABLE_DESTRUCTIVE=true` | Skip only the `destructive` tools (deletes). |
| `--dry-run` | — | Plan-and-record mode (v0.2). Write/destructive tools short-circuit before the upstream mutation and log the intended payload to a ring buffer surfaced by `stack.dryrun_log`. Reads run normally. |
| `--transport stdio` | — | Default. Use for Claude Desktop and Claude Code. |
| `--transport streamable-http` | — | HTTP transport for n8n / remote consumers. |
| `--bearer-token-env ARR_STACK_MCP_BEARER_TOKEN` | (env name) | Env var the server reads the bearer token from. Streamable-HTTP on a non-loopback bind refuses to start when this env var is unset. |
| `--config path/to/config.yaml` | — | Override config path. Defaults to `./arr-stack-mcp.yaml`, then XDG. |

### Confirm-token persistence (v0.2)

Confirm tokens default to in-memory storage. Set `policy.state_db_path` in the config to persist tokens across server restarts and across streamable-HTTP request lifetimes:

```yaml
policy:
  state_db_path: ~/.local/state/arr-stack-mcp/state.db
```

The path is created idempotently. SQLite WAL mode lets multiple worker processes share the same DB safely.

### Hourly per-tool call cap (v0.2)

Opt-in runaway-agent protection. Tools without an entry are uncapped:

```yaml
policy:
  hourly_caps:
    sonarr.series_add: 50
    radarr.movie_add: 50
    sonarr.series_delete: 10
```

Per-process, per-tool, rolling-hour. Failed upstream calls still consume budget so a runaway loop hits the cap on the Nth attempt.

## Capability matrix

Tools follow the `<service>.<verb_object>` convention. Tags drive flag-based gating.

### Sonarr

| Tool | Tag | Use |
|---|---|---|
| `sonarr.system_status` | read | Version + branch + uptime. First call when diagnosing. |
| `sonarr.series_search` | read | Search the existing library (already-added). |
| `sonarr.series_lookup` | read | Search TVDB to discover series to add. |
| `sonarr.series_status` | read | Per-season breakdown (v0.2). Episode counts, files on disk, missing. |
| `sonarr.queue` | read | Active downloads with progress. |
| `sonarr.calendar` | read | Upcoming + recently-aired episodes. |
| `sonarr.missing` | read | Monitored episodes not on disk. |
| `sonarr.series_add` | write | Add a series by TVDB id. Idempotent. |
| `sonarr.series_delete` | destructive | Two-call confirm-token flow. |

### Radarr

| Tool | Tag | Use |
|---|---|---|
| `radarr.system_status` | read | Mirrors Sonarr. |
| `radarr.movie_search` | read | Search the existing library. |
| `radarr.movie_lookup` | read | Search TMDB to discover movies to add. |
| `radarr.queue` | read | Active downloads. |
| `radarr.calendar` | read | Upcoming + recently-released movies. |
| `radarr.missing` | read | Monitored movies not on disk. |
| `radarr.movie_add` | write | Add a movie by TMDB id. Idempotent. |
| `radarr.movie_delete` | destructive | Two-call confirm-token flow. |

### Lidarr

| Tool | Tag | Use |
|---|---|---|
| `lidarr.system_status` | read | — |
| `lidarr.artist_search` | read | Search the existing library. |
| `lidarr.artist_lookup` | read | Search MusicBrainz to discover artists. |
| `lidarr.artist_albums` | read | List albums under one artist. |
| `lidarr.queue` | read | Active downloads. |
| `lidarr.artist_add` | write | Add an artist by MusicBrainz id. Idempotent. |
| `lidarr.artist_delete` | destructive | Two-call confirm-token flow. |

### Jellyfin

| Tool | Tag | Use |
|---|---|---|
| `jellyfin.system_info` | read | Version + server name. Public endpoint. |
| `jellyfin.library_search` | read | Search items by name. Pass `user_id=` for per-user scoping (v0.2). |
| `jellyfin.recent_additions` | read | Newest items by date_added. Pass `user_id=` for per-user scoping (v0.2). |
| `jellyfin.users_list` | read | Enumerate user accounts (v0.2). Returns `user_id`, name, admin flag, last login. |
| `jellyfin.now_playing` | read | Currently-active sessions with progress. |
| `jellyfin.scan_library` | write | Trigger a library refresh. |

### Prowlarr (v0.2)

| Tool | Tag | Use |
|---|---|---|
| `prowlarr.system_status` | read | Version + branch. First call when diagnosing Prowlarr. |
| `prowlarr.health` | read | Health-check issues (warnings, errors, wiki links). |
| `prowlarr.indexer_list` | read | Configured indexers with implementation, protocol, priority, enable. |
| `prowlarr.indexer_stats` | read | Query / grab / failure counts per indexer + average response time. |
| `prowlarr.indexer_status` | read | Currently-failing indexers with retry-after timestamps. |
| `prowlarr.indexer_test_all` | write | Trigger the test-every-indexer probe; returns per-indexer pass/fail. |
| `prowlarr.search` | read | Search across configured indexers. Returns title, indexer, size, age, seeders. Does NOT download — use `*.add` on Sonarr / Radarr / Lidarr with catalog id. |

### stack.* (v0.2, cross-service)

| Tool | Tag | Use |
|---|---|---|
| `stack.health` | read | Probe every enabled service's `*.system_status` in parallel. Returns reachability matrix + `overall_ok`. |
| `stack.dryrun_log` | read | Read the ring buffer of would-have-fired mutations recorded under `--dry-run`. |
| `stack.report_issue` | read | Compose a pre-filled GitHub issue URL the user can post upstream. Never auto-submits. |
| `stack.find_anywhere` | read | Fan a query across every enabled arr + Jellyfin library; merged result with `source` per row. |
| `stack.queue_status_all` | read | Aggregate download queue across Sonarr, Radarr, Lidarr. Normalized row shape. |

## Confirm-token flow

Destructive tools (`*_delete`) implement a two-call confirm:

```
# Call 1: returns plan + token, no side effect
> sonarr.series_delete(sonarr_id=42, delete_files=False)
{
  "ok": true,
  "needs_confirm": true,
  "confirm_token": "abc123",
  "summary": "remove 'Foo Bar' (sonarr_id=42) from Sonarr; keep files on disk",
  "expires_in_seconds": 300
}

# Call 2: executes
> sonarr.series_delete(sonarr_id=42, delete_files=False, confirm_token="abc123")
{
  "ok": true,
  "deleted_sonarr_id": 42,
  "title": "Foo Bar",
  "files_deleted": false,
  "msg": "deleted sonarr_id=42"
}
```

Tokens are single-use, time-limited, and bound to the request payload — a token from one tool will not confirm another.

## Architecture

Two layers:

```
┌────────────────────────────────────────────────────────────┐
│  Curated MCP tools (arr_stack_mcp.tools.<service>.tools)  │
│  Hand-written, LLM-friendly names, descriptions, schemas. │
├────────────────────────────────────────────────────────────┤
│  Generated thin clients (arr_stack_mcp.generated.<svc>)   │
│  openapi-python-client output. Do not hand-edit; regen    │
│  via scripts/regen-clients.sh on upstream version bumps.  │
├────────────────────────────────────────────────────────────┤
│  httpx + pydantic + structlog + mcp.server.fastmcp         │
└────────────────────────────────────────────────────────────┘
```

See `docs/ARCHITECTURE.md` for the longer walk-through.

## Development

```
uv sync                              # install runtime + dev deps
uv run pytest -q                     # fast unit tests
uv run ruff check src/ tests/        # lint
uv run mypy src/ tests/              # type check (strict)
uv run ruff format src/ tests/       # format
```

Integration tests require the docker test stack:

```
scripts/test-stack-up.sh             # boots Sonarr/Radarr/Lidarr/Prowlarr/Jellyfin
uv run pytest -m integration         # runs once stack is healthy
scripts/test-stack-down.sh --clean   # teardown
```

## Contributing

See `CONTRIBUTING.md` for the OpenAPI regeneration flow and the verification checklist that gates every release.

## License

MIT
