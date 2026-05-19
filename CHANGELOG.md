# Changelog

All notable changes to arr-stack-mcp are tracked here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0](https://github.com/new-usemame/arr-stack-mcp/compare/v0.1.2...v0.2.0) (2026-05-19)


### Features

* **auth:** streamable-HTTP transport with static bearer-token auth ([9353ad5](https://github.com/new-usemame/arr-stack-mcp/commit/9353ad5972510f88af63dc130c4687ba3f0f9420))
* **config:** widen init wizard probe to docker-internal + mDNS + compose hostnames ([97e1895](https://github.com/new-usemame/arr-stack-mcp/commit/97e189514bfa5f18d40a67f2892526cd5b6a1e43))
* **jellyfin:** per-call `user_id` override + `jellyfin.users_list` tool ([7c2b568](https://github.com/new-usemame/arr-stack-mcp/commit/7c2b5682fbe5a4f8fb9173728fc6af2b870095c6))
* **policy:** dry-run mode at the curated-tool boundary ([c3fea4e](https://github.com/new-usemame/arr-stack-mcp/commit/c3fea4e5a7c4a32a50ee0f4d0846437cc42a831e))
* **policy:** per-tool hourly call cap for runaway-agent protection ([74b0c9f](https://github.com/new-usemame/arr-stack-mcp/commit/74b0c9f841bd02f82cdbe90151ff989c85d846a1))
* **policy:** SQLite-backed confirm-token persistence ([4b5bf5f](https://github.com/new-usemame/arr-stack-mcp/commit/4b5bf5f6142604f44afe519632d39bd9a0b26599))
* **prowlarr:** v0.2 curated tool surface (7 tools) ([edb3623](https://github.com/new-usemame/arr-stack-mcp/commit/edb3623f79968fa6917bc6eea979ee1e8aa426b6))
* **server:** richer instructions field with LLM-discipline anchors ([39c1772](https://github.com/new-usemame/arr-stack-mcp/commit/39c1772dac7bb2954a7eecc7a3de9067e4446a4f))
* **sonarr:** per-season `sonarr.series_status` tool ([9c38491](https://github.com/new-usemame/arr-stack-mcp/commit/9c384918cfde8e91f9f2783ecd05972d247a688b))
* **stack:** cross-service find_anywhere + queue_status_all ([3cb04e8](https://github.com/new-usemame/arr-stack-mcp/commit/3cb04e8cb11547dba9e6e274d30f5ea8d89fcbd0))
* **stack:** cross-service stack.dryrun_log + stack.report_issue + stack.health ([3e4936f](https://github.com/new-usemame/arr-stack-mcp/commit/3e4936fdf3ef7fe4ffb00da375cfb331a4ea3b88))


### Bug Fixes

* **server:** rename underscore-prefixed handler params; FastMCP rejects them ([d4bbdb4](https://github.com/new-usemame/arr-stack-mcp/commit/d4bbdb48cfbc43145030d677aa7ae8d03c520f6f))
* **tests:** mypy strict pass over tests/ (CI gate) ([aef6ee9](https://github.com/new-usemame/arr-stack-mcp/commit/aef6ee95d041af304a2a53ab99555e064f514fe8))


### Documentation

* **design:** v0.2 + book-stack-mcp + ibis-bot migration design note ([23ce25c](https://github.com/new-usemame/arr-stack-mcp/commit/23ce25c16f5139fa5b0aa322bbf4d3871b05e4e3))
* **examples:** refresh live-homelab transcript for v0.2 ([2c6a172](https://github.com/new-usemame/arr-stack-mcp/commit/2c6a172d17a634713978f0f0f2bbd51421acbd2c))
* **goals:** add v0.2 + ibis-bot migration goal prompt for next session ([6486b09](https://github.com/new-usemame/arr-stack-mcp/commit/6486b0944e4d4f9e31ac8f2fa068c89596c01bad))
* **goals:** expand v0.2 prompt to cover book-stack-mcp sibling project ([38be11d](https://github.com/new-usemame/arr-stack-mcp/commit/38be11d27dddd8257878b9c624418913fc8e3121))
* v0.2 smoke test + extended live homelab + README capability matrix ([c38ce6d](https://github.com/new-usemame/arr-stack-mcp/commit/c38ce6db9023732de844e20f8193688694dd4380))

## [0.1.2](https://github.com/new-usemame/arr-stack-mcp/compare/v0.1.1...v0.1.2) (2026-05-19)


### Bug Fixes

* **fuzzy:** port acronym-aware match + year-tag extraction from ibis-bot ([bcbf6f7](https://github.com/new-usemame/arr-stack-mcp/commit/bcbf6f7eb1d03e7c4f5e91e4b05931c84cde0a1d))

## [0.1.1](https://github.com/new-usemame/arr-stack-mcp/compare/v0.1.0...v0.1.1) (2026-05-18)


### Bug Fixes

* **gen:** None-tolerant from_dict + list-iter response.json + live homelab transcript ([11d0e15](https://github.com/new-usemame/arr-stack-mcp/commit/11d0e15aeaf3fc03e2e9b781f3840ca2b42807ca))
* **gen:** patch response.text-&gt;response.json() across 179 endpoints + record MCP-client transcript ([c9efbe4](https://github.com/new-usemame/arr-stack-mcp/commit/c9efbe4bac0a32a591a2603051a24d515ac7c45e))

## 0.1.0 (2026-05-18)


### Features

* **d:** full v0.1.0 curated tool surface across all four services ([3305cca](https://github.com/new-usemame/arr-stack-mcp/commit/3305cca32e0b931fd84981ffdb31b04c661fdc10))
* documentation + CI + Dockerfile for v0.1.0 release ([96f4d55](https://github.com/new-usemame/arr-stack-mcp/commit/96f4d5579f8e393c15ef4a050d3d00032f522510))
* initial scaffolding through Phase C ([97890e8](https://github.com/new-usemame/arr-stack-mcp/commit/97890e83e0ddeaf47d91a1400b5d3f6e6e21855d))
* **radarr:** wire eight curated tools mirroring Sonarr's shape ([f3534e7](https://github.com/new-usemame/arr-stack-mcp/commit/f3534e7ca6ea62f735c932d85173fc7830141c83))
* **sonarr:** wire eight curated tools into the MCP server ([905b1c2](https://github.com/new-usemame/arr-stack-mcp/commit/905b1c29b00de3016593472c4c1bb12cf3199fec))


### Bug Fixes

* **ci:** teardown reclaims container-owned files before delete ([c0a941f](https://github.com/new-usemame/arr-stack-mcp/commit/c0a941f3da3aacd7ed96f2af77a3be116a9e417a))


### Documentation

* v0.1.0 release readiness hand-off note ([eb31d85](https://github.com/new-usemame/arr-stack-mcp/commit/eb31d85be1664ee1a53498af80c1c684e65d5e6e))

## [Unreleased]
