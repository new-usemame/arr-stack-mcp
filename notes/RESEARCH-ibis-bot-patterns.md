# ibis-bot patterns to port into arr-stack-mcp

ibis-bot is a Matrix bot with a hand-written tool registry executed against an OpenRouter LLM loop. arr-stack-mcp is an MCP server. The two share a domain (Sonarr/Radarr/Lidarr/Jellyfin) but differ in transport (Matrix turn-loop vs single MCP `tools/call`) and identity model (per-Matrix-user vs per-MCP-session). The notes below extract patterns worth porting, and flag what must be reshaped for MCP.

All file references are relative to `research/ibis-bot-tools/`.

## 1. Confirm-token pattern

Reference: `tools/discover.py:37-48` (`_stash`/`consume`), `tools/bulk.py:30-99`, `tools/music.py:447-491` (`delete_artist`), `store.py:154-209` (`session_save`/`session_pop`/`op_session_create`/`op_session_consume`).

Shape:
- Tool A returns `{"ok": True, "needs_confirm": True, "confirm_token": "<urlsafe-8>", "items": [...], "msg": "plan: …"}`.
- Token is stashed in SQLite (`discover_sessions` table) with a typed `mode` (`"op:delete_artist"`, `"series_fill"`, etc.).
- Tool B (`bulk_download_books` or the same tool re-invoked with `confirm_token=`) calls `session_pop`/`op_session_consume` — one-shot delete-on-read. A wrong-kind token is rejected, not silently consumed (`store.py:204-207`).
- Tokens survive process restart (durable store), and the in-Matrix-turn auto-consume is blocked at the bot loop layer.

What we keep:
- One-shot durable token semantics.
- Typed `op:<kind>` namespace per the prefix in `op_session_create` — prevents a `delete_artist` token from confirming a `delete_movie`.
- Plan-then-execute split: the destructive tool reports the exact plan (what gets removed, whether files go with it, on whose behalf) before any side effect.

What we change for MCP:
- ibis-bot needs a human saying "go" between turns. In MCP the agent drives the loop, so the contract becomes: call tool X without `confirm_token` for the plan + token, then re-call with the token. Spell that out in the tool description. The token gives belt-and-suspenders alongside any client-side confirm UI.
- Skip the "different LLM turn" rule — MCP has no turn concept.
- Persistence: small SQLite under `XDG_DATA_HOME/arr-stack-mcp/state.db` or in-memory with ~5 min TTL.
- `confirm_token` is an optional pydantic field on the destructive tool itself (not a separate "execute" tool) — same shape as `DeleteArtistArgs.confirm_token` at `tools/music.py:447-450`.

## 2. Fuzzy match / owned-set / candidate disambiguation

Reference: `tools/discover.py:50-258`. Key helpers: `_author_tokens` (54-59), `_title_contains` (62-78), `_owned_index` (222-242), `_is_owned_fuzzy` (245-258), `_filter_garbage` (112-127). Sonarr-side equivalents are in `tools/arrs.py:177-218` (`_norm`/`_series_score`/`_extract_year`) and `tools/music.py:78-113` (`_normalize`/`_fuzzy_score`/`_best_artist_match`).

Shape:
- Two-stage normalize: lowercase + strip non-alphanum (`_norm`), plus token-set decomposition for set-overlap scoring.
- Tiered scoring: exact = 1.0, normalized-exact = 0.95, substring = 0.6–0.9 ratio-weighted by length, fallback Jaccard over word tokens (`tools/arrs.py:181-202`, `tools/music.py:82-101`).
- Ambiguity surfaced when top-2 are within 0.1 and top is < 0.85 — handler returns `{"ambiguous": True, "candidates": [...]}` (`tools/arrs.py:244-252`).
- Year-extraction from free-text query for reboot disambiguation: `_extract_year` (`tools/arrs.py:205-217`) pulls 4-digit and 2-digit year hints. `year_filter` short-circuits scoring to 0 for wrong years.
- "Owned" index built once per call, lookup by author-token-overlap then bidirectional title containment with a guard against trivial substring matches (`_title_contains` rejects `"dune"` matching every Dune-universe title unless the short side is ≥8 chars or multi-word).

For arr-stack-mcp (drop Calibre-book domain; target entities are series / movie / artist+album):
- Helpers in `arr_stack_mcp/_fuzzy.py`:
  - `normalize(s) -> str` — strip non-alphanum, lowercase.
  - `score(query, target, *, year=None, target_year=None) -> float` — tiered scorer from `arrs._series_score`.
  - `extract_year(s) -> int | None` — port verbatim.
  - `best_match(query, items, key, *, year=None, threshold=0.6) -> (best, alternatives)` — generic.
  - `disambiguate(query, items, key, *, year=None) -> {best, ambiguous, candidates}` — wrapper that picks single-match vs candidates payload.
- Ambiguity threshold + min-score configurable per call — movies usually have years, artists rarely.
- "Owned" semantics matter less than for Calibre (the arrs already track library state). Keep the index pattern for cross-source tools ("find artists like ours" → MusicBrainz/Last.fm, filter against Lidarr).

## 3. Tool registration + tagging

Reference: `tools/registry.py:7-46`, `tools/__init__.py:1-18`, `tools/arrs.py:167-172` and similar `REGISTRY.register(...)` calls throughout.

Shape:
- `Tool` dataclass: `name`, `description`, `schema` (Pydantic BaseModel class), `handler` (async callable), `summarize_args` (for audit-log), `format_result` (for Matrix rendering).
- `Registry.register` raises on duplicate names — fail-fast at import time.
- Each module imports the registry, calls `REGISTRY.register(...)` as an import side-effect, and `tools/__init__.py` simply `from . import <modulename>` to trigger the side effects.
- `Registry.openai_schemas()` (registry.py:32-43) converts to the OpenAI function-calling shape; FastMCP equivalent is `Registry.mcp_tool_descriptors()`.

What we keep:
- Pydantic `BaseModel` schemas as the source of truth — generates MCP JSON Schema for free.
- Per-module side-effect registration. Easy to add a new domain by creating one file.
- Fail-fast duplicate detection.

What we change for MCP:
- Add `kind: Literal["read", "write", "destructive"]` so `--read-only` / `--disable-destructive` (jaredtrent's flag-driven pattern, also CLAUDE.md) can filter at startup.
- Add `toolset: Literal["sonarr", "radarr", "lidarr", "prowlarr", "jellyfin", "stack"]` for per-service enable/disable in one line.
- Drop `summarize_args` (Matrix-audit-room rendering). Keep `format_result` as optional `text_summary(result) -> str` for MCP `content`; default to JSON.

## 4. Per-tool daily caps

Reference: `policy.py:1-69`, `config.py:119-203` (`daily_limits`).

Shape:
- `Policy` holds a `dict[str, int]` of per-tool daily limits, counted per UTC day per (user, tool).
- Pluggable durable backend (SQLite) so counts survive restart within the same day; in-memory mode falls back for tests.
- `can_call` / `can_call_n` / `remaining` / `record` — the bot checks `can_call(sender, tool)` before invoking the handler, calls `record(sender, tool, n)` after success.
- ibis-bot's caps encode risk tolerance, not just abuse prevention — `delete_artist=5/day` is tight because destructive; `find_artist=1000/day` is generous because read-only.

For MCP:
- No per-user concept — daily caps lose meaning. Carry forward as optional `--max-calls-per-tool-per-hour` (default off) for runaway-agent paranoia.
- More valuable: per-service rate limiting against upstream 429s. Global `asyncio.Semaphore` per service, not a daily cap.
- Keep the pluggable-backend shape for any persistence (confirm-tokens, counters).

## 5. Per-toolset enable/disable

Reference: `tools/__init__.py:1-15` (per-module imports drive what's registered), `tools/hide_tools.py` (per-item content filtering), `config.py:43-56` (`alex_only_tools` — admin-restricted tool list).

Shape:
- ibis-bot has no "toolset" abstraction. Each tool file is a unit. Excluding a module means commenting an import in `__init__.py`.
- `alex_only_tools` is a tuple of tool names checked at the bot-loop layer before dispatch.

For MCP:
- Adopt jaredtrent/jellyfin-mcp's pattern: `toolset` enum on each tool, CLI/env-var to enable a list (default all). E.g. `ARR_STACK_TOOLSETS=sonarr,radarr,jellyfin`.
- `--read-only` (drop `write` + `destructive`) and `--disable-destructive` (drop only `destructive`).
- Document the resulting toolset matrix in the README — sweetener for LLM discovery.

## 6. Self-describing result shapes

Reference: every handler in `tools/arrs.py`, `tools/music.py`, `tools/jellyfin.py`. Especially `tools/arrs.py:62-68` (already-added case — `ok=True, already_added=True, msg="..."` instead of false-negative), `tools/music.py:264-274` (artist-album result shape), `tools/jellyfin.py:541` (`{"ok": True, "kind": "show", "query": ..., "matches": [...]}`).

Shape:
- Every handler returns a dict with `ok: bool` + `msg: str` minimum. Success cases include `already_added`, `ambiguous`, `needs_confirm`, `candidates`, `items`, etc. — keys the LLM can reason on.
- "Already exists / no-op" is `ok=True` not `ok=False` — the LLM doesn't need to retry; the action is logically satisfied. The `msg` is self-describing so the LLM doesn't have to add a clarifying paragraph (`tools/arrs.py:58-61` has the comment for this rule).
- Counts are flat integers, never strings. Sizes are unit-suffixed in the message but raw bytes in the structured field.
- Lists are bounded at the handler (`queued[:50]`, `failed[:10]` — `tools/bulk.py:151-152`) so the response doesn't explode the LLM's context.

For MCP:
- Port the convention. MCP `content` returns structured JSON + formatted `msg` text.
- Strip emoji prefixes (📺 / ❌ / ❤️) — MCP consumers re-render for the user, so they're noise here. Per CLAUDE.md's tone hot-list.
- Add a Pydantic output model per tool — advertised as the response schema.
- Use discriminated unions for variant shapes (success / ambiguous / needs_confirm) — type-level certainty for the caller.

## 7. Selftest / health check

Reference: `tools/selftest.py:1-200`.

Shape:
- One tool (`selftest`) runs all probes in parallel via `asyncio.gather`, each bounded at 8s timeout, each catching its own exceptions so one outage doesn't mask others.
- Per probe: `{"name", "ok", "ms", "detail"}`. Detail is a short diagnostic string ("HTTP 200" or "ConnectError: ..." or "auth=ok v=10.10 libs=5").
- Probes are typed by transport: `_probe_http`, `_probe_sqlite`, custom probes for AA reachability and Jellyfin auth.

For MCP:
- Port as `stack.health` (toolset = `stack`). The obvious first call for an LLM diagnosing "why isn't X working".
- Drop Calibre/AA/LL probes (out of scope).
- Per-arr probes: `/api/v3/system/status` (Sonarr/Radarr), `/api/v1/system/status` (Lidarr, Prowlarr), `/System/Info` (Jellyfin). Each probe surfaces the version in `detail` — useful for "endpoint X doesn't exist in your version" diagnosis.
- `--strict-health` startup flag: run probes at boot, refuse to start if any fail. Default off.

## 8. Per-user scoping (Jellyfin)

Reference: `tools/jellyfin.py:7-17` (docstring spelling out the model), `:169-235` (identity helpers — `matrix_sender_to_jellyfin_username`, `is_admin_sender`, `_resolve_user_id`, `library_visible_to_sender`), `:246-267` (`_list_libraries` filtering by sender), `:509-541` (`_find_jellyfin_item` resolving caller UserId for per-user library scoping), `tools/music.py:124-143` (`_visible_artist_names_for_caller` + Lidarr-by-visibility filter).

Shape:
- The bot holds ONE Jellyfin admin token. Per-user authorization is enforced in the handler layer by:
  1. Mapping caller-identity → Jellyfin username (`matrix_sender_to_jellyfin_username`).
  2. Resolving Jellyfin UserId via `/Users` lookup.
  3. Passing `UserId=<resolved>` to `/Items` queries — Jellyfin applies that user's library ACL server-side.
- Admins (Matrix localpart in `_ADMIN_LOCALPARTS`) bypass filtering; `library_visible_to_sender` returns True for them unconditionally.
- For Lidarr (which has no per-user concept), we infer visibility by intersecting the Lidarr artist list with the artist names the caller's Jellyfin user can see (`tools/music.py:124-143`).

For MCP (no built-in caller identity), three modes:
1. **Single-user (default):** server configured with one Jellyfin user; all `/Items` queries use that UserId. Matches "Claude Desktop on my machine against my Jellyfin".
2. **Per-call user param:** every Jellyfin tool takes optional `user: str | None`; resolves to that Jellyfin user when set. For "what does maggie see" reasoning.
3. **Admin token + `as_user=`:** mirror ibis-bot. Useful for multi-user agent platforms (n8n).

Recommendation: ship (1) as default, (2) as always-present escape hatch, skip (3) unless asked. Keep `library_visible_to_sender` as a helper; surface `jellyfin.who_can_see(item_id) -> [usernames]` for "who has access to X".

## 9. Dry-run pattern

Reference: `tools/dryrun.py:1-184`, `IBIS-WORKFLOW.md:138-177`.

Shape:
- `is_dry_run()` checks `IBIS_DRY_RUN=1` (or programmatic `set_force(True)`).
- Every `_post`/`_put`/`_delete` helper in `arrs.py`/`music.py`/`jellyfin.py` short-circuits to `fake_http()` when dry-run is on.
- `fake_http` returns success-shaped responses pattern-matched by URL — `/Users/New` returns `{"Id": "DRYRUN-...", "Name": ...}`, `/api/v3/series` returns `{"id": 0, "title": ...}`, etc.
- Reads pass through to live backends; only mutations are intercepted. Read-after-write on a `DRYRUN-` ID is synthesized via `fake_get`.
- Logged per-call for assertion in tests; `dryrun_safety.py` snapshots pre/post state across all backends and asserts no drift.

For MCP:
- Port verbatim. Rename to `ARR_STACK_DRY_RUN=1`.
- High value for LLM-tool-calling tests — wire into Claude Desktop in dry-run and let the agent mash buttons without touching real arrs.
- Implementation: dry-run lives in `arr_stack_mcp/_http.py` (single `httpx.AsyncClient` wrapper). Generated thin clients respect a single switch — don't scatter it per handler.
- Expose `stack.dryrun_log` MCP tool returning recorded calls — agents can verify "what would my plan do" in one round trip.

## What NOT to port

- **Matrix-specific bits.** `summarize_args`, `current_sender` ContextVar, Pantalaimon device verification, room ACL.
- **LLM-agent loop logic.** `bot.py`'s OpenRouter loop, `TURN_TOKENS` auto-consume blocking, NL router. MCP is the target of the loop, not the source.
- **Calibre / CW / LazyLibrarian / Anna's Archive.** Out of scope. Skip `tools/calibre.py`, `tools/reading.py`, `tools/follow.py`, `tools/aa_*.py`, `tools/lazylibrarian.py`, the book bits of `tools/discover.py`.
- **"Spotify-style my likes" as a top-level concern.** Worth one read tool (`jellyfin.favorites_list`), not the seven ibis-bot has.
- **Daily caps as hard requirement** — optional rate-limit only.
- **`hide_from_user`.** Tag-based per-user content filtering is admin home-lab parenting, not general MCP fare.
- **Two-turn "go" / "go N" / "go A-B" UX.** Replace with `confirm_token` in a single tool.

## Recommended new tool signatures for arr-stack-mcp

Format: `name(args) -> ResultShape` [kind] — one-line LLM-facing description. Aim for compact result shapes; lists are bounded at the handler. Names use dot-namespacing per service.

### Sonarr

- `sonarr.library_search(query, year=None, limit=10) -> {ok, ambiguous, candidates: [{tvdb_id, title, year, status, monitored, on_disk, total_episodes}]}` [read] — Search existing Sonarr library. `year=` disambiguates reboots.
- `sonarr.series_status(tvdb_id|title, year=None) -> {ok, title, year, tvdb_id, monitored, ended, seasons: [{season, label, monitored, episode_count, total_count, on_disk}], size_on_disk_gb}` [read] — Per-season episode counts. Direct port of `_sonarr_series_status` (`arrs.py:231-280`).
- `sonarr.lookup(query, limit=10) -> {ok, candidates: [{tvdb_id, title, year, status, overview, runtime, network, already_added}]}` [read] — TVDB search via `/series/lookup`.
- `sonarr.add_series(tvdb_id, quality_profile_id=None, root_folder=None, monitor="all", search=True) -> {ok, series_id, title, year}` [write] — Defaults to first profile/folder. Idempotent on `already_added`.
- `sonarr.queue(limit=20) -> {ok, items: [{series, episode, status, progress_pct, eta, client, size_gb}], total}` [read]
- `sonarr.missing_episodes(limit=50, monitored_only=True) -> {ok, items: [{series, season, episode, title, airdate, age_days}], total}` [read]
- `sonarr.calendar(from_date=None, days=7) -> {ok, items: [{series, season, episode, title, airdate, has_file}]}` [read]
- `sonarr.update_monitor(tvdb_id, seasons=None, monitored=True) -> {ok, changed}` [write] — Per-season or whole-series.
- `sonarr.remove_series(tvdb_id, delete_files=False, confirm_token=None) -> {ok, needs_confirm?, confirm_token?, msg}` [destructive]
- `sonarr.health() -> {ok, version, branch, root_folders: [{path, free_gb, accessible}], issues}` [read]

### Radarr

- `radarr.library_search(query, year=None, limit=10) -> {ok, ambiguous, candidates: [{tmdb_id, imdb_id, title, year, status, monitored, has_file, size_gb}]}` [read]
- `radarr.lookup(query, limit=10) -> {ok, candidates: [{tmdb_id, imdb_id, title, year, runtime, certification, overview, already_added}]}` [read]
- `radarr.add_movie(tmdb_id, quality_profile_id=None, root_folder=None, monitored=True, search=True) -> {ok, movie_id, title, year}` [write]
- `radarr.movie_status(tmdb_id|title, year=None) -> {ok, title, year, monitored, has_file, file_quality, file_size_gb, path, status, in_cinemas, digital_release}` [read]
- `radarr.queue(limit=20) -> {ok, items, total}` [read]
- `radarr.missing(limit=50, monitored_only=True) -> {ok, items, total}` [read]
- `radarr.calendar(from_date=None, days=30) -> {ok, items}` [read]
- `radarr.update_monitor(tmdb_id, monitored=True) -> {ok, changed}` [write]
- `radarr.remove_movie(tmdb_id, delete_files=False, confirm_token=None) -> {ok, needs_confirm?, confirm_token?}` [destructive]
- `radarr.health() -> {ok, version, branch, root_folders, issues}` [read]

### Lidarr

- `lidarr.artist_search(query, limit=10) -> {ok, ambiguous, candidates: [{mbid, name, monitored, album_count, track_count, path}]}` [read] — Port of `_find_artist` (`music.py:150-169`).
- `lidarr.list_artists(starts_with=None, limit=50) -> {ok, total, shown, truncated, artists}` [read] — Port of `_list_artists`.
- `lidarr.artist_albums(mbid|name) -> {ok, artist, albums: [{title, year, type, monitored, tracks, have, missing}]}` [read] — Port of `_artist_albums`.
- `lidarr.lookup(query) -> {ok, candidates: [{mbid, name, overview, album_count}]}` [read]
- `lidarr.add_artist(mbid, quality_profile_id=None, metadata_profile_id=None, root_folder=None, monitor="all", search=True) -> {ok, artist_id, name}` [write]
- `lidarr.queue(limit=20) -> {ok, items, total}` [read]
- `lidarr.album_status(mbid|title, artist=None) -> {ok, title, year, type, monitored, tracks, have, missing, size_gb}` [read]
- `lidarr.update_monitor(mbid, monitored=True) -> {ok, changed}` [write]
- `lidarr.remove_artist(mbid, delete_files=False, confirm_token=None) -> {ok, needs_confirm?, confirm_token?}` [destructive] — Port of `_delete_artist` (`music.py:453-491`).
- `lidarr.health() -> {ok, version, branch, root_folders, issues}` [read]

### Prowlarr (new — ibis-bot doesn't cover it)

- `prowlarr.indexer_list() -> {ok, indexers: [{id, name, protocol, enabled, priority, categories, last_query_time}]}` [read]
- `prowlarr.search(query, categories=None, type="search", limit=30) -> {ok, results: [{indexer, title, size_gb, seeders, leechers, publish_date, download_url, info_url, categories}]}` [read] — Cross-indexer search; the headline Prowlarr feature.
- `prowlarr.test_indexer(indexer_id) -> {ok, ms, msg}` [read]
- `prowlarr.indexer_stats(indexer_id=None, since_days=7) -> {ok, stats: [{indexer, queries, grabs, fail_rate, avg_response_ms}]}` [read]
- `prowlarr.health() -> {ok, version, branch, issues}` [read]

### Jellyfin

- `jellyfin.list_libraries(visible_to=None) -> {ok, libraries: [{name, type, paths, id}], count}` [read] — Port of `_list_libraries`. `visible_to=` overrides default user.
- `jellyfin.library_stats(library=None) -> {ok, stats: [{name, type, count, paths}]}` [read] — Port of `_library_stats`.
- `jellyfin.recent_additions(library=None, limit=10) -> {ok, items: [{library, name, type, added}]}` [read]
- `jellyfin.find_item(title, kind: Literal["show","movie","album","artist"], year=None) -> {ok, matches: [{name, year, library, path, ids: {tvdb, tmdb, imdb, mbid}}]}` [read] — Generalized port of `_find_jellyfin_item`; one tool, four kinds.
- `jellyfin.now_playing() -> {ok, sessions: [{user, device, client, item, type, position_pct}]}` [read] — Often admin-gated; operator decides via config.
- `jellyfin.users_list() -> {ok, users: [{name, admin, all_libs, library_count}]}` [read]
- `jellyfin.scan_library(library=None) -> {ok, msg}` [write]
- `jellyfin.create_user(username, password, libraries=[], is_admin=False) -> {ok, user_id, msg}` [write]
- `jellyfin.grant_library_access(username, library, allow: bool) -> {ok, msg}` [write] — Collapse ibis-bot's grant + revoke into one with `allow=`.
- `jellyfin.playback_history(user=None, days=7, limit=50) -> {ok, items: [{user, item, type, played_at, completed}]}` [read] — New: "what's the family been watching".

### stack (composite — v0.2)

- `stack.health() -> {ok, probes: [{name, ok, ms, detail, version}]}` [read] — Port of `selftest`. First-call diagnostic.
- `stack.queue_status_all() -> {ok, sonarr, radarr, lidarr, totals: {downloading, pending, failed}}` [read] — Cross-service queue snapshot.
- `stack.find_anywhere(query, kinds=["show","movie","album","artist"]) -> {ok, sonarr, radarr, lidarr, jellyfin}` [read] — Fan-out "do we have X anywhere".
- `stack.dryrun_log() -> {ok, calls: [{ts, kind, service, method, url, body}]}` [read]
