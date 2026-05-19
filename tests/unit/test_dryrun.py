"""Dry-run seam: Policy ring buffer + `dryrun_short_circuit` helper.

Validates the architectural decision in notes/DESIGN-v0.2.md §1.2 — dry-run
lives at the curated-tool boundary, not at the httpx transport. Each WRITE
tool calls `dryrun_short_circuit` AFTER read-side prep and BEFORE the
mutating upstream call; the helper records the intended payload and returns
a synthetic envelope, short-circuiting the mutation.
"""

from __future__ import annotations

from pydantic import BaseModel

from arr_stack_mcp.policy import DRYRUN_LOG_CAPACITY, Policy, PolicyConfig
from arr_stack_mcp.tools.common import dryrun_short_circuit


def _policy(*, dry_run: bool) -> Policy:
    cfg = PolicyConfig(dry_run=dry_run)
    return Policy.from_config(cfg, read_only=False, disable_destructive=False, dry_run=dry_run)


class _FakeEnvelope(BaseModel):
    ok: bool = True
    msg: str


# ---------- Policy.record_dryrun / dryrun_log ----------


def test_record_dryrun_appends() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("sonarr.series_add", {"tvdb_id": 42})
    log = p.dryrun_log()
    assert len(log) == 1
    assert log[0]["tool_name"] == "sonarr.series_add"
    assert log[0]["payload"] == {"tvdb_id": 42}
    assert isinstance(log[0]["recorded_at"], float)


def test_dryrun_log_returns_newest_last() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("first", {})
    p.record_dryrun("second", {})
    p.record_dryrun("third", {})
    assert [e["tool_name"] for e in p.dryrun_log()] == ["first", "second", "third"]


def test_dryrun_log_limit_trims_to_most_recent() -> None:
    p = _policy(dry_run=True)
    for i in range(5):
        p.record_dryrun(f"tool{i}", {})
    assert [e["tool_name"] for e in p.dryrun_log(limit=2)] == ["tool3", "tool4"]


def test_dryrun_log_limit_zero_or_negative_returns_all() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("a", {})
    p.record_dryrun("b", {})
    assert len(p.dryrun_log(limit=0)) == 2
    assert len(p.dryrun_log(limit=-1)) == 2


def test_dryrun_log_caps_at_ring_buffer_capacity() -> None:
    p = _policy(dry_run=True)
    for i in range(DRYRUN_LOG_CAPACITY + 50):
        p.record_dryrun(f"tool{i}", {})
    log = p.dryrun_log()
    assert len(log) == DRYRUN_LOG_CAPACITY
    # Newest preserved; oldest dropped.
    assert log[-1]["tool_name"] == f"tool{DRYRUN_LOG_CAPACITY + 49}"
    assert log[0]["tool_name"] == f"tool{50}"


def test_clear_dryrun_log_empties_buffer() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("x", {})
    p.clear_dryrun_log()
    assert p.dryrun_log() == []


# ---------- Policy.from_config(dry_run=...) ----------


def test_from_config_propagates_dry_run_from_arg() -> None:
    cfg = PolicyConfig(dry_run=False)
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False, dry_run=True)
    assert p.dry_run is True


def test_from_config_propagates_dry_run_from_config() -> None:
    cfg = PolicyConfig(dry_run=True)
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False, dry_run=False)
    assert p.dry_run is True


def test_from_config_defaults_dry_run_off() -> None:
    cfg = PolicyConfig()
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    assert p.dry_run is False


# ---------- dryrun_short_circuit helper ----------


def test_short_circuit_returns_none_when_dry_run_off() -> None:
    p = _policy(dry_run=False)
    envelope = _FakeEnvelope(msg="would have added")
    result = dryrun_short_circuit(p, "sonarr.series_add", {"tvdb_id": 1}, envelope)
    assert result is None
    # No recording when dry-run is off.
    assert p.dryrun_log() == []


def test_short_circuit_returns_envelope_when_dry_run_on() -> None:
    p = _policy(dry_run=True)
    envelope = _FakeEnvelope(msg="DRY-RUN: would add")
    result = dryrun_short_circuit(p, "sonarr.series_add", {"tvdb_id": 42}, envelope)
    assert result is envelope
    # Payload landed in the ring buffer.
    log = p.dryrun_log()
    assert len(log) == 1
    assert log[0]["tool_name"] == "sonarr.series_add"
    assert log[0]["payload"] == {"tvdb_id": 42}


def test_short_circuit_preserves_envelope_type() -> None:
    """The helper must return the exact envelope it was given, not a copy."""
    p = _policy(dry_run=True)
    envelope = _FakeEnvelope(msg="x")
    result = dryrun_short_circuit(p, "tool.x", {}, envelope)
    assert result is envelope
    assert isinstance(result, _FakeEnvelope)


def test_short_circuit_records_each_call_separately() -> None:
    p = _policy(dry_run=True)
    for i in range(3):
        env = _FakeEnvelope(msg=f"call {i}")
        out = dryrun_short_circuit(p, f"tool.{i}", {"i": i}, env)
        assert out is env
    log = p.dryrun_log()
    assert [e["tool_name"] for e in log] == ["tool.0", "tool.1", "tool.2"]
    assert [e["payload"]["i"] for e in log] == [0, 1, 2]
