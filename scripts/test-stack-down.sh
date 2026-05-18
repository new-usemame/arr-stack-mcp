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
  rm -rf "$STACK_DIR/config" "$STACK_DIR/media" "$STACK_DIR/downloads"
fi
