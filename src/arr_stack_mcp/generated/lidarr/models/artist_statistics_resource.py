from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtistStatisticsResource")


@_attrs_define
class ArtistStatisticsResource:
    """
    Attributes:
        album_count (Union[Unset, int]):
        track_file_count (Union[Unset, int]):
        track_count (Union[Unset, int]):
        total_track_count (Union[Unset, int]):
        size_on_disk (Union[Unset, int]):
        percent_of_tracks (Union[Unset, float]):
    """

    album_count: Union[Unset, int] = UNSET
    track_file_count: Union[Unset, int] = UNSET
    track_count: Union[Unset, int] = UNSET
    total_track_count: Union[Unset, int] = UNSET
    size_on_disk: Union[Unset, int] = UNSET
    percent_of_tracks: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        album_count = self.album_count

        track_file_count = self.track_file_count

        track_count = self.track_count

        total_track_count = self.total_track_count

        size_on_disk = self.size_on_disk

        percent_of_tracks = self.percent_of_tracks

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if album_count is not UNSET:
            field_dict["albumCount"] = album_count
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        album_count = d.pop("albumCount", UNSET)

        track_file_count = d.pop("trackFileCount", UNSET)

        track_count = d.pop("trackCount", UNSET)

        total_track_count = d.pop("totalTrackCount", UNSET)

        size_on_disk = d.pop("sizeOnDisk", UNSET)

        percent_of_tracks = d.pop("percentOfTracks", UNSET)

        artist_statistics_resource = cls(
            album_count=album_count,
            track_file_count=track_file_count,
            track_count=track_count,
            total_track_count=total_track_count,
            size_on_disk=size_on_disk,
            percent_of_tracks=percent_of_tracks,
        )

        return artist_statistics_resource
