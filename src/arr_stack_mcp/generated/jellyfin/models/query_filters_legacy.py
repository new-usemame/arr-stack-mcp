from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryFiltersLegacy")


@_attrs_define
class QueryFiltersLegacy:
    """
    Attributes:
        genres (Union[None, Unset, list[str]]):
        tags (Union[None, Unset, list[str]]):
        official_ratings (Union[None, Unset, list[str]]):
        years (Union[None, Unset, list[int]]):
    """

    genres: Union[None, Unset, list[str]] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    official_ratings: Union[None, Unset, list[str]] = UNSET
    years: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        genres: Union[None, Unset, list[str]]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        official_ratings: Union[None, Unset, list[str]]
        if isinstance(self.official_ratings, Unset):
            official_ratings = UNSET
        elif isinstance(self.official_ratings, list):
            official_ratings = self.official_ratings

        else:
            official_ratings = self.official_ratings

        years: Union[None, Unset, list[int]]
        if isinstance(self.years, Unset):
            years = UNSET
        elif isinstance(self.years, list):
            years = self.years

        else:
            years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if official_ratings is not UNSET:
            field_dict["OfficialRatings"] = official_ratings
        if years is not UNSET:
            field_dict["Years"] = years

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_genres(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(list[str], data)

                return genres_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        genres = _parse_genres(d.pop("Genres", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("Tags", UNSET))

        def _parse_official_ratings(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                official_ratings_type_0 = cast(list[str], data)

                return official_ratings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        official_ratings = _parse_official_ratings(d.pop("OfficialRatings", UNSET))

        def _parse_years(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                years_type_0 = cast(list[int], data)

                return years_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        years = _parse_years(d.pop("Years", UNSET))

        query_filters_legacy = cls(
            genres=genres,
            tags=tags,
            official_ratings=official_ratings,
            years=years,
        )

        return query_filters_legacy
