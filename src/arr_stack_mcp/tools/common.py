"""Helpers shared across every per-service tool module.

Defines the ``ToolEnvelope`` shape every tool returns, the destructive-tool
confirm-token plumbing, and a decorator that wires every registered MCP tool
through policy gating + error serialization.

The pattern: per-service modules build a curated tool function (taking pydantic
input, returning a typed result), call ``register_tool`` on the FastMCP
instance, and rely on this module to consistently translate ToolError into the
MCP error envelope.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from arr_stack_mcp.errors import ToolError
from arr_stack_mcp.policy import Policy, Tag

if TYPE_CHECKING:
    from arr_stack_mcp._mcp import FastMCP
    from arr_stack_mcp.config import ServiceConfig


class ToolEnvelope[T](BaseModel):
    """Self-describing wire shape every tool's success path returns.

    ``query`` repeats the caller's input so dedupe-by-string in chat clients
    keeps two different invocations distinct. ``count`` and ``total`` are
    used by list tools to surface pagination. ``items`` carries the typed
    payload.
    """

    query: str | None = None
    count: int | None = None
    total: int | None = None
    items: T


class ConfirmPlan(BaseModel):
    """First-call return shape for destructive tools.

    Carries the confirm token + a human-readable preview the agent must echo
    to the user before invoking the tool a second time with ``confirm_token``.
    """

    needs_confirm: bool = True
    confirm_token: str
    summary: str
    affected_count: int = Field(default=1, ge=0)
    expires_in_seconds: int


def make_descriptor(
    *,
    tool_name: str,
    tag: Tag,
    summary: str,
) -> ToolDescriptor:
    """Convenience constructor that pins the tool's identity + risk tag.

    The descriptor is later registered with the MCP server alongside the
    handler. Keeping these decoupled makes the tool's policy gating testable
    without touching the FastMCP runtime.
    """
    return ToolDescriptor(tool_name=tool_name, tag=tag, summary=summary)


class ToolDescriptor(BaseModel):
    """Metadata for a single MCP tool. Stored alongside its handler in the registry."""

    tool_name: str
    tag: Tag
    summary: str


def dryrun_short_circuit[T](
    policy: Policy,
    tool_name: str,
    intended_payload: dict[str, object],
    envelope_on_dryrun: T,
) -> T | None:
    """Short-circuit the mutating call when dry-run is active.

    Each WRITE / DESTRUCTIVE tool calls this AFTER read-side prep + confirm-
    token validation, and BEFORE the upstream mutating call. If
    ``policy.dry_run`` is set, the intended payload is recorded into the ring
    buffer (surfaced by ``stack.dryrun_log``) and ``envelope_on_dryrun`` is
    returned to the caller. Otherwise returns ``None`` and the caller
    proceeds with the real upstream call.

    See notes/DESIGN-v0.2.md §1.2 for the seam choice rationale: dry-run
    lives at the curated-tool boundary, not at the httpx transport, because
    the openapi-python-client thin clients raise on missing required fields
    and per-endpoint synthetic responses are structurally fragile.

    Usage::

        short = dryrun_short_circuit(
            policy,
            "sonarr.series_add",
            body.to_dict() if hasattr(body, "to_dict") else {},
            AddResult(
                sonarr_id=0,
                tvdb_id=args.tvdb_id,
                title="DRYRUN",
                already_added=False,
                msg="DRY-RUN: would add",
            ),
        )
        if short is not None:
            return short
        added = await post_api_v3_series.asyncio(client=client, body=body)
    """
    if not policy.dry_run:
        return None
    policy.record_dryrun(tool_name, intended_payload)
    return envelope_on_dryrun


__all__ = [
    "ConfirmPlan",
    "FastMCP",
    "Policy",
    "ServiceConfig",
    "Tag",
    "ToolDescriptor",
    "ToolEnvelope",
    "ToolError",
    "dryrun_short_circuit",
    "make_descriptor",
]
