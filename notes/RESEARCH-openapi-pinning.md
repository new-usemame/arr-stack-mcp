# OpenAPI pinning — source of truth per service

Specs in `research/openapi/`. Pulled from upstream `latest` GitHub releases (servarr family) and live transcoder (Jellyfin).

| Service | Pinned tag | Spec path on upstream | Paths | Live version (teenyverse) | Drift |
|---|---|---|---|---|---|
| Sonarr | v4.0.17.2952 | `src/Sonarr.Api.V3/openapi.json` | 162 | 4.0.16.2944 | -1 patch |
| Radarr | v6.1.1.10360 | `src/Radarr.Api.V3/openapi.json` | 164 | 6.0.4.10291 | -1 minor |
| Lidarr | v3.1.0.4875 | `src/Lidarr.Api.V1/openapi.json` | 161 | 3.1.0.4875 | exact |
| Prowlarr | v2.3.5.5327 | `src/Prowlarr.Api.V1/openapi.json` | 93 | 2.3.0.5236 | -5 patch |
| Jellyfin | 10.11.8 | live `/api-docs/openapi.json` from transcoder | TBC | 10.11.8 | exact |

## Notes

- Sonarr/Radarr/Lidarr/Prowlarr do **not** serve the OpenAPI spec at runtime — `/api/v*/openapi.json` returns 404 even with a valid API key. The spec is published only in the source tree under `src/<Project>.Api.V*/openapi.json`. Regen script must fetch from GitHub, not the running service.
- Jellyfin **does** serve its spec at `/api-docs/openapi.json` from the running server — pulling from there gives a guarantee that the spec matches the running version.
- All four Servarr services serve over HTTPS only on teenyverse (self-signed cert; `verify=False` for development; production deployments should set `JELLYFIN_VERIFY=true` or equivalent and trust the cert).
- Servarr internal API spec version (the `info.version` inside the JSON) is meaningless — Sonarr ships `info.version=3.0.0` for v4 of the product. Pin by upstream **release tag**, not by spec self-version.

## Regeneration policy

`scripts/regen-clients.sh` (Phase C):

1. Read the pinned tag from `research/openapi/<service>.tag`.
2. Fetch the spec from `https://raw.githubusercontent.com/<Project>/<Project>/<tag>/src/<Project>.Api.V*/openapi.json` (or Jellyfin's live URL).
3. Diff against the on-disk copy in `research/openapi/`.
4. If diff is non-empty: regen the generated client into `src/arr_stack_mcp/generated/<service>/`, run unit tests, bump the project minor version, write a CHANGELOG entry.
5. If diff is empty: print "no upstream change since <tag>" and exit 0.

To bump the pinned tag: `scripts/regen-clients.sh --bump-tag <service> <new-tag>` updates the `.tag` file and re-runs regen.
