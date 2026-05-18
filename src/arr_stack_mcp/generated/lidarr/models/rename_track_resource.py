from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenameTrackResource")


@_attrs_define
class RenameTrackResource:
    """
    Attributes:
        id (Union[Unset, int]):
        artist_id (Union[Unset, int]):
        album_id (Union[Unset, int]):
        track_numbers (Union[None, Unset, list[int]]):
        track_file_id (Union[Unset, int]):
        existing_path (Union[None, Unset, str]):
        new_path (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    artist_id: Union[Unset, int] = UNSET
    album_id: Union[Unset, int] = UNSET
    track_numbers: Union[None, Unset, list[int]] = UNSET
    track_file_id: Union[Unset, int] = UNSET
    existing_path: Union[None, Unset, str] = UNSET
    new_path: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        artist_id = self.artist_id

        album_id = self.album_id

        track_numbers: Union[None, Unset, list[int]]
        if isinstance(self.track_numbers, Unset):
            track_numbers = UNSET
        elif isinstance(self.track_numbers, list):
            track_numbers = self.track_numbers

        else:
            track_numbers = self.track_numbers

        track_file_id = self.track_file_id

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
        if artist_id is not UNSET:
            field_dict["artistId"] = artist_id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if track_numbers is not UNSET:
            field_dict["trackNumbers"] = track_numbers
        if track_file_id is not UNSET:
            field_dict["trackFileId"] = track_file_id
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

        artist_id = d.pop("artistId", UNSET)

        album_id = d.pop("albumId", UNSET)

        def _parse_track_numbers(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                track_numbers_type_0 = cast(list[int], data)

                return track_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        track_numbers = _parse_track_numbers(d.pop("trackNumbers", UNSET))

        track_file_id = d.pop("trackFileId", UNSET)

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

        rename_track_resource = cls(
            id=id,
            artist_id=artist_id,
            album_id=album_id,
            track_numbers=track_numbers,
            track_file_id=track_file_id,
            existing_path=existing_path,
            new_path=new_path,
        )

        return rename_track_resource
