from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_guid_pair import NameGuidPair


T = TypeVar("T", bound="QueryFilters")


@_attrs_define
class QueryFilters:
    """
    Attributes:
        genres (Union[None, Unset, list['NameGuidPair']]):
        tags (Union[None, Unset, list[str]]):
    """

    genres: Union[None, Unset, list["NameGuidPair"]] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        genres: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = []
            for genres_type_0_item_data in self.genres:
                genres_type_0_item = genres_type_0_item_data.to_dict()
                genres.append(genres_type_0_item)

        else:
            genres = self.genres

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if tags is not UNSET:
            field_dict["Tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.name_guid_pair import NameGuidPair

        d = dict(src_dict)

        def _parse_genres(data: object) -> Union[None, Unset, list["NameGuidPair"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = []
                _genres_type_0 = data
                for genres_type_0_item_data in _genres_type_0:
                    genres_type_0_item = NameGuidPair.from_dict(genres_type_0_item_data)

                    genres_type_0.append(genres_type_0_item)

                return genres_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NameGuidPair"]], data)

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

        query_filters = cls(
            genres=genres,
            tags=tags,
        )

        return query_filters
