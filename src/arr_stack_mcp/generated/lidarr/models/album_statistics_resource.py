from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumStatisticsResource")


@_attrs_define
class AlbumStatisticsResource:
    """
    Attributes:
        track_file_count (Union[Unset, int]):
        track_count (Union[Unset, int]):
        total_track_count (Union[Unset, int]):
        size_on_disk (Union[Unset, int]):
        percent_of_tracks (Union[Unset, float]):
    """

    track_file_count: Union[Unset, int] = UNSET
    track_count: Union[Unset, int] = UNSET
    total_track_count: Union[Unset, int] = UNSET
    size_on_disk: Union[Unset, int] = UNSET
    percent_of_tracks: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        track_file_count = self.track_file_count

        track_count = self.track_count

        total_track_count = self.total_track_count

        size_on_disk = self.size_on_disk

        percent_of_tracks = self.percent_of_tracks

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if track_file_count is not UNSET:
            field_dict["trackFileCount"] = track_file_count
        if track_count is not UNSET:
            field_dict["trackCount"] = track_count
        if total_track_count is not UNSET:
            field_dict["totalTrackCount"] = total_track_count
        if size_on_disk is not UNSET:
            field_dict["sizeOnDisk"] = size_on_disk
        if percent_of_tracks is not UNSET:
            field_dict["percentOfTracks"] = percent_of_tracks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        track_file_count = d.pop("trackFileCount", UNSET)

        track_count = d.pop("trackCount", UNSET)

        total_track_count = d.pop("totalTrackCount", UNSET)

        size_on_disk = d.pop("sizeOnDisk", UNSET)

        percent_of_tracks = d.pop("percentOfTracks", UNSET)

        album_statistics_resource = cls(
            track_file_count=track_file_count,
            track_count=track_count,
            total_track_count=total_track_count,
            size_on_disk=size_on_disk,
            percent_of_tracks=percent_of_tracks,
        )

        return album_statistics_resource
