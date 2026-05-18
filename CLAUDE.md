# arr-stack-mcp — operator instructions

You're building and maintaining **arr-stack-mcp** — an MCP (Model Context Protocol) server that gives any MCP-capable client (Claude Desktop, Claude Code, ibis-bot, n8n, custom agents) a clean, intelligent, unified interface to the *arr media stack: **Sonarr, Radarr, Lidarr, Prowlarr, and Jellyfin**. Explicitly NOT Calibre-Web / Calibre-Web-NextGen — that's a separate project.

The repo lives at **`https://github.com/new-usemame/arr-stack-mcp`** under operator's `new-usemame` GitHub identity.

## Identity

All work is by GitHub user **`new-usemame`** (id `248195428`, noreply email `248195428+new-usemame@users.noreply.github.com`).

**Never** use, mention, or attribute anything to `Condo97` (operator's other account). Not in commits, branches, PR bodies, or drafts.

Per-command identity for git:

```
git -c user.name='new-usemame' -c user.email='248195428+new-usemame@users.noreply.github.com' commit ...
```

Don't touch global git config. Don't add `Co-Authored-By:`, `Signed-off-by:`, or Claude attribution.

GitHub CLI: ensure `gh auth status` shows `new-usemame` as the active account. Switch with `gh auth switch --user new-usemame` if not. A classic PAT under macOS Keychain service `github-pat-arr-stack-mcp` can be created if a new scope is needed.

## Mission

Ship an MCP server that:

1. **Works against real arr/Jellyfin instances** — not mocks, not aspirational stubs. v0.1.0 is a real release backed by integration tests against running LinuxServer.io / Jellyfin containers.
2. **Reads as cared-for, not auto-generated.** The MCP space is full of single-author hobby servers with no tests, no rate limiting, hardcoded secrets, and shallow API coverage. This repo's distinguishing trait is craft: typed schemas, LLM-ergonomic tool descriptions, smart defaults, real CI.
3. **Is genuinely useful for an LLM consumer.** Tool descriptions are written for an agent's decision-making, not for human docs. Result shapes are compact and self-describing. Errors are diagnostic, not stack traces.
4. **Is customizable without being baroque.** Smart config + first-run discovery wizard. Per-service toolsets independently toggleable. Read-only and disable-destructive flags for risk-tolerance scaling.
5. **Stays in scope.** No Calibre-Web, no LazyLibrarian, no SAB queue control. The point of this repo is the *arrs and Jellyfin. Other media-stack pieces are out.

## Architecture (the two-layer rule)

This is the spine of the project. Don't deviate without diagnosis.

```
┌─────────────────────────────────────────────────────┐
│ Hand-curated LLM-friendly tools  (sonarr.search,    │
│   sonarr.series_status, stack.queue_status_all, …)  │  ← intelligence
├─────────────────────────────────────────────────────┤
│ Auto-generated thin clients per service             │
│   (from each upstream's live OpenAPI spec)          │  ← upstream sync
├─────────────────────────────────────────────────────┤
│ httpx + pydantic + MCP SDK + FastMCP                │  ← plumbing
└─────────────────────────────────────────────────────┘
```

- **Generated layer** stays dumb. Pinned OpenAPI commit, regen script, version-bumped on upstream changes. Don't hand-edit.
- **Curated layer** is where craft lives. Good tool names, good descriptions for LLM consumption, fuzzy-match helpers, compact result shapes, idempotency, confirm-token pattern for destructive ops.
- **Plumbing** is FastMCP-style. Pydantic schemas pin every tool input and output. mypy strict, ruff clean.

## Hard rules

1. **Always perform root-cause analysis.** Symptom-fixes mask real problems and pile up tech debt. Diagnose first; surface the chain (symptom → immediate cause → underlying mechanism) before touching code.
2. **No mocks for the API surface.** Every tool gets a real integration test against a real running Sonarr / Radarr / Lidarr / Prowlarr / Jellyfin container. `docker-compose.test.yml` is the source of truth.
3. **Live test from a real MCP client before claiming done.** Wire the server to Claude Desktop (or Claude Code's MCP client) and actually use it. Record the session.
4. **Confidence ≥95% before ship.** Target >95% the user-visible capability works end-to-end through a real MCP client. Self-evaluate after each phase. Below 95% → keep going.
5. **No shortcuts on the LLM-facing tool descriptions.** Drafting them is the actual product work. Read Anthropic's published guidance + OpenAI function-calling docs. A great tool description doubles real-world success rate.
6. **License is MIT.** Conventional Commits. release-please for changelogs + tags. Pre-commit hooks for ruff + mypy strict + pytest fast subset.
7. **Never ship a v0.0.1 stub.** Initial release is v0.1.0 with the full Sonarr / Radarr / Lidarr / Jellyfin read+write surface working through real containers. Prowlarr and `stack.*` can be v0.2.

## Tone for human-facing text

The Jellyfin LLM contribution policy applies to **every** human-facing surface — README, CHANGELOG entries, release notes, GitHub Issues/Discussions, PR bodies, replies to upstream, social posts. The full policy doc is at `~/Downloads/llm-contribution-policy-jellyfin.md`.

Hot-list to grep your prose against before posting/committing:

- No emoji in body copy (section icons OK; inline ☕ ✅ ❌ are not)
- Em-dash budget: ~one per paragraph max
- No marketing intensifiers (robust, powerful, seamless, delightful, comprehensive, elegant, modern, blazing fast)
- No apologetic framings
- No flourishes ("stands on a tower of work")
- No "TL;DR" / "In summary" / "In conclusion" wrappers
- No "Great question!" / "Happy to help!" sycophancy
- No bulleted lists where every item starts with a bolded phrase (as a default)

The MCP ecosystem is noisy with single-author slop. The project's quality signal is what makes it discoverable.

## Where the live arrs are (for development + testing)

Alex's home lab runs all the target services. Available for live development testing:

| Service | Host | Port | Notes |
|---|---|---|---|
| Sonarr | teenyverse `10.0.30.36` | `8989` | API key in homelab-API-keys memory |
| Radarr | teenyverse | `7878` | same memory |
| Lidarr | teenyverse | `8686` | same |
| Prowlarr | teenyverse | `9696` | API key rotates; pull live from container |
| Jellyfin | transcoder `10.0.20.150` | `8096` | admin API key file mounted into ibis-bot |
| SAB | teenyverse | `8085` | not in scope but visible |

SSH access via the `FIX-agent-get-into-ssh` skill. Sudo passwords in memory.

**Don't ship breaking changes against the live home lab.** Develop against the dockerised test stack; verify against the home lab as a final sanity check before tagging.

## Prior art to read before designing

Before deciding any architectural detail, **read** these — your design should learn from what they did well and avoid what they did badly:

- **ibis-bot's bespoke tools** at `defaultuser@10.0.30.36:~/ibis-bot/tools/` — battle-tested Sonarr/Radarr/Lidarr/Jellyfin Python tools with fuzzy matching, confirm-tokens, per-user scoping, daily-limit gates. Borrow the patterns shamelessly; ibis-bot's tools/jellyfin.py per-user-library helper is gold. Memory pointer: `reference_ibis_bot.md` + `feedback_ibis_bot_invariants.md` in the NAS-RAID6-Build memory dir.
- **`aplaceforallmystuff/mcp-arr`** — current best-in-class unified arr MCP (~137⭐, MIT, JS). Single-author, no rate limiting, shallower Lidarr coverage than ours will be, but the right shape for a unified server. Read it.
- **`abl030/lidarr-mcp`** — OpenAPI-generator approach (Python, MIT, pre-1.0). The auto-generation pattern is what you're stealing.
- **`jaredtrent/jellyfin-mcp`** — Go, ~13⭐, gold standard for Jellyfin specifically. 31 tools / 8 toolsets, `--read-only` and `--disable-destructive` flags, env-var auth. Read it for the flag-driven risk-tolerance pattern.
- **`eejd/arr-controlarr`** — vendored unified server that pulls jaredtrent's Jellyfin code. Shows what composition looks like.

Skip the dozens of single-author 0-star toy repos. They mostly teach what not to do.

## Verification standard before any release

Same enterprise bar as the operator's other projects. Don't skip rows; if you skip one, state the reason in the release notes.

1. **Research** — every tool's behavior cross-checked against the upstream OpenAPI spec for the version pinned.
2. **Unit tests** — pydantic schema round-trips, fuzzy match helpers, confirm-token lifecycle.
3. **Integration tests** — every tool exercised against a real container in `docker-compose.test.yml`. The dockerised stack is the source of truth.
4. **MCP client test** — server wired into a real client (Claude Desktop / Claude Code's MCP support / `mcp inspector`), at least 5 distinct tools called interactively, results screenshotted or transcribed into `examples/`.
5. **Resilience** — what happens when Sonarr is down? When the API key is wrong? When the URL is unreachable? Each branch hit at least once.
6. **Documentation** — README quickstart works on a clean machine. Capability matrix per service is accurate. Config reference covers every env var and every YAML key.
7. **Release gate** — version bumped, CHANGELOG entry written (passed through the LLM-tone grep), tag pushed, GitHub release created with artifacts, Docker image on GHCR built and signed.

If you can't fully verify in one session, write `notes/STOP-<topic>.md` with the chain you walked + what's still unknown. Don't ship a guess.

## Memory entries are rules, not narrative

When you write or revise memory entries for this project (`~/.claude/projects/-Users-acoundou-Other-Projects-arr-stack-mcp/memory/`), they read as standing rules:

- **Out:** "Settled YYYY-MM-DD after operator reversed earlier decision."
- **In:** rule plainly stated, **Why:** line, **How to apply:** line, `[[cross-links]]` to related memories.

Absolute dates only when load-bearing for the rule itself.

## Related projects (cross-reference)

- **NAS-RAID6-Build** (`/Users/acoundou/Other Projects/NAS-RAID6-Build/`) — the home lab itself. Contains ibis-bot, all the live arr instances, the Matrix server. Skill `/ibis-bot-soft` is the related operator-driven UX improvement effort. Many memory files in that project's memory dir apply here too.
- **Calibre-Web-NextGen** (`/Users/acoundou/Other Projects/Calibre-Web-NextGen/`) — sister project under same `new-usemame` identity. Different scope (book stack, not media stack). The tone policy, identity rules, and verification standard mirror what's used here.

If you find a memory entry in NAS-RAID6-Build or CWNG that should also apply to arr-stack-mcp, copy it into this project's memory dir (don't reference across projects — each memory dir is self-sufficient).
