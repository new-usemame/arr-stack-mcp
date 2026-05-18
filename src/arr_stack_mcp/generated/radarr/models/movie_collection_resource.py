from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MovieCollectionResource")


@_attrs_define
class MovieCollectionResource:
    """
    Attributes:
        title (Union[None, Unset, str]):
        tmdb_id (Union[Unset, int]):
    """

    title: Union[None, Unset, str] = UNSET
    tmdb_id: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        tmdb_id = self.tmdb_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if tmdb_id is not UNSET:
            field_dict["tmdbId"] = tmdb_id

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

        tmdb_id = d.pop("tmdbId", UNSET)

        movie_collection_resource = cls(
            title=title,
            tmdb_id=tmdb_id,
        )

        return movie_collection_resource
