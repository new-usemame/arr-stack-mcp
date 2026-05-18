# OpenAPI surface map — what we expose vs what we skip

Source specs in `research/openapi/`. This note distills which upstream endpoints become curated MCP tools in v0.1.0.

## Servarr family — shared shape

Sonarr, Radarr, Lidarr, and Prowlarr share Servarr's API shape. All four have the same set of cross-cutting tag categories:

| Category | Purpose | v0.1.0 coverage |
|---|---|---|
| `System` | health, status, ping, version | Yes — `*.system_status`, `*.health` |
| `Command` | trigger background actions (Refresh, Search) | Yes — `*.run_command` (gated) |
| `Queue` | active downloads | Yes — `*.queue_list`, `*.queue_remove` |
| `History` | past actions | Yes — `*.history` (read-only) |
| `Blocklist` | rejected releases | Read-only `*.blocklist_list` |
| `Calendar` | upcoming releases | Yes — `*.calendar` |
| `Tag` | user tags | Read-only `*.tag_list` |
| `QualityProfile` / `MetadataProfile` / `LanguageProfile` / `ReleaseProfile` | profile config | Read-only `*.profiles` (used to surface profile ids for add operations) |
| `RootFolder` | filesystem roots | Read-only `*.root_folders` |
| `DownloadClient` / `Indexer` / `ImportList` / `Notification` | per-service config | **Skip** — admin surface, not for an LLM consumer |
| `CustomFormat` / `CustomFilter` / `AutoTagging` | curator-only | **Skip** |
| `Backup` / `Update` / `LogFile` / `Task` | maintenance | **Skip** |
| `Authentication` / `Login` | session login | **Skip** — we use API-key auth, never the login form |

The MCP tool surface focuses on the **user-visible workflow**: search for media, add it, see what's queued, see what's downloaded, see what's missing, trigger a search. The admin surface (download clients, indexers, custom formats) is left to the upstream UI.

## Per-service highlights

### Sonarr (v4.0.17, 162 paths, V3 API)
- `Series` (5): list, add, lookup, edit, delete
- `Episode` (4) + `EpisodeFile` (7): episode-level monitoring + file edits
- `SeriesLookup` (1) — `GET /api/v3/series/lookup?term=...` — primary discovery endpoint
- `Queue` (3): list, paged, single-item detail
- `Calendar` (2) + `Wanted/Missing` (1)
- `SeasonPass` (1) — bulk monitor flip
- `Command` (4)

### Radarr (v6.1.1, 164 paths, V3 API)
- `Movie` (5): list, add, lookup, edit, delete
- `MovieFile` (7), `MovieLookup` (3), `Collection` (4)
- `Calendar` (1) + `Missing` (1)
- `Queue` (3), `Command` (4)

### Lidarr (v3.1.0, 161 paths, V1 API)
- `Artist` (5), `Album` (6), `Track` (2), `TrackFile` (6)
- `ArtistLookup` (1) + `AlbumLookup` (1)
- `AlbumStudio` (1) — bulk monitor flip
- `MetadataProfile` (5) — distinct from Sonarr/Radarr's QualityProfile-only model
- `Queue` (3), `Command` (4)

### Prowlarr (v2.3.5, 93 paths, V1 API)
- `Indexer` (11) — read-only `*.indexer_list`
- `Search` (3) — `POST /api/v1/search` is the cross-indexer search endpoint, useful for "is this release findable on my pool?"
- `IndexerStats` (1), `IndexerStatus` (1)
- `Application` (11) — read-only; surfaces which arrs are linked
- **Deferred to v0.2** per CLAUDE.md hard rule #7

### Jellyfin (10.11.8 live, 388 paths)
- Top tags: `LiveTv` (41 — **skip**, niche), `Image` (37 — read-only image serving), `Library` (25), `User` (14), `UserLibrary` (10), `Session` (16), `Playstate` (9), `Playlists` (11), `Library Structure` (8), `ItemLookup` (11)
- v0.1.0 coverage: library browse + search, item details, user list, recent additions, watch state (play/pause/seek by session), now-playing / sessions list, scan trigger.
- **Per-user scoping is load-bearing** — Jellyfin returns different results depending on the `userId` param. ibis-bot's `jellyfin.py` handles this via a default-admin + opt-in per-user resolution; port that pattern.
- **Skip** in v0.1.0: LiveTv, SyncPlay, DynamicHls, Subtitle editing, Plugins, Configuration (admin).

## Pattern: write-side has bulk-everywhere

All four arrs ship `*/bulk` endpoints (PUT/DELETE) for collection-level edits — bulk monitor flips, bulk delete, bulk tag. ibis-bot's `bulk_*` confirm-token pattern maps cleanly. Tool naming: `sonarr.series_bulk_monitor(ids: [int], monitored: bool, confirm_token: str | None)`.

## Pattern: every entity supports `lookup` separately from `list`

`*/lookup` is the discovery endpoint (TVDB / TMDB / MusicBrainz search) — what you call before adding. `*/<entity>` is the library endpoint — what you call to see what's already added. The curated tool layer should expose these as distinct tools with distinct names: `sonarr.series_search` (library) vs `sonarr.series_lookup_external` (TVDB).

## What stays in the generated layer only

The full 162/164/161/93 endpoints are accessible via the generated thin client (`from arr_stack_mcp.generated.sonarr import SonarrClient`). The curated MCP tool layer only exposes the workflow-relevant subset. Power users who need admin surface can call the thin client directly from the same package.
