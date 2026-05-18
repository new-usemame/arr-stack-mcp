from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtistTitleInfo")


@_attrs_define
class ArtistTitleInfo:
    """
    Attributes:
        title (Union[None, Unset, str]):
        title_without_year (Union[None, Unset, str]):
        year (Union[Unset, int]):
    """

    title: Union[None, Unset, str] = UNSET
    title_without_year: Union[None, Unset, str] = UNSET
    year: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        title_without_year: Union[None, Unset, str]
        if isinstance(self.title_without_year, Unset):
            title_without_year = UNSET
        else:
            title_without_year = self.title_without_year

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if title_without_year is not UNSET:
            field_dict["titleWithoutYear"] = title_without_year
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_title_without_year(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title_without_year = _parse_title_without_year(d.pop("titleWithoutYear", UNSET))

        year = d.pop("year", UNSET)

        artist_title_info = cls(
            title=title,
            title_without_year=title_without_year,
            year=year,
        )

        return artist_title_info
