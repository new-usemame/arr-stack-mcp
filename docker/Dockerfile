# syntax=docker/dockerfile:1.7
# Multi-stage build for arr-stack-mcp. uv installs deps + project into the
# final /opt/venv path in the builder (so shebangs are already correct when
# the venv lands in the runtime stage), then a slim python:3.12 runtime
# picks the venv up unchanged.

FROM ghcr.io/astral-sh/uv:0.10.8-python3.12-trixie-slim AS builder

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_NO_CACHE=1 \
    UV_PROJECT_ENVIRONMENT=/opt/venv

WORKDIR /build

# Copy lockfile + project metadata first so dependency resolution caches
# across code-only changes.
COPY pyproject.toml uv.lock README.md LICENSE ./

# Install dependencies into /opt/venv without the project itself, so the
# generated console-script shebangs already point at /opt/venv/bin/python
# (the same path the runtime stage will use).
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

COPY src/ ./src/
COPY specs/ ./specs/

# Install the project itself NON-editable. The default `uv sync` editable
# install drops a .pth file pointing at /build/src — fine inside the builder
# but the source dir does not exist in the slim runtime stage, so imports
# fail with ModuleNotFoundError. --no-editable copies the source into the
# site-packages dir, making the venv fully self-contained.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-editable


FROM python:3.12-slim-trixie AS runtime

# Run as non-root for safety. UID/GID 1000 matches the LinuxServer.io pattern
# so volume mounts line up out of the box.
RUN groupadd --system --gid 1000 arr && \
    useradd --system --uid 1000 --gid arr --create-home --shell /usr/sbin/nologin arr

# Copy the resolved venv from the builder. arr-stack-mcp's console_scripts
# entrypoint lands at /opt/venv/bin/arr-stack-mcp.
COPY --from=builder /opt/venv /opt/venv
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
