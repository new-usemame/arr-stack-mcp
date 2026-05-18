#!/usr/bin/env bash
# Tear down the integration-test arr stack. Pass --clean to also wipe the
# seeded config and media volumes (resets API keys and library state).

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STACK_DIR="${HERE}/docker/test-stack"
COMPOSE_FILE="${STACK_DIR}/docker-compose.test.yml"

docker compose -f "$COMPOSE_FILE" down --remove-orphans

if [[ "${1:-}" == "--clean" ]]; then
  echo "==> Clearing seeded config and media"
  # The arr containers write as PUID=1000 inside the container, which usually
  # does NOT line up with the host user on GitHub-hosted runners. A plain `rm`
  # then fails with EACCES. Reclaim ownership first (passwordless sudo on the
  # runner; no-op locally when running as the owning UID).
  for d in "$STACK_DIR/config" "$STACK_DIR/media" "$STACK_DIR/downloads"; do
    [[ -e "$d" ]] || continue
    if [[ -w "$d" ]] && [[ "$(stat -f '%u' "$d" 2>/dev/null || stat -c '%u' "$d" 2>/dev/null)" == "$(id -u)" ]]; then
      rm -rf "$d"
    elif command -v sudo >/dev/null 2>&1; then
      sudo rm -rf "$d"
    else
      # Last resort: borrow a privileged container to do the delete from inside.
      docker run --rm -v "$STACK_DIR:/work" alpine sh -c "rm -rf /work/$(basename "$d")"
    fi
  done
fi
