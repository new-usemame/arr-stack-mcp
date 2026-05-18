#!/usr/bin/env bash
# Regenerate the per-service OpenAPI clients under src/arr_stack_mcp/generated/.
#
# Each Servarr-family spec is pulled from upstream GitHub at the tag stored in
# specs/<svc>.tag. The Jellyfin spec is pulled live from the running transcoder
# instance OR from the snapshot in specs/jellyfin.openapi.json — pick by flag.
#
# Usage:
#   scripts/regen-clients.sh                 # regen all services from snapshots
#   scripts/regen-clients.sh sonarr radarr   # regen named services only
#   scripts/regen-clients.sh --refresh       # re-pull every spec from upstream
#                                             # before regenerating
#   scripts/regen-clients.sh --check         # diff snapshots against upstream
#                                             # without writing anything
#
# Lives in scripts/ so it's executable; the actual spec snapshots and pin tags
# live in specs/ (committed). research/openapi/ is the gitignored scratch dir
# used during the initial Phase A research and is not the source of truth.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPECS_DIR="${HERE}/specs"
OUT_DIR="${HERE}/src/arr_stack_mcp/generated"

# Lock to a specific generator version so regen is reproducible.
GEN="openapi-python-client==0.24.3"

declare -A SERVARR_REPO=(
  [sonarr]="Sonarr/Sonarr"
  [radarr]="Radarr/Radarr"
  [lidarr]="Lidarr/Lidarr"
  [prowlarr]="Prowlarr/Prowlarr"
)
declare -A SERVARR_APIVER=(
  [sonarr]=V3
  [radarr]=V3
  [lidarr]=V1
  [prowlarr]=V1
)
declare -A SERVARR_PROJECT=(
  [sonarr]=Sonarr
  [radarr]=Radarr
  [lidarr]=Lidarr
  [prowlarr]=Prowlarr
)

JELLYFIN_LIVE_URL="${JELLYFIN_LIVE_URL:-http://10.0.20.150:8096/api-docs/openapi.json}"

mode="regen"
services=()
while (( $# )); do
  case "$1" in
    --refresh) mode="refresh" ;;
    --check)   mode="check" ;;
    -h|--help)
      sed -n '1,30p' "$0"; exit 0 ;;
    -*) echo "unknown flag: $1" >&2; exit 2 ;;
    *)  services+=("$1") ;;
  esac
  shift
done
if (( ${#services[@]} == 0 )); then
  services=(sonarr radarr lidarr prowlarr jellyfin)
fi

mkdir -p "$SPECS_DIR" "$OUT_DIR"

fetch_servarr_spec() {
  local svc=$1 tag=$2
  local repo=${SERVARR_REPO[$svc]}
  local apiver=${SERVARR_APIVER[$svc]}
  local project=${SERVARR_PROJECT[$svc]}
  local url="https://raw.githubusercontent.com/$repo/$tag/src/$project.Api.$apiver/openapi.json"
  curl -sL --fail -o "$SPECS_DIR/$svc.openapi.json" "$url"
}

latest_tag() {
  local repo=$1
  gh api -X GET "repos/$repo/releases/latest" --jq '.tag_name' 2>/dev/null
}

regen_service() {
  local svc=$1
  local spec="$SPECS_DIR/$svc.openapi.json"
  local out="$OUT_DIR/$svc"

  if [[ ! -f "$spec" ]]; then
    echo "==> $svc: spec missing at $spec — run with --refresh first" >&2
    return 1
  fi

  echo "==> $svc: regenerating client into $out"
  rm -rf "$out"
  mkdir -p "$out"

  # openapi-python-client wants a writable workdir; run inside specs/ so its
  # generated package lands next to the spec, then move it.
  local workdir
  workdir=$(mktemp -d)
  trap "rm -rf '$workdir'" RETURN
  (
    cd "$workdir"
    uvx --quiet "$GEN" generate \
      --path "$spec" \
      --meta none \
      --output-path "$svc" \
      --overwrite
  )
  # Move generated content into the canonical generated/<svc>/ folder.
  rm -rf "$out"
  mv "$workdir/$svc" "$out"
  echo "    wrote $(find "$out" -type f -name '*.py' | wc -l | tr -d ' ') python files"
}

case "$mode" in
  refresh|check)
    for svc in "${services[@]}"; do
      if [[ "$svc" == jellyfin ]]; then
        url="$JELLYFIN_LIVE_URL"
        tmp=$(mktemp)
        if ! curl -sLk --fail -o "$tmp" "$url"; then
          echo "==> jellyfin: live fetch from $url failed; keeping existing snapshot" >&2
          rm -f "$tmp"
          continue
        fi
        if [[ "$mode" == check ]]; then
          if cmp -s "$tmp" "$SPECS_DIR/jellyfin.openapi.json"; then
            echo "==> jellyfin: snapshot matches live"
          else
            echo "==> jellyfin: drift detected from live"
            diff <(jq -S . "$SPECS_DIR/jellyfin.openapi.json" 2>/dev/null) \
                 <(jq -S . "$tmp" 2>/dev/null) | head -40 || true
          fi
          rm -f "$tmp"
        else
          mv "$tmp" "$SPECS_DIR/jellyfin.openapi.json"
          # Capture the running version into the .tag file so regen is reproducible.
          jq -r '.info.version' "$SPECS_DIR/jellyfin.openapi.json" > "$SPECS_DIR/jellyfin.tag"
          echo "==> jellyfin: snapshot updated to v$(<$SPECS_DIR/jellyfin.tag)"
        fi
      else
        repo=${SERVARR_REPO[$svc]}
        tag=$(latest_tag "$repo")
        if [[ -z "$tag" ]]; then
          echo "==> $svc: could not resolve latest tag (gh auth issue?)" >&2
          continue
        fi
        tmp=$(mktemp)
        url="https://raw.githubusercontent.com/$repo/$tag/src/${SERVARR_PROJECT[$svc]}.Api.${SERVARR_APIVER[$svc]}/openapi.json"
        if ! curl -sL --fail -o "$tmp" "$url"; then
          echo "==> $svc: fetch from $url failed" >&2
          rm -f "$tmp"
          continue
        fi
        if [[ "$mode" == check ]]; then
          if cmp -s "$tmp" "$SPECS_DIR/$svc.openapi.json"; then
            echo "==> $svc: snapshot matches upstream $tag"
          else
            echo "==> $svc: drift detected from upstream $tag"
          fi
          rm -f "$tmp"
        else
          mv "$tmp" "$SPECS_DIR/$svc.openapi.json"
          echo "$tag" > "$SPECS_DIR/$svc.tag"
          echo "==> $svc: snapshot updated to $tag"
        fi
      fi
    done
    [[ "$mode" == check ]] && exit 0
    ;;
esac

for svc in "${services[@]}"; do
  regen_service "$svc"
done

echo
echo "==> All requested services regenerated. Run \`uv run mypy src/\` and \`uv run pytest -q\` to verify."
