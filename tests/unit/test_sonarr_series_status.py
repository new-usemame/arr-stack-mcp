"""Per-season projection for `sonarr.series_status`.

The tool itself is exercised by the integration suite against a real Sonarr
container (task #19). This unit test pins the pure projection function
`_series_to_status` — given a synthetic `SeriesResource`, the resulting
`SeriesStatusResult` should carry the season-level rows + rolled-up totals
without depending on the generated client's HTTP path.

See notes/DESIGN-v0.2.md §2.4.
"""

from __future__ import annotations

from types import SimpleNamespace

from arr_stack_mcp.tools.sonarr.tools import _series_to_status


def _stats(*, episode_count: int = 0, episode_file_count: int = 0, total_episode_count: int = 0, size_on_disk: int = 0) -> SimpleNamespace:
    """Mimic the SeasonStatisticsResource shape the generated client exposes."""
    return SimpleNamespace(
        episode_count=episode_count,
        episode_file_count=episode_file_count,
        total_episode_count=total_episode_count,
        size_on_disk=size_on_disk,
    )


def _season(season_number: int, *, monitored: bool = True, **stats_kwargs: int) -> SimpleNamespace:
    return SimpleNamespace(
        season_number=season_number,
        monitored=monitored,
        statistics=_stats(**stats_kwargs),
    )


def _series(*, seasons: list[SimpleNamespace] | None = None) -> SimpleNamespace:
    """Mimic the SeriesResource shape `_series_to_status` consumes."""
    return SimpleNamespace(
        id=42,
        tvdb_id=12345,
        title="Battlestar Galactica",
        year=2004,
        status=SimpleNamespace(value="ended"),
        monitored=True,
        seasons=seasons,
    )


def test_no_seasons_yields_zero_totals() -> None:
    result = _series_to_status(_series(seasons=[]))  # type: ignore[arg-type]
    assert result.sonarr_id == 42
    assert result.tvdb_id == 12345
    assert result.title == "Battlestar Galactica"
    assert result.year == 2004
    assert result.status == "ended"
    assert result.monitored is True
    assert result.seasons == []
    assert result.total_episode_count == 0
    assert result.total_episode_file_count == 0
    assert result.total_size_on_disk == 0


def test_seasons_rollup_sums_per_season_counts() -> None:
    seasons = [
        _season(1, episode_count=10, episode_file_count=10, total_episode_count=10, size_on_disk=1000),
        _season(2, episode_count=10, episode_file_count=8, total_episode_count=10, size_on_disk=800),
        _season(3, episode_count=20, episode_file_count=0, total_episode_count=20, size_on_disk=0),
    ]
    result = _series_to_status(_series(seasons=seasons))  # type: ignore[arg-type]
    assert len(result.seasons) == 3
    # Per-season pin
    assert result.seasons[0].season_number == 1
    assert result.seasons[0].episode_count == 10
    assert result.seasons[0].episode_file_count == 10
    assert result.seasons[1].episode_file_count == 8  # the season with missing episodes
    assert result.seasons[2].episode_file_count == 0
    # Roll-up
    assert result.total_episode_count == 40
    assert result.total_episode_file_count == 18
    assert result.total_size_on_disk == 1800


def test_unmonitored_season_preserved() -> None:
    seasons = [_season(1, monitored=False, episode_count=5)]
    result = _series_to_status(_series(seasons=seasons))  # type: ignore[arg-type]
    assert result.seasons[0].monitored is False


def test_missing_seasons_field_treated_as_empty() -> None:
    """If the upstream payload omits `seasons`, the result has no season rows but totals are still 0."""
    result = _series_to_status(_series(seasons=None))  # type: ignore[arg-type]
    assert result.seasons == []
    assert result.total_episode_count == 0


def test_partial_season_missing_episodes_visible_in_diff() -> None:
    """The agent's typical question 'what's missing from X?' is answered by ep_count - ep_file_count."""
    seasons = [
        _season(1, episode_count=10, episode_file_count=10),  # complete
        _season(2, episode_count=10, episode_file_count=7),  # 3 missing
    ]
    result = _series_to_status(_series(seasons=seasons))  # type: ignore[arg-type]
    missing_by_season = [s.episode_count - s.episode_file_count for s in result.seasons]
    assert missing_by_season == [0, 3]
