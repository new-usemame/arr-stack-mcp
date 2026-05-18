# syntax=docker/dockerfile:1.7
# Multi-stage build for arr-stack-mcp. uv-based dependency install in the
# builder stage; python:3.12-slim runtime keeps the published image small.

FROM ghcr.io/astral-sh/uv:0.10.8-python3.12-bookworm-slim AS builder

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_NO_CACHE=1

WORKDIR /build

# Copy lockfile + project metadata first so dependency resolution caches across
# code-only changes.
COPY pyproject.toml uv.lock README.md LICENSE ./

# Install dependencies into /build/.venv without the project itself.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

COPY src/ ./src/
COPY specs/ ./specs/

# Install the project itself (final-step layer).
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


FROM python:3.12-slim-trixie AS runtime

# Run as non-root for safety. UID/GID 1000 matches the LinuxServer.io pattern
# so volume mounts line up out of the box.
RUN groupadd --system --gid 1000 arr && \
    useradd --system --uid 1000 --gid arr --create-home --shell /usr/sbin/nologin arr

# Copy the resolved venv from the builder. arr-stack-mcp's console_scripts
# entrypoint lands at /opt/venv/bin/arr-stack-mcp.
COPY --from=builder /build/.venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER arr
WORKDIR /home/arr

# MCP via stdio is the default; streamable-http opt-in via --transport http.
EXPOSE 8080

LABEL org.opencontainers.image.source="https://github.com/new-usemame/arr-stack-mcp" \
      org.opencontainers.image.description="MCP server for Sonarr / Radarr / Lidarr / Jellyfin" \
      org.opencontainers.image.licenses="MIT"

ENTRYPOINT ["arr-stack-mcp"]
CMD ["serve", "--transport", "stdio"]
