# DESIGN — arr-stack-mcp v0.2 + book-stack-mcp v0.1 + ibis-bot migration

Working design for the four intertwined deliverables in `goals/GOAL-v0.2-and-ibis-migration.md`. One decision per section. Each decision states the root cause it addresses, the seam it lands at, the test surface that proves it works, and the risk surface it might break.

Treat this as a working document — revise in place when implementation surfaces a wrong call. Do not turn it into a narrative ledger; rules + reasoning, not history.

## 0. Sequencing

Build order, chosen so each phase's output is the next phase's input:

1. arr-stack-mcp v0.2 server-level seams (instructions / dry-run helper / SQLite confirm-token / hourly caps / streamable-HTTP+bearer / init wizard probe widening)
2. arr-stack-mcp v0.2 per-service tools (Prowlarr / `stack.*` / Jellyfin per-user / `sonarr.series_status`)
3. arr-stack-mcp v0.2 verification (MCP-client smoke, live homelab read-only, MCPB eval)
4. arr-stack-mcp v0.2.0 release
5. book-stack-mcp v0.1.0 scaffold (mirrors arr-stack-mcp's shape)
6. book-stack-mcp v0.1.0 tool surface (ports from ibis-bot's working `lazylibrarian.py` / `aa_*.py` / `calibre.py` / `reading.py` / `follow.py` / `discover.py` / `bulk.py`)
7. book-stack-mcp v0.1.0 verification + release
8. ibis-bot MCP adapter (in-place, e2e suite must stay 10/10 green BEFORE old tool files are deleted)
9. ibis-bot redeploy + delete migrated modules

Hard gate between 4 and 5: arr-stack-mcp v0.2.0 must be on PyPI before book-stack-mcp v0.1.0 scaffolding starts, so the second project's PyPI trusted-publisher setup happens cleanly against a known-working pattern.

Hard gate between 7 and 8: both MCPs must be `pip install`-able and serve cleanly via stdio before any line of ibis-bot's adapter is written. ibis-bot's e2e is the migration's only meaningful integration test.

---

## 1. arr-stack-mcp v0.2 — server-level decisions

### 1.1 MCP `instructions` field

**Root cause:** `server.py:_server_instructions()` is five sentences (lines 74-79). The LLM consumer gets no discipline about result envelopes, confirm-token UX, disambiguation, or tool-selection guidance. ibis-bot's `llm.py:SYSTEM_PROMPT` has 250 lines of LLM-facing discipline — but most of it is Matrix-specific.

**Decision:** Lift the *transferable* discipline from `llm.py:SYSTEM_PROMPT` into a richer `_server_instructions()`. Specifically port:

- Output discipline: tools return self-describing envelopes; don't re-render result fields verbatim.
- Confirm-required UX: when `needs_confirm: true` is returned, the plan is in the envelope; don't repeat the token or re-prompt; the consumer's second call passes the token.
- Disambiguation: `Ambiguous` envelope carries `candidates[]` with stable ids; retry with `id=`, do NOT append fields to the query string.
- Bulk-over-fanout: prefer a single bulk tool (when one exists) over N parallel calls.
- Acronym + year-tag awareness: `TMNT`/`LOTR`/`MCU` resolve via initials; year tags in titles (`Dune (2021)`, `BSG (2004)`) need either structured `year=` or get extracted via `fuzzy.extract_year_tag`.
- Tool-selection nudges: `*.search` for already-in-library; `*.lookup` (Sonarr/Radarr/Lidarr) for discovery-from-external-catalog; `*.system_status` first when diagnosing.

Do NOT port (Matrix-bot-specific): the `-> Operator` ACL, personality/tone (lowercase, no filler), bot-side bulk-flow patterns, vocabulary mapping ("kobo" / "collection" / etc.), Spotify favorites model, alex-only admin gating, dry-run env vars.

**Seam:** `server.py:_server_instructions(cfg)` returns a multi-section string. Section headers use plain text, no emoji. Tone-grep before commit.

**Test surface:** Unit test asserts the instructions string contains the expected discipline anchors ("self-describing envelope", "needs_confirm", "Ambiguous", "acronym"). MCP-client smoke asserts `init.instructions` is non-empty and reasonable length (~3-8KB).

**Risk:** Excessive instructions slow down the LLM's first turn (cache miss on prompt). Cap target: ≤ 8KB. If we go over, split into per-toolset descriptions and use the server `instructions` for cross-cutting only.

### 1.2 Dry-run mode

**Root cause:** Mutations against the live homelab must be safe to plan-and-record without firing. ibis-bot's `tools/dryrun.py` does this at the httpx layer with per-URL-pattern synthetic responses. arr-stack-mcp uses openapi-python-client thin clients that call `from_dict(response.json())` and **raise on missing required fields** — transport-layer mock-response synthesis would need to satisfy strict pydantic deserialization for every mutating endpoint we expose. Brittle when upstream schemas change.

**Decision:** Dry-run at the **curated-tool boundary**, not the transport. Write a helper in `tools/common.py`:

```python
def dryrun_short_circuit(
    policy: Policy,
    tool_name: str,
    intended_payload: dict[str, object],
    envelope_on_dryrun: T,
) -> T | None:
    """If policy.dry_run is on, record the intended call into the ring buffer and return envelope_on_dryrun.
    Else return None — caller proceeds with the real mutating call.
    Read-side prep BEFORE this helper is fine; only the mutating call is short-circuited."""
    if not policy.dry_run:
        return None
    policy.record_dryrun(tool_name, intended_payload)
    return envelope_on_dryrun
```

Each WRITE/DESTRUCTIVE tool adds ~4 lines after read-side prep + confirm-token consume:

```python
short = dryrun_short_circuit(policy, "sonarr.series_add", body.to_dict() if hasattr(body, "to_dict") else {},
    AddResult(sonarr_id=0, tvdb_id=args.tvdb_id, title=candidate.title or "DRYRUN", already_added=False, msg="DRY-RUN: would add"))
if short is not None:
    return short
added = await post_api_v3_series.asyncio(client=client, body=body)
```

~28 write-tool sites in arr-stack-mcp today. ~112 lines of explicit dry-run wiring across the codebase. Accept the duplication; the alternative (transport-layer synthesis) is structurally fragile.

`stack.dryrun_log` reads from a thread-safe ring buffer on `Policy`. Cap at 200 entries (per-process, no persistence).

**Seam:** `tools/common.py` for the helper. `policy.py` for the ring buffer + `record_dryrun()` method + `dry_run: bool` field. `tools/stack/tools.py` for the read tool.

**Test surface:** Unit test asserts a sample WRITE tool short-circuits when `policy.dry_run=True`, returns the supplied envelope, records the payload in the ring buffer, and skips the upstream call (via `pytest-httpx` assertion that no request fired). Integration test with `--dry-run` + write tools confirms no real state changes on the docker stack (snapshot pre / call / snapshot post).

**Risk:** A future contributor forgets the `dryrun_short_circuit` line on a new write tool. Mitigation: integration test runs all write tools under `--dry-run` and asserts no upstream mutation. If any pre/post snapshot diverges, the missing dry-run gate is the cause.

### 1.3 Confirm-token persistence

**Root cause:** `Policy._tokens` is in-memory (`policy.py:49`). Stdio transport (single-process-per-session) is fine. Streamable-HTTP transport (long-running server, multiple stream lifetimes per session) breaks if a token issued on one stream needs consumption on another. Server restart mid-plan also breaks.

**Decision:** SQLite at `$XDG_STATE_HOME/arr-stack-mcp/state.db` (defaults to `~/.local/state/arr-stack-mcp/state.db`). Single table:

```sql
CREATE TABLE IF NOT EXISTS confirm_tokens (
  token              TEXT PRIMARY KEY,
  tool_name          TEXT NOT NULL,
  payload_fingerprint TEXT NOT NULL,
  expires_at         REAL NOT NULL,         -- unix epoch
  created_at         REAL NOT NULL
);
CREATE INDEX idx_expires ON confirm_tokens(expires_at);
```

`Policy.issue_token` / `consume_token` / `_sweep` move from dict ops to SQL. Sweep on every issue/consume (current behavior); also a startup sweep clears stale rows.

Use `aiosqlite` if already pulled by something, else stdlib `sqlite3` with `asyncio.to_thread` for the calls. **Check the dep tree before adding aiosqlite** — keep the dep surface small.

**Seam:** `policy.py:Policy` keeps its public API exactly the same. Internal `_tokens` swapped for SQL operations. Backing-store wired at `Policy.from_config` via a path config (`policy.state_db_path: str | None`, default = XDG state). For tests, an `:memory:` override.

**Test surface:** Existing `test_policy.py` tests pass unchanged (interface-compatible). New tests:
- Survives `Policy` re-construction with same `state_db_path` (issue with instance A; consume with instance B; both pointing at same SQLite path).
- Sweep removes rows older than `confirm_token_ttl_seconds`.

**Risk:** Multi-process write contention on streamable-HTTP. SQLite handles this via WAL mode; enable WAL at table creation. Test concurrent issue+consume from two processes against the same DB path.

### 1.4 Hourly rate limiter (runaway-agent protection)

**Root cause:** A misbehaving agent loop could fire a tool 1000× in 5 minutes. arr-stack-mcp has no per-process tool-call cap. ibis-bot's per-user per-day caps don't translate — the MCP server has no user concept.

**Decision:** Per-process, per-tool, hourly counter. Config-driven, **off by default**. Name the config key `policy.hourly_caps` (matches actual cadence — the goal text says `daily_caps` but the cadence is per-hour; pick the accurate name and document the divergence).

Config shape:

```yaml
policy:
  hourly_caps:
    sonarr.series_add: 50
    radarr.movie_add: 50
    sonarr.series_delete: 10
    # …
```

Env-var override: `ARR_STACK_MCP_HOURLY_CAP_<TOOL>=N` (uppercase, dots replaced with underscores). Single key per tool — no global default; tools without an explicit cap are uncapped.

`Policy` gets:
- `hourly_caps: dict[str, int]`
- `_hourly_counters: dict[tuple[int, str], int]` keyed by `(epoch_hour, tool_name)`
- `_check_hourly_cap(tool_name)` called inside `Policy.check()` after the flag gates. Raises `PolicyDenied(reason="hourly cap reached: <tool>")`.

In-memory counters. Hourly rollover via fresh `epoch_hour = int(time.time() // 3600)` keying — old keys auto-drop on the next sweep.

**Why not per-day**: per-day caps don't catch runaway loops fast enough. The user-level per-day concept already exists at the bot layer (ibis-bot's `policy.py`); duplicating it server-side adds no signal.

**Seam:** `policy.py:Policy._check_hourly_cap(tool_name)` + extension to `PolicyConfig`.

**Test surface:** Unit test asserts caps trip at N+1, reset after hourly rollover (mocking `time.time`).

**Risk:** False trips during legitimate bulk operations. Mitigation: caps are opt-in (no defaults), operator picks numbers that fit their workflow.

### 1.5 Streamable-HTTP transport with bearer auth

**Root cause:** `server.py:45-46` calls `mcp.run("streamable-http")` with no host/port/auth wiring. `config.py:TransportConfig` has `http_host` and `http_port` that do nothing today (no code reads them). The transport spec calls for fatal-on-non-localhost without a token; we have no enforcement.

**Decision:** Three changes:

1. Thread `cfg.transport.http_host` and `cfg.transport.http_port` into `FastMCP(..., host=..., port=...)` constructor.
2. Implement `auth.StaticBearerVerifier(TokenVerifier)` that constant-time compares against `ARR_STACK_MCP_BEARER_TOKEN` env. Returns `AccessToken(token=token, client_id="mcp-bearer", scopes=[])` on match, `None` on miss.
3. At `server.run()` boot:
   - If transport is stdio: no auth, no host/port. (Stdio is local-only by definition.)
   - If transport is streamable-http AND `http_host` is loopback (`127.0.0.1`, `::1`, `localhost`): bearer is OPTIONAL (warn if no token set; users on localhost can opt out).
   - If transport is streamable-http AND `http_host` is non-loopback: bearer is REQUIRED. Refuse to start without `ARR_STACK_MCP_BEARER_TOKEN` set. Print a one-line message naming the env var.

`StaticBearerVerifier` is async (matches the `TokenVerifier` protocol). It uses `secrets.compare_digest` for the comparison.

**Seam:** New `auth.py` module. `cli.py` accepts `--bearer-token-from-env=VAR` for the rare case the operator wants a non-default env name. `server.py:run()` does the host-vs-token enforcement.

**Test surface:** Unit test for the verifier (correct token → AccessToken; wrong → None; empty → None; timing-safe). Integration test boots streamable-HTTP on a free port, drives an authenticated HTTP request, asserts 200 with token / 401 without.

**Risk:** OAuth metadata advertisement is gated by the FastMCP `auth: AuthSettings` parameter. Passing only `token_verifier=` without `auth=` means no OAuth Protected Resource Metadata endpoint — verify this works (it should, based on the signatures). If it doesn't, write a minimal `AuthSettings` with `issuer_url=resource_server_url=<our base URL>`.

### 1.6 Init wizard probe widening

**Root cause:** `config.py:_probe_services` probes `localhost` only (`_SERVICE_DEFAULT_PORTS` loop, single host). Real users run their arrs at `host.docker.internal` (Mac/Win Docker users), docker-compose service names (`sonarr:8989`, `radarr:7878`), mDNS hostnames (`teenyverse.lan`, `myhomelab.local`), or behind reverse proxies at `https://sonarr.mydomain.com`. The current probe yields false negatives and writes "not found" into the generated YAML.

**Decision:** Widen the probe in three orthogonal axes:

1. **Host list**: `localhost`, `127.0.0.1`, `host.docker.internal`, `<service>` (docker-compose hostname pattern), `<service>.lan` (mDNS).
2. **Scheme list**: `http`, `https` (already there).
3. **Concurrency**: 5 services × 5 hosts × 2 schemes × 1s timeout = 50s worst case sequentially. Run probes concurrently via `asyncio.gather` (per-target, with a 1.5s individual timeout). Total wall time = ~2s.

Reverse-proxy URLs can't be auto-probed (operator-specific). Instead, the wizard prints a footer reminding the operator to override any service URL manually.

The probe also reports *what* it tried (which host/scheme combinations succeeded vs failed). Surfaces it in the wizard output so the operator can sanity-check.

**Seam:** `config.py:init_config` and `_probe_services`. Probe results carry the resolved `url` and the list of attempted hosts.

**Test surface:** Unit test mocks `httpx.AsyncClient` to return 200 for one host+scheme combination and verifies that the wizard picks it. Integration test against the docker test stack confirms a fresh probe finds all five services.

**Risk:** mDNS probing can hang on networks that don't resolve `.lan` (DNS NXDOMAIN with slow timeout). Mitigation: hard 1.5s timeout per probe + DNS failures caught as `httpx.ConnectError`.

### 1.7 `tools/common.py` shared `_or_none` helpers

**Root cause:** `_str_or_none / _int_or_none / _bool_or_none / _dt_or_none / _status_to_str / _kind_to_str` are duplicated across all four service `tools.py` files (sonarr, radarr, lidarr, jellyfin). Drift risk is non-zero, and adding Prowlarr means a fifth copy.

**Decision:** Not v0.2 *deliverable* scope (no behavior change), but bundle as cleanup with the per-service Prowlarr addition. Lift to `tools/common.py:_coerce` module. Each per-service module imports.

**Risk:** Pure-refactor PRs are easy to verify but can drift mypy types if not careful. Mark as `chore:` (not feat) in the conventional commit so release-please correctly classifies it. Defer if time-pressed; not a blocker.

### 1.8 `http.py:build_httpx_client` is dead code

**Root cause:** `http.py:build_httpx_client` was documented as the shared httpx factory but no per-service `_client.py` uses it — each builds its own httpx via the generated `Client(...)` constructor. The `upstream_call` context manager is used (for error translation), but the factory isn't.

**Decision:** Either wire up via `Client.set_async_httpx_client(build_httpx_client(svc))` in each per-service `_client.py`, or delete the dead function. **Delete** — wiring it up adds no value today (dry-run lands at a different seam per 1.2; per-service `_client.py` already handles auth headers correctly).

Add a one-line comment in `http.py` noting that the AsyncClient is now owned by the generated Client and the only shared concern is the `upstream_call` error envelope.

**Risk:** Future need for shared httpx-level concerns (HTTP/2, custom DNS, retry policy). When that day comes, re-introduce `build_httpx_client` and wire it in via `set_async_httpx_client`. Not v0.2 scope.

---

## 2. arr-stack-mcp v0.2 — per-service decisions

### 2.1 Prowlarr toolset (~7 tools)

**Root cause:** Prowlarr is the indexer manager. ibis-bot doesn't use it (the bot doesn't search; the *arrs do). But the MCP exposes a full unified stack — Prowlarr is the missing service.

**Decision:** Seven tools, all using the pinned `specs/prowlarr.openapi.json` (v2.3.5.5327, 93 paths total).

| Tool | OpenAPI endpoint | Tag |
|---|---|---|
| `prowlarr.system_status` | `GET /api/v1/system/status` | read |
| `prowlarr.health` | `GET /api/v1/health` | read |
| `prowlarr.indexer_list` | `GET /api/v1/indexer` | read |
| `prowlarr.indexer_stats` | `GET /api/v1/indexerstats` | read |
| `prowlarr.indexer_status` | `GET /api/v1/indexerstatus` | read |
| `prowlarr.indexer_test` | `POST /api/v1/indexer/test` | write |
| `prowlarr.search` | `POST /api/v1/search` | read (no state change) |

`prowlarr.search` is `Tag.READ` because it queries indexers without mutating state. The downstream act-on-result (download, grab) lives in Sonarr/Radarr/Lidarr — Prowlarr just returns release candidates.

No destructive Prowlarr tools in v0.2 (delete indexer, system restart). They're available in the API but out of v0.2 scope — defer to v0.3 if requested.

**Per-service module:** `src/arr_stack_mcp/tools/prowlarr/{__init__.py,tools.py,_client.py,_models.py}` mirroring sonarr/. Generated client at `src/arr_stack_mcp/generated/prowlarr/` already regen-able via `scripts/regen-clients.sh`.

**Test surface:** Five integration tests against the docker test stack's Prowlarr container (status, health, indexer_list, indexer_stats, search-with-mocked-indexer). The `indexer_test` write test uses a known-bad indexer config and asserts the error envelope.

**Risk:** Prowlarr's `/api/v1/search` returns a list of `ReleaseResource` rows — the shape includes infohash, magnet URI, indexer protocol info. We should NOT surface the magnet URI / infohash to the LLM as a raw field (downstream `*.add` tools take TVDB id / TMDB id / MusicBrainz id, NOT release identifiers). Compact the search result to just (title, indexer, size, age, seeders, leechers, categories). The LLM uses this to nudge the user, not to act directly.

### 2.2 `stack.*` cross-service tools (5 tools)

**Root cause:** Today every diagnostic is per-service. "Why isn't my download going?" requires the user to ask each service separately. Cross-service queries should be first-class.

**Decision:** Five tools in `src/arr_stack_mcp/tools/stack/tools.py`:

| Tool | Purpose | Tag |
|---|---|---|
| `stack.health` | Calls each enabled service's `system_status` + `health` (Prowlarr) in parallel; returns a compact pass/fail matrix with version + uptime + auth-status. | read |
| `stack.queue_status_all` | Aggregates `sonarr.queue` + `radarr.queue` + `lidarr.queue` + `prowlarr.indexer_status` into one consolidated download/grab view. | read |
| `stack.find_anywhere` | Routes a free-text query across `sonarr.series_search`, `radarr.movie_search`, `lidarr.artist_search`, `jellyfin.library_search` in parallel; returns merged results with `source` field. | read |
| `stack.dryrun_log` | Reads the in-memory ring buffer of recorded dry-run calls. | read |
| `stack.report_issue` | Returns a self-link to `github.com/new-usemame/arr-stack-mcp/issues/new` with diagnostic context pre-filled. Inspired by `abl030/lidarr-mcp`'s pattern — every tool's description nudges the LLM to call this on unexpected errors. | read |

**Cross-cutting concerns:**

- `stack.health` only calls services the operator has enabled. Disabled services don't appear in the matrix.
- `stack.find_anywhere` returns a unified `{source: "sonarr"|"radarr"|"lidarr"|"jellyfin", items: [...]}` per-source. Each item carries its native id (sonarr_id, tmdb_id, mbid, jellyfin item id) so follow-up tools work.
- `stack.queue_status_all` is the natural "what's downloading right now?" answer. It does NOT aggregate Jellyfin (Jellyfin doesn't download — that's Sonarr/Radarr/Lidarr's job).
- `stack.dryrun_log` returns ring-buffer entries with `tool_name`, `recorded_at`, `payload`. Trims old entries to last 200.
- `stack.report_issue` echoes server version, transport, enabled services, last N tool errors (from a separate error-ring-buffer) into a pre-filled issue template URL. **Does not auto-submit.** The LLM surfaces the URL to the user, who decides.

**Risk:** `stack.find_anywhere` makes 4-5 parallel HTTP calls. A slow service blocks the whole result. Mitigation: `asyncio.gather(..., return_exceptions=True)` with per-call 5s timeout; failed services appear in the result as `{source: "sonarr", error: "timeout"}` rather than failing the whole tool.

### 2.3 Per-user Jellyfin scoping

**Root cause:** `ServiceConfig.default_user_id` exists (config.py:65) and is used in `jellyfin.library_search` / `recent_additions` (jellyfin/tools.py:55, 100, 167). But no per-call `user=` override. The ibis-bot migration requires Maggie's Matrix-sender → her Jellyfin user-id resolution. arr-stack-mcp must support `user=` as a per-call arg so the bot adapter can pass it through.

**Decision:** Three changes:

1. Add optional `user_id: str | None` (UUID string) to every Jellyfin tool that touches user-scoped endpoints — `library_search`, `recent_additions`, `now_playing` (sessions filter), and any new ones.
2. When the arg is set, use it as the `user_id` parameter. When unset, fall back to `default_user_id`. When both are unset and the endpoint requires it, raise `ToolError` with hint.
3. New tool: `jellyfin.users_list` (admin-only at the upstream API; if the API key is admin-scoped, this works; if not, returns 403). Returns `[{user_id, name, is_administrator, has_password, last_login_date}]`. The bot adapter calls this at startup to build its Matrix-sender → user_id map.

`jellyfin.who_can_see` (proposed in goal) is more speculative — I'll defer it until a clear consumer use case (likely book-stack-mcp's `kobo_sync` user mapping or similar). Document the deferral.

**Seam:** Each Jellyfin tool's input model gets a `user_id: str | None = None` field. The handler resolves to UUID via existing `_user_uuid_or_unset` helper, falling back to `default_user_id`.

**Test surface:** Integration test boots Jellyfin docker container, creates two users via the API, asserts `library_search(user_id=X)` returns X's accessible items and `library_search(user_id=Y)` returns Y's.

**Risk:** If the API key is user-scoped (not admin), the `user_id` override is ineffective — Jellyfin returns 403. Surface a clear error envelope in that case.

### 2.4 `sonarr.series_status` per-season breakdown

**Root cause:** Today's `sonarr.series_search` returns `episode_count / episode_file_count` at the SERIES level. The natural follow-up question "which season am I missing episodes from?" has no tool. ibis-bot's `tools/series.py` (the Calibre series-status tool, different domain) inspired the name — but the actual reference is ibis-bot's `sonarr_series_status` in `tools/arrs.py` (per `IBIS-WORKFLOW.md` line 41).

**Decision:** New `sonarr.series_status` tool. Input: `sonarr_id` (or `tvdb_id` for convenience). Output: per-season breakdown — `[{season_number, monitored, episode_count, episode_file_count, total_episode_count, missing_count, on_disk_pct}]` plus series-level summary.

Implementation: calls `GET /api/v3/series/{id}` (already used for series fetch) and reads the `seasons[]` field. Each entry has `seasonNumber`, `monitored`, `statistics: {episodeCount, episodeFileCount, totalEpisodeCount, sizeOnDisk}`. Plus optionally a `GET /api/v3/episode?seriesId={id}` for episode-level detail when `detail=True`.

**Seam:** `src/arr_stack_mcp/tools/sonarr/tools.py` adds the tool function. New pydantic model `SeasonSummary` (already declared in `_models.py:31-39` from a prior planning pass — confirm it's not wired and wire it).

**Test surface:** Integration test against Sonarr docker container with a seeded series; assert per-season counts match expected.

**Risk:** Spec lag — `Statistics` field shape may have drifted in newer Sonarr versions. Pinned spec is v4.0.16 (per `docker-compose.test.yml:19`), confirm `seasons[].statistics` is present in that version.

---

## 3. arr-stack-mcp v0.2 — release decisions

### 3.1 MCPB / DXT bundle

**Root cause:** Universal install. Anthropic's `mcpb` and `dxt` repos are the Claude-Desktop one-click bundle format. If mature, we ship a bundle. If not, we document the decision to wait.

**Decision:** Inspect upstream readiness at implementation time (task #19). Decision criteria:

- Is `anthropics/mcpb` a tagged release (≥ v0.1.0)?
- Does the bundle format support env-var-driven config (we MUST pass API keys via env, not bake them in)?
- Does Claude Desktop's UI prompt the user for the env-vars at install?

If ALL three: ship `arr-stack-mcp.mcpb` as a release artifact alongside the PyPI wheel + GHCR image. Document one-click install in README.

If any are NO: defer to v0.3; document the gap in README under "Future". This is a "stop and ask" condition per the goal's stop conditions, *only* if the decision is non-obvious.

### 3.2 PyPI + GHCR + cosign

**Root cause:** Same release path as v0.1.x. release-please + GitHub Actions handle this.

**Decision:** No changes to release infrastructure for v0.2. Conventional Commits: `feat: <scope> <change>` minor-bumps to v0.2.0. Pre-existing `publish.yml` workflow does PyPI OIDC + GHCR build/push + cosign keyless signing.

Edge case: if v0.1.x patch parity (e.g., ibis-bot compatibility fix) ships first, it goes as `fix(...)` and release-please correctly cuts a v0.1.3. v0.2.0 lands after.

---

## 4. book-stack-mcp v0.1.0 — companion project

### 4.1 Repo shape

**Root cause:** New sibling project at `github.com/new-usemame/book-stack-mcp`. Must mirror arr-stack-mcp's architectural shape (two-layer auto-gen + curated, dotted MCP namespacing, pydantic I/O, MIT, release-please, GHCR + PyPI + cosign).

**Decision:** Copy arr-stack-mcp's structure wholesale, adapt scope. Specifically:

- `pyproject.toml` adapted with new name, description, keywords. Same dep set + `aiosqlite` (for direct Calibre SQLite access in async context).
- `pre-commit-config.yaml`, `ruff` config (line 140), `mypy` strict — same.
- `.github/workflows/{ci,release-please,publish}.yml` — same shapes, adapted for the new project name.
- `Dockerfile` — same multi-stage `uv builder → python:3.12-slim-trixie runtime` pattern. Same `UV_PROJECT_ENVIRONMENT=/opt/venv`, `--no-editable` install flags.
- `scripts/regen-clients.sh` — pattern carried; the only generated client (if any) is for CWNG's HTTP API if it exposes a sufficient OpenAPI spec.
- `src/book_stack_mcp/` mirrors `src/arr_stack_mcp/`: `cli.py`, `config.py`, `errors.py`, `fuzzy.py` (book-domain calibration), `http.py`, `policy.py`, `server.py`, `_mcp.py`, `tools/{lazylibrarian,aa,calibre,reading,follow,stack}/`.

### 4.2 Tool surface

**Root cause:** Direct lift from ibis-bot's working surface, minus Spotify favorites + Matrix room ACL + Pantalaimon.

**Decision:** ~25 tools across six toolsets, every name dotted:

| Toolset | Tools |
|---|---|
| `lazylibrarian.*` | `download_book`, `queue`, `search_books`, `status`, `retry` |
| `aa.*` | `discover` (subject/trending/similar/by_author via OL + AA), `direct_download` (Lucky-Librarian fast-download), `quota_status` |
| `calibre.*` | `search_library`, `list_shelves`, `create_shelf`, `delete_shelf`, `set_shelf_kobo_sync`, `add_book_to_shelf`, `remove_book_from_shelf`, `list_shelf_contents`, `find_book_in_shelves`, `recent_library_additions`, `library_stats`, `rename_shelf`, `merge_shelves`, `clear_shelf`, `delete_book_from_library`, `bulk_add_to_shelf`, `kobo_sync_status` |
| `reading.*` | `set_reading_status` (Reading/Finished/DNF/TBR), `reading_status` (filter by status) |
| `follow.*` | `follow_author`, `unfollow_author`, `list_followed_authors` |
| `stack.*` | `stack.health`, `stack.dryrun_log`, `stack.report_issue` (target `book-stack-mcp` GitHub) |

**Transport for upstreams:**

- LL: hand-rolled httpx thin client (no OpenAPI spec). Port from ibis-bot's `tools/lazylibrarian.py:_ll(...)` shape.
- AA: hand-rolled httpx (no OpenAPI). `discover` uses OpenLibrary + AA hybrid pattern from ibis-bot. `direct_download` uses `/dyn/api/fast_download.json` with Lucky-Librarian key. ONLY `annas-archive.gl` per `[[reference_homelab_api_keys]]` memory.
- Calibre / CWNG: HTTP API where it exists (verify scope during scaffolding), direct SQLite fallback for shelf operations CW lacks. Two DBs: `cw/app.db` (writable — shelves, users) and `cw/metadata.db` (read-only — library catalog).
- Open Library: public, no key. `discover` book-domain queries route here.
- Hardcover: optional, file-mounted key, currently empty per ibis-bot's deploy. Skip in v0.1.0.

**Confirm-token + dry-run patterns:** Same as arr-stack-mcp. `bulk_add_to_shelf`, `delete_shelf` (with 3+ books), `delete_book_from_library`, `merge_shelves`, `clear_shelf` are confirm-gated. Reuse the SAME `dryrun_short_circuit` helper pattern.

**CWNG HTTP API depth:** **Verify during scaffolding (task #20).** Specifically, what shelf operations does CWNG expose over HTTP vs require SQLite? If CWNG's HTTP surface is too thin and we'd need to write through CW's SQLite from a process that doesn't co-locate with CWNG, **stop and ask** per the goal's stop conditions.

### 4.3 Verification

**Root cause:** Same standard as arr-stack-mcp.

**Decision:** Match arr-stack-mcp's verification standard row-by-row. `docker-compose.test.yml` spins Calibre-Web + LazyLibrarian containers. AA tests use live `annas-archive.gl` with `read-only` operations only (no downloads in CI). Live homelab read-only smoke against `teenyverse:8787` (LL), `teenyverse:8083` (CWNG, **verify port at scaffold time** — listed as 8083 in the goal but the live deployment may differ), `annas-archive.gl`.

---

## 5. ibis-bot migration — adapter design

### 5.1 The Tool dataclass impedance mismatch

**Root cause:** ibis-bot's `Tool` dataclass (registry.py:7-14) requires:
- `name: str`
- `description: str`
- `schema: type[BaseModel]` (**pydantic class, not JSON schema dict**)
- `handler: Callable[..., Awaitable[Any]]` (takes `**kwargs`, returns dict)
- `summarize_args: Callable[[dict], str]` (Matrix-side preview)
- `format_result: Callable[[dict], str]` (Matrix-side response rendering)

The MCP `session.list_tools()` returns JSON schemas, not pydantic classes. Server-side validation is the authority either way (the MCP server owns the schema). The agent loop (`test_e2e.py:163`) does `tool.schema.model_validate(args)` — passing arbitrary args through is fine, as long as a pydantic class exists to call `model_validate` on.

**Decision:** Synthesize pydantic classes from MCP `inputSchema` at adapter startup via `pydantic.create_model()`. 50-line helper:

```python
def _json_schema_to_pydantic(name: str, schema: dict) -> type[BaseModel]:
    """Build a pydantic model class from an MCP tool's JSON-schema inputSchema.
    Walks top-level properties; required fields have no default, optional get None.
    Server-side is the validation authority — we just want a class for ibis-bot's
    .model_validate(args) call."""
    fields = {}
    properties = schema.get("properties", {})
    required = set(schema.get("required", []))
    for fname, fschema in properties.items():
        py_type = _map_json_type(fschema)  # string→str, integer→int, …
        default = ... if fname in required else None
        fields[fname] = (py_type, default)
    return create_model(name, __base__=_PassthroughBase, **fields)


class _PassthroughBase(BaseModel):
    model_config = {"extra": "allow"}  # tolerate fields the MCP server adds before adapter restart
```

Stored as `ADAPTER_SCHEMAS: dict[str, type[BaseModel]]` keyed by MCP tool name.

### 5.2 Handler shape

**Root cause:** ibis-bot's bot loop calls `await tool.handler(**handler_kwargs)`, where `handler_kwargs = args_model.model_dump()`. Handler returns a dict — `format_result(r)` is called on that dict. For MCP tools, the handler must:
- Call `session.call_tool(name, arguments=...)`
- Parse the response into a dict
- Inject per-user context (Matrix-sender → Jellyfin-user-id for relevant tools)
- Translate MCP error responses into ibis-bot's `{ok: False, msg: ...}` shape

**Decision:** Factory function in `~/ibis-bot/tools/mcp_adapter.py`:

```python
def _make_mcp_handler(
    session: ClientSession,
    tool_name: str,
    arg_wrapper_key: str | None,  # FastMCP wraps pydantic input as {"args": {...}}, raw FastMCP tool fns take direct kwargs
) -> Callable[..., Awaitable[dict]]:
    async def _h(**kwargs) -> dict:
        # Per-user context: tools that take user_id and the caller didn't pass it
        # get the sender's Jellyfin user-id injected at call time.
        if "user_id" in (kwargs or {}) and not kwargs.get("user_id"):
            sender_jf = SENDER_TO_JELLYFIN.get(current_sender.get())
            if sender_jf:
                kwargs["user_id"] = sender_jf
        if arg_wrapper_key:
            arguments = {arg_wrapper_key: kwargs}
        else:
            arguments = kwargs
        try:
            result = await session.call_tool(tool_name, arguments=arguments)
        except McpError as e:
            return {"ok": False, "msg": f"{tool_name}: {e}", "_mcp_error": str(e)}
        if result.isError:
            return _mcp_error_to_dict(result.content)
        return _mcp_content_to_dict(result.content)
    return _h
```

The `arg_wrapper_key` problem: FastMCP tools that take a single pydantic-model arg (`async def tool(args: SeriesSearchInput)`) accept `arguments={"args": {...}}` over the wire. Tools that take inline kwargs (`async def tool(query: str, limit: int)`) accept `arguments={"query": ..., "limit": ...}` directly. Both arr-stack-mcp and book-stack-mcp use the single-model pattern, so `arg_wrapper_key="args"` for all migrated tools.

### 5.3 Per-tool renderers (`summarize_args`, `format_result`)

**Root cause:** ibis-bot's Matrix output uses per-tool `format_result` lambdas that render dicts into Matrix-friendly multi-line strings. A generic JSON dump would degrade UX for the 12 most-used tools. But ibis-bot used to have these inline with the tool definitions — now those definitions live in the MCP server, not the bot.

**Decision:** Sidecar map in `~/ibis-bot/tools/mcp_renderers.py`. Keyed by MCP tool name. The dozen most-used tools get bespoke renderers; the rest fall back to generic JSON. Example:

```python
MCP_RENDERERS: dict[str, dict[str, Callable]] = {
    "sonarr.series_search": {
        "summarize": lambda a: f'"{a.get("query")}"',
        "format": _fmt_series_search,  # the existing tools/arrs.py fmt code, lifted
    },
    "sonarr.series_add": {...},
    # …
}

def _generic_summarize(args: dict) -> str:
    return ", ".join(f"{k}={v!r}" for k, v in (args or {}).items())[:80]

def _generic_format(r: dict) -> str:
    if not r.get("ok", True):
        return f"❌ {r.get('msg', 'failed')}"
    # Compact pretty-print for unknown tools
    return json.dumps(r, indent=2, default=str)[:1200]
```

Cap renderers at ~150 lines total. The 12 highest-value tools cover ~80% of Matrix volume.

### 5.4 Confirm-token pass-through

**Root cause:** Both ibis-bot and the MCPs have confirm-token state machines. They MUST NOT double-prompt.

The lifecycle:
1. User asks bot to delete X.
2. Bot calls `sonarr.series_delete` with no token.
3. MCP server returns `DeletePlan{needs_confirm: true, confirm_token: T, ...}`.
4. Bot's renderer formats this into a Matrix message: "Plan: remove 'X' [...] — say go".
5. User says "go".
6. Bot's policy lookup finds the prior turn's token T (from `store.op_session` or similar).
7. Bot calls `sonarr.series_delete` again with `confirm_token=T`.
8. MCP server validates T against the persisted token DB, consumes it, executes.

The bot's `policy.py` (the daily-cap one) is orthogonal — it gates per-user-per-day call counts. ibis-bot's confirm-token logic was previously in the tool modules; it now flows transparently because the MCP server returns the `needs_confirm` shape that ibis-bot's existing two-step UX expects.

**Decision:** No bot-side confirm-token state needed beyond passing the field. `mcp_adapter.py`'s handler doesn't filter the `confirm_token` field — it passes through. The existing `bot.py` two-step UX continues to work without modification.

**Risk:** Token TTL mismatch. Bot stores tokens in `op_session` with a 5-minute TTL (same as arr-stack-mcp's `confirm_token_ttl_seconds` default). If they diverge (operator changes one), confusion. Mitigation: bot's adapter reads the MCP server's TTL from a session-init resource OR documents the requirement that both TTLs match.

### 5.5 Per-user Matrix-sender → Jellyfin-user mapping

**Root cause:** ibis-bot's `tools/jellyfin.py:matrix_sender_to_jellyfin_username` maps `@alex:host` → `alex` (Jellyfin username), then `_resolve_user_id(username)` resolves to the user UUID. The MCP server only takes the UUID. The mapping logic stays in the bot.

**Decision:** At adapter startup:
1. Call `jellyfin.users_list` once via the MCP session.
2. Build `JF_USERNAME_TO_ID: dict[str, str]` (username → UUID).
3. Resolve `matrix_sender_to_jellyfin_username` via existing `tools/context.py:current_sender` + ibis-bot's existing override map.
4. The handler factory injects `user_id` into MCP calls when the tool accepts it AND the caller didn't supply it (per 5.2).

Admin detection (`is_admin_sender`) similarly stays bot-side: at startup, parse `users_list` for `is_administrator: true` users; cache the localparts. Admin-only tool refusal happens bot-side BEFORE calling the MCP (preserves current UX).

### 5.6 The 12 files to delete

Per goal, these get rsynced-away from `~/ibis-bot/tools/` AFTER the e2e suite is 10/10 green under the new adapter:

- `arrs.py` (Sonarr/Radarr/Lidarr wrappers)
- `jellyfin.py` (Jellyfin wrappers — only the API-talking; the Matrix-sender mapping moves to `mcp_adapter.py` per 5.5)
- `series.py` (sonarr.series_status etc.)
- `music.py` (Lidarr + Jellyfin music)
- `lazylibrarian.py` (LL wrapper)
- `aa_check.py`, `aa_direct.py`, `aa_quota.py` (AA)
- `calibre.py` (CW shelf operations)
- `reading.py` (reading status)
- `follow.py` (author follow)
- `discover.py` (book discovery)
- `bulk.py` (bulk_download_books)

**Keep native to ibis-bot:**

- `bot.py`, `llm.py`, `watcher.py`, `audit.py`, `store.py`, `config.py`, `policy.py`, `selftest.py`
- `tools/__init__.py`, `tools/registry.py` (modified to source from MCP via adapter)
- `tools/context.py`, `tools/hide_tools.py` (Matrix-room ACL stays bot-side)
- `tools/dryrun.py` (bot-side dry-run env; the MCP-side dry-run is separate; they coexist)

### 5.7 Deployment + redeploy plan

**Root cause:** ibis-bot runs as a Docker container on teenyverse. Both MCPs must be reachable from inside that container via stdio. Two options:

- **Option A: pip-install both MCPs into the ibis-bot Docker image.** `requirements.txt` adds `arr-stack-mcp>=0.2.0`, `book-stack-mcp>=0.1.0`. The adapter spawns them via `subprocess` + MCP stdio client. Simplest.
- **Option B: run MCPs as separate sidecar containers.** Adapter connects via streamable-HTTP. More complex, no clear benefit when ibis-bot's the only consumer.

**Decision:** Option A. Update `~/ibis-bot/requirements.txt`, `~/ibis-bot/Dockerfile` (no structural change — same `pip install -r requirements.txt`). The Dockerfile already has `python:3.12-slim` and pip — adding two pure-Python wheels costs nothing.

Both MCPs read their config from env vars (URLs + API keys) that ibis-bot's compose file already sets. So no new compose-time config — the MCPs see the same env that the bot's tool modules used to.

Redeploy sequence:
1. Update `requirements.txt`, `Dockerfile`, write `tools/mcp_adapter.py` + `tools/mcp_renderers.py`, modify `tools/__init__.py` to import from `mcp_adapter` instead of the old per-domain modules.
2. Build the image locally on dev workstation: `docker build` against the modified bot.
3. `docker compose up -d --force-recreate ibis-bot` on teenyverse at a moment the Matrix room is idle.
4. Run `selftest` from the bot post-deploy. Expect all-green.
5. After 24 hours of live use without regressions, delete the 12 old tool files. Run e2e again.

**Risk:** The Dockerfile change rebuilds the image from scratch — adds 30-60s vs current cached layers. Acceptable. The MCPs are pure Python — no native deps, no slow compilation.

---

## 6. Open questions deferred to implementation time

These need verification before the relevant phase, but don't block the current design:

1. **MCPB / DXT bundle readiness.** Check at task #19. If immature, document in README and ship without.
2. **CWNG HTTP API surface depth.** Check at task #20 during book-stack-mcp scaffolding. If too thin to cover all shelf operations and direct-SQLite-from-non-co-located-process is needed → stop and ask operator.
3. **CWNG live port.** Goal lists `teenyverse:8083`; verify with `docker ps | grep calibre-web` on teenyverse during book-stack-mcp scaffolding.
4. **`AuthSettings` requirement when using only `token_verifier`.** Verify at task #17 that passing `token_verifier=` alone (without `auth=AuthSettings(...)`) actually works for static-bearer enforcement. If it doesn't, construct a minimal `AuthSettings` with `issuer_url=resource_server_url=<our URL>`.
5. **Sonarr v4.0.16 `seasons[].statistics` field shape.** Verify at task #18 by reading the pinned OpenAPI spec or hitting a docker container.
6. **Hardcover key**: empty per ibis-bot's deploy. Book-stack-mcp's `discover` skips Hardcover until the file is populated. Document the env-var hook for future use.

---

## 7. Non-deliverables (explicit out-of-scope)

These could plausibly land but are NOT v0.2 scope:

- Spotify-style music favorites (operator-rejected).
- Pantalaimon device verification (architecturally cannot live in an MCP server).
- Matrix-room ACL (transport-side, stays in ibis-bot).
- MCP resources/notifications for watcher events (v0.3 candidate; bot keeps polling for v0.2).
- Per-endpoint dry-run synthesis at the transport layer (1.2 rejected this in favor of curated-tool boundary).
- Removing the per-service `_int_or_none / _str_or_none / _dt_or_none` duplication (1.7 — cleanup, bundled with Prowlarr addition; defer if time-pressed).
- Streaming v0.2 features back into ibis-bot's `tools/series.py` (Calibre series) — that's book-stack-mcp's domain.
