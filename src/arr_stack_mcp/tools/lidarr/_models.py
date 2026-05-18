"""Pydantic input / output models for Lidarr tools.

Lidarr is the music sibling of Sonarr/Radarr — entity grain is artist + album.
Identifiers come from MusicBrainz (``mbid``); Lidarr also keeps an internal
``lidarr_id``.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class ArtistSummary(BaseModel):
    """Compact artist view."""

    lidarr_id: int = Field(description="Internal Lidarr ID.")
    foreign_artist_id: str | None = Field(default=None, description="MusicBrainz id (mbid); stable across Lidarr instances.")
    name: str
    overview: str | None = None
    status: str | None = Field(default=None, description="continuing, ended, etc.")
    monitored: bool = True
    album_count: int | None = None
    track_count: int | None = None
    track_file_count: int | None = None
    size_on_disk: int | None = None
    path: str | None = None


class AlbumSummary(BaseModel):
    """One album under an artist."""

    lidarr_id: int
    foreign_album_id: str | None = Field(default=None, description="MusicBrainz release-group id.")
    title: str
    artist_name: str | None = None
    release_date: str | None = None
    album_type: str | None = None
    monitored: bool = True
    has_file: bool = False
    track_count: int | None = None
    track_file_count: int | None = None


class QueueItem(BaseModel):
    queue_id: int
    artist_id: int | None = None
    album_id: int | None = None
    title: str
    status: str
    progress_pct: float
    size: int
    size_left: int
    estimated_completion: str | None = None
    download_client: str | None = None
    protocol: str | None = None


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


class ArtistSearchInput(BaseModel):
    """Search the Lidarr library (already-added artists)."""

    query: str = Field(min_length=1)
    limit: int = Field(default=10, ge=1, le=50)


class ArtistLookupInput(BaseModel):
    """Search MusicBrainz through Lidarr for an artist to add."""

    query: str = Field(min_length=1)
    limit: int = Field(default=5, ge=1, le=20)


class ArtistAlbumsInput(BaseModel):
    """List all albums under one Lidarr artist."""

    lidarr_id: int = Field(description="Internal Lidarr artist id from a prior search.")
    monitored_only: bool = False


class ArtistAddInput(BaseModel):
    foreign_artist_id: str = Field(description="MusicBrainz id (mbid) from ``lidarr.artist_lookup``.")
    quality_profile_id: int | None = None
    metadata_profile_id: int | None = None
    root_folder_path: str | None = None
    monitor: Literal["all", "future", "missing", "existing", "first", "latest", "none"] = "all"
    search_for_missing_albums: bool = True


class ArtistDeleteInput(BaseModel):
    lidarr_id: int
    delete_files: bool = False
    add_import_list_exclusion: bool = False
    confirm_token: str | None = None


class QueueInput(BaseModel):
    limit: int = Field(default=20, ge=1, le=100)


# --- Output envelopes ---


class SearchResult(BaseModel):
    ok: bool = True
    query: str
    count: int
    total: int
    truncated: bool = False
    items: list[ArtistSummary]


class LookupResult(BaseModel):
    ok: bool = True
    query: str
    candidates: list[ArtistSummary]


class AlbumsResult(BaseModel):
    ok: bool = True
    artist_lidarr_id: int
    count: int
    items: list[AlbumSummary]


class AddResult(BaseModel):
    ok: bool = True
    lidarr_id: int
    foreign_artist_id: str | None
    name: str
    already_added: bool
    msg: str


class DeletePlan(BaseModel):
    ok: bool = True
    needs_confirm: bool = True
    confirm_token: str
    summary: str
    target: ArtistSummary
    expires_in_seconds: int


class DeleteResult(BaseModel):
    ok: bool = True
    deleted_lidarr_id: int
    name: str
    files_deleted: bool
    msg: str


class QueueResult(BaseModel):
    ok: bool = True
    count: int
    total: int
    items: list[QueueItem]


class StatusResult(BaseModel):
    ok: bool = True
    service: str = "lidarr"
    url: str
    status: SystemStatus
