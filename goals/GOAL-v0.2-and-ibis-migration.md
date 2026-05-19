# Goal: arr-stack-mcp v0.2 + book-stack-mcp v0.1 + ibis-bot migrated off its hand-rolled transport to both MCPs

You are Claude Opus 4.7 or higher — Max Ultra tier, high context window. You are running with full agency to research, design, implement, test, and publish v0.2 of arr-stack-mcp on Alex's behalf, **build a new sibling project `book-stack-mcp` v0.1.0 from scratch**, AND migrate the operator's locally-developed Matrix tool runner (ibis-bot at `defaultuser@10.0.30.36:~/ibis-bot/`) off its hand-rolled httpx layer so it goes through both MCPs instead. **No cope. No bandaids. Find root causes. Test against real containers, a real MCP client, and ibis-bot's real e2e suite — never mocks.** If you can't measure it, you don't know it. If something seems hard, you haven't dug deep enough yet.

You have a large context window. Use it. Read the codebase, the prior research notes, the upstream specs, and ibis-bot's current source thoroughly before designing anything. This prompt sets the goal and the constraints — it does not enumerate implementation steps. That's your job.

## Mission

Four intertwined deliverables, one release window.

1. **arr-stack-mcp v0.2.0** — Prowlarr + cross-service `stack.*` tools + the in-scope ibis-bot patterns v0.1 deferred. Cut from `github.com/new-usemame/arr-stack-mcp` via release-please.
2. **book-stack-mcp v0.1.0** — new sibling project at `/Users/acoundou/Other Projects/book-stack-mcp/` and `github.com/new-usemame/book-stack-mcp`. Mirror arr-stack-mcp's architecture (two-layer auto-gen + curated, dotted MCP namespacing, pydantic in/out, MIT, release-please, GHCR + PyPI signed). Covers LazyLibrarian, Anna's Archive direct-download, Calibre / Calibre-Web (via CWNG's HTTP surface where it exists; via direct SQLite where it doesn't — CW lacks a JSON shelf API), reading-status tracking, author-follow / new-release watching.
3. **Universal install for both MCPs** — anyone with an arr or book stack installs and configures the relevant MCP in under five minutes via the path of their choice (uvx, PyPI, Docker, Claude Desktop one-click bundle if mature). Streamable-HTTP transport with bearer auth. An `init` wizard that just works on a typical home-lab setup. A config-by-env-var story documented end-to-end. Per-platform Claude Desktop config snippets. Both MCPs install side-by-side and the consumer (Claude Desktop, ibis-bot, n8n, etc.) loads both.
4. **ibis-bot migration** — `~/ibis-bot/tools/arrs.py`, `~/ibis-bot/tools/jellyfin.py`, `~/ibis-bot/tools/lazylibrarian.py`, `~/ibis-bot/tools/aa_*.py`, `~/ibis-bot/tools/calibre.py`, `~/ibis-bot/tools/reading.py`, `~/ibis-bot/tools/follow.py`, `~/ibis-bot/tools/discover.py`, `~/ibis-bot/tools/bulk.py`, `~/ibis-bot/tools/music.py`, `~/ibis-bot/tools/series.py` deleted on teenyverse. ibis-bot's tool registry now sources those tools from `arr-stack-mcp serve --transport stdio` AND `book-stack-mcp serve --transport stdio` via the standard MCP stdio client. Matrix / watcher / per-user-Matrix-scoping / OpenRouter ReAct loop / SYSTEM_PROMPT / room ACL / E2EE-via-Pantalaimon stay native to ibis-bot. The migration must keep ibis-bot's 10-scenario `data/test_e2e.py` suite passing, redeploy cleanly, and not interrupt Alex + Maggie's live Matrix usage.

## Hard preconditions (refuse if any fail)

1. `pwd` is `/Users/acoundou/Other Projects/arr-stack-mcp`. If not, instruct `cd "/Users/acoundou/Other Projects/arr-stack-mcp"` and exit cleanly.
2. `gh auth status` shows active = `new-usemame`. If `Condo97` is active, run `gh auth switch --user new-usemame`. If the new-usemame token is invalid, instruct the operator to re-auth (Keychain service `github-pat-arr-stack-mcp`) and exit cleanly.
3. **Read `./CLAUDE.md` first.** Standing rules for this project — identity, mission, hard rules, architecture spine, tone policy, verification standard. Internalize before touching anything.
4. **Read `./notes/V0.1.0-HANDOFF.md`, `./notes/RESEARCH-ibis-bot-followups.md`, and `./CHANGELOG.md`.** They document exactly where v0.1 stopped, what we explicitly deferred to v0.2, and the three generator-bug patches the regen script applies post-codegen.
5. v0.1.2 is already published (PyPI + GHCR + cosign). Don't re-publish it. Your output tags as v0.2.0 (or as a v0.1.x patch first if you need one for ibis-bot-migration parity before the minor bump).

## How to develop your own context

Don't take this prompt as a prescription. Build your own model by reading. The starting reading list below is suggestive, not exhaustive — go where curiosity takes you.

### Read the project as it stands

- `CLAUDE.md` — operator instructions, identity rules, architecture spine, tone, verification standard
- `README.md` — install + config + capability matrix
- `docs/ARCHITECTURE.md` — the two-layer auto-gen + curated story
- `CONTRIBUTING.md` — OpenAPI regeneration flow + tool description style
- `notes/RESEARCH-prior-art.md` — the v0.1 prior-art critique (mcp-arr, lidarr-mcp, jellyfin-mcp, arr-controlarr)
- `notes/RESEARCH-ibis-bot-patterns.md` — what we ported from ibis-bot for v0.1
- `notes/RESEARCH-ibis-bot-followups.md` — what's still in scope from ibis-bot. Your starting point for the in-scope feature list.
- `notes/RESEARCH-openapi-pinning.md` and `notes/RESEARCH-openapi-surface.md` — how the generated clients are pinned and which upstream endpoints we expose
- `notes/RESEARCH-toolchain.md` — pin choices (mcp 1.27, openapi-python-client 0.24.3, pydantic v2, Python 3.12)
- `notes/V0.1.0-HANDOFF.md` — the seven-row verification checklist and what was unchecked when v0.1 closed
- `src/arr_stack_mcp/` — current source. Pay attention to `server.py:_server_instructions()` (the MCP instructions field that's already wired but sparse), `policy.py` (confirm-token lifecycle, currently in-memory), `fuzzy.py` (acronym + year-tag helpers ported from ibis-bot in v0.1.2), and `tools/<service>/` (eight tools each for Sonarr/Radarr, seven for Lidarr, five for Jellyfin)
- `scripts/regen-clients.sh` — three post-regen patches for openapi-python-client 0.24.3 generator bugs (HttpUri string-vs-object, `response.text` → `response.json()` for 232 endpoints, None-tolerance for 688 model `from_dict` methods). Patch markers: `ARRSTACK_HTTPURI_STR_OK`, `ARRSTACK_FROM_DICT_NONE_OK`.
- `examples/mcp-smoke.py` — how to drive arr-stack-mcp over stdio from the official MCP Python SDK
- `examples/mcp-live-homelab.py` — the read-only sweep template against the operator's live stack; reuse this shape for v0.2 verification

### Read the persistent memory

- `~/.claude/projects/-Users-acoundou-Other-Projects-arr-stack-mcp/memory/MEMORY.md` — index
- Standing rules: `feedback_no_bandaids`, `feedback_enterprise_verification`, `feedback_no_laziness`, `feedback_jellyfin_llm_tone`, `feedback_ibis_bot_invariants`, `feedback_memory_no_narrative`
- Reference: `reference_homelab_api_keys` (Sonarr/Radarr/Lidarr/Prowlarr/Jellyfin keys + sudo passwords + qBit creds + AirVPN scoping), `reference_homelab_ssh`
- Project state: `project_identity_and_gh`, `project_live_stack_view_only` (now relaxed for v0.2 — live writes are allowed AFTER v0.2.0 tag)

### Read ibis-bot's current source over SSH

ibis-bot evolved after our Phase A snapshot. The fresh source is at `defaultuser@10.0.30.36:~/ibis-bot/`. The files you care about most:

**Will be deleted from ibis-bot in the migration:**

- `tools/arrs.py` — Sonarr + Radarr + Lidarr wrappers, hand-rolled httpx → goes to arr-stack-mcp
- `tools/jellyfin.py` — Jellyfin wrappers, per-user Matrix-sender mapping → arr-stack-mcp (the Matrix-sender mapping stays in ibis-bot, only the Jellyfin API talking moves)
- `tools/series.py` — Sonarr series helpers → arr-stack-mcp
- `tools/music.py` — Lidarr + Jellyfin music tools → arr-stack-mcp
- `tools/lazylibrarian.py` → book-stack-mcp
- `tools/aa_check.py`, `tools/aa_direct.py`, `tools/aa_quota.py` → book-stack-mcp
- `tools/calibre.py` (~63KB, biggest single file) → book-stack-mcp
- `tools/reading.py` (Reading / Finished / DNF / TBR status tracking) → book-stack-mcp
- `tools/follow.py` (author follow + new-release watcher) → book-stack-mcp
- `tools/discover.py` (fuzzy + owned-set + bulk discovery) → split: fuzzy helpers stay in book-stack-mcp's `_fuzzy.py` (book domain); the arr-stack-mcp version already has the v0.1.2 port for arr-flavored fuzzy
- `tools/bulk.py` (bulk_download_books with two-step confirm) → book-stack-mcp

**Stays native to ibis-bot (do not migrate):**

- `bot.py` — the OpenRouter ReAct loop. ibis-bot remains the LLM driver.
- `llm.py` — 250-line SYSTEM_PROMPT for the ReAct loop. Matrix-specific.
- `config.py` — Matrix bot config + per-user allowlist + daily caps
- `policy.py` — confirm-token gate at the bot layer (different from our MCP-server-side confirm gates)
- `watcher.py` — the background asyncio task that polls and posts unsolicited "✅ landed" notifications to Matrix. This stays. ibis-bot listens for completion events from both MCPs via their MCP `notifications/resources/updated` if that's how we expose it, or via polling specific status tools.
- `audit.py`, `store.py` — bot-side audit room + SQLite store (thread_messages, discover_sessions, quota_counters, notify_seen)
- `tools/context.py`, `tools/hide_tools.py`, `tools/dryrun.py` — bot-side context vars + tool filtering + dry-run env. The dry-run *pattern* gets lifted into both MCPs' shared httpx wrapper; ibis-bot keeps its own env-var for bot-side simulation.
- `selftest.py` — gets RE-WIRED to call `stack.health` from each MCP rather than running its own probes.
- `tools/registry.py`, `tools/__init__.py` — registry gets a new adapter that creates MCP-backed Tool entries from the two MCP-stdio sessions opened at bot startup.

**Read for context:**

- `IBIS-WORKFLOW.md` — the design doc
- `data/test_e2e.py` — the 10-scenario e2e suite. Must stay green after the migration.
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — how it's deployed. Will need updates: add `mcp>=1.27` + `arr-stack-mcp` + `book-stack-mcp` as deps; the Dockerfile may need to bundle both MCPs or fetch them at boot.

Use `ssh defaultuser@10.0.30.36` (the `FIX-agent-get-into-ssh` skill if interactive; SSH key auth otherwise). Sudo password in the homelab-API-keys memory. Read-only sweeps + `rsync -az` are fine; do not push changes back without confirmation.

### Companion project: book-stack-mcp

Sibling of arr-stack-mcp. Same identity (`new-usemame`), same architecture (two-layer auto-gen + curated, dotted MCP namespacing, pydantic in/out, FastMCP via `mcp.server.fastmcp`, ruff + mypy strict, MIT, release-please, GHCR + PyPI cosign-signed), same tone policy, same verification standard. Lives at `/Users/acoundou/Other Projects/book-stack-mcp/` and `github.com/new-usemame/book-stack-mcp`.

**Upstream surfaces it talks to:**

- **LazyLibrarian** — host `teenyverse 10.0.30.36:8787`. API key `[[reference_homelab_api_keys]]`. No OpenAPI spec; the upstream is sparse on docs. Use ibis-bot's working `tools/lazylibrarian.py` as the reference for which endpoints actually work in practice; thin-client it directly via httpx rather than codegen (the spec is too thin to be worth generating).
- **Anna's Archive** — `https://annas-archive.gl` only (`.org`/`.se`/`.fi` are NXDOMAIN globally; `.li` is an ad-injected scam clone per `[[reference_homelab_api_keys]]` memory). Lucky-Librarian key at `teenyverse:/home/defaultuser/matrix/.aa-secret-key`. Fast-download API at `/dyn/api/fast_download.json?md5=X&key=Y`. ibis-bot's `tools/aa_direct.py` is the reference.
- **Calibre-Web-NextGen (CWNG)** — the operator's fork of CW lives at `/Users/acoundou/Other Projects/Calibre-Web-NextGen/`. CWNG runs in production at `teenyverse:8083` (verify port). It has SOME HTTP API beyond CW's standard surface, plus the per-shelf SQLite at `teenyverse:/home/defaultuser/media-stack/config/calibre-web/app.db` (writable) and `metadata.db` (read-only library). Prefer CWNG's HTTP API where it exists; fall back to direct SQLite (as ibis-bot does) where it doesn't.
- **Hardcover** (book-discovery) — optional. ibis-bot reads `/home/defaultuser/ibis-bot/.hardcover-key` if non-empty; book-stack-mcp should do the same. Currently the file is empty (OL-only); skip until populated.
- **Open Library** — public, no key. Used for trending / subject / similar / by_author discovery.

**Tool surface to ship in book-stack-mcp v0.1.0:**

- `lazylibrarian.*` — download_book, queue, search_books, status, retry
- `aa.*` — discover (annas-archive subject/trending/similar), direct_download (Lucky-Librarian fast-download), quota_status
- `calibre.*` — search_library, list_shelves, create_shelf, delete_shelf, set_shelf_kobo_sync, add_book_to_shelf, remove_book_from_shelf, list_shelf_contents, find_book_in_shelves, recent_library_additions, library_stats, rename_shelf, merge_shelves, clear_shelf, delete_book_from_library, bulk_add_to_shelf, kobo_sync_status
- `reading.*` — set_reading_status (Reading/Finished/DNF/TBR), reading_status (filter by status)
- `follow.*` — follow_author, unfollow_author, list_followed_authors. The watcher background task that fires when a new release lands stays in ibis-bot; book-stack-mcp exposes the data, ibis-bot does the polling.
- `stack.*` — `stack.health`, `stack.dryrun_log`, `stack.report_issue` (target `github.com/new-usemame/book-stack-mcp`). Same shape as arr-stack-mcp.

**Patterns to copy verbatim from arr-stack-mcp:**

- `src/<pkg>/policy.py` — confirm-token lifecycle with payload fingerprint binding
- `src/<pkg>/errors.py` — diagnostic ToolError envelopes with self-suggesting hints
- `src/<pkg>/fuzzy.py` — but use a book-domain calibration (author tokens, title-substring-with-trivial-guard, year extraction) rather than the arr-flavored one. ibis-bot's `tools/discover.py:_author_tokens / _title_contains / _owned_index / _is_owned_fuzzy` is the calibrated reference.
- `src/<pkg>/server.py` — same `_server_instructions()` pattern, content adapted to book-stack
- `scripts/regen-clients.sh` — pattern; the only generated client is for whatever services actually have OpenAPI specs. LL/AA/Calibre don't; the CWNG HTTP API might (verify).

The book-stack-mcp scope OVERLAPS Calibre-Web-NextGen, but does not duplicate it. CWNG is the *fork of the upstream Calibre-Web web app*. book-stack-mcp is a *thin MCP client surface that talks to CWNG over HTTP/SQLite*. The two install side-by-side. CWNG owns the user-facing web app + ebook ingestion + reader; book-stack-mcp owns the MCP tool surface that agents call.

### Read the upstream MCP and Servarr surfaces

- MCP spec at `spec.modelcontextprotocol.io` — `instructions` field, streamable-HTTP transport with auth, resources/notifications (relevant if you tackle watcher-as-MCP-notifications)
- `anthropics/dxt` and `anthropics/mcpb` repos — if MCPB / DXT one-click bundles for Claude Desktop are mature, ship one; if not, document the decision to wait and revisit at v0.3
- `jaredtrent/jellyfin-mcp` `internal/server/server.go:81-104` — gold-standard server-level instructions template. Adapt, don't copy
- `abl030/lidarr-mcp` `lidarr_report_issue` shape — every tool's description nudges the LLM to call it on unexpected errors. Port as `stack.report_issue` with the target `github.com/new-usemame/arr-stack-mcp`
- Prowlarr OpenAPI snapshot at `specs/prowlarr.openapi.json` (pinned to v2.3.5.5327). 93 paths; the search + indexer subset is what's user-facing

### Read the universal-install gap

- The current `arr-stack-mcp init` probes localhost only. Real users run their arrs at `host.docker.internal`, docker-compose hostnames like `sonarr:8989`, mDNS-style `teenyverse.lan`, or behind reverse proxies at `https://sonarr.mydomain.com`. Widen the probe.
- Streamable-HTTP transport currently has the flag wired but no bearer auth. jaredtrent's pattern at `server.go:115-156` (constant-time compare, fatal on non-localhost without token) is the right shape.
- README has per-platform Claude Desktop snippets but they haven't been verified on Windows or Linux yet.
- Confirm the install on a fresh machine. If you can't spin a VM, do it inside `docker run --rm -it python:3.12-slim bash` and document the walk-through.

## Operator's homelab — read freely; live writes allowed AFTER v0.2.0 tag

| Service | Where | Notes |
|---|---|---|
| Sonarr | `teenyverse 10.0.30.36:8989` HTTPS | API key in `[[reference_homelab_api_keys]]` memory; self-signed cert, `verify_tls: false` |
| Radarr | teenyverse `:7878` HTTPS | same |
| Lidarr | teenyverse `:8686` HTTPS | same |
| Prowlarr | teenyverse `:9696` HTTPS | key rotates; live pull via `docker exec prowlarr cat /config/config.xml \| grep -oP "(?<=<ApiKey>)[^<]+"` |
| Jellyfin | `transcoder 10.0.20.150:8096` HTTP | live pull via `docker exec ibis-bot cat /secrets/jellyfin-key` |
| ibis-bot | `defaultuser@10.0.30.36:~/ibis-bot/` | container `ibis-bot` on the same host |

Sudo passwords for all four hosts (teenyverse / transcoder / basket / router) in the homelab-API-keys memory. SSH via the `FIX-agent-get-into-ssh` skill.

**Anonymity constraint, non-negotiable:** torrent traffic routes through gluetun/AirVPN (static reserved port `47591`). Nothing you write touches that netns, the qBit port, or the gluetun container's network namespace. Reads against the arrs are LAN-only HTTPS — fine. Anything torrent-adjacent is out of scope.

**Phase ordering:**
- Development: read-only against the live stack, full-write against `docker/test-stack/docker-compose.test.yml`
- After v0.2.0 tag is published: live read-only sweep via `examples/mcp-live-homelab.py` (extend it for new tools)
- After live read-only is green: ibis-bot migration on teenyverse with the new MCP-backed wiring, e2e suite re-run, then container redeploy. This is a live write surface — operator wants the migration to be invisible to Matrix users.

## Identity + tone (non-negotiable)

Every commit, PR body, release note, README change, GitHub Issues / Discussions reply, replies to upstream maintainers — under `new-usemame`. Per-command git identity:

```
git -c user.name='new-usemame' -c user.email='248195428+new-usemame@users.noreply.github.com' commit ...
```

Never `Condo97`. Never `Co-Authored-By:`. Never `Signed-off-by:`. Never Claude attribution. Don't touch global git config.

Apply the Jellyfin LLM contribution policy to every human-facing surface. Hot-list (grep your prose before posting):

- No emoji in body copy (section icons OK; inline ☕ ✅ ❌ are not)
- Em-dash budget: ~one per paragraph max
- No marketing intensifiers: robust, powerful, seamless, delightful, comprehensive, elegant, modern, blazing fast
- No apologetic framings, no flourishes ("stands on a tower of work")
- No "TL;DR" / "In summary" / "In conclusion" wrappers
- No "Great question!" / "Happy to help!" sycophancy
- No bulleted lists where every item starts with a bolded phrase (default)
- No trash-talk of upstream maintainers

## What's in scope vs out

### In scope for arr-stack-mcp v0.2

- Richer MCP `instructions` field (lift discipline from ibis-bot's SYSTEM_PROMPT, drop the Matrix-specific bits)
- Per-user Jellyfin scoping (single-user default + per-call `user=` override + `default_user_id` config)
- `stack.*` cross-service toolset: `stack.health`, `stack.queue_status_all`, `stack.find_anywhere`, `stack.dryrun_log`, `stack.report_issue`
- Full Prowlarr surface (system_status, indexer_list, search, indexer_stats, test_indexer, health)
- Dry-run mode (`ARR_STACK_MCP_DRY_RUN=1` or `--dry-run`); short-circuit at the httpx wrapper, not per handler
- `sonarr.series_status` per-season episode breakdown
- Confirm-token persistence (SQLite at `XDG_STATE_HOME/arr-stack-mcp/state.db`)
- Streamable-HTTP transport with bearer-token auth + constant-time compare
- Init wizard probe coverage extended (docker-internal, mDNS, reverse-proxy)
- MCPB / DXT bundle for Claude Desktop one-click install, if mature
- Daily-cap-per-tool-per-hour rate limiter as runaway-agent protection. Optional; off by default; configured via `policy.daily_caps: {tool_name: int}` in YAML or `ARR_STACK_MCP_DAILY_CAP_<TOOL>=N` env var. Implementation in `policy.py`. ibis-bot's per-user caps were Matrix-driven; for an MCP server with no per-user concept, this is per-process protection against a runaway agent.

### In scope for book-stack-mcp v0.1.0

Same architectural deliverables as arr-stack-mcp v0.1.0 took (research notes, scaffolding, generated clients where applicable, curated tools, docker test stack, integration tests, CI, MCP-client smoke, release). Tool surface listed above under "Companion project: book-stack-mcp". Match arr-stack-mcp's verification standard.

### Out of scope (cannot live in an MCP server architecture)

- **Spotify-style music favorites** — explicitly excluded by the operator.
- **Pantalaimon device verification** — Pantalaimon is a Matrix E2EE proxy. It runs as a separate process between ibis-bot and the Matrix homeserver. Nothing about it maps to an MCP server. Stays Matrix-side.
- **Matrix-room awareness / room ACL** — transport-side authentication for the consumer. MCP servers don't have a Matrix concept. ibis-bot's `-> Operator` allowlist stays in `bot.py`.

### Stays native to ibis-bot during and after the migration

The OpenRouter ReAct loop, the SYSTEM_PROMPT for that loop, the Matrix room ACL (`-> Operator` allowlist), the watcher background task that posts unsolicited completion notifications, the per-user Matrix-sender → Jellyfin-user mapping, the bot-side `IBIS_DRY_RUN` env var (separate from the MCPs' dry-run), the SQLite store for discover_sessions / thread_messages / notify_seen, the bulk_download_books two-step "go" UX, audit-room rendering. ibis-bot becomes a thin Matrix shim over the two MCPs plus its own bot-loop concerns.

## Non-negotiables

- **No mocks for the API surface.** Every new tool gets an integration test against `docker/test-stack/docker-compose.test.yml`. Sonarr / Radarr / Lidarr / Prowlarr / Jellyfin containers boot cleanly in ~30s via `scripts/test-stack-up.sh`.
- **CI green on every PR.** ruff + ruff-format + mypy strict + pytest unit + pytest integration against the dockerised stack.
- **MCP-client live test before claiming done.** Extend `examples/mcp-smoke.py` (or add `examples/mcp-smoke-v02.py`) to call at least five new v0.2 tools end-to-end through the official MCP Python SDK's stdio client. Commit the transcript.
- **Live homelab smoke after release.** Extend `examples/mcp-live-homelab.py` to call at least eight read-only tools against the operator's live stack with `policy.read_only: true`. Commit the sanitized transcript.
- **ibis-bot e2e suite green before deletion.** All 10 scenarios in `data/test_e2e.py` pass under the new MCP-backed wiring BEFORE you delete `tools/arrs.py` and `tools/jellyfin.py`. After deletion, run the e2e suite again. After redeploy, run `selftest` in production via the bot.
- **Confidence ≥95% before tagging v0.2.0.** Use the seven-row checklist in `CLAUDE.md` § "Verification standard." Skipped rows require a stated reason in the release notes.
- **No breaking changes to v0.1.x tool signatures.** Additions are fine; renames or removals are not. SemVer minor, not major.
- **MIT license. Conventional Commits. release-please rolls the tag.** `feat:` minor-bumps to v0.2.0; `fix:` patch-bumps to v0.1.x. Match scope correctly — if you ship ibis-bot-migration parity as a v0.1.x patch first, use `fix:` and let v0.2.0 land later with the user-facing feature deliverables.
- **Anonymity intact.** Nothing touches gluetun or the AirVPN-scoped port. Nothing pulls live torrent data.

## Deliverables

### arr-stack-mcp v0.2.0

1. Prowlarr toolset (six tools minimum).
2. `stack.*` toolset (five tools).
3. Dry-run mode wired into the shared httpx wrapper + new `stack.dryrun_log` tool surfacing recorded calls.
4. Per-user Jellyfin scoping (config + per-call override; new `jellyfin.users_list` + `jellyfin.who_can_see` if natural).
5. `sonarr.series_status` per-season breakdown.
6. Richer MCP `instructions` field, tone-grepped.
7. Streamable-HTTP transport with bearer auth, fatal on non-localhost without token.
8. Init wizard probe coverage widened.
9. Confirm-token persistence in SQLite at the XDG state path.
10. Daily-cap-per-tool-per-hour rate limiter (config + env-var; off by default).
11. MCPB / DXT bundle for Claude Desktop one-click install if mature, else a documented decision to wait with the link to the upstream's readiness status.
12. v0.2.0 release on PyPI + GHCR + cosign-signed.
13. `examples/mcp-smoke-v02.py` + transcript.
14. Extended `examples/mcp-live-homelab.py` + sanitized transcript.
15. README updated to reflect v0.2 surface + universal-install story; ARCHITECTURE.md updated if the two-layer story gained a wrinkle.

### book-stack-mcp v0.1.0

16. Repo provisioned at `github.com/new-usemame/book-stack-mcp`, MIT-licensed, scaffolded with the same shape as arr-stack-mcp (pyproject.toml + uv + ruff + mypy strict + pytest + Conventional Commits + release-please + GHCR + cosign).
17. Tool surface: `lazylibrarian.*`, `aa.*`, `calibre.*`, `reading.*`, `follow.*`, `stack.*` (~25 tools total based on ibis-bot's working surface).
18. Generated thin client where it makes sense (CWNG HTTP API if it has an OpenAPI spec); hand-rolled httpx for LL + AA + direct-SQLite for the Calibre shelf operations CW doesn't expose over HTTP.
19. `docker-compose.test.yml` spinning Calibre-Web (or CWNG) + LazyLibrarian containers for integration tests. AA tests use the live Lucky-Librarian key against `annas-archive.gl` (read-only operations only — no actual downloads in CI).
20. CI green: ruff + mypy strict + unit + integration + MCP-client live test.
21. v0.1.0 release on PyPI + GHCR + cosign-signed.
22. README + ARCHITECTURE.md + CONTRIBUTING.md. Capability matrix.
23. Live homelab read-only smoke transcript at `examples/mcp-live-homelab.py`.

### ibis-bot migration

24. ibis-bot's deleted-file list (see "Will be deleted from ibis-bot" above) actually deleted from `teenyverse:~/ibis-bot/tools/`.
25. New adapter at `~/ibis-bot/tools/mcp_adapter.py` (or equivalent) that opens two long-lived MCP stdio sessions at bot startup — one to `arr-stack-mcp serve`, one to `book-stack-mcp serve` — and registers each MCP tool into ibis-bot's existing `REGISTRY` via thin wrappers that preserve `format_result` rendering for Matrix and surface `needs_confirm` / `confirm_token` through ibis-bot's existing two-step UX.
26. ibis-bot's `Dockerfile` updated to pull both MCPs (either as PyPI deps in `requirements.txt` or as bundled wheels). Compose file updated if needed.
27. e2e suite at `data/test_e2e.py` re-run end-to-end and 10/10 green under the new wiring BEFORE deletion is committed.
28. Container redeployed on teenyverse with `docker compose up -d --force-recreate ibis-bot` at a moment when nobody is mid-conversation in the Matrix room. Confirm by calling `selftest` from the bot post-deploy and getting back all-green probes.
29. Sanitized transcript of a post-migration Matrix exchange (or a `mcp inspector` session) committed to `examples/` showing the bot answering an arr+book query end-to-end.

## Operator hand-off note

CLAUDE.md as it stands today reads "Explicitly NOT Calibre-Web / Calibre-Web-NextGen — that's a separate project." That rule still holds for arr-stack-mcp. **book-stack-mcp is the new home for book-stack tool surface**; CWNG remains the web-app fork. Update arr-stack-mcp's CLAUDE.md to point at book-stack-mcp as the sibling, and create a new CLAUDE.md inside book-stack-mcp mirroring arr-stack-mcp's identity/tone/architecture rules with book-stack adapted scope.

## Stop conditions

Stop and ask Alex if any of these come up:

- You discover a v0.2 / v0.1 design choice is materially wrong and want to flip it before sinking implementation effort.
- ibis-bot's e2e suite fails under the new MCP-backed wiring AND you can't trace the cause to a missing tool or parity gap within one focused investigation.
- The migration would require deleting MORE files from ibis-bot than the "Will be deleted" list above. If `bot.py` / `llm.py` / `watcher.py` / `audit.py` / `store.py` / `config.py` / `policy.py` depend on something inside the migrated modules in a way that isn't a clean function-call boundary, scope it back to the operator first.
- A live home-lab write would touch the gluetun netns, the AirVPN port (47591), the qBit container, or any torrent-adjacent surface. LazyLibrarian uses the gluetun-shared providers but the LL API itself is on host network — verify before writing anything to LL.
- CWNG's HTTP API turns out to be too thin to cover the shelf operations and you'd need to write through CWNG's SQLite from a process that doesn't co-locate with it. The operator may want to add the HTTP API to CWNG first; ask.
- A credential you can't infer from the homelab-API-keys memory + the SSH read paths.
- Push access to `github.com/new-usemame/arr-stack-mcp`, the new `github.com/new-usemame/book-stack-mcp`, or `gh auth` for `new-usemame` fails. For the second repo you'll need to `gh repo create new-usemame/book-stack-mcp --public --description ...` first.
- PyPI trusted-publisher setup needed for `book-stack-mcp` (the operator's already done it for `arr-stack-mcp`; the second project needs its own publisher registered at `https://pypi.org/manage/account/publishing/`). This is operator-only.
- A license or product-policy decision only the operator can make.
- ibis-bot is mid-conversation with Maggie or Alex when you'd otherwise redeploy. Wait. The bot's logs make this visible.

Otherwise: research, design, build, test, publish, migrate. **Don't ask permission for each step — you have it.**
