from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.colon_replacement_format import ColonReplacementFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="NamingConfigResource")


@_attrs_define
class NamingConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        rename_movies (Union[Unset, bool]):
        replace_illegal_characters (Union[Unset, bool]):
        colon_replacement_format (Union[Unset, ColonReplacementFormat]):
        standard_movie_format (Union[None, Unset, str]):
        movie_folder_format (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    rename_movies: Union[Unset, bool] = UNSET
    replace_illegal_characters: Union[Unset, bool] = UNSET
    colon_replacement_format: Union[Unset, ColonReplacementFormat] = UNSET
    standard_movie_format: Union[None, Unset, str] = UNSET
    movie_folder_format: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rename_movies = self.rename_movies

        replace_illegal_characters = self.replace_illegal_characters

        colon_replacement_format: Union[Unset, str] = UNSET
        if not isinstance(self.colon_replacement_format, Unset):
            colon_replacement_format = self.colon_replacement_format.value

        standard_movie_format: Union[None, Unset, str]
        if isinstance(self.standard_movie_format, Unset):
            standard_movie_format = UNSET
        else:
            standard_movie_format = self.standard_movie_format

        movie_folder_format: Union[None, Unset, str]
        if isinstance(self.movie_folder_format, Unset):
            movie_folder_format = UNSET
        else:
            movie_folder_format = self.movie_folder_format

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if rename_movies is not UNSET:
            field_dict["renameMovies"] = rename_movies
        if replace_illegal_characters is not UNSET:
            field_dict["replaceIllegalCharacters"] = replace_illegal_characters
        if colon_replacement_format is not UNSET:
            field_dict["colonReplacementFormat"] = colon_replacement_format
        if standard_movie_format is not UNSET:
            field_dict["standardMovieFormat"] = standard_movie_format
        if movie_folder_format is not UNSET:
            field_dict["movieFolderFormat"] = movie_folder_format

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        rename_movies = d.pop("renameMovies", UNSET)

        replace_illegal_characters = d.pop("replaceIllegalCharacters", UNSET)

        _colon_replacement_format = d.pop("colonReplacementFormat", UNSET)
        colon_replacement_format: Union[Unset, ColonReplacementFormat]
        if isinstance(_colon_replacement_format, Unset):
            colon_replacement_format = UNSET
        else:
            colon_replacement_format = ColonReplacementFormat(_colon_replacement_format)

        def _parse_standard_movie_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        standard_movie_format = _parse_standard_movie_format(
            d.pop("standardMovieFormat", UNSET)
        )

        def _parse_movie_folder_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        movie_folder_format = _parse_movie_folder_format(
            d.pop("movieFolderFormat", UNSET)
        )

        naming_config_resource = cls(
            id=id,
            rename_movies=rename_movies,
            replace_illegal_characters=replace_illegal_characters,
            colon_replacement_format=colon_replacement_format,
            standard_movie_format=standard_movie_format,
            movie_folder_format=movie_folder_format,
        )

        return naming_config_resource
