"""Prowlarr toolset projection helpers.

Network-level integration is exercised by the integration suite against a
real Prowlarr container (task #19). This file unit-tests the pure
projection helpers — `_health_to_issue`, `_indexer_to_summary`,
`_stats_to_row`, `_status_to_row`, `_testall_to_row`,
`_release_to_compact` — that translate generated-client shapes into the
LLM-friendly compact envelopes.
"""

from __future__ import annotations

from types import SimpleNamespace

from arr_stack_mcp.tools.prowlarr.tools import (
    _health_to_issue,
    _indexer_to_summary,
    _release_to_compact,
    _stats_to_row,
    _status_to_row,
    _testall_to_row,
)

# ---------- health ----------


def test_health_issue_projects_known_fields() -> None:
    h = SimpleNamespace(
        source="IndexerStatusCheck",
        type_="warning",
        message="Indexer X failed last check",
        wiki_url="https://wiki/...",
    )
    out = _health_to_issue(h)
    assert out.source == "IndexerStatusCheck"
    assert out.type == "warning"
    assert out.message == "Indexer X failed last check"
    assert out.wiki_url == "https://wiki/..."


def test_health_issue_falls_back_when_message_missing() -> None:
    h = SimpleNamespace(source=None, type_=None, message=None, wiki_url=None)
    out = _health_to_issue(h)
    assert out.message == "<unknown>"


# ---------- indexer list ----------


def test_indexer_summary_projects_full_row() -> None:
    r = SimpleNamespace(
        id=7,
        name="Rarbg",
        implementation="Cardigann",
        protocol="torrent",
        priority=25,
        enable=True,
        tags=[1, 2, 3],
    )
    out = _indexer_to_summary(r)
    assert out.id == 7
    assert out.name == "Rarbg"
    assert out.implementation == "Cardigann"
    assert out.protocol == "torrent"
    assert out.priority == 25
    assert out.enable is True
    assert out.tags == [1, 2, 3]


def test_indexer_summary_handles_missing_tags() -> None:
    r = SimpleNamespace(id=1, name="x", implementation=None, protocol=None, priority=None, enable=False, tags=None)
    out = _indexer_to_summary(r)
    assert out.tags == []
    assert out.enable is False


# ---------- indexer stats ----------


def test_stats_row_projects_counts() -> None:
    r = SimpleNamespace(
        indexer_id=3,
        indexer_name="Rarbg",
        number_of_queries=100,
        number_of_grabs=10,
        number_of_rss_queries=50,
        number_of_auth_queries=5,
        number_of_failed_queries=2,
        number_of_failed_grabs=1,
        number_of_failed_rss_queries=0,
        number_of_failed_auth_queries=0,
        average_response_time=450,
    )
    out = _stats_to_row(r)
    assert out.indexer_id == 3
    assert out.num_queries == 100
    assert out.num_grabs == 10
    assert out.num_failed_queries == 2
    assert out.average_response_time == 450


# ---------- indexer status ----------


def test_status_row_projects_failure_timestamps() -> None:
    r = SimpleNamespace(
        indexer_id=7,
        disabled_till="2026-05-20T00:00:00Z",
        most_recent_failure="2026-05-19T10:00:00Z",
        initial_failure="2026-05-19T08:00:00Z",
    )
    out = _status_to_row(r)
    assert out.indexer_id == 7
    assert out.disabled_till == "2026-05-20T00:00:00Z"
    assert out.most_recent_failure == "2026-05-19T10:00:00Z"


# ---------- test all ----------


def test_testall_row_from_dict_shape() -> None:
    r = {"id": 5, "isValid": True, "validationFailures": []}
    out = _testall_to_row(r)
    assert out.indexer_id == 5
    assert out.is_valid is True
    assert out.validation_failures == []


def test_testall_row_from_object_shape_with_failures() -> None:
    r = SimpleNamespace(
        id=9,
        is_valid=False,
        validation_failures=[
            SimpleNamespace(error_message="API key rejected"),
            SimpleNamespace(error_message="Captcha required"),
        ],
    )
    out = _testall_to_row(r)
    assert out.indexer_id == 9
    assert out.is_valid is False
    assert out.validation_failures == ["API key rejected", "Captcha required"]


def test_testall_row_from_dict_with_failures() -> None:
    r = {"id": 9, "isValid": False, "validationFailures": [{"errorMessage": "API key rejected"}]}
    out = _testall_to_row(r)
    assert out.is_valid is False
    assert out.validation_failures == ["API key rejected"]


# ---------- search release ----------


def test_release_compact_projects_known_fields() -> None:
    r = SimpleNamespace(
        title="Show.S01E01.1080p.x265-RELEASE",
        indexer="Rarbg",
        indexer_id=7,
        size=1_000_000_000,
        age_minutes=300,
        seeders=50,
        leechers=2,
        categories=[SimpleNamespace(id=5040), SimpleNamespace(id=5070)],
        protocol="torrent",
    )
    out = _release_to_compact(r)
    assert out.title == "Show.S01E01.1080p.x265-RELEASE"
    assert out.indexer == "Rarbg"
    assert out.indexer_id == 7
    assert out.size == 1_000_000_000
    assert out.age_minutes == 300
    assert out.seeders == 50
    assert out.categories == [5040, 5070]
    assert out.protocol == "torrent"


def test_release_compact_handles_missing_fields() -> None:
    r = SimpleNamespace(
        title=None,
        indexer=None,
        indexer_id=None,
        size=None,
        age_minutes=None,
        seeders=None,
        leechers=None,
        categories=None,
        protocol=None,
    )
    out = _release_to_compact(r)
    assert out.title == "<unknown>"
    assert out.size is None
    assert out.categories == []


def test_release_compact_falls_back_to_age_when_age_minutes_missing() -> None:
    """Some Prowlarr versions surface the field as `age` rather than `age_minutes`."""
    r = SimpleNamespace(
        title="x",
        indexer=None,
        indexer_id=None,
        size=None,
        age_minutes=None,
        age=42,
        seeders=None,
        leechers=None,
        categories=None,
        protocol=None,
    )
    out = _release_to_compact(r)
    assert out.age_minutes == 42


def test_release_compact_categories_from_ints() -> None:
    """Some upstream shapes surface category ids as bare ints rather than wrapper objects."""
    r = SimpleNamespace(
        title="x",
        indexer=None,
        indexer_id=None,
        size=None,
        age_minutes=None,
        seeders=None,
        leechers=None,
        categories=[2000, 5000],
        protocol=None,
    )
    out = _release_to_compact(r)
    # Bare ints come through as-is.
    assert out.categories == [2000, 5000]
