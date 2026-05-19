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


class JellyfinUser(BaseModel):
    """Compact view of a Jellyfin user account. Returned by ``jellyfin.users_list``.

    Designed so a consumer (e.g. ibis-bot) can map an external identity to a
    Jellyfin user id at session start: take ``name`` (or a friendly mapping
    of it) to resolve a sender; carry ``user_id`` through subsequent calls
    that accept ``user_id=``. ``is_administrator`` lets the consumer gate
    admin-only operations before the MCP call.
    """

    user_id: str = Field(description="Jellyfin user UUID. Pass as `user_id=` to per-user tools.")
    name: str
    is_administrator: bool = False
    has_password: bool | None = None
    last_login_date: str | None = None


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
    user_id: str | None = Field(
        default=None,
        description=(
            "Jellyfin user UUID. When set, scopes the search to that user's accessible libraries. "
            "When omitted, falls back to `services.jellyfin.default_user_id` from config. "
            "Obtain via `jellyfin.users_list`. Consumers (e.g. ibis-bot) use this to honor per-user "
            "library scoping."
        ),
    )


class RecentAdditionsInput(BaseModel):
    """List recently-added items across the user's libraries."""

    limit: int = Field(default=20, ge=1, le=100)
    parent_id: str | None = Field(
        default=None,
        description="Restrict to a single library by its id. Omit for all libraries.",
    )
    user_id: str | None = Field(
        default=None,
        description=(
            "Jellyfin user UUID. When set, scopes the recent-additions list to that user's accessible "
            "libraries (Jellyfin filters via `EnabledFolders` / `EnableAllFolders` in the user's policy). "
            "When omitted, falls back to `services.jellyfin.default_user_id` from config."
        ),
    )


class ScanLibraryInput(BaseModel):
    """Trigger a full library scan."""

    library_id: str | None = Field(
        default=None,
        description="Specific library id to scan. Omit to refresh all libraries.",
    )


class UsersListInput(BaseModel):
    """List Jellyfin user accounts.

    The MCP server uses one admin API key for all calls; per-user scoping
    happens via the `user_id` argument on each per-user tool. This tool
    returns the catalog of users so consumers can build their own
    sender-to-Jellyfin-user mapping.
    """

    include_disabled: bool = Field(
        default=False,
        description="Include accounts the admin has marked disabled. Default false (matches the typical 'who are my users?' question).",
    )
    include_hidden: bool = Field(
        default=False,
        description="Include accounts the admin has marked hidden from public login screens. Default false.",
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


class UsersListResult(BaseModel):
    ok: bool = True
    count: int
    users: list[JellyfinUser]
