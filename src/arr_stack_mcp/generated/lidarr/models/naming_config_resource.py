from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NamingConfigResource")


@_attrs_define
class NamingConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        rename_tracks (Union[Unset, bool]):
        replace_illegal_characters (Union[Unset, bool]):
        colon_replacement_format (Union[Unset, int]):
        standard_track_format (Union[None, Unset, str]):
        multi_disc_track_format (Union[None, Unset, str]):
        artist_folder_format (Union[None, Unset, str]):
        include_artist_name (Union[Unset, bool]):
        include_album_title (Union[Unset, bool]):
        include_quality (Union[Unset, bool]):
        replace_spaces (Union[Unset, bool]):
        separator (Union[None, Unset, str]):
        number_style (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    rename_tracks: Union[Unset, bool] = UNSET
    replace_illegal_characters: Union[Unset, bool] = UNSET
    colon_replacement_format: Union[Unset, int] = UNSET
    standard_track_format: Union[None, Unset, str] = UNSET
    multi_disc_track_format: Union[None, Unset, str] = UNSET
    artist_folder_format: Union[None, Unset, str] = UNSET
    include_artist_name: Union[Unset, bool] = UNSET
    include_album_title: Union[Unset, bool] = UNSET
    include_quality: Union[Unset, bool] = UNSET
    replace_spaces: Union[Unset, bool] = UNSET
    separator: Union[None, Unset, str] = UNSET
    number_style: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        rename_tracks = self.rename_tracks

        replace_illegal_characters = self.replace_illegal_characters

        colon_replacement_format = self.colon_replacement_format

        standard_track_format: Union[None, Unset, str]
        if isinstance(self.standard_track_format, Unset):
            standard_track_format = UNSET
        else:
            standard_track_format = self.standard_track_format

        multi_disc_track_format: Union[None, Unset, str]
        if isinstance(self.multi_disc_track_format, Unset):
            multi_disc_track_format = UNSET
        else:
            multi_disc_track_format = self.multi_disc_track_format

        artist_folder_format: Union[None, Unset, str]
        if isinstance(self.artist_folder_format, Unset):
            artist_folder_format = UNSET
        else:
            artist_folder_format = self.artist_folder_format

        include_artist_name = self.include_artist_name

        include_album_title = self.include_album_title

        include_quality = self.include_quality

        replace_spaces = self.replace_spaces

        separator: Union[None, Unset, str]
        if isinstance(self.separator, Unset):
            separator = UNSET
        else:
            separator = self.separator

        number_style: Union[None, Unset, str]
        if isinstance(self.number_style, Unset):
            number_style = UNSET
        else:
            number_style = self.number_style

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if rename_tracks is not UNSET:
            field_dict["renameTracks"] = rename_tracks
        if replace_illegal_characters is not UNSET:
            field_dict["replaceIllegalCharacters"] = replace_illegal_characters
        if colon_replacement_format is not UNSET:
            field_dict["colonReplacementFormat"] = colon_replacement_format
        if standard_track_format is not UNSET:
            field_dict["standardTrackFormat"] = standard_track_format
        if multi_disc_track_format is not UNSET:
            field_dict["multiDiscTrackFormat"] = multi_disc_track_format
        if artist_folder_format is not UNSET:
            field_dict["artistFolderFormat"] = artist_folder_format
        if include_artist_name is not UNSET:
            field_dict["includeArtistName"] = include_artist_name
        if include_album_title is not UNSET:
            field_dict["includeAlbumTitle"] = include_album_title
        if include_quality is not UNSET:
            field_dict["includeQuality"] = include_quality
        if replace_spaces is not UNSET:
            field_dict["replaceSpaces"] = replace_spaces
        if separator is not UNSET:
            field_dict["separator"] = separator
        if number_style is not UNSET:
            field_dict["numberStyle"] = number_style

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        rename_tracks = d.pop("renameTracks", UNSET)

        replace_illegal_characters = d.pop("replaceIllegalCharacters", UNSET)

        colon_replacement_format = d.pop("colonReplacementFormat", UNSET)

        def _parse_standard_track_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        standard_track_format = _parse_standard_track_format(
            d.pop("standardTrackFormat", UNSET)
        )

        def _parse_multi_disc_track_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        multi_disc_track_format = _parse_multi_disc_track_format(
            d.pop("multiDiscTrackFormat", UNSET)
        )

        def _parse_artist_folder_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist_folder_format = _parse_artist_folder_format(
            d.pop("artistFolderFormat", UNSET)
        )

        include_artist_name = d.pop("includeArtistName", UNSET)

        include_album_title = d.pop("includeAlbumTitle", UNSET)

        include_quality = d.pop("includeQuality", UNSET)

        replace_spaces = d.pop("replaceSpaces", UNSET)

        def _parse_separator(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        separator = _parse_separator(d.pop("separator", UNSET))

        def _parse_number_style(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number_style = _parse_number_style(d.pop("numberStyle", UNSET))

        naming_config_resource = cls(
            id=id,
            rename_tracks=rename_tracks,
            replace_illegal_characters=replace_illegal_characters,
            colon_replacement_format=colon_replacement_format,
            standard_track_format=standard_track_format,
            multi_disc_track_format=multi_disc_track_format,
            artist_folder_format=artist_folder_format,
            include_artist_name=include_artist_name,
            include_album_title=include_album_title,
            include_quality=include_quality,
            replace_spaces=replace_spaces,
            separator=separator,
            number_style=number_style,
        )

        return naming_config_resource
