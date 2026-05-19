"""SQLite-backed confirm-token store.

The backend choice is driven by `PolicyConfig.state_db_path`:
  - None  -> _InMemoryTokenStore (default; correct for stdio transport)
  - path  -> _SQLiteTokenStore at that path

Persistence is load-bearing for streamable-HTTP transport (one stream issues
the token; another may consume it) and convenient for any restart-mid-plan
scenario. See notes/DESIGN-v0.2.md §1.3.
"""

from __future__ import annotations

import sqlite3
import time
from pathlib import Path

import pytest

from arr_stack_mcp.errors import ConfirmRequired
from arr_stack_mcp.policy import (
    Policy,
    PolicyConfig,
    _InMemoryTokenStore,
    _PendingToken,
    _SQLiteTokenStore,
    fingerprint,
)

# ---------- backend selection ----------


def test_from_config_no_path_uses_in_memory(tmp_path: Path) -> None:
    cfg = PolicyConfig(state_db_path=None)
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    assert isinstance(p._token_store, _InMemoryTokenStore)  # type: ignore[reportPrivateUsage]


def test_from_config_with_path_uses_sqlite(tmp_path: Path) -> None:
    db = tmp_path / "state.db"
    cfg = PolicyConfig(state_db_path=str(db))
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    assert isinstance(p._token_store, _SQLiteTokenStore)  # type: ignore[reportPrivateUsage]
    assert db.exists()


def test_from_config_with_empty_string_uses_in_memory(tmp_path: Path) -> None:
    """`state_db_path: ""` shouldn't try to create a SQLite file at the empty path."""
    cfg = PolicyConfig(state_db_path="")
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    assert isinstance(p._token_store, _InMemoryTokenStore)  # type: ignore[reportPrivateUsage]


# ---------- schema ----------


def test_sqlite_store_creates_schema_idempotently(tmp_path: Path) -> None:
    db = tmp_path / "state.db"
    _SQLiteTokenStore(db)
    # Construct again — must not crash on re-creation.
    _SQLiteTokenStore(db)
    # Validate the schema exists.
    with sqlite3.connect(db) as conn:
        rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='confirm_tokens'").fetchall()
        assert rows == [("confirm_tokens",)]


def test_sqlite_store_creates_parent_directory(tmp_path: Path) -> None:
    """Nested parent dirs are created idempotently."""
    db = tmp_path / "nested" / "deeper" / "state.db"
    _SQLiteTokenStore(db)
    assert db.exists()
    assert db.parent.is_dir()


def test_sqlite_store_uses_wal_mode(tmp_path: Path) -> None:
    """WAL is enabled for multi-process write tolerance."""
    db = tmp_path / "state.db"
    _SQLiteTokenStore(db)
    with sqlite3.connect(db) as conn:
        mode = conn.execute("PRAGMA journal_mode").fetchone()
    assert (mode or ["?"])[0] == "wal"


# ---------- round-trip ----------


def test_sqlite_store_put_and_pop(tmp_path: Path) -> None:
    db = tmp_path / "state.db"
    store = _SQLiteTokenStore(db)
    pending = _PendingToken(
        token="tok-1",
        tool_name="sonarr.series_delete",
        expires_at=time.time() + 300,
        payload_fingerprint="abc123",
    )
    store.put(pending)
    got = store.pop("tok-1")
    assert got is not None
    assert got.token == "tok-1"
    assert got.tool_name == "sonarr.series_delete"
    assert got.payload_fingerprint == "abc123"
    # Single-use: second pop returns None.
    assert store.pop("tok-1") is None


def test_sqlite_store_pop_unknown_returns_none(tmp_path: Path) -> None:
    db = tmp_path / "state.db"
    store = _SQLiteTokenStore(db)
    assert store.pop("nonexistent") is None


def test_sqlite_store_sweep_drops_expired(tmp_path: Path) -> None:
    db = tmp_path / "state.db"
    store = _SQLiteTokenStore(db)
    store.put(_PendingToken("fresh", "x", time.time() + 300, "fp"))
    store.put(_PendingToken("stale", "x", time.time() - 10, "fp"))
    store.sweep(time.time())
    # Fresh survives; stale is gone.
    assert store.pop("fresh") is not None
    assert store.pop("stale") is None


# ---------- persistence across instances ----------


def test_token_survives_across_policy_reconstruction(tmp_path: Path) -> None:
    """A token issued by Policy instance A is consumable by instance B against the same db path."""
    db = tmp_path / "state.db"
    cfg = PolicyConfig(state_db_path=str(db), confirm_token_ttl_seconds=300)

    # First server lifetime: issue the token.
    p1 = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    fp = fingerprint({"sonarr_id": 42})
    token = p1.issue_token("sonarr.series_delete", fp)

    # Simulate process restart: build a fresh Policy against the same DB.
    p2 = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    # Should consume without complaint.
    p2.consume_token("sonarr.series_delete", fp, token)


def test_token_consumed_in_one_instance_is_gone_in_another(tmp_path: Path) -> None:
    """A token consumed by instance A cannot be re-consumed by instance B."""
    db = tmp_path / "state.db"
    cfg = PolicyConfig(state_db_path=str(db))

    p1 = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    fp = fingerprint({})
    token = p1.issue_token("sonarr.series_delete", fp)
    p1.consume_token("sonarr.series_delete", fp, token)

    p2 = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    with pytest.raises(ConfirmRequired) as exc:
        p2.consume_token("sonarr.series_delete", fp, token)
    assert "unknown" in (exc.value.message or "").lower() or "expired" in (exc.value.message or "").lower()


def test_token_expires_with_wall_clock(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Wall-clock expiry: a SQLite-backed token issued with a 1-second TTL is dead after that elapses."""
    db = tmp_path / "state.db"
    cfg = PolicyConfig(state_db_path=str(db), confirm_token_ttl_seconds=10)
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)
    fp = fingerprint({})
    token = p.issue_token("sonarr.series_delete", fp)

    real_now = time.time()
    monkeypatch.setattr("arr_stack_mcp.policy.time.time", lambda: real_now + 30)
    with pytest.raises(ConfirmRequired) as exc:
        p.consume_token("sonarr.series_delete", fp, token)
    assert "unknown" in (exc.value.message or "").lower() or "expired" in (exc.value.message or "").lower()


# ---------- full Policy round-trip exercises the integration ----------


def test_full_policy_round_trip_through_sqlite_backend(tmp_path: Path) -> None:
    db = tmp_path / "state.db"
    cfg = PolicyConfig(state_db_path=str(db), confirm_token_ttl_seconds=60)
    p = Policy.from_config(cfg, read_only=False, disable_destructive=False)

    payload = {"sonarr_id": 42, "delete_files": True}
    fp = fingerprint(payload)
    token = p.issue_token("sonarr.series_delete", fp)
    assert token

    # Wrong payload — rejected.
    with pytest.raises(ConfirmRequired) as exc:
        p.consume_token("sonarr.series_delete", fingerprint({"sonarr_id": 99}), token)
    assert "does not match" in (exc.value.message or "")

    # The mismatched consume popped the token from storage (current contract),
    # so the correct re-issue lands a fresh token.
    token2 = p.issue_token("sonarr.series_delete", fp)
    p.consume_token("sonarr.series_delete", fp, token2)
