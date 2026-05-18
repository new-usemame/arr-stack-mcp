from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlternateTitleResource")


@_attrs_define
class AlternateTitleResource:
    """
    Attributes:
        title (Union[None, Unset, str]):
        season_number (Union[None, Unset, int]):
        scene_season_number (Union[None, Unset, int]):
        scene_origin (Union[None, Unset, str]):
        comment (Union[None, Unset, str]):
    """

    title: Union[None, Unset, str] = UNSET
    season_number: Union[None, Unset, int] = UNSET
    scene_season_number: Union[None, Unset, int] = UNSET
    scene_origin: Union[None, Unset, str] = UNSET
    comment: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        season_number: Union[None, Unset, int]
        if isinstance(self.season_number, Unset):
            season_number = UNSET
        else:
            season_number = self.season_number

        scene_season_number: Union[None, Unset, int]
        if isinstance(self.scene_season_number, Unset):
            scene_season_number = UNSET
        else:
            scene_season_number = self.scene_season_number

        scene_origin: Union[None, Unset, str]
        if isinstance(self.scene_origin, Unset):
            scene_origin = UNSET
        else:
            scene_origin = self.scene_origin

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if season_number is not UNSET:
            field_dict["seasonNumber"] = season_number
        if scene_season_number is not UNSET:
            field_dict["sceneSeasonNumber"] = scene_season_number
        if scene_origin is not UNSET:
            field_dict["sceneOrigin"] = scene_origin
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_season_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        season_number = _parse_season_number(d.pop("seasonNumber", UNSET))

        def _parse_scene_season_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scene_season_number = _parse_scene_season_number(
            d.pop("sceneSeasonNumber", UNSET)
        )

        def _parse_scene_origin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scene_origin = _parse_scene_origin(d.pop("sceneOrigin", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        alternate_title_resource = cls(
            title=title,
            season_number=season_number,
            scene_season_number=scene_season_number,
            scene_origin=scene_origin,
            comment=comment,
        )

        return alternate_title_resource
