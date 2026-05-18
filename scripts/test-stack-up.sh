#!/usr/bin/env bash
# Boot the integration-test arr stack and wait for every service to be healthy.
# Seeds predictable API keys into each LinuxServer config so the test harness
# can authenticate without going through Sonarr's UI-driven first-run wizard.
#
# Usage: scripts/test-stack-up.sh [--clean]

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STACK_DIR="${HERE}/docker/test-stack"
COMPOSE_FILE="${STACK_DIR}/docker-compose.test.yml"

# Predictable test-only API keys. These are not secrets — they're used solely
# against ephemeral containers on localhost and are committed for
# reproducibility. Never reuse against a real arr instance.
declare -rA TEST_KEYS=(
  [sonarr]=ar5tcmcptestsonarr00000000000001
  [radarr]=ar5tcmcptestradarr00000000000002
  [lidarr]=ar5tcmcptestlidarr00000000000003
  [prowlarr]=ar5tcmcptestprowlarr0000000000004
)

if [[ "${1:-}" == "--clean" ]]; then
  echo "==> Tearing down any existing test stack and removing volumes"
  docker compose -f "$COMPOSE_FILE" down -v --remove-orphans || true
  rm -rf "$STACK_DIR/config" "$STACK_DIR/media" "$STACK_DIR/downloads"
fi

echo "==> Seeding LinuxServer config volumes with predictable API keys"
for svc in sonarr radarr lidarr prowlarr; do
  cfg_dir="$STACK_DIR/config/$svc"
  mkdir -p "$cfg_dir"
  key="${TEST_KEYS[$svc]}"
  case $svc in
    sonarr|radarr) ver=v3 ;;
    *) ver=v1 ;;
  esac
  cat > "$cfg_dir/config.xml" <<EOF
<?xml version="1.0" encoding="utf-8"?>
<Config>
  <BindAddress>*</BindAddress>
  <Port>$( [[ $svc == sonarr ]] && echo 8989; [[ $svc == radarr ]] && echo 7878; [[ $svc == lidarr ]] && echo 8686; [[ $svc == prowlarr ]] && echo 9696 )</Port>
  <UrlBase></UrlBase>
  <EnableSsl>False</EnableSsl>
  <SslPort>9898</SslPort>
  <ApiKey>$key</ApiKey>
  <AuthenticationMethod>None</AuthenticationMethod>
  <AuthenticationRequired>DisabledForLocalAddresses</AuthenticationRequired>
  <Branch>main</Branch>
  <LogLevel>info</LogLevel>
  <SslCertPath></SslCertPath>
  <SslCertPassword></SslCertPassword>
  <UpdateMechanism>Docker</UpdateMechanism>
  <InstanceName>$( echo $svc | tr a-z A-Z )</InstanceName>
</Config>
EOF
  echo "  $svc → $key"
done

mkdir -p "$STACK_DIR/config/jellyfin" "$STACK_DIR/media" "$STACK_DIR/downloads"

echo "==> docker compose up -d"
docker compose -f "$COMPOSE_FILE" up -d

echo "==> Waiting for healthchecks to converge…"
deadline=$(( $(date +%s) + 240 ))
declare -a services=(sonarr radarr lidarr prowlarr jellyfin)
declare -A status
for svc in "${services[@]}"; do status[$svc]=pending; done

while (( $(date +%s) < deadline )); do
  all_healthy=true
  for svc in "${services[@]}"; do
    name="arr-mcp-test-$svc"
    state=$(docker inspect -f '{{.State.Health.Status}}' "$name" 2>/dev/null || echo "missing")
    if [[ "$state" == "healthy" ]]; then
      if [[ "${status[$svc]}" != "healthy" ]]; then
        echo "  $svc ✓"
        status[$svc]=healthy
      fi
    else
      all_healthy=false
      status[$svc]=$state
    fi
  done
  if $all_healthy; then
    echo "==> Stack healthy"
    echo "    sonarr   http://localhost:18989   X-Api-Key: ${TEST_KEYS[sonarr]}"
    echo "    radarr   http://localhost:17878   X-Api-Key: ${TEST_KEYS[radarr]}"
    echo "    lidarr   http://localhost:18686   X-Api-Key: ${TEST_KEYS[lidarr]}"
    echo "    prowlarr http://localhost:19696   X-Api-Key: ${TEST_KEYS[prowlarr]}"
    echo "    jellyfin http://localhost:18096   (no key yet — Jellyfin needs first-run wizard or scripted setup)"
    exit 0
  fi
  sleep 3
done

echo "==> Timed out waiting for stack. Current state:"
for svc in "${services[@]}"; do
  echo "  $svc: ${status[$svc]}"
done
echo
echo "==> Logs from any unhealthy container:"
for svc in "${services[@]}"; do
  if [[ "${status[$svc]}" != "healthy" ]]; then
    echo "--- $svc ---"
    docker logs --tail 40 "arr-mcp-test-$svc" || true
  fi
done
exit 1
