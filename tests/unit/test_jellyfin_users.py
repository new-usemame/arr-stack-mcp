"""Per-user Jellyfin scoping (design §2.3).

`jellyfin.users_list` returns the compact-projection of `UserDto`. Tests pin
the projection's correctness for the fields that matter to a consumer
building a sender-to-user mapping:
  - `user_id` (UUID string) for passing through to per-user tools
  - `name` for friendly resolution from external identities
  - `is_administrator` (sourced from the nested `policy` object) for
    bot-side admin gating

`LibrarySearchInput` / `RecentAdditionsInput` now carry an optional
`user_id` field; the per-call value takes precedence over the config-level
`default_user_id`. The handler integration is exercised by the integration
suite — this file pins the pure projection.
"""

from __future__ import annotations

from types import SimpleNamespace

from arr_stack_mcp.tools.jellyfin._models import LibrarySearchInput, RecentAdditionsInput
from arr_stack_mcp.tools.jellyfin.tools import _user_to_compact


def _policy(*, is_administrator: bool = False) -> SimpleNamespace:
    return SimpleNamespace(is_administrator=is_administrator)


def _user(
    *,
    user_id: str = "11111111-2222-3333-4444-555555555555",
    name: str = "alex",
    has_password: bool | None = True,
    last_login_date: str | None = "2026-05-18T12:34:56+00:00",
    policy: SimpleNamespace | None = None,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=user_id,
        name=name,
        has_password=has_password,
        last_login_date=last_login_date,
        policy=policy,
    )


def test_compact_user_projects_admin_policy() -> None:
    u = _user(name="alex", policy=_policy(is_administrator=True))
    out = _user_to_compact(u)
    assert out.user_id == "11111111-2222-3333-4444-555555555555"
    assert out.name == "alex"
    assert out.is_administrator is True


def test_compact_user_projects_non_admin_policy() -> None:
    u = _user(name="maggie", policy=_policy(is_administrator=False))
    out = _user_to_compact(u)
    assert out.is_administrator is False


def test_compact_user_defaults_admin_false_when_policy_missing() -> None:
    """If the API key lacks admin scope, Jellyfin may omit `policy`. Default to non-admin."""
    u = _user(policy=None)
    out = _user_to_compact(u)
    assert out.is_administrator is False


def test_compact_user_preserves_has_password_and_last_login() -> None:
    u = _user(has_password=False, last_login_date="2026-01-01T00:00:00+00:00")
    out = _user_to_compact(u)
    assert out.has_password is False
    assert out.last_login_date == "2026-01-01T00:00:00+00:00"


def test_compact_user_unknown_name_falls_through() -> None:
    u = _user(name=None)  # type: ignore[arg-type]
    out = _user_to_compact(u)
    assert out.name == "<unknown>"


# ---------- Input schema pinning ----------


def test_library_search_input_accepts_user_id() -> None:
    """The per-call `user_id` field exists and validates as a string."""
    args = LibrarySearchInput(query="dune", user_id="abc-uuid")
    assert args.user_id == "abc-uuid"


def test_library_search_input_user_id_is_optional() -> None:
    args = LibrarySearchInput(query="dune")
    assert args.user_id is None


def test_recent_additions_input_accepts_user_id() -> None:
    args = RecentAdditionsInput(user_id="abc-uuid")
    assert args.user_id == "abc-uuid"


def test_recent_additions_input_user_id_is_optional() -> None:
    args = RecentAdditionsInput()
    assert args.user_id is None
