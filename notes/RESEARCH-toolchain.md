# Toolchain validation (2026-05)

Sources: Context7 (`/modelcontextprotocol/python-sdk`, `/openapi-generators/openapi-python-client`) and PyPI JSON endpoints. Docker Hub for the base image.

## MCP SDK
- Package: `mcp == 1.27.1` (PyPI latest stable)
- FastMCP: built-in to `mcp`. Import path confirmed in Context7 examples: `from mcp.server.fastmcp import FastMCP`.
- Standalone `fastmcp` (Prefect, currently 3.3.1) is a separate ecosystem fork. FastMCP 1.0 was upstreamed into the official SDK; the standalone repo continues to add features outside the spec. For an MCP server that should track the protocol cleanly, prefer the in-SDK FastMCP. Note: the SDK migration guide mentions a rename `FastMCP` -> `MCPServer` (new import path `mcp.server.mcpserver`), so wrap the import in one module and only use it from there to limit blast radius if/when the rename lands in a release we adopt.
- Why this pin: 1.27.x is the active 1.x line. Pin minor with a compatible range to pick up patch fixes without surprise on a rename release.

## OpenAPI generator
- Pick: `openapi-python-client == 0.24.2` (latest, March 2025).
- Why: generates async `httpx.AsyncClient` clients natively (every endpoint module ships `asyncio` and `asyncio_detailed`); pins `pydantic>=2.10,<3`; supports Python 3.9-3.13 (3.12 fine); produces typed `Response[T]`, `UNSET` sentinel, fluent `with_headers` / `with_timeout`. Matches our async + pydantic v2 + httpx stack exactly.
- Considered and rejected: `datamodel-code-generator` (0.57.0) emits pydantic models only - no client. We'd still hand-roll the httpx layer. Use case is narrower; skip.
- Known compat issues with Servarr specs: the live Sonarr/Radarr/Lidarr/Prowlarr OpenAPI documents historically contain a few enums and oneOf shapes that trip strict generators. Plan to vendor the spec and run `openapi-python-client generate --custom-template` if needed; expect to set `field_extra_keys`/discriminator tweaks in `openapi-python-client.yaml`. Not blocking - documented as a known wrinkle in the upstream issue tracker.
- Known compat issues with Jellyfin's spec: Jellyfin publishes an OpenAPI 3.0 spec via `/openapi`. It is large (~1MB) with deep polymorphism on `BaseItemDto`. Generation works but produces a large package; we should `--meta=none` and treat the generated client as an internal sub-package. Watch for date-time format strings (`yyyy-MM-ddTHH:mm:ss.fffffffZ`) - the generator emits `datetime` and httpx handles it, but tests should round-trip a real response.

## pyproject.toml deps (exact pins or compatible ranges)

```toml
[project]
requires-python = ">=3.12"
dependencies = [
  "mcp>=1.27,<2",
  "httpx>=0.28,<1",
  "pydantic>=2.10,<3",
  "pydantic-settings>=2.6,<3",
  "structlog>=25.5,<26",
  "typer>=0.25,<1",
  "anyio>=4.6,<5",
  "pyyaml>=6.0,<7",
]

[dependency-groups]
dev = [
  "ruff>=0.15.13,<0.16",
  "mypy>=2.1,<3",
  "pytest>=9.0,<10",
  "pytest-asyncio>=1.1,<2",
  "pytest-httpx>=0.35,<1",
  "pre-commit>=4.6,<5",
  "openapi-python-client>=0.24.2,<0.25",
  "types-pyyaml",
]
```

`pytest-asyncio` 1.x: set `asyncio_mode = "auto"` under `[tool.pytest.ini_options]` so plain `async def test_*` functions are collected without per-test decorators. Context7 did not surface the default in this query - verify against the project's own docs when wiring CI, but `auto` is the well-known recommended setting for async-heavy test suites.

`mypy` 2.x is a real major version bump from 1.x with stricter defaults; pin upper bound to `<3` and enable `strict = true` in `[tool.mypy]`. If 2.x produces noise on generated client code, exclude the generated package directory rather than relaxing strictness on hand-written code.

`structlog` 25.5.0 has asyncio support; pair with `structlog.contextvars` for request-scoped binding. No separate anyio package needed.

## Docker base
- Pick: `python:3.12-slim` (currently aliased to `slim-trixie`, Debian 13).
- Why: smallest practical Debian-based image with full glibc and apt available. `httpx[http2]`, `cryptography`, and any future native dep build cleanly. `python:3.12-alpine` saves ~30MB but uses musl libc - wheels for `cryptography`/`orjson`/`watchfiles` are not always published for musl, forcing source builds and slow CI. `ghcr.io/astral-sh/uv:python3.12-bookworm-slim` is attractive if we standardise on `uv` for both dev and runtime install, but locks the image to Bookworm (Debian 12) until Astral publishes a Trixie variant, and the "uv-native" benefit is moot at runtime (uv only matters at build time). Use `python:3.12-slim` for the final stage; optionally use `ghcr.io/astral-sh/uv` as a builder stage in a multi-stage Dockerfile for fast deps install, then copy `.venv` into the slim runtime.

## Open issues to revisit after Phase C
- Confirm `pytest-asyncio` 1.1 default `asyncio_mode` against its docs before merge; pin in `pyproject.toml` regardless.
- Watch for the `FastMCP` -> `MCPServer` rename landing in a tagged `mcp` release; if it does before v0.1.0, isolate the import in one module and bump the lower bound.
- Re-evaluate `openapi-python-client` >=0.25 when released; check whether Servarr spec quirks needed custom templates and whether the new version removes the need.
- Decide whether to vendor each upstream OpenAPI spec at a pinned commit (preferred, per `RESEARCH-openapi-pinning.md`) versus fetching live at codegen time.
- If we add HTTP/2 to httpx (`httpx[http2]`), confirm `h2` builds on the slim base; if not, drop HTTP/2 or switch base.
