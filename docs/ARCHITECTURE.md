# Architecture

arr-stack-mcp is a Python 3.12 MCP server built on `mcp.server.fastmcp`. The codebase deliberately splits into two layers: an auto-generated thin client per upstream service, and a hand-curated tool layer on top.

## The two-layer rule

```
┌─────────────────────────────────────────────────────────────┐
│ Curated MCP tools                                            │
│ src/arr_stack_mcp/tools/<service>/                           │
│   tools.py        — registers tools with FastMCP             │
│   _client.py      — constructs the generated client          │
│   _models.py      — pydantic input + output schemas          │
└─────────────────────────────────────────────────────────────┘
                            ▲
┌─────────────────────────────────────────────────────────────┐
│ Generated thin clients                                       │
│ src/arr_stack_mcp/generated/<service>/                       │
│   client.py       — Client + AuthenticatedClient             │
│   api/<tag>/      — one module per upstream operation        │
│   models/         — pydantic models for every spec component │
└─────────────────────────────────────────────────────────────┘
                            ▲
┌─────────────────────────────────────────────────────────────┐
│ Plumbing                                                     │
│   httpx async + pydantic v2 + structlog + mcp 1.27           │
└─────────────────────────────────────────────────────────────┘
```

### Generated layer

Pulled from each upstream's published OpenAPI spec by `scripts/regen-clients.sh`, which fetches from GitHub at a pinned release tag and runs `uvx openapi-python-client@0.24.3 generate`. Specs and tags live in `specs/`.

Rules:

- Do not hand-edit anything under `src/arr_stack_mcp/generated/`.
- Re-run regen on upstream version bumps. The diff is the source of truth for what changed.
- The generated layer is excluded from `mypy` strict and ruff lint — its hygiene is the upstream tool's responsibility.

### Curated layer

Each service has three files:

- `_client.py`: constructs the generated `Client` / `AuthenticatedClient` with the operator's URL, API key, timeout, and TLS posture.
- `_models.py`: pydantic input and output schemas for every tool. Input models become the JSON Schema the MCP catalogue advertises; output models become the response shape.
- `tools.py`: a single `register_all(mcp, svc, policy)` function that uses `@mcp.tool(...)` decorators to register every tool against the running FastMCP instance.

Rules:

- Every tool's first line is `policy.check(tool_name, Tag.READ | Tag.WRITE | Tag.DESTRUCTIVE)`. The policy module raises `PolicyDenied` when `--read-only` or `--disable-destructive` is active.
- Every destructive tool follows the two-call confirm-token flow: first call without token returns a plan + token, second call with the token executes.
- Result envelopes use the shared `ToolEnvelope[T]` shape — `{ok, query, count, total, items}` — for list-style tools.

## Error model

`src/arr_stack_mcp/errors.py` defines the diagnostic envelopes:

- `ToolError` — base class. Carries `message` and a self-suggesting `hint`.
- `PolicyDenied` — the call shape was valid; the server posture (flags) blocked it.
- `ConfirmRequired` — destructive tool called without a valid confirm token.
- `UpstreamUnavailable` — the arr / Jellyfin service did not respond (transport failure).
- `UpstreamAuthFailed` — 401 / 403 from the upstream service (likely rotated key).
- `UpstreamBadRequest` — non-auth 4xx (usually generated-client lag).
- `Ambiguous` — free-text lookup matched multiple rows.

These translate cleanly into MCP error responses with hints the agent can act on.

## Policy

`src/arr_stack_mcp/policy.py` implements:

- Per-tool risk tags (`read`, `write`, `destructive`).
- Two flags drawn from jellyfin-mcp's design (`--read-only`, `--disable-destructive`).
- Confirm-token issuance + single-use consumption, bound to the request payload via `fingerprint(payload)` so a token cannot be reused with different args.
- Time-limited tokens with TTL sweep on every operation.

## Server bootstrap

`arr-stack-mcp serve` (defined in `src/arr_stack_mcp/cli.py`):

1. Loads YAML config + expands env-var references.
2. Constructs the `Policy` from flags + config.
3. Builds the `FastMCP` server with server-level instructions.
4. Calls `register_all(mcp, svc, policy)` for each enabled service.
5. Runs the chosen transport (stdio default; streamable-http opt-in).

## Verification standard

Every release passes the seven-row gate in `CLAUDE.md` §verification standard:

1. Research — every tool cross-checked against the pinned OpenAPI version.
2. Unit tests — pydantic schema round-trips, fuzzy match helpers, confirm-token lifecycle.
3. Integration tests — every tool exercised against a real LinuxServer.io / Jellyfin container.
4. MCP client test — server in a real client (`mcp inspector`, Claude Desktop), 5+ tools called interactively.
5. Resilience — service down, wrong key, unreachable URL each hit once.
6. Documentation — README quickstart works on a clean machine; capability matrix accurate.
7. Release gate — version bumped, CHANGELOG entry tone-grepped, tag pushed, GHCR + PyPI artifacts published.

## Where to look first

- A tool description reads odd → `src/arr_stack_mcp/tools/<service>/tools.py` (the `@mcp.tool(...)` description= block).
- A schema doesn't validate → `src/arr_stack_mcp/tools/<service>/_models.py`.
- A confirm flow misbehaves → `src/arr_stack_mcp/policy.py` + `tests/unit/test_policy.py`.
- Upstream returned a shape we didn't expect → `scripts/regen-clients.sh --check` shows drift from the pinned snapshot.
- The agent picked the wrong tool → revise the description in `tools.py`; cross-reference related tools by name.
