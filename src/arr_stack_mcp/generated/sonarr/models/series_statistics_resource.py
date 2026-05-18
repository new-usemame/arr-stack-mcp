from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeriesStatisticsResource")


@_attrs_define
class SeriesStatisticsResource:
    """
    Attributes:
        season_count (Union[Unset, int]):
        episode_file_count (Union[Unset, int]):
        episode_count (Union[Unset, int]):
        total_episode_count (Union[Unset, int]):
        size_on_disk (Union[Unset, int]):
        release_groups (Union[None, Unset, list[str]]):
        percent_of_episodes (Union[Unset, float]):
    """

    season_count: Union[Unset, int] = UNSET
    episode_file_count: Union[Unset, int] = UNSET
    episode_count: Union[Unset, int] = UNSET
    total_episode_count: Union[Unset, int] = UNSET
    size_on_disk: Union[Unset, int] = UNSET
    release_groups: Union[None, Unset, list[str]] = UNSET
    percent_of_episodes: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_count = self.season_count

        episode_file_count = self.episode_file_count

        episode_count = self.episode_count

        total_episode_count = self.total_episode_count

        size_on_disk = self.size_on_disk

        release_groups: Union[None, Unset, list[str]]
        if isinstance(self.release_groups, Unset):
            release_groups = UNSET
        elif isinstance(self.release_groups, list):
            release_groups = self.release_groups

        else:
            release_groups = self.release_groups

        percent_of_episodes = self.percent_of_episodes

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if season_count is not UNSET:
            field_dict["seasonCount"] = season_count
        if episode_file_count is not UNSET:
            field_dict["episodeFileCount"] = episode_file_count
        if episode_count is not UNSET:
            field_dict["episodeCount"] = episode_count
        if total_episode_count is not UNSET:
            field_dict["totalEpisodeCount"] = total_episode_count
        if size_on_disk is not UNSET:
            field_dict["sizeOnDisk"] = size_on_disk
        if release_groups is not UNSET:
            field_dict["releaseGroups"] = release_groups
        if percent_of_episodes is not UNSET:
            field_dict["percentOfEpisodes"] = percent_of_episodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season_count = d.pop("seasonCount", UNSET)

        episode_file_count = d.pop("episodeFileCount", UNSET)

        episode_count = d.pop("episodeCount", UNSET)

        total_episode_count = d.pop("totalEpisodeCount", UNSET)

        size_on_disk = d.pop("sizeOnDisk", UNSET)

        def _parse_release_groups(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                release_groups_type_0 = cast(list[str], data)

                return release_groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        release_groups = _parse_release_groups(d.pop("releaseGroups", UNSET))

        percent_of_episodes = d.pop("percentOfEpisodes", UNSET)

        series_statistics_resource = cls(
            season_count=season_count,
            episode_file_count=episode_file_count,
            episode_count=episode_count,
            total_episode_count=total_episode_count,
            size_on_disk=size_on_disk,
            release_groups=release_groups,
            percent_of_episodes=percent_of_episodes,
        )

        return series_statistics_resource
