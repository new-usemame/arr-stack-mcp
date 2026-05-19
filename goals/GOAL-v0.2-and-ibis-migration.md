# Goal: arr-stack-mcp v0.2 — universal install + in-scope ibis-bot patterns + ibis-bot migrated off its hand-rolled httpx layer

You are Claude Opus 4.7 or higher — Max Ultra tier, high context window. You are running with full agency to research, design, implement, test, and publish v0.2 of arr-stack-mcp on Alex's behalf, AND to migrate the operator's locally-developed Matrix tool runner (ibis-bot at `defaultuser@10.0.30.36:~/ibis-bot/`) off its hand-rolled arr+Jellyfin transport so it goes through arr-stack-mcp instead. **No cope. No bandaids. Find root causes. Test against real containers, a real MCP client, and ibis-bot's real e2e suite — never mocks.** If you can't measure it, you don't know it. If something seems hard, you haven't dug deep enough yet.

You have a large context window. Use it. Read the codebase, the prior research notes, the upstream specs, and ibis-bot's current source thoroughly before designing anything. This prompt sets the goal and the constraints — it does not enumerate implementation steps. That's your job.

## Mission

Three intertwined deliverables, one release window.

1. **arr-stack-mcp v0.2.0** — Prowlarr + cross-service `stack.*` tools + the in-scope ibis-bot patterns v0.1 deferred. Cut from `github.com/new-usemame/arr-stack-mcp` via release-please.
2. **Universal install** — anyone running an arr stack should install and configure arr-stack-mcp in under five minutes via the path of their choice (uvx, PyPI, Docker, Claude Desktop one-click bundle if mature). Streamable-HTTP transport with bearer auth. An `init` wizard that just works on a typical home-lab setup. A config-by-env-var story documented end-to-end. Per-platform Claude Desktop config snippets (macOS, Windows, Linux).
3. **ibis-bot migration** — `~/ibis-bot/tools/arrs.py` and `~/ibis-bot/tools/jellyfin.py` deleted on teenyverse; ibis-bot's tool registry now sources those tools from `arr-stack-mcp serve --transport stdio` via the standard MCP stdio client. Calibre / LazyLibrarian / Anna's Archive / Matrix / watcher / per-user-Matrix-scoping stay native to ibis-bot. The migration must keep ibis-bot's 10-scenario `data/test_e2e.py` suite passing, redeploy cleanly, and not interrupt Alex + Maggie's live Matrix usage.

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

- `tools/arrs.py` — Sonarr + Radarr + Lidarr wrappers, hand-rolled httpx. You will delete this.
- `tools/jellyfin.py` — Jellyfin wrappers, per-user Matrix-sender mapping. You will delete this.
- `tools/registry.py` and `tools/__init__.py` — how tools register
- `tools/dryrun.py` — the IBIS_DRY_RUN pattern. Lift the shape, not the file. Apply at our shared httpx wrapper, not per-handler.
- `tools/hide_tools.py` — toolset enable/disable
- `selftest.py` (top-level + `tools/selftest.py`) — parallel `asyncio.gather` health probes with per-probe timeouts and per-probe exception isolation. Port as `stack.health`.
- `policy.py` — confirm-token lifecycle. Compare against our `src/arr_stack_mcp/policy.py`.
- `llm.py` — 250-line SYSTEM_PROMPT for ibis-bot's OpenRouter loop. Read it for ideas, but DON'T port verbatim — most of it is Matrix-specific consumer-side. The MCP-relevant lessons (compact-vs-detailed contract, "do not restate tool output", confirm-token discipline, vocabulary mapping) belong in our `instructions` field at a far higher level of abstraction.
- `bot.py` — how the agent loop calls the tool registry. You'll need to know this for the migration.
- `IBIS-WORKFLOW.md` — the design doc
- `data/test_e2e.py` — the 10-scenario e2e suite. Must stay green after the migration.
- `docker-compose.yml`, `Dockerfile`, `requirements.txt` — how it's deployed

Use `ssh defaultuser@10.0.30.36` (the `FIX-agent-get-into-ssh` skill if interactive; SSH key auth otherwise). Sudo password `Correct-Horse-Battery-9Staple`. Read-only sweeps + `rsync -az` are fine; do not push changes back without confirmation.

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

In scope for v0.2 (port from ibis-bot or build natively):

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

Out of scope (different domains; the book stack lives at `/Users/acoundou/Other Projects/Calibre-Web-NextGen/`):

- LazyLibrarian, Anna's Archive, Calibre / Calibre-Web shelves, reading-status tracking, author-follow / new-release watching, Spotify-style music favorites, daily-caps-per-user, Matrix-room awareness, Pantalaimon device verification.

Stays native to ibis-bot during and after the migration:

- The OpenRouter ReAct loop, the SYSTEM_PROMPT for that loop, the Matrix room ACL (`-> Operator` allowlist), the watcher background task that posts "✅ landed" notifications, the per-user Matrix-sender → Jellyfin-user mapping, the `IBIS_DRY_RUN` env var (ibis-bot's separate from ours), the SQLite store for discover_sessions / thread_messages / notify_seen, the bulk_download_books two-step UX, every Calibre/LL/AA-flavored tool.

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

## Deliverables (v0.2.0)

1. Prowlarr toolset (six tools minimum).
2. `stack.*` toolset (five tools).
3. Dry-run mode wired into the shared httpx wrapper + new `stack.dryrun_log` tool surfacing recorded calls.
4. Per-user Jellyfin scoping (config + per-call override; new `jellyfin.users_list` + `jellyfin.who_can_see` if natural).
5. `sonarr.series_status`.
6. Richer MCP `instructions` field, tone-grepped.
7. Streamable-HTTP transport with bearer auth, fatal on non-localhost without token.
8. Init wizard probe coverage widened.
9. Confirm-token persistence in SQLite at the XDG state path.
10. MCPB / DXT bundle for Claude Desktop one-click install if mature, else a documented decision to wait with the link to the upstream's readiness status.
11. v0.2.0 release on PyPI + GHCR + cosign-signed.
12. `examples/mcp-smoke-v02.py` + transcript.
13. Extended `examples/mcp-live-homelab.py` + sanitized transcript.
14. ibis-bot's `tools/arrs.py` + `tools/jellyfin.py` deleted on teenyverse; replaced by MCP-stdio shim. e2e suite green. Container redeployed cleanly.
15. README updated to reflect v0.2 surface + universal-install story; ARCHITECTURE.md updated if the two-layer story gained a wrinkle.

## Stop conditions

Stop and ask Alex if any of these come up:

- You discover a v0.2 design choice is materially wrong and want to flip it before sinking implementation effort.
- ibis-bot's e2e suite fails under the new MCP-backed wiring AND you can't trace the cause to a missing tool or parity gap within one focused investigation.
- The migration would require deleting more than `tools/arrs.py` and `tools/jellyfin.py` from ibis-bot. If Calibre / LL / AA / watcher / bot.py depends on something inside those modules, scope it back to the operator first.
- A live home-lab write would touch the gluetun netns, the AirVPN port (47591), the qBit container, or any torrent-adjacent surface.
- A credential you can't infer from the homelab-API-keys memory + the SSH read paths above.
- Push access to `github.com/new-usemame/arr-stack-mcp` or `gh auth` for `new-usemame` fails.
- A license or product-policy decision only the operator can make.
- ibis-bot is mid-conversation with Maggie or Alex when you'd otherwise redeploy. Wait. The bot's logs make this visible.

Otherwise: research, design, build, test, publish, migrate. **Don't ask permission for each step — you have it.**
