"""Confirm-token lifecycle + flag-driven gating."""

from __future__ import annotations

import pytest

from arr_stack_mcp.errors import ConfirmRequired, PolicyDenied
from arr_stack_mcp.policy import Policy, PolicyConfig, Tag, fingerprint


def _make_policy(*, read_only: bool = False, disable_destructive: bool = False) -> Policy:
    cfg = PolicyConfig(
        read_only=read_only,
        disable_destructive=disable_destructive,
        confirm_token_ttl_seconds=60,
        require_confirm_for_destructive=True,
    )
    return Policy.from_config(cfg, read_only=read_only, disable_destructive=disable_destructive)


def test_read_tag_is_always_allowed() -> None:
    p = _make_policy(read_only=True, disable_destructive=True)
    p.check("sonarr.series_search", Tag.READ)


def test_write_tag_blocked_in_read_only() -> None:
    p = _make_policy(read_only=True)
    with pytest.raises(PolicyDenied) as exc:
        p.check("sonarr.series_add", Tag.WRITE)
    assert "read-only" in exc.value.message
    assert exc.value.hint is not None


def test_destructive_tag_blocked_when_disable_destructive() -> None:
    p = _make_policy(disable_destructive=True)
    with pytest.raises(PolicyDenied) as exc:
        p.check("sonarr.series_delete", Tag.DESTRUCTIVE)
    assert "destructive" in exc.value.message


def test_write_tag_allowed_when_only_destructive_disabled() -> None:
    p = _make_policy(disable_destructive=True)
    # write is not destructive — should pass even when destructive tools are disabled.
    p.check("sonarr.series_add", Tag.WRITE)


def test_confirm_token_lifecycle_happy_path() -> None:
    p = _make_policy()
    payload = {"series_id": 42}
    fp = fingerprint(payload)
    token = p.issue_token("sonarr.series_delete", fp)
    assert token
    # consume succeeds
    p.consume_token("sonarr.series_delete", fp, token)
    # token is single-use
    with pytest.raises(ConfirmRequired):
        p.consume_token("sonarr.series_delete", fp, token)


def test_confirm_token_rejects_wrong_tool() -> None:
    p = _make_policy()
    fp = fingerprint({})
    token = p.issue_token("sonarr.series_delete", fp)
    with pytest.raises(ConfirmRequired) as exc:
        p.consume_token("radarr.movie_delete", fp, token)
    assert "different tool" in (exc.value.message or "")


def test_confirm_token_rejects_payload_drift() -> None:
    p = _make_policy()
    token = p.issue_token("sonarr.series_delete", fingerprint({"id": 42}))
    with pytest.raises(ConfirmRequired) as exc:
        p.consume_token("sonarr.series_delete", fingerprint({"id": 99}), token)
    assert "does not match" in (exc.value.message or "")


def test_confirm_token_required_when_omitted() -> None:
    p = _make_policy()
    with pytest.raises(ConfirmRequired):
        p.consume_token("sonarr.series_delete", fingerprint({}), confirm_token=None)


def test_fingerprint_stable_under_key_order() -> None:
    assert fingerprint({"a": 1, "b": 2}) == fingerprint({"b": 2, "a": 1})


def test_fingerprint_changes_with_value() -> None:
    assert fingerprint({"id": 1}) != fingerprint({"id": 2})


def test_confirm_token_expires(monkeypatch: pytest.MonkeyPatch) -> None:
    import time as _time_mod

    cfg = PolicyConfig(confirm_token_ttl_seconds=10)
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    fp = fingerprint({})
    token = p.issue_token("sonarr.series_delete", fp)

    # Fast-forward the monotonic clock past the TTL by patching the function
    # the policy module captured at import.
    real_time = _time_mod.monotonic()
    monkeypatch.setattr("arr_stack_mcp.policy.time.monotonic", lambda: real_time + 30)

    with pytest.raises(ConfirmRequired) as exc:
        p.consume_token("sonarr.series_delete", fp, token)
    assert "expired" in (exc.value.message or "").lower()
