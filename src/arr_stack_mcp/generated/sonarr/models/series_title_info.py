from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeriesTitleInfo")


@_attrs_define
class SeriesTitleInfo:
    """
    Attributes:
        title (Union[None, Unset, str]):
        title_without_year (Union[None, Unset, str]):
        year (Union[Unset, int]):
        all_titles (Union[None, Unset, list[str]]):
    """

    title: Union[None, Unset, str] = UNSET
    title_without_year: Union[None, Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    all_titles: Union[None, Unset, list[str]] = UNSET

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

        all_titles: Union[None, Unset, list[str]]
        if isinstance(self.all_titles, Unset):
            all_titles = UNSET
        elif isinstance(self.all_titles, list):
            all_titles = self.all_titles

        else:
            all_titles = self.all_titles

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if title_without_year is not UNSET:
            field_dict["titleWithoutYear"] = title_without_year
        if year is not UNSET:
            field_dict["year"] = year
        if all_titles is not UNSET:
            field_dict["allTitles"] = all_titles

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

        def _parse_title_without_year(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title_without_year = _parse_title_without_year(d.pop("titleWithoutYear", UNSET))

        year = d.pop("year", UNSET)

        def _parse_all_titles(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                all_titles_type_0 = cast(list[str], data)

                return all_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        all_titles = _parse_all_titles(d.pop("allTitles", UNSET))

        series_title_info = cls(
            title=title,
            title_without_year=title_without_year,
            year=year,
            all_titles=all_titles,
        )

        return series_title_info
