from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_difference import TagDifference


T = TypeVar("T", bound="RetagTrackResource")


@_attrs_define
class RetagTrackResource:
    """
    Attributes:
        id (Union[Unset, int]):
        artist_id (Union[Unset, int]):
        album_id (Union[Unset, int]):
        track_numbers (Union[None, Unset, list[int]]):
        track_file_id (Union[Unset, int]):
        path (Union[None, Unset, str]):
        changes (Union[None, Unset, list['TagDifference']]):
    """

    id: Union[Unset, int] = UNSET
    artist_id: Union[Unset, int] = UNSET
    album_id: Union[Unset, int] = UNSET
    track_numbers: Union[None, Unset, list[int]] = UNSET
    track_file_id: Union[Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    changes: Union[None, Unset, list["TagDifference"]] = UNSET

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

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        changes: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.changes, Unset):
            changes = UNSET
        elif isinstance(self.changes, list):
            changes = []
            for changes_type_0_item_data in self.changes:
                changes_type_0_item = changes_type_0_item_data.to_dict()
                changes.append(changes_type_0_item)

        else:
            changes = self.changes

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
        if path is not UNSET:
            field_dict["path"] = path
        if changes is not UNSET:
            field_dict["changes"] = changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_difference import TagDifference

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

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_changes(data: object) -> Union[None, Unset, list["TagDifference"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = []
                _changes_type_0 = data
                for changes_type_0_item_data in _changes_type_0:
                    changes_type_0_item = TagDifference.from_dict(
                        changes_type_0_item_data
                    )

                    changes_type_0.append(changes_type_0_item)

                return changes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TagDifference"]], data)

        changes = _parse_changes(d.pop("changes", UNSET))

        retag_track_resource = cls(
            id=id,
            artist_id=artist_id,
            album_id=album_id,
            track_numbers=track_numbers,
            track_file_id=track_file_id,
            path=path,
            changes=changes,
        )

        return retag_track_resource
