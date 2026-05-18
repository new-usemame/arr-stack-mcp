# Goal: Design, build, integration-test, and publish arr-stack-mcp v0.1.0

You are Claude Opus 4.7 or higher — Max Ultra tier. You are running with full agency to research, design, implement, test, and publish a real open-source project on Alex's behalf. **No cope. No bandaids. Find root causes. Test against live systems with real containers — never against mocks.** If you can't measure it, you don't know it. If something seems hard, you haven't dug deep enough yet.

## Mission

Build and publish **arr-stack-mcp** — an MCP server that gives any MCP-capable agent (Claude Desktop, Claude Code, ibis-bot, n8n, custom agents) a clean, intelligent, unified interface to the *arr media stack: **Sonarr, Radarr, Lidarr, Prowlarr, Jellyfin**. Explicitly NOT Calibre-Web / Calibre-Web-NextGen — that's a separate project.

Publish target: **`https://github.com/new-usemame/arr-stack-mcp`** (the username is "new-usemame" — the missing 'n' in "username" is intentional, do not "correct" it).

The design intent is **"intelligent softbody"**: customizable, gracefully discoverable, simple and logical codepaths, smart config that does the right thing by default, easy to interface with and easy to use. It must feel cared-for, not auto-generated boilerplate.

## Hard preconditions (refuse if any fail)

1. `pwd` is `/Users/acoundou/Other Projects/arr-stack-mcp`. If not, instruct `cd "/Users/acoundou/Other Projects/arr-stack-mcp"` and exit cleanly.
2. `gh auth status` shows active = `new-usemame`. If `Condo97` is active, instruct `gh auth switch --user new-usemame` and exit cleanly.
3. **Read `./CLAUDE.md` first.** It has the standing rules for this project (identity, mission, hard rules, architecture spine, tone policy, verification standard). Internalize before starting.

## Recommended starting design (challenge it if research suggests better)

The operator and I converged on this shape. **You are free — encouraged — to challenge any of these picks if your research turns up better options.** Don't waste cycles second-guessing the easy stuff (MIT license, SemVer). Do challenge architecture if you've found something genuinely better.

- **Language:** Python 3.12 + `uv`. FastMCP / official `mcp` SDK. MIT license.
- **Architecture:** Two layers — an auto-generated thin client per service (from each upstream's live OpenAPI spec) plus a hand-curated LLM-friendly tool layer on top. The curated layer is where the intelligence lives.
- **Tool taxonomy:** per-tool tags `read` / `write` / `destructive`. Global `--read-only` and `--disable-destructive` flags.
- **Confirm-token pattern** for destructive ops (borrowed from ibis-bot). Optional per-deployment.
- **Toolsets:** per-service (`sonarr.*`, `radarr.*`, `lidarr.*`, `prowlarr.*`, `jellyfin.*`) plus a separate `stack.*` toolset for cross-service composables (queue across all, unified health check, search media everywhere). Each toolset independently toggleable.
- **Smart config:** YAML with env-var overrides. `arr-stack-mcp init` first-run wizard probes localhost / standard ports / common docker networks and auto-fills.
- **Transports:** stdio + streamable-HTTP.
- **Distribution:** Docker image (primary, on GHCR), PyPI package, `uvx` one-shot.
- **Testing:** pytest + dockerised LinuxServer arr containers + real Jellyfin container. CI on GitHub Actions. **No mocks for the API surface.**
- **Conventional Commits + release-please.** Pre-commit hooks for ruff + mypy strict + a fast pytest subset.

## How to develop your own context

Don't take any of this as a prescription. Build your own model by reading.

### Read the prior art

- **ibis-bot's bespoke tools** at `defaultuser@10.0.30.36:~/ibis-bot/tools/` over SSH (key-based via `FIX-agent-get-into-ssh` skill). Read `arrs.py`, `jellyfin.py`, `music.py`, `discover.py`, `registry.py`, `policy.py`. Battle-tested Python tools for the exact same services you're wrapping. The fuzzy-matching, confirm-token, per-user-scoping patterns are gold.
- `https://github.com/aplaceforallmystuff/mcp-arr` — current best-in-class unified arr MCP. Single-author JS, no rate limiting. Read it for shape; you should aim to be its better-tested, better-typed sibling.
- `https://github.com/abl030/lidarr-mcp` — Python, OpenAPI-generator pattern. Steal the regeneration approach.
- `https://github.com/jaredtrent/jellyfin-mcp` — Go, gold standard for Jellyfin specifically. 31 tools / 8 toolsets, `--read-only` / `--disable-destructive` flags. Read it for the flag pattern.
- `https://github.com/eejd/arr-controlarr` — composition example.

### Read each arr's live OpenAPI

Pull from the running services rather than stale docs:

| Service | OpenAPI URL (against teenyverse `10.0.30.36`) |
|---|---|
| Sonarr | `http://10.0.30.36:8989/api/v3/openapi.json` |
| Radarr | `http://10.0.30.36:7878/api/v3/openapi.json` |
| Lidarr | `http://10.0.30.36:8686/api/v1/openapi.json` |
| Prowlarr | `http://10.0.30.36:9696/api/v1/openapi.json` |
| Jellyfin | `http://10.0.20.150:8096/api-docs/openapi.json` |

API keys per `reference_homelab_api_keys.md` in the NAS-RAID6-Build memory dir (read it).

### Look at the operator's memory for tone + tactics

- `/Users/acoundou/.claude/projects/-Users-acoundou-Other-Projects-NAS-RAID6-Build/memory/` — `reference_ibis_bot.md`, `feedback_ibis_bot_invariants.md`, `feedback_no_bandaids.md`, `reference_homelab_api_keys.md`, `reference_teenyverse_ssh.md` apply.
- `/Users/acoundou/.claude/projects/-Users-acoundou-Other-Projects-Calibre-Web-NextGen/memory/` — `feedback-always-root-cause.md`, `feedback-enterprise-verification-standard.md`, `feedback-jellyfin-llm-tone.md`, `feedback-memory-no-date-narrative.md`, `feedback-no-laziness-no-guessing.md` apply.

These are the operator's standing rules. Honor them even though they live in sister projects' memory dirs — copy any you need into this project's memory as you go.

## What "intelligent softbody" means in practice

- **Tool descriptions** are written for an LLM consumer, not a human reading docs. Each tool description should make an agent's decision easier: when to call it, what to pass, what to expect back. Read Anthropic's published guidance on tool-use prompting before drafting.
- **Result shapes** are LLM-ergonomic. Don't dump 200-key JSON for a series lookup. Surface the 6 fields a human cares about, with a compact `extra` blob for callers that need more.
- **Errors are diagnostic.** "Sonarr returned 503 — is the indexer pool healthy? try `sonarr.indexer_status`." Self-suggesting next steps.
- **Auto-discovery is real.** `arr-stack-mcp init` should find a typical docker-compose-on-localhost arr stack without help. If it can't, it should tell the user exactly what's missing and how to provide it.
- **Idempotent everywhere it can be.** Re-running an "add" returns the existing item, doesn't 500, doesn't duplicate.
- **Confirm tokens are opaque (UUID), single-use, time-limited, and audit-logged** when logging is enabled.
- **The server itself is observable.** `/health` endpoint, structured logs, per-tool latency metrics when HTTP transport is on.

## Non-negotiables

- **No mocks for the API surface.** Every tool gets a real test against a real running Sonarr / Radarr / Lidarr / Prowlarr / Jellyfin container. Use LinuxServer.io images — they're what people actually run. Provide a single `docker-compose.test.yml` that spins the entire test stack.
- **CI runs integration tests on every PR**, not just unit tests. If GHA runner specs make the full stack too heavy, run a slimmer subset (Sonarr + Jellyfin) on PR and the full stack on tag.
- **Live test from a real MCP client before claiming done.** Hook the server up to Claude Desktop (or Claude Code's MCP client, or `mcp inspector`). Actually use it for at least 5 distinct tools. Record the session — commit transcript or screenshots into `examples/`.
- **Document the OpenAPI version each generated client is pinned to.** Ship a regeneration script. When upstream changes, regen → re-test → bump version → release.
- **Don't ship a v0.0.1 stub.** Initial release is **v0.1.0** with the full Sonarr / Radarr / Lidarr / Jellyfin read+write surface working end-to-end against real containers. Prowlarr and `stack.*` can be v0.2.
- **MIT license. Conventional Commits. release-please for changelog + tags. ruff + mypy strict.**
- **Confidence ≥95% before tagging v0.1.0.** Use the verification checklist in `CLAUDE.md` § "Verification standard." Skipped rows require a stated reason in release notes.

## Deliverables (v0.1.0)

1. **The repo** at `github.com/new-usemame/arr-stack-mcp`, populated with:
   - Working MCP server (Docker image on GHCR + PyPI package)
   - README with quickstart, full config reference, capability matrix per service
   - ARCHITECTURE.md or equivalent — written walkthrough of the two-layer design
   - CONTRIBUTING.md explaining the OpenAPI regeneration flow
   - `docker-compose.test.yml` reproducing the integration test stack
   - Pre-commit hooks + `.github/workflows/ci.yml`
2. **A v0.1.0 GitHub release** with built artifacts (wheel on PyPI + Docker image on GHCR, tagged + signed).
3. **A demonstration session** showing arr-stack-mcp answering a real "what's on my stack?" question from a real MCP client, with the transcript or screenshots committed to `examples/`.
4. **A short final report back here** covering: what you built, what surprised you, what you cut from scope and why, what's next on the v0.2 path.

## Stop conditions

Stop and ask Alex if any of these come up:

- Push access to `github.com/new-usemame/arr-stack-mcp` fails (you might need a new PAT scope; keychain service `github-pat-arr-stack-mcp`).
- You discover a design choice in the recommended stack is materially wrong and you want to flip it before sinking implementation effort.
- You hit a credential you don't have and can't infer (the homelab API-keys memory should have most).
- You hit a license or product-policy decision only the operator can make.

Otherwise: research, design, build, test, publish. **Don't ask permission for each step — you have it.**
