"""Pydantic input / output models for the `stack.*` cross-service toolset.

These tools aggregate or surface state that spans services rather than
belonging to any one of them. They're always registered (not gated on a
single service's config). See notes/DESIGN-v0.2.md §2.2.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

# ---------- stack.dryrun_log ----------


class DryRunLogInput(BaseModel):
    """Read the in-memory ring buffer of recorded would-have-fired mutations.

    Each entry has the tool name, the wall-clock timestamp the call was
    recorded at, and a dict-shaped representation of the payload the
    upstream client would have sent. Cap at 200 entries (per-process).
    """

    limit: int = Field(
        default=50,
        ge=1,
        le=200,
        description="Maximum number of entries to return (newest-last). Defaults to 50.",
    )


class DryRunEntry(BaseModel):
    """One recorded dry-run mutation."""

    tool_name: str
    recorded_at: float = Field(description="Wall-clock unix epoch seconds.")
    payload: dict[str, object] | None = None


class DryRunLogResult(BaseModel):
    ok: bool = True
    count: int
    entries: list[DryRunEntry]


# ---------- stack.report_issue ----------


class ReportIssueInput(BaseModel):
    """Compose a pre-filled GitHub issue URL the user can post upstream.

    The MCP server does NOT auto-submit; it returns a URL with a templated
    title and body that the consumer surfaces. The user reviews and submits
    manually.
    """

    summary: str = Field(
        min_length=1,
        description=("One-line description of what went wrong, in the user's words. Will be the issue title. Keep under ~80 chars."),
    )
    detail: str | None = Field(
        default=None,
        description=("Optional longer explanation, error excerpt, or repro steps. Will be embedded in the issue body."),
    )
    include_dryrun_log: bool = Field(
        default=False,
        description="Embed the last 20 dry-run-log entries into the issue body. Useful for plan-and-record bug reports.",
    )


class ReportIssueResult(BaseModel):
    ok: bool = True
    url: str = Field(description="Click-to-create issue URL with title + body pre-filled.")
    repo: str = Field(description="The GitHub repo target (e.g. new-usemame/arr-stack-mcp).")


# ---------- stack.health ----------


class StackHealthInput(BaseModel):
    """No-arg health snapshot across every enabled service."""


class StackHealthService(BaseModel):
    """One service's reachability snapshot."""

    name: str
    enabled: bool
    reachable: bool
    version: str | None = None
    error: str | None = None


class StackHealthResult(BaseModel):
    ok: bool = True
    overall_ok: bool = Field(description="True when every enabled service is reachable AND reported a version.")
    services: list[StackHealthService]


# ---------- stack.find_anywhere ----------


class FindAnywhereInput(BaseModel):
    """Search a free-text query across every enabled arr / Jellyfin library in parallel.

    Use when the user's intent spans services ("where is X?"). For
    service-specific searches, call `*.search` on that service directly.
    """

    query: str = Field(min_length=1, description="Free-text search term.")
    limit_per_service: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum results returned per service. Total result count is at most 4x this (one per arr + Jellyfin).",
    )


class StackFoundItem(BaseModel):
    """One result from a cross-service `find_anywhere` aggregation.

    Carries the source service plus a small set of stable identifiers and
    the title/year/type so the LLM can route a follow-up call to the right
    per-service tool with the right id.
    """

    source: str = Field(description="Which service this row came from: sonarr / radarr / lidarr / jellyfin.")
    id: str | int = Field(description="Stable id within the source (sonarr_id / radarr_id / lidarr_id / Jellyfin item UUID).")
    title: str
    year: int | None = None
    type: str | None = Field(default=None, description="Item kind (series / movie / artist / Movie / Series / Episode etc).")
    external_id: str | None = Field(default=None, description="TVDB / TMDB / MusicBrainz id when known.")


class FindAnywhereSourceResult(BaseModel):
    """Per-source slice of the cross-service find result."""

    source: str
    count: int
    items: list[StackFoundItem]
    error: str | None = None


class FindAnywhereResult(BaseModel):
    ok: bool = True
    query: str
    total_count: int
    sources: list[FindAnywhereSourceResult]


# ---------- stack.queue_status_all ----------


class QueueStatusAllInput(BaseModel):
    """Aggregate the download / grab queue across Sonarr, Radarr, Lidarr."""

    limit_per_service: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Maximum queue rows per service.",
    )


class StackQueueItem(BaseModel):
    """One queue row, normalized across services.

    Each row carries the source service, the upstream queue-row id, a
    human-readable title, and progress / size info. Service-specific
    fields (sonarr's `series_id`, radarr's `movie_id`, lidarr's
    `artist_id`) are surfaced as `entity_id` for the LLM to route a
    follow-up call against the right service.
    """

    source: str
    queue_id: int
    entity_id: int | None = Field(default=None, description="Series / movie / artist id within the source.")
    title: str
    status: str
    progress_pct: float
    size: int = Field(description="Total bytes.")
    size_left: int = Field(description="Remaining bytes.")
    estimated_completion: str | None = None
    download_client: str | None = None
    protocol: str | None = None


class QueueStatusAllSource(BaseModel):
    """Per-source slice of the queue aggregation."""

    source: str
    count: int
    total: int
    items: list[StackQueueItem]
    error: str | None = None


class QueueStatusAllResult(BaseModel):
    ok: bool = True
    total_count: int
    sources: list[QueueStatusAllSource]
