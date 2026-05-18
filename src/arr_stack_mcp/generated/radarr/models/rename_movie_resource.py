from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenameMovieResource")


@_attrs_define
class RenameMovieResource:
    """
    Attributes:
        id (Union[Unset, int]):
        movie_id (Union[Unset, int]):
        movie_file_id (Union[Unset, int]):
        existing_path (Union[None, Unset, str]):
        new_path (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    movie_id: Union[Unset, int] = UNSET
    movie_file_id: Union[Unset, int] = UNSET
    existing_path: Union[None, Unset, str] = UNSET
    new_path: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        movie_id = self.movie_id

        movie_file_id = self.movie_file_id

        existing_path: Union[None, Unset, str]
        if isinstance(self.existing_path, Unset):
            existing_path = UNSET
        else:
            existing_path = self.existing_path

        new_path: Union[None, Unset, str]
        if isinstance(self.new_path, Unset):
            new_path = UNSET
        else:
            new_path = self.new_path

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if movie_id is not UNSET:
            field_dict["movieId"] = movie_id
        if movie_file_id is not UNSET:
            field_dict["movieFileId"] = movie_file_id
        if existing_path is not UNSET:
            field_dict["existingPath"] = existing_path
        if new_path is not UNSET:
            field_dict["newPath"] = new_path

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        movie_id = d.pop("movieId", UNSET)

        movie_file_id = d.pop("movieFileId", UNSET)

        def _parse_existing_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        existing_path = _parse_existing_path(d.pop("existingPath", UNSET))

        def _parse_new_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        new_path = _parse_new_path(d.pop("newPath", UNSET))

        rename_movie_resource = cls(
            id=id,
            movie_id=movie_id,
            movie_file_id=movie_file_id,
            existing_path=existing_path,
            new_path=new_path,
        )

        return rename_movie_resource
