# Contributing to arr-stack-mcp

Thanks for considering a contribution. This document covers the workflow for code, the OpenAPI regeneration cadence, and the verification gate every change passes before merge.

## Setup

```
git clone https://github.com/new-usemame/arr-stack-mcp
cd arr-stack-mcp
uv sync
uv run pre-commit install
```

`uv sync` installs runtime and dev dependencies into a project-local `.venv`. The pre-commit hook runs ruff format + lint + mypy + a fast pytest subset on every commit.

## Daily workflow

```
# Fast inner loop
uv run pytest -q                     # unit tests only
uv run ruff check src/ tests/        # lint
uv run mypy src/ tests/              # types (strict)

# Before pushing
scripts/test-stack-up.sh             # docker-compose with real arrs + Jellyfin
uv run pytest                        # all tests including integration
scripts/test-stack-down.sh --clean
```

## OpenAPI regeneration

The generated thin clients in `src/arr_stack_mcp/generated/<service>/` are produced by `scripts/regen-clients.sh` from the OpenAPI specs vendored in `specs/`. Specs are pinned per service at a specific upstream release tag (or, for Jellyfin, at a running-server version snapshot).

### When to regenerate

- An upstream service published a new release with API additions or signature changes.
- A new endpoint becomes useful for a curated tool.
- The integration tests start failing with `UpstreamBadRequest` (shape mismatch).

### How

```
# Check whether any upstream has drifted from our pinned snapshot.
scripts/regen-clients.sh --check

# Pull the latest GitHub release of each Servarr family service + Jellyfin live spec.
scripts/regen-clients.sh --refresh

# Regenerate only the named services from the on-disk snapshots.
scripts/regen-clients.sh sonarr radarr

# Full regen (default).
scripts/regen-clients.sh
```

After regenerating:

1. Run `uv run mypy src/` and `uv run pytest -q`.
2. If a curated tool now references a removed endpoint or shape, fix it before committing the generated diff.
3. Commit the spec snapshot, tag file, and generated client together with a `feat(deps): regen <service> client to <tag>` message.

The regeneration script intentionally uses `uvx openapi-python-client@0.24.3` in an ephemeral env, because that tool pins older versions of typer + ruff that conflict with this project's dev deps. Do not add it to `pyproject.toml`.

## Adding a tool

1. Pick the service. Open `src/arr_stack_mcp/tools/<service>/_models.py` and add Pydantic input + output models. Inputs become the JSON Schema the MCP catalogue advertises; outputs pin the response shape.
2. Open `src/arr_stack_mcp/tools/<service>/tools.py` and add an `@mcp.tool(name="<service>.<verb_object>", description="...")` block inside `register_all`. The description is written for an agent's decision-making — describe when to call it, what to pass, what comes back, and which related tools to use instead when likely to misroute.
3. First line of the handler is `policy.check("<service>.<verb_object>", Tag.READ | Tag.WRITE | Tag.DESTRUCTIVE)`.
4. Call the appropriate generated-client function. Coerce UNSET sentinels through the local `_str_or_none / _int_or_none / _bool_or_none` helpers.
5. Add a unit test in `tests/unit/test_<service>_<tool>.py`. Real-network exercise goes in `tests/integration/`, gated by the `integration` marker.
6. Update `README.md`'s capability matrix.

## Tool description style

Tool descriptions are the product. Follow these rules:

- Open with what the tool does and the user question it answers.
- State which related tool to use *instead* if the agent is likely to misroute (cross-reference by tool name).
- Define niche terms (TVDB id, MusicBrainz mbid, BaseItemKind) inline.
- Specify the result shape — what comes back, what fields are compact vs detailed.
- Note pre-conditions (which other tool to call first to obtain the id).
- Idempotency, side effects, and confirm-token requirements stated explicitly.

## Verification checklist

Every PR is verified against the seven-row checklist in `CLAUDE.md`:

1. **Research** — tool behavior cross-checked against the pinned OpenAPI spec.
2. **Unit tests** — schema round-trips, fuzzy match, confirm-token lifecycle.
3. **Integration tests** — exercised against a real container in `docker-compose.test.yml`.
4. **MCP client test** — server in a real client, 5+ distinct tools called.
5. **Resilience** — service down, wrong key, unreachable URL.
6. **Documentation** — README + capability matrix accurate.
7. **Release gate** — version + CHANGELOG + tag + GHCR + PyPI.

If a row is skipped, state the reason in the PR body or release notes.

## Commit + PR style

- Use Conventional Commits (`feat(sonarr): ...`, `fix(policy): ...`, `chore(deps): ...`).
- `release-please` consumes these to generate the CHANGELOG and tag.
- PR bodies stay plain text, ideally under six sentences. No emoji, no marketing intensifiers, no apologetic framings. The Jellyfin LLM contribution policy applies (see `CLAUDE.md` §tone).

## Identity

This repo is published under the GitHub user `new-usemame`. Commits use that identity per-command:

```
git -c user.name='new-usemame' \
    -c user.email='248195428+new-usemame@users.noreply.github.com' \
    commit -m "..."
```

Do not touch global git config.

## License

MIT. By contributing you agree your contribution will be licensed under the same.
