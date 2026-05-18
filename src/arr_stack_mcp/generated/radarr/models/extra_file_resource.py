from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.extra_file_type import ExtraFileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtraFileResource")


@_attrs_define
class ExtraFileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        movie_id (Union[Unset, int]):
        movie_file_id (Union[None, Unset, int]):
        relative_path (Union[None, Unset, str]):
        extension (Union[None, Unset, str]):
        language_tags (Union[None, Unset, list[str]]):
        title (Union[None, Unset, str]):
        type_ (Union[Unset, ExtraFileType]):
    """

    id: Union[Unset, int] = UNSET
    movie_id: Union[Unset, int] = UNSET
    movie_file_id: Union[None, Unset, int] = UNSET
    relative_path: Union[None, Unset, str] = UNSET
    extension: Union[None, Unset, str] = UNSET
    language_tags: Union[None, Unset, list[str]] = UNSET
    title: Union[None, Unset, str] = UNSET
    type_: Union[Unset, ExtraFileType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        movie_id = self.movie_id

        movie_file_id: Union[None, Unset, int]
        if isinstance(self.movie_file_id, Unset):
            movie_file_id = UNSET
        else:
            movie_file_id = self.movie_file_id

        relative_path: Union[None, Unset, str]
        if isinstance(self.relative_path, Unset):
            relative_path = UNSET
        else:
            relative_path = self.relative_path

        extension: Union[None, Unset, str]
        if isinstance(self.extension, Unset):
            extension = UNSET
        else:
            extension = self.extension

        language_tags: Union[None, Unset, list[str]]
        if isinstance(self.language_tags, Unset):
            language_tags = UNSET
        elif isinstance(self.language_tags, list):
            language_tags = self.language_tags

        else:
            language_tags = self.language_tags

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if movie_id is not UNSET:
            field_dict["movieId"] = movie_id
        if movie_file_id is not UNSET:
            field_dict["movieFileId"] = movie_file_id
        if relative_path is not UNSET:
            field_dict["relativePath"] = relative_path
        if extension is not UNSET:
            field_dict["extension"] = extension
        if language_tags is not UNSET:
            field_dict["languageTags"] = language_tags
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        movie_id = d.pop("movieId", UNSET)

        def _parse_movie_file_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        movie_file_id = _parse_movie_file_id(d.pop("movieFileId", UNSET))

        def _parse_relative_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        relative_path = _parse_relative_path(d.pop("relativePath", UNSET))

        def _parse_extension(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        extension = _parse_extension(d.pop("extension", UNSET))

        def _parse_language_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                language_tags_type_0 = cast(list[str], data)

                return language_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        language_tags = _parse_language_tags(d.pop("languageTags", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ExtraFileType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ExtraFileType(_type_)

        extra_file_resource = cls(
            id=id,
            movie_id=movie_id,
            movie_file_id=movie_file_id,
            relative_path=relative_path,
            extension=extension,
            language_tags=language_tags,
            title=title,
            type_=type_,
        )

        return extra_file_resource
