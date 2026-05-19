"""Hourly per-tool rate limiter (runaway-agent protection).

See notes/DESIGN-v0.2.md §1.4. Caps are per-process, per-tool, per-hour. They
are config-driven and OFF by default; tools without an entry in
``policy.hourly_caps`` are uncapped. A capped tool's count increments on every
``policy.check()`` call that passes the flag gates, regardless of whether the
upstream call ultimately succeeded — failed calls count.

The bot-side per-user-per-day caps in ibis-bot are orthogonal and live at the
bot layer; this hourly cap is server-process-wide runaway-loop protection.
"""

from __future__ import annotations

import pytest

from arr_stack_mcp.errors import PolicyDenied
from arr_stack_mcp.policy import Policy, PolicyConfig, Tag


def _policy(*, hourly_caps: dict[str, int] | None = None) -> Policy:
    cfg = PolicyConfig(hourly_caps=hourly_caps or {})
    return Policy.from_config(cfg, read_only=False, disable_destructive=False)


def test_uncapped_tool_passes_through() -> None:
    p = _policy()  # no caps at all
    for _ in range(100):
        p.check("sonarr.series_search", Tag.READ)
    # No exception; no recorded counter for uncapped tools (zero in dict).
    assert p._hourly_counters == {}


def test_cap_blocks_after_n_calls() -> None:
    p = _policy(hourly_caps={"sonarr.series_add": 3})
    p.check("sonarr.series_add", Tag.WRITE)
    p.check("sonarr.series_add", Tag.WRITE)
    p.check("sonarr.series_add", Tag.WRITE)
    with pytest.raises(PolicyDenied) as exc:
        p.check("sonarr.series_add", Tag.WRITE)
    assert "hourly cap" in exc.value.message
    assert "sonarr.series_add" in exc.value.message
    assert "3" in exc.value.message
    assert exc.value.hint is not None


def test_cap_does_not_affect_other_tools() -> None:
    p = _policy(hourly_caps={"sonarr.series_add": 1})
    p.check("sonarr.series_add", Tag.WRITE)
    with pytest.raises(PolicyDenied):
        p.check("sonarr.series_add", Tag.WRITE)
    # Other tools still pass.
    for _ in range(10):
        p.check("radarr.movie_add", Tag.WRITE)


def test_cap_zero_or_negative_treated_as_uncapped() -> None:
    """A cap of 0 or below means 'no cap configured for this tool' (no-op entry)."""
    p = _policy(hourly_caps={"sonarr.series_add": 0, "radarr.movie_add": -5})
    for _ in range(50):
        p.check("sonarr.series_add", Tag.WRITE)
        p.check("radarr.movie_add", Tag.WRITE)


def test_cap_rolls_over_on_hour_boundary(monkeypatch: pytest.MonkeyPatch) -> None:
    """A new hour resets the counter — the previous hour's count does not carry over."""
    p = _policy(hourly_caps={"x.add": 2})

    # Pin time to hour H.
    base = 1_700_000_000  # arbitrary epoch
    monkeypatch.setattr("arr_stack_mcp.policy.time.time", lambda: float(base))
    p.check("x.add", Tag.WRITE)
    p.check("x.add", Tag.WRITE)
    with pytest.raises(PolicyDenied):
        p.check("x.add", Tag.WRITE)

    # Jump to H+1.
    monkeypatch.setattr("arr_stack_mcp.policy.time.time", lambda: float(base + 3600))
    p.check("x.add", Tag.WRITE)  # fresh bucket — succeeds
    p.check("x.add", Tag.WRITE)
    with pytest.raises(PolicyDenied):
        p.check("x.add", Tag.WRITE)


def test_sweep_drops_old_hour_buckets(monkeypatch: pytest.MonkeyPatch) -> None:
    """Counter dict stays bounded — buckets older than the previous hour are dropped."""
    p = _policy(hourly_caps={"x.add": 100})

    # Hour H — record one.
    base = 1_700_000_000
    monkeypatch.setattr("arr_stack_mcp.policy.time.time", lambda: float(base))
    p.check("x.add", Tag.WRITE)
    assert len(p._hourly_counters) == 1

    # Hour H+5 — earlier bucket should be swept on the next check.
    monkeypatch.setattr("arr_stack_mcp.policy.time.time", lambda: float(base + 5 * 3600))
    p.check("x.add", Tag.WRITE)
    # Only the current hour remains (previous-hour retention covers H+4 only,
    # which had no traffic; H got swept).
    assert len(p._hourly_counters) == 1


def test_failed_call_still_counts_against_cap() -> None:
    """A tool that passes policy.check() but errors downstream still consumed budget.

    The design intent: runaway loops that retry failing calls hit the cap on
    the Nth attempt, not bypass it because each attempt failed.
    """
    p = _policy(hourly_caps={"x.add": 2})
    p.check("x.add", Tag.WRITE)  # caller simulates failure after this
    p.check("x.add", Tag.WRITE)  # caller simulates failure after this
    with pytest.raises(PolicyDenied):
        p.check("x.add", Tag.WRITE)


def test_cap_evaluated_after_flag_gates() -> None:
    """Read-only / disable-destructive rejections happen BEFORE the hourly cap, so
    a blocked-tool call does not consume hourly budget."""
    cfg = PolicyConfig(read_only=True, hourly_caps={"x.add": 1})
    p = Policy.from_config(cfg, read_only=True, disable_destructive=False)
    # Read-only blocks WRITE — should NOT count toward x.add's cap.
    with pytest.raises(PolicyDenied) as exc:
        p.check("x.add", Tag.WRITE)
    assert "read-only" in exc.value.message
    # Counter for x.add should be unchanged (zero).
    import time as _t

    hour = int(_t.time() // 3600)
    assert p._hourly_counters.get((hour, "x.add"), 0) == 0


def test_caps_dict_is_copied_not_shared() -> None:
    """Mutating the original config dict after Policy construction must not affect the live policy."""
    src = {"x.add": 5}
    cfg = PolicyConfig(hourly_caps=src)
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    src["x.add"] = 1  # try to mutate the source
    # Should still see the cap of 5.
    for _ in range(5):
        p.check("x.add", Tag.WRITE)
    with pytest.raises(PolicyDenied):
        p.check("x.add", Tag.WRITE)
