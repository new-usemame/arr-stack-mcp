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
        description=(
            "One-line description of what went wrong, in the user's words. "
            "Will be the issue title. Keep under ~80 chars."
        ),
    )
    detail: str | None = Field(
        default=None,
        description=(
            "Optional longer explanation, error excerpt, or repro steps. "
            "Will be embedded in the issue body."
        ),
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
