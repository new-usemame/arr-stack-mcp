from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReleaseEpisodeResource")


@_attrs_define
class ReleaseEpisodeResource:
    """
    Attributes:
        id (Union[Unset, int]):
        season_number (Union[Unset, int]):
        episode_number (Union[Unset, int]):
        absolute_episode_number (Union[None, Unset, int]):
        title (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    season_number: Union[Unset, int] = UNSET
    episode_number: Union[Unset, int] = UNSET
    absolute_episode_number: Union[None, Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        season_number = self.season_number

        episode_number = self.episode_number

        absolute_episode_number: Union[None, Unset, int]
        if isinstance(self.absolute_episode_number, Unset):
            absolute_episode_number = UNSET
        else:
            absolute_episode_number = self.absolute_episode_number

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if season_number is not UNSET:
            field_dict["seasonNumber"] = season_number
        if episode_number is not UNSET:
            field_dict["episodeNumber"] = episode_number
        if absolute_episode_number is not UNSET:
            field_dict["absoluteEpisodeNumber"] = absolute_episode_number
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        season_number = d.pop("seasonNumber", UNSET)

        episode_number = d.pop("episodeNumber", UNSET)

        def _parse_absolute_episode_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        absolute_episode_number = _parse_absolute_episode_number(
            d.pop("absoluteEpisodeNumber", UNSET)
        )

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        release_episode_resource = cls(
            id=id,
            season_number=season_number,
            episode_number=episode_number,
            absolute_episode_number=absolute_episode_number,
            title=title,
        )

        return release_episode_resource
