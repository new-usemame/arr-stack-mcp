"""Pydantic input / output models for Sonarr tools.

Input models pin every tool's argument schema. Output models pin the LLM-facing
response shape — compact by default, with a ``response_format="detailed"``
switch to surface full upstream payloads when the agent needs them.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class SeriesSummary(BaseModel):
    """Compact series view. Returned by ``sonarr.series_search`` and ``sonarr.calendar``."""

    sonarr_id: int = Field(description="Internal Sonarr ID. Use to identify in subsequent calls.")
    tvdb_id: int | None = Field(default=None, description="TVDB id; stable across Sonarr instances.")
    imdb_id: str | None = None
    title: str
    year: int | None = None
    status: str | None = Field(default=None, description="continuing, ended, upcoming, deleted")
    monitored: bool = True
    episode_count: int | None = None
    episode_file_count: int | None = None
    size_on_disk: int | None = Field(default=None, description="Bytes")
    path: str | None = None


class SeasonSummary(BaseModel):
    """One season inside a series_status response."""

    season_number: int
    monitored: bool
    episode_count: int
    episode_file_count: int
    total_episode_count: int
    size_on_disk: int = 0


class SystemStatus(BaseModel):
    """Returned by ``sonarr.system_status``. The single most-useful diagnostic for an agent."""

    version: str
    branch: str | None = None
    runtime_version: str | None = None
    is_production: bool | None = None
    is_admin: bool | None = None
    is_docker: bool | None = None
    start_time: str | None = None
    instance_name: str | None = None


class QueueItem(BaseModel):
    """One download in the active Sonarr queue."""

    queue_id: int
    series_id: int | None = None
    episode_id: int | None = None
    title: str
    status: str
    tracked_status: str | None = None
    progress_pct: float
    size: int
    size_left: int
    estimated_completion: str | None = None
    download_client: str | None = None
    protocol: str | None = None


class CalendarItem(BaseModel):
    """One upcoming or recently-aired episode."""

    series_id: int
    series_title: str
    season_number: int
    episode_number: int
    title: str
    air_date_utc: str | None = None
    has_file: bool
    monitored: bool


class MissingEpisode(BaseModel):
    """One missing-from-disk episode the user might want."""

    series_id: int
    series_title: str
    season_number: int
    episode_number: int
    title: str
    air_date_utc: str | None = None


# --- Input schemas ---


class SeriesSearchInput(BaseModel):
    """Search the Sonarr library (already-added series).

    Use this when the user asks 'what shows do I have?' or 'is X in my library?'.
    For discovering shows that aren't already added, use ``sonarr.series_lookup``.
    """

    query: str = Field(
        description="Free-text search against series titles in the existing Sonarr library.",
        min_length=1,
    )
    year: int | None = Field(
        default=None,
        description="Optional year filter — disambiguates reboots like Battlestar Galactica (1978) vs (2004).",
    )
    limit: int = Field(default=10, ge=1, le=50)


class SeriesLookupInput(BaseModel):
    """Search TVDB for a series to add to Sonarr.

    Use this *before* ``sonarr.series_add`` — the TVDB id this returns is what
    ``series_add`` needs. Note: this returns external-catalog candidates, not the
    current library; for that use ``sonarr.series_search``.
    """

    query: str = Field(min_length=1)
    limit: int = Field(default=5, ge=1, le=20)


class SeriesAddInput(BaseModel):
    """Add a new series to Sonarr's library and trigger an initial search."""

    tvdb_id: int = Field(description="TVDB id; obtain from ``sonarr.series_lookup``.")
    quality_profile_id: int | None = Field(
        default=None,
        description="Defaults to the first quality profile if omitted. Use ``sonarr.quality_profiles`` to list.",
    )
    root_folder_path: str | None = Field(
        default=None,
        description="Defaults to the first configured root folder if omitted.",
    )
    monitor: Literal["all", "future", "missing", "existing", "pilot", "firstSeason", "lastSeason", "none"] = "all"
    search_for_missing_episodes: bool = True


class SeriesDeleteInput(BaseModel):
    """Remove a series from Sonarr.

    Destructive — the first call returns a plan + confirm_token; call again with
    ``confirm_token`` set to actually delete.
    """

    sonarr_id: int = Field(description="Internal Sonarr id from a prior search.")
    delete_files: bool = Field(
        default=False,
        description="When true, also removes files on disk. False keeps the files but unmanages the series.",
    )
    add_import_list_exclusion: bool = Field(
        default=False,
        description="When true, prevents this series from being re-added by an import list.",
    )
    confirm_token: str | None = Field(
        default=None,
        description=(
            "Confirm token from the previous unconfirmed call. Omit on the first call "
            "to receive a plan + token; include on the second call to execute."
        ),
    )


class QueueInput(BaseModel):
    """List active downloads in the Sonarr queue."""

    limit: int = Field(default=20, ge=1, le=100)
    include_unknown_series: bool = False


class CalendarInput(BaseModel):
    """List upcoming or recently-aired episodes."""

    days_back: int = Field(default=2, ge=0, le=60)
    days_forward: int = Field(default=14, ge=0, le=365)
    unmonitored: bool = Field(
        default=False,
        description="Include unmonitored episodes. Default false matches the typical 'what's airing for me' question.",
    )


class SeriesStatusInput(BaseModel):
    """Per-season breakdown for one series. Either id may be supplied.

    Use this when the user asks 'what seasons does X have?' / 'is X complete?'
    / 'how many episodes of X do we have?' / 'what's missing from X?'.
    The result names each season's monitor state, episode count, and
    on-disk count so the LLM can answer per-season questions accurately.
    """

    sonarr_id: int | None = Field(
        default=None,
        description="Internal Sonarr id from a prior `*.search` / `*.lookup` call. Either this or `tvdb_id` must be supplied.",
    )
    tvdb_id: int | None = Field(
        default=None,
        description="TVDB id; resolved to a `sonarr_id` internally. Useful when the agent only has the external id.",
    )


class MissingInput(BaseModel):
    """List monitored episodes that have aired but aren't on disk."""

    limit: int = Field(default=50, ge=1, le=200)
    monitored_only: bool = True


# --- Output envelopes ---


class SearchResult(BaseModel):
    ok: bool = True
    query: str
    count: int
    total: int
    truncated: bool = False
    items: list[SeriesSummary]


class LookupResult(BaseModel):
    ok: bool = True
    query: str
    candidates: list[SeriesSummary]


class AddResult(BaseModel):
    ok: bool = True
    sonarr_id: int
    tvdb_id: int | None
    title: str
    already_added: bool
    msg: str


class DeletePlan(BaseModel):
    """First-call response from ``sonarr.series_delete``."""

    ok: bool = True
    needs_confirm: bool = True
    confirm_token: str
    summary: str
    target: SeriesSummary
    expires_in_seconds: int


class DeleteResult(BaseModel):
    """Second-call (executed) response from ``sonarr.series_delete``."""

    ok: bool = True
    deleted_sonarr_id: int
    title: str
    files_deleted: bool
    msg: str


class QueueResult(BaseModel):
    ok: bool = True
    count: int
    total: int
    items: list[QueueItem]


class CalendarResult(BaseModel):
    ok: bool = True
    count: int
    items: list[CalendarItem]


class MissingResult(BaseModel):
    ok: bool = True
    count: int
    total: int
    items: list[MissingEpisode]


class StatusResult(BaseModel):
    ok: bool = True
    service: str = "sonarr"
    url: str
    status: SystemStatus


class SeriesStatusResult(BaseModel):
    """Returned by ``sonarr.series_status``. One series, expanded per-season."""

    ok: bool = True
    sonarr_id: int
    tvdb_id: int | None
    title: str
    year: int | None
    status: str | None = Field(default=None, description="continuing / ended / upcoming / deleted")
    monitored: bool
    seasons: list[SeasonSummary]
    total_episode_count: int = Field(description="Sum of episode_count across all seasons.")
    total_episode_file_count: int = Field(description="Sum of episode_file_count across all seasons (how many are on disk).")
    total_size_on_disk: int = Field(description="Bytes on disk across all seasons.")
