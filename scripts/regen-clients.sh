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

JELLYFIN_LIVE_URL="${JELLYFIN_LIVE_URL:-http://localhost:8096/api-docs/openapi.json}"

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

  # Post-regen patch: Sonarr/Radarr/Lidarr/Prowlarr ship an OpenAPI HttpUri
  # object schema but serialize the field as a plain string at runtime
  # (e.g. health-check wikiUrl). The generated `HttpUri.from_dict` calls
  # `dict(src_dict)` which crashes on strings. Patch it to accept either.
  patch_http_uri "$out"

  # Post-regen patch: openapi-python-client 0.24.3 emits
  # `from_dict(response.text)` instead of `from_dict(response.json())` when
  # the OpenAPI spec lists multiple content types for a response (the Servarr
  # specs include `application/json`, `text/json`, and `application/*+json`
  # — the generator picks `text/json` and treats it as plain text). Affects
  # ~179 endpoints across Sonarr/Radarr/Lidarr/Prowlarr.
  patch_response_text_to_json "$out"

  # Post-regen patch: make every model's `from_dict` tolerate None. Upstream
  # frequently returns `null` for a nullable nested object (Lidarr's
  # nextAlbum on a newly-added artist is the canonical case). Without this,
  # nested-model parsers crash with `'NoneType' object is not iterable`.
  patch_models_none_tolerance "$out"
}

patch_response_text_to_json() {
  local out=$1
  # Two flavors of the same generator bug, both triggered by the Servarr
  # specs listing application/json + text/json + application/*+json for the
  # same operation:
  #   1) single-object: `from_dict(response.text)` — string parsed as a dict
  #   2) list:          `_response_xxx = response.text` followed by
  #                     `for item in _response_xxx` — iterates over characters
  #
  # Both are deterministic; sed substitution is safe because every endpoint
  # already gates parsing on response.status_code matching the response shape.
  local files1 files2 c1 c2
  files1=$(grep -rl "from_dict(response\.text)" "$out/api/" 2>/dev/null || true)
  files2=$(grep -rl "_response_[0-9]* = response\.text" "$out/api/" 2>/dev/null || true)
  c1=0; [[ -n "$files1" ]] && c1=$(echo "$files1" | wc -l | tr -d ' ')
  c2=0; [[ -n "$files2" ]] && c2=$(echo "$files2" | wc -l | tr -d ' ')
  if [[ "$c1" == "0" && "$c2" == "0" ]]; then
    return 0
  fi
  for f in $files1 $files2; do
    if [[ "$(uname)" == "Darwin" ]]; then
      sed -i '' \
        -e 's/from_dict(response\.text)/from_dict(response.json())/g' \
        -e 's/\(_response_[0-9]*\) = response\.text/\1 = response.json()/g' \
        "$f"
    else
      sed -i \
        -e 's/from_dict(response\.text)/from_dict(response.json())/g' \
        -e 's/\(_response_[0-9]*\) = response\.text/\1 = response.json()/g' \
        "$f"
    fi
  done
  echo "    patched response.text -> response.json() in single-object ($c1) and list ($c2) endpoints"
}

patch_http_uri() {
  local out=$1
  local http_uri="$out/models/http_uri.py"
  if [[ ! -f "$http_uri" ]]; then
    return 0
  fi
  python3 - <<PY "$http_uri"
import sys, re
path = sys.argv[1]
src = open(path).read()
if "ARRSTACK_HTTPURI_STR_OK" in src:
    sys.exit(0)
needle = "    @classmethod\n    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:\n        d = dict(src_dict)"
patched = (
    "    @classmethod\n"
    "    def from_dict(cls: type[T], src_dict):\n"
    "        # ARRSTACK_HTTPURI_STR_OK — Servarr family serializes some HttpUri\n"
    "        # fields as plain strings even though the spec models them as objects.\n"
    "        if isinstance(src_dict, str):\n"
    "            return cls(full_uri=src_dict)\n"
    "        d = dict(src_dict)"
)
new = src.replace(needle, patched)
if new == src:
    sys.exit(0)
open(path, "w").write(new)
PY
}

patch_models_none_tolerance() {
  # Make every generated model's `from_dict` accept None gracefully.
  #
  # Pattern bug in openapi-python-client 0.24.3: parent models that hold
  # nullable nested objects emit `if isinstance(_x, Unset): x = UNSET else:
  # x = Inner.from_dict(_x)`. When upstream returns `x: null`, _x is None,
  # falls through to the else branch, and `Inner.from_dict(None)` crashes
  # in `dict(None)`. Lidarr's ArtistResource hit this on `nextAlbum: null`
  # for newly-added artists.
  #
  # Cheapest universal fix: insert a `None -> cls()` guard immediately
  # before the first `d = dict(src_dict)` in each generated model. Inserting
  # at that location (rather than transforming the function signature)
  # handles models that have lazy `from ..models.* import` lines between
  # the function signature and `d = dict(...)`.
  local out=$1
  local count=0
  while IFS= read -r f; do
    grep -q "ARRSTACK_FROM_DICT_NONE_OK" "$f" 2>/dev/null && continue
    python3 - <<'PY' "$f"
import sys
path = sys.argv[1]
src = open(path).read()
if "ARRSTACK_FROM_DICT_NONE_OK" in src:
    sys.exit(0)
needle = "        d = dict(src_dict)"
i = src.find(needle)
if i < 0:
    sys.exit(0)
guard = (
    "        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a\n"
    "        # nullable nested object; treat it as 'no fields supplied'.\n"
    "        if src_dict is None:\n"
    "            return cls()\n"
)
open(path, "w").write(src[:i] + guard + src[i:])
PY
    count=$((count+1))
  done < <(grep -rl "^        d = dict(src_dict)$" "$out/models" 2>/dev/null)
  if [[ "$count" -gt 0 ]]; then
    echo "    patched None-tolerance into $count model from_dict()"
  fi
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
