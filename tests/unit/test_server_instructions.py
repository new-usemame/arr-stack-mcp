"""Unit tests for the MCP server instructions string.

The instructions field is what the consuming LLM sees at session start. It
encodes output discipline, confirm-token UX, disambiguation rules, and tool-
selection nudges. These tests pin:

  - the discipline anchors are present (Result envelopes / Confirm tokens /
    Disambiguation / Tool selection / Heuristics / Errors), so a future edit
    can't silently strip a section
  - marketing intensifiers banned by the project's tone policy do not appear
  - the active services + risk-tolerance flags interpolate correctly
  - the total length stays within an LLM-first-turn-friendly budget

See notes/DESIGN-v0.2.md §1.1.
"""

from __future__ import annotations

import pytest
from pydantic import HttpUrl

from arr_stack_mcp.config import Config, ServiceConfig
from arr_stack_mcp.policy import PolicyConfig
from arr_stack_mcp.server import _server_instructions

# Project tone policy hot-list (CLAUDE.md). Substring match, case-insensitive.
_BANNED_INTENSIFIERS = (
    "robust",
    "powerful",
    "seamless",
    "delightful",
    "comprehensive",
    "elegant",
    "blazing",
    "world-class",
    "best-in-class",
    "cutting-edge",
)

_BANNED_WRAPPERS = ("TL;DR", "In summary", "In conclusion")


def _config(*, services: dict[str, ServiceConfig] | None = None, policy: PolicyConfig | None = None) -> Config:
    return Config(
        services=services or {},
        policy=policy or PolicyConfig(),
    )


def _svc(name: str, *, enabled: bool = True) -> ServiceConfig:
    return ServiceConfig(name=name, enabled=enabled, url=HttpUrl(f"http://localhost:8989/{name}"))


def test_contains_all_discipline_section_anchors() -> None:
    text = _server_instructions(_config())
    for section in ("Result envelopes", "Confirm tokens", "Disambiguation", "Tool selection", "Heuristics", "Errors"):
        assert section in text, f"missing section anchor: {section!r}"


def test_contains_lift_from_ibis_bot_system_prompt() -> None:
    """Specific guidance lifted from ibis-bot's SYSTEM_PROMPT (Matrix bits stripped).

    See notes/RESEARCH-ibis-bot-patterns.md + notes/DESIGN-v0.2.md §1.1 for the
    porting rationale. Each substring below is a non-obvious rule the LLM needs
    that we deliberately ported.
    """
    text = _server_instructions(_config())
    # Output discipline — don't re-render the envelope back to the user.
    assert "re-render JSON" in text
    # Confirm-token UX — the plan is in the first envelope; second call passes the token.
    assert "needs_confirm" in text
    assert "confirm_token" in text
    # Disambiguation — retry with the id, do not append fields.
    assert "Ambiguous" in text
    assert "candidates" in text
    # Tool-selection — *.search vs *.lookup.
    assert "*.search" in text
    assert "*.lookup" in text
    assert "already_added" in text
    # Heuristics — year tags + acronyms.
    assert "year" in text.lower()
    assert "Acronym" in text or "acronym" in text.lower()
    # Error vocabulary mapped to actionable hints.
    assert "policy_denied" in text
    assert "upstream_unavailable" in text
    assert "upstream_auth_failed" in text
    assert "confirm_required" in text


@pytest.mark.parametrize("banned", _BANNED_INTENSIFIERS)
def test_tone_policy_no_marketing_intensifiers(banned: str) -> None:
    text = _server_instructions(_config()).lower()
    assert banned.lower() not in text, f"tone policy violation: {banned!r}"


@pytest.mark.parametrize("banned", _BANNED_WRAPPERS)
def test_tone_policy_no_summary_wrappers(banned: str) -> None:
    text = _server_instructions(_config())
    assert banned not in text, f"tone policy violation: {banned!r} wrapper"


def test_em_dash_budget_one_per_paragraph_average() -> None:
    """The CLAUDE.md em-dash budget is ~one per paragraph. Audit the actual count.

    Not a hard ceiling — em-dashes do real work in prose — but a regression test
    against a future edit that loses the budget entirely.
    """
    text = _server_instructions(_config())
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    em_dashes = text.count("—")
    # Allow up to one per paragraph on average.
    assert em_dashes <= len(paragraphs), f"em-dash budget exceeded: {em_dashes} dashes across {len(paragraphs)} paragraphs"


def test_length_within_first_turn_budget() -> None:
    """Cap the instructions at ~8KB so first-turn prompt-cache misses are tolerable.

    Set in DESIGN-v0.2.md §1.1. Above this, split into per-toolset descriptions.
    """
    text = _server_instructions(_config())
    assert len(text) <= 8000, f"instructions length {len(text)} exceeds 8KB cap"


def test_active_services_interpolated() -> None:
    cfg = _config(services={"sonarr": _svc("sonarr"), "radarr": _svc("radarr")})
    text = _server_instructions(cfg)
    assert "Active services: sonarr, radarr" in text


def test_active_services_none_when_all_disabled() -> None:
    cfg = _config(services={"sonarr": _svc("sonarr", enabled=False)})
    text = _server_instructions(cfg)
    assert "Active services: none" in text


def test_flags_interpolated_read_only() -> None:
    cfg = _config(policy=PolicyConfig(read_only=True))
    text = _server_instructions(cfg)
    assert "read-only mode" in text


def test_flags_interpolated_disable_destructive() -> None:
    cfg = _config(policy=PolicyConfig(disable_destructive=True))
    text = _server_instructions(cfg)
    assert "destructive tools disabled" in text


def test_flags_both_set_combined() -> None:
    cfg = _config(policy=PolicyConfig(read_only=True, disable_destructive=True))
    text = _server_instructions(cfg)
    assert "read-only mode; destructive tools disabled" in text


def test_no_emoji_in_body() -> None:
    """CLAUDE.md tone policy: no emoji in body copy. Section icons OK; inline emoji are not.

    No section icons today, so the rule degenerates to 'no emoji anywhere'.
    """
    text = _server_instructions(_config())
    # Common inline emoji that have slipped into prior drafts.
    for emoji in ("✅", "❌", "⚠", "☕", "🙊", "🔟"):
        assert emoji not in text, f"emoji {emoji!r} in instructions"
