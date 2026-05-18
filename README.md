# arr-stack-mcp

A Model Context Protocol server that gives any MCP-capable agent a clean, unified interface to the *arr media stack and Jellyfin.

- Sonarr, Radarr, Lidarr — series, movies, music
- Prowlarr — indexer health and cross-indexer search (v0.2)
- Jellyfin — library browse, playback control, recent additions
- Cross-service composables under `stack.*` (v0.2)

Status: pre-v0.1.0. The published v0.1.0 release will cover the full Sonarr / Radarr / Lidarr / Jellyfin read+write surface, backed by integration tests against real containers in `docker-compose.test.yml`. Detailed quickstart, config reference, and capability matrix land with v0.1.0.

## License

MIT
