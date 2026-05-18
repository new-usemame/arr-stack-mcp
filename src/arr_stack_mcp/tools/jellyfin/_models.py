"""Pydantic input / output models for Jellyfin tools.

Item-grain APIs (``library_search``, ``recent_additions``) deliberately return
a compact view of ``BaseItemDto`` — the upstream model carries 80+ fields
that an LLM rarely needs.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class JellyfinItem(BaseModel):
    """Compact view of a Jellyfin library item."""

    id: str
    name: str
    type: str
    year: int | None = None
    overview: str | None = None
    runtime_minutes: int | None = None
    series_name: str | None = None
    season_number: int | None = None
    episode_number: int | None = None
    date_created: str | None = None
    user_play_count: int | None = None
    play_state: Literal["unplayed", "in-progress", "played"] | None = None


class SessionInfo(BaseModel):
    """One active Jellyfin session."""

    session_id: str
    user: str | None = None
    client: str | None = None
    device: str | None = None
    item_name: str | None = None
    item_type: str | None = None
    position_pct: float | None = None
    is_paused: bool | None = None
    last_activity: str | None = None


class SystemInfo(BaseModel):
    """Returned by ``jellyfin.system_info``."""

    version: str
    server_name: str | None = None
    operating_system: str | None = None
    id: str | None = None


# --- Input schemas ---


class LibrarySearchInput(BaseModel):
    """Search Jellyfin's library by name. Returns matching items across all media types."""

    query: str = Field(min_length=1)
    types: list[str] | None = Field(
        default=None,
        description=(
            "Restrict by Jellyfin BaseItemKind (Movie, Series, Episode, Audio, MusicAlbum, MusicArtist, BoxSet). Omit for all types."
        ),
    )
    limit: int = Field(default=20, ge=1, le=100)


class RecentAdditionsInput(BaseModel):
    """List recently-added items across the user's libraries."""

    limit: int = Field(default=20, ge=1, le=100)
    parent_id: str | None = Field(
        default=None,
        description="Restrict to a single library by its id. Omit for all libraries.",
    )


class ScanLibraryInput(BaseModel):
    """Trigger a full library scan."""

    library_id: str | None = Field(
        default=None,
        description="Specific library id to scan. Omit to refresh all libraries.",
    )


# --- Output envelopes ---


class SearchResult(BaseModel):
    ok: bool = True
    query: str
    count: int
    total: int
    truncated: bool = False
    items: list[JellyfinItem]


class RecentAdditionsResult(BaseModel):
    ok: bool = True
    count: int
    items: list[JellyfinItem]


class SessionsResult(BaseModel):
    ok: bool = True
    count: int
    sessions: list[SessionInfo]


class StatusResult(BaseModel):
    ok: bool = True
    service: str = "jellyfin"
    url: str
    info: SystemInfo


class ScanResult(BaseModel):
    ok: bool = True
    msg: str
    library_id: str | None = None
