"""Pydantic input / output models for Radarr tools.

Radarr's API mirrors Sonarr's but at the movie grain. The shape choices here
intentionally parallel ``tools/sonarr/_models.py`` so the agent can pattern-match
between services.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class MovieSummary(BaseModel):
    """Compact movie view. Returned by ``radarr.movie_search`` and ``radarr.calendar``."""

    radarr_id: int = Field(description="Internal Radarr ID. Use to identify in subsequent calls.")
    tmdb_id: int | None = Field(default=None, description="TMDB id; stable across Radarr instances.")
    imdb_id: str | None = None
    title: str
    year: int | None = None
    status: str | None = Field(default=None, description="released, inCinemas, announced, deleted")
    monitored: bool = True
    has_file: bool = False
    size_on_disk: int | None = Field(default=None, description="Bytes")
    runtime_minutes: int | None = None
    certification: str | None = None
    path: str | None = None
    in_cinemas: str | None = None
    digital_release: str | None = None


class QueueItem(BaseModel):
    queue_id: int
    movie_id: int | None = None
    title: str
    status: str
    progress_pct: float
    size: int
    size_left: int
    estimated_completion: str | None = None
    download_client: str | None = None
    protocol: str | None = None


class CalendarItem(BaseModel):
    movie_id: int
    title: str
    year: int | None = None
    in_cinemas: str | None = None
    digital_release: str | None = None
    physical_release: str | None = None
    has_file: bool
    monitored: bool


class MissingMovie(BaseModel):
    movie_id: int
    title: str
    year: int | None = None
    in_cinemas: str | None = None
    digital_release: str | None = None


class SystemStatus(BaseModel):
    version: str
    branch: str | None = None
    runtime_version: str | None = None
    is_production: bool | None = None
    is_admin: bool | None = None
    is_docker: bool | None = None
    start_time: str | None = None
    instance_name: str | None = None


# --- Input schemas ---


class MovieSearchInput(BaseModel):
    """Search the Radarr library (already-added movies)."""

    query: str = Field(min_length=1)
    year: int | None = None
    limit: int = Field(default=10, ge=1, le=50)


class MovieLookupInput(BaseModel):
    """Search TMDB through Radarr for a movie to add."""

    query: str = Field(min_length=1)
    limit: int = Field(default=5, ge=1, le=20)


class MovieAddInput(BaseModel):
    tmdb_id: int = Field(description="TMDB id obtained from ``radarr.movie_lookup``.")
    quality_profile_id: int | None = None
    root_folder_path: str | None = None
    minimum_availability: Literal["announced", "inCinemas", "released", "tba"] = "released"
    monitored: bool = True
    search_for_movie: bool = True


class MovieDeleteInput(BaseModel):
    radarr_id: int
    delete_files: bool = False
    add_import_list_exclusion: bool = False
    confirm_token: str | None = None


class QueueInput(BaseModel):
    limit: int = Field(default=20, ge=1, le=100)


class CalendarInput(BaseModel):
    days_back: int = Field(default=2, ge=0, le=60)
    days_forward: int = Field(default=30, ge=0, le=365)
    unmonitored: bool = False


class MissingInput(BaseModel):
    limit: int = Field(default=50, ge=1, le=200)
    monitored_only: bool = True


# --- Output envelopes ---


class SearchResult(BaseModel):
    ok: bool = True
    query: str
    count: int
    total: int
    truncated: bool = False
    items: list[MovieSummary]


class LookupResult(BaseModel):
    ok: bool = True
    query: str
    candidates: list[MovieSummary]


class AddResult(BaseModel):
    ok: bool = True
    radarr_id: int
    tmdb_id: int | None
    title: str
    already_added: bool
    msg: str


class DeletePlan(BaseModel):
    ok: bool = True
    needs_confirm: bool = True
    confirm_token: str
    summary: str
    target: MovieSummary
    expires_in_seconds: int


class DeleteResult(BaseModel):
    ok: bool = True
    deleted_radarr_id: int
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
    items: list[MissingMovie]


class StatusResult(BaseModel):
    ok: bool = True
    service: str = "radarr"
    url: str
    status: SystemStatus
