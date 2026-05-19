"""Pydantic input / output models for Prowlarr tools.

Prowlarr's role in the stack is indexer management — it brokers between the
*arr services and the underlying tracker / newznab endpoints. The curated
tool surface here focuses on the workflow-relevant subset: system status,
health alerts, indexer enumeration / stats / status, the test-all probe,
and unified search across configured indexers. See notes/DESIGN-v0.2.md §2.1.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

# ---------- system / health ----------


class SystemStatus(BaseModel):
    """Returned by ``prowlarr.system_status``. Single most-useful diagnostic for an agent."""

    version: str
    branch: str | None = None
    runtime_version: str | None = None
    is_production: bool | None = None
    is_admin: bool | None = None
    is_docker: bool | None = None
    start_time: str | None = None
    instance_name: str | None = None


class StatusResult(BaseModel):
    ok: bool = True
    service: str = "prowlarr"
    url: str
    status: SystemStatus


class HealthIssue(BaseModel):
    """One Prowlarr health check entry. Mirrors HealthResource."""

    source: str | None = None
    type: str | None = Field(default=None, description="ok / notice / warning / error")
    message: str
    wiki_url: str | None = None


class HealthResult(BaseModel):
    ok: bool = True
    count: int
    issues: list[HealthIssue]


# ---------- indexers ----------


class IndexerInput(BaseModel):
    """List the configured indexers. By default returns every entry."""

    enabled_only: bool = Field(
        default=False,
        description="When true, omit indexers with `enable: false` from the result.",
    )


class IndexerSummary(BaseModel):
    """Compact view of an IndexerResource."""

    id: int
    name: str
    implementation: str | None = None
    protocol: str | None = Field(default=None, description="usenet / torrent")
    priority: int | None = None
    enable: bool = True
    tags: list[int] = Field(default_factory=list)


class IndexerListResult(BaseModel):
    ok: bool = True
    count: int
    items: list[IndexerSummary]


class IndexerStatsRow(BaseModel):
    """One indexer's recent stats."""

    indexer_id: int
    indexer_name: str
    num_queries: int = 0
    num_grabs: int = 0
    num_rss_queries: int = 0
    num_auth_queries: int = 0
    num_failed_queries: int = 0
    num_failed_grabs: int = 0
    num_failed_rss_queries: int = 0
    num_failed_auth_queries: int = 0
    average_response_time: int = 0


class IndexerStatsResult(BaseModel):
    ok: bool = True
    count: int
    items: list[IndexerStatsRow]


class IndexerStatusRow(BaseModel):
    """One indexer's outage state."""

    indexer_id: int
    disabled_till: str | None = None
    most_recent_failure: str | None = None
    initial_failure: str | None = None


class IndexerStatusResult(BaseModel):
    ok: bool = True
    count: int
    items: list[IndexerStatusRow]


class TestAllInput(BaseModel):
    """No-arg trigger for the test-every-indexer probe.

    Tagged WRITE because it instructs Prowlarr to fire test queries against
    every configured indexer (rate-limited at the upstream side, but
    still a side effect). For testing a single indexer's config, the
    indexer must be created/updated first via the Prowlarr UI.
    """


class TestAllRow(BaseModel):
    indexer_id: int
    is_valid: bool
    validation_failures: list[str] = Field(default_factory=list)


class TestAllResult(BaseModel):
    ok: bool = True
    count: int
    pass_count: int
    fail_count: int
    items: list[TestAllRow]


# ---------- search ----------


class SearchInput(BaseModel):
    """Search across configured Prowlarr indexers.

    Returns release candidates (title, indexer, size, age, seeders, leechers,
    categories). DOES NOT download — the downstream act-on-result lives in
    Sonarr / Radarr / Lidarr's `*.add` flow. Use this when the user wants to
    SEE what's available before deciding to add.
    """

    query: str = Field(min_length=1)
    indexer_ids: list[int] | None = Field(
        default=None,
        description="Restrict to specific indexer ids (from `prowlarr.indexer_list`). Omit for all.",
    )
    categories: list[int] | None = Field(
        default=None,
        description="Newznab category ids (e.g. 2000 = movies, 5000 = tv). Omit for any category.",
    )
    limit: int = Field(default=25, ge=1, le=100)
    search_type: Literal["search", "tvsearch", "movie", "music", "book"] = Field(
        default="search",
        description="Search type. `search` is the broadest; the others narrow by content type.",
    )


class SearchRelease(BaseModel):
    """Compact view of a Prowlarr ReleaseResource.

    Deliberately omits the magnet URI / infohash — the agent should NOT act
    directly on release identifiers. Downstream `*.add` tools take the
    catalog id (TVDB / TMDB / MusicBrainz), not the release id.
    """

    title: str
    indexer: str | None = None
    indexer_id: int | None = None
    size: int | None = Field(default=None, description="Bytes")
    age_minutes: int | None = None
    seeders: int | None = None
    leechers: int | None = None
    categories: list[int] = Field(default_factory=list)
    protocol: str | None = None


class SearchResult(BaseModel):
    ok: bool = True
    query: str
    count: int
    items: list[SearchRelease]
