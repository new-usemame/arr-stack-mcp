# Prior art research

Five reference projects plus Anthropic + OpenAI guidance. File:line citations against `main` as of 2026-05-17.

## Per-repo critiques

### aplaceforallmystuff/mcp-arr

TypeScript / Node, ~137 stars, MIT. Single `src/index.ts` (2,498 lines), `src/arr-client.ts` (861), `src/trash-client.ts`. 55 tools in `tools.json`.

- **Shape:** Flat namespace per service (`sonarr_*`, `radarr_*`, `lidarr_*`, `prowlarr_*`, `trash_*`) plus four cross-cutting (`arr_status`, `search`, `fetch`, `arr_search_all`). Dual transport: stdio default, Streamable HTTP via `MCP_TRANSPORT=http` (`src/index.ts:35-38`). Env-var config (`:48-53`); services missing URL+key silently dropped (`:56`); descriptions self-rewrite to list configured services (`:88-91`).
- **What's good:**
  - `search`/`fetch` pair (`tools.json:8-25`, dispatch `src/index.ts:1141-1151`) — the right shape for ChatGPT remote-MCP discovery: opaque IDs from `search`, resolvable via `fetch`.
  - "Configured / not configured" reflection in `arr_status` desc — the LLM sees what's actually available.
  - Reusable per-service config-review pack (`src/index.ts:132-198`): quality_profiles, health, root_folders, download_clients, naming, tags, `review_setup`. The `*_review_setup` aggregator returns everything an LLM needs to reason about misconfiguration in one call.
- **What we should do differently:**
  - No fuzzy match anywhere — search just forwards `term`; the LLM drives disambiguation.
  - No confirm token, no destructive gating, no read-only flag. `sonarr_search_missing` triggers downloads with zero guardrail.
  - No toolset toggle — 55 tools always register. Sonnet's ~100-tool sweet spot, four services eats half the budget.
  - Raw upstream JSON in responses; no projection, no compaction. 200-episode show blows the window.
  - Only `test/http-transport.test.mjs` (2.4 KB) — transport smoke test, not API contracts.
  - Single 2,500-line `index.ts`.
- **Steal:** `tools.json` as machine-readable catalogue alongside the live server. The `search`/`fetch` contract (`src/index.ts:99-125`) verbatim — ChatGPT clients depend on these names. Per-service `*_review_setup` aggregator (`:188-196`).

### abl030/lidarr-mcp

Python 3, MIT, FastMCP. Auto-generated `generated/server.py` (574 KB, ~237 tools) plus hand-written `generator/` consuming the upstream OpenAPI spec. Nix flake.

- **Shape:** Two-layer architecture identical to ours: thin auto-generated tools per OpenAPI operation, plus three hand-written high-level tools (`lidarr_get_overview`, `lidarr_search_tools`, `lidarr_report_issue`). Env-var config with `LIDARR_MODULES`, `LIDARR_READ_ONLY`, defaults env vars.
- **What's good:**
  - **Confirm-token with rich dry-run preview.** `confirm=False` performs *read-only* prep (artist lookup, album match) and returns resolved IDs plus what would happen. `confirm=True` executes. Strictly better than refusing — the LLM gets actionable feedback.
  - **`lidarr_report_issue`** returns a ready-to-paste `gh issue create` command with structured context. Every other tool's docstring nudges the LLM to call it on unexpected errors.
  - **`lidarr_search_tools` keyword search** over tool names + descriptions. With 237 tools the LLM can't see them all; in-server discovery is the workaround.
  - **`_filter_response`** auto-compacts list responses: keys projected via `fields=`, rows filtered via `key=value`, oversized nested objects replaced with `{id}` or `[N items]`. Envelope: `{summary, count, data}`.
  - **Unicode normalisation table** for MusicBrainz exotic dashes/spaces — Lidarr chokes on them. Bake in.
  - **Smart defaults chain**: explicit arg → env-var default → API auto-detect → structured `{error, step, options}` if ambiguous. Lets the LLM re-call with the disambiguated value.
  - Real integration tests in `tests/test_integration.py` (24 KB), auto-skipped without `LIDARR_API_KEY`, driven via `docker compose up -d` + `wait-for-ready.sh`.
- **What we should do differently:**
  - 237 tools is too many even with module filter — default is "all on", past OpenAI's ~100-tool bound.
  - No MCP `ToolAnnotations` — read-only mode is a string-prefix scan on HTTP verb. Annotations let smart clients show user-facing badges.
  - `verify=False` hardcoded on the httpx client. Make it configurable, default `true`.
- **Steal:** Confirm-with-preview. `*_report_issue` (target `new-usemame/arr-stack-mcp`). `*_search_tools` discovery. `_filter_response` envelope + `fields=`/`filter=`. The Unicode table. Defaults resolution chain. Docker-compose + `wait-for-ready.sh` + `@pytest.mark.integration` rig.

### jaredtrent/jellyfin-mcp

Go 1.25, MIT, modelcontextprotocol/go-sdk. 31 tools across 8 toolsets. Single static binary. The gold standard.

- **Shape:** Cobra-flagged `main.go` (`:25-32`). Tools split by domain into 11 files under `internal/server/tools/`. Dual transport: stdio default or Streamable HTTP via `--http` with bearer auth (`server.go:115-156`).
- **What's good:**
  - **Three orthogonal filter dimensions.** `--toolsets`, `--read-only`, `--disable-destructive`. `BuildToolFilter` (`tools.go:78-119`) composes them cleanly. Copy verbatim into Python.
  - **Annotation presets** — four shared `ToolAnnotations`: `AnnotReadOnly`, `AnnotWriteOp`, `AnnotWriteCreate`, `AnnotDestructive` (`tools.go:60-65`). Every registration cites one; flags filter on these, not string scans.
  - **`ConfirmationGate` with MCP elicitation fallback** (`internal/jellyfin/helpers.go`). When the client supports elicitation, actively prompts via `sess.Elicit(...)`. Otherwise returns a warning instructing retry with `confirm=true`. The right 2026 contract — graceful degradation across client capabilities.
  - **Server-level instructions string** (`server.go:81-104`). Pinned current date, "USE THESE TOOLS not your training data", compact-vs-detailed contract, per-flow troubleshoot guidance. Cheapest single-pass quality lift available.
  - **Tool descriptions cross-reference each other.** `jellyfin_search` desc: *"This tool searches by keyword only. To filter by genre, year, rating, use jellyfin_browse — e.g. jellyfin_browse genre=\"Horror\" rather than searching for \"horror\"."* One sentence prevents an entire misuse class.
  - **Compact-vs-detailed contract explicit in every list-tool description** — compact summaries vs `jellyfin_get_item` for full metadata. Stated so the LLM doesn't infer "missing field in data" from "missing in projection".
  - **`ErrResultWithHint`** (`helpers.go`) — every error carries a recovery hint. Compare mcp-arr returning raw `error.message`.
  - **Resources + prompts + completions**, not just tools. `jellyfin://server/info`, `jellyfin://guides/transcoding` — cheap reads that don't burn a tool slot. Prompts (named multi-step workflows) worth porting; resources probably v0.2.
  - **HTTP transport safety**: constant-time bearer compare (`server.go:158-170`), fatal on non-localhost without token (`:147-150`), graceful SIGINT for HTTP only (stdio must never have signal handlers — comment at `:127`).
- **What we should do differently:**
  - Action-enum-per-tool pattern (`jellyfin_system_info` with `action` ∈ {whoami, info, storage, …}) collapses related queries — saves slots but pydantic discriminated unions get awkward. See Open questions.
  - Emoji "⚠️" in `ConfirmationGate`. Strip per tone policy.
- **Steal:** `BuildToolFilter` (`tools.go:78-119`) and the four annotation presets (`:60-65`). `ConfirmationGate` with elicitation primary. Instructions block (`server.go:81-104`). `ErrResultWithHint`. Per-tool cross-references. Compact-vs-detailed contract. `ToolsetMap` declarative shape (`tools.go:18-58`).

### eejd/arr-controlarr

TypeScript, MIT, Node 22+, monorepo (`packages/{radarr,sonarr,prowlarr,bazarr,jellyseerr,server,core}`). 77 tools across six services. Vendors jaredtrent/jellyfin-mcp as a Go binary (`scripts/build-jellyfin-mcp.sh`).

- **Shape:** Each service is its own npm package + standalone MCP server (`controlarr-radarr`, etc.). `packages/server/src/index.ts` is 7 lines of re-exports. CLI wires env-configured services into one server.
- **What's good:**
  - **Per-service standalone + unified façade.** Sonarr-only users get a small binary; power users get the unified server. Mirror this.
  - **Same four annotation presets** as jellyfin-mcp (`packages/sonarr/src/tools.ts:5-12`), transplanted Go→TS. Confirms it's the right cross-language design.
  - **`shouldRegisterTool(annot, options)`** in `@controlarr/core` — cleanest implementation of the three.
  - **Compact result shapes explicit in code.** `sonarr_library` drops 30+ unused fields; `sonarr_episodes` uses single-letter keys `s`, `e` to shave tokens (`packages/sonarr/src/tools.ts:71-83`).
  - **Workflow-chaining descriptions.** `sonarr_add_series`: *"First use sonarr_search to find the tvdbId, sonarr_quality_profiles for the profile ID, and sonarr_root_folders for the path."*
  - `--services=radarr,sonarr` — axis distinct from `--toolsets` (within-service). Both useful.
- **What we should do differently:**
  - No confirm-token pattern — `--disable-destructive` is install-time only. We want the in-band gate.
  - "85 passing tests" is mock-only; no real integration tests. Don't be impressed by the badge.
  - Vendoring jaredtrent at build time via shell script is a maintenance trap. Expose Jellyfin natively in-process — that's the point of being Python.
  - No fuzzy match. Bazarr + Jellyseerr in scope — their choice, not ours.
- **Steal:** Per-service standalone + unified façade pattern. Single-letter compact keys for high-cardinality lists. Centralised `shouldRegisterTool` in a shared `core` package.

## Anthropic + OpenAI guidance synthesized

Sources: Anthropic engineering "Writing tools for agents", Anthropic docs `/docs/build-with-claude/tool-use/overview`, OpenAI function-calling guide.

- **Tool naming takeaway:** Namespace by service and resource. Anthropic endorses both prefix and suffix forms — pick one and stay consistent. Specific param names (`series_id`, not `id`). Don't have `*_search` and `*_browse` meaning "same thing, different filters" — distinct verbs.
- **Description style takeaway:** Write for a new team member, not human docs. Define niche terms (TVDB ID, MusicBrainz release group, quality profile), spell out relationships (series → seasons → episodes), call out which tool to use *instead* when likely to misroute. Cross-reference related tools by name (jellyfin-mcp does this well). Anthropic notes Opus asks for missing required params more reliably than Sonnet — so for Sonnet-tier clients, default-valued params should have explicit safe defaults rather than be inferred.
- **Schema design takeaway:** Enums and structured objects to make invalid states unrepresentable (OpenAI). Resolve cryptic IDs — accept `series_id` OR `slug` OR `tvdb_id` with documented precedence. Offer `response_format` enum (`"compact" | "detailed"`) where it matters. Pagination + truncation defaults; steer toward more targeted queries when truncating. OpenAI quotes ≤100 tools and ≤20 args/tool as in-distribution; descriptions count as input tokens — specific but concise. `strict: true` / strict-schema where supported; pydantic `model_validate` round-trip is our equivalent.
- **Error takeaway:** Actionable, not opaque — instead of "404", say "Series ID 1234 not found. Use sonarr.series_search first to discover valid IDs." Every error carries a recovery hint (jellyfin-mcp's `ErrResultWithHint`).
- **Return shape takeaway:** High-signal only. Compact list + dedicated detail tool. State explicitly which fields are *not* in the compact view so the LLM doesn't infer "missing field in data" from "missing in projection".

## Design recommendations for arr-stack-mcp

- **Tool taxonomy:**
  - Dotted namespacing (`sonarr.series_status`) preferred — dots visually signal "namespaced". If FastMCP rejects dots (spike before committing), fall back to `sonarr_series_status`. Decide once.
  - Per-service curated surface ≈ 12–18 tools. Five services × 15 ≈ 75 curated tools, headroom for `stack.*` under OpenAI's 100-tool window. Auto-generated thin clients NOT exposed by default — gated behind `--expose-raw` for power users.
  - **`stack.*` cross-cutting layer** (~6–8 tools): `stack.search` (unified across configured services, opaque IDs), `stack.fetch`, `stack.queue_status_all`, `stack.health_all`, `stack.disk_space_all`, `stack.now_playing` (Jellyfin), `stack.report_issue` (target `new-usemame/arr-stack-mcp`), `stack.what_tools` (in-server tool keyword search).
  - One toolset per service domain plus cross-cuts: `sonarr.discovery`, `sonarr.library`, `sonarr.queue`, `sonarr.config`, `jellyfin.discovery`, `jellyfin.playback`, `jellyfin.admin`, `stack`. Mirror jaredtrent's 8-toolset shape.
- **Result shapes:**
  - List tools return `{summary, count, total, items: [...]}`. Items compact (id, name/title, year, status, key counts); full detail via dedicated `*.get`.
  - Optional `fields=` on every list tool (lidarr-mcp projection).
  - Optional `filter=` as `key=value,key=value` (lidarr-mcp).
  - Compact-vs-detailed contract spelled out in *every* list tool description.
  - Every error: `{error: true, source: "<service>_api"|"validation"|"network", status?: int, message: str, hint: str, retry_with?: {...}}`.
- **Confirm-token shape:**
  - Every mutation tool takes `confirm: bool = False`. When `False`: (1) run all read-only preparatory steps (lookup, disambiguation, defaults resolution); (2) if the client supports MCP elicitation, elicit; (3) otherwise return structured `{preview: true, would_do: "...", resolved_args: {...}, confirm: "Set confirm=true to execute."}`.
  - Destructive tools (delete series, delete movie, Jellyfin restart/shutdown) carry `AnnotDestructive` *and* require `confirm=True`. `--disable-destructive` strips them entirely; otherwise the confirm gate still applies.
- **Flag set (CLI + env-var pairs):**
  - `--read-only` / `ARRSTACK_READ_ONLY=true`
  - `--disable-destructive` / `ARRSTACK_DISABLE_DESTRUCTIVE=true`
  - `--services=sonarr,radarr` / `ARRSTACK_SERVICES=...` (arr-controlarr axis)
  - `--toolsets=sonarr.discovery,jellyfin.playback` / `ARRSTACK_TOOLSETS=...` (jaredtrent axis)
  - `--expose-raw` / `ARRSTACK_EXPOSE_RAW=true` — register auto-generated thin clients (default off)
  - `--http --http-addr 127.0.0.1:8080 --http-token <token>` — bearer auth, fatal on non-localhost without token (jaredtrent pattern)
  - Per-service: `<SERVICE>_URL`, `<SERVICE>_API_KEY`, `<SERVICE>_VERIFY_TLS` (default `true`, unlike lidarr-mcp).
  - Defaults: `SONARR_DEFAULT_QUALITY_PROFILE_ID`, `SONARR_DEFAULT_ROOT_FOLDER`, etc.
- **Server-level instructions string:** Adapted from jaredtrent's, current date pinned at process start, "use these tools not your training data", compact-vs-detailed contract, per-service troubleshoot flow. No emoji, no marketing intensifiers — drop the "⚠️".

## Open questions for the implementer

- Dotted vs underscored tool names — FastMCP acceptance for `sonarr.series_status`. Spike before committing.
- Action-enum-per-tool vs one-tool-per-action. jaredtrent collapses `jellyfin_system_info` into 9 actions, saving 6 slots. Pro: tighter budget. Con: pydantic discriminated unions awkward, errors less specific. Probably worth it for config-style tools; not for action-vs-query splits.
- `stack.search` semantics: search *added* media, or upstream catalogues (TVDB/TMDB/MusicBrainz via arrs' search endpoints), or both with a `mode` enum? ChatGPT remote-MCP is more often "discover new"; home-lab LLM use is more often "what do I already have". Decide and document.
- Fuzzy match: `rapidfuzz` at the curated-layer boundary, not in thin clients. Threshold? Read ibis-bot `~/ibis-bot/tools/` first — that's the reference.
- Per-user Jellyfin scoping. ibis-bot does this; jaredtrent does not. Punt to v0.2 unless it falls out naturally.
- MCPB / DXT bundle for Claude Desktop one-click — v0.1 or wait? arr-controlarr ships one.
- Confirm 2026 Lidarr still trips on exotic Unicode dashes; apply the `_UNICODE_REPLACEMENTS` table unless verified fixed upstream.
- Auto-generated layer regen cadence: pinned commit per service + `make regen-clients`. Renovate-driven minor bumps, or manual + CHANGELOG-driven?
- `stack.queue_status_all` partial-failure shape: per-service status with structured errors (mcp-arr `arr_status` at `src/index.ts:1155-1182`), but structured envelopes not raw `error.message`.
