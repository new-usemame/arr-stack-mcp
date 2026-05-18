from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artist_resource import ArtistResource
    from ..models.ratings import Ratings
    from ..models.track_file_resource import TrackFileResource


T = TypeVar("T", bound="TrackResource")


@_attrs_define
class TrackResource:
    """
    Attributes:
        id (Union[Unset, int]):
        artist_id (Union[Unset, int]):
        foreign_track_id (Union[None, Unset, str]):
        foreign_recording_id (Union[None, Unset, str]):
        track_file_id (Union[Unset, int]):
        album_id (Union[Unset, int]):
        explicit (Union[Unset, bool]):
        absolute_track_number (Union[Unset, int]):
        track_number (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        duration (Union[Unset, int]):
        track_file (Union[Unset, TrackFileResource]):
        medium_number (Union[Unset, int]):
        has_file (Union[Unset, bool]):
        artist (Union[Unset, ArtistResource]):
        ratings (Union[Unset, Ratings]):
    """

    id: Union[Unset, int] = UNSET
    artist_id: Union[Unset, int] = UNSET
    foreign_track_id: Union[None, Unset, str] = UNSET
    foreign_recording_id: Union[None, Unset, str] = UNSET
    track_file_id: Union[Unset, int] = UNSET
    album_id: Union[Unset, int] = UNSET
    explicit: Union[Unset, bool] = UNSET
    absolute_track_number: Union[Unset, int] = UNSET
    track_number: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    track_file: Union[Unset, "TrackFileResource"] = UNSET
    medium_number: Union[Unset, int] = UNSET
    has_file: Union[Unset, bool] = UNSET
    artist: Union[Unset, "ArtistResource"] = UNSET
    ratings: Union[Unset, "Ratings"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        artist_id = self.artist_id

        foreign_track_id: Union[None, Unset, str]
        if isinstance(self.foreign_track_id, Unset):
            foreign_track_id = UNSET
        else:
            foreign_track_id = self.foreign_track_id

        foreign_recording_id: Union[None, Unset, str]
        if isinstance(self.foreign_recording_id, Unset):
            foreign_recording_id = UNSET
        else:
            foreign_recording_id = self.foreign_recording_id

        track_file_id = self.track_file_id

        album_id = self.album_id

        explicit = self.explicit

        absolute_track_number = self.absolute_track_number

        track_number: Union[None, Unset, str]
        if isinstance(self.track_number, Unset):
            track_number = UNSET
        else:
            track_number = self.track_number

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        duration = self.duration

        track_file: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.track_file, Unset):
            track_file = self.track_file.to_dict()

        medium_number = self.medium_number

        has_file = self.has_file

        artist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist.to_dict()

        ratings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if artist_id is not UNSET:
            field_dict["artistId"] = artist_id
        if foreign_track_id is not UNSET:
            field_dict["foreignTrackId"] = foreign_track_id
        if foreign_recording_id is not UNSET:
            field_dict["foreignRecordingId"] = foreign_recording_id
        if track_file_id is not UNSET:
            field_dict["trackFileId"] = track_file_id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if explicit is not UNSET:
            field_dict["explicit"] = explicit
        if absolute_track_number is not UNSET:
            field_dict["absoluteTrackNumber"] = absolute_track_number
        if track_number is not UNSET:
            field_dict["trackNumber"] = track_number
        if title is not UNSET:
            field_dict["title"] = title
        if duration is not UNSET:
            field_dict["duration"] = duration
        if track_file is not UNSET:
            field_dict["trackFile"] = track_file
        if medium_number is not UNSET:
            field_dict["mediumNumber"] = medium_number
        if has_file is not UNSET:
            field_dict["hasFile"] = has_file
        if artist is not UNSET:
            field_dict["artist"] = artist
        if ratings is not UNSET:
            field_dict["ratings"] = ratings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artist_resource import ArtistResource
        from ..models.ratings import Ratings
        from ..models.track_file_resource import TrackFileResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        artist_id = d.pop("artistId", UNSET)

        def _parse_foreign_track_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_track_id = _parse_foreign_track_id(d.pop("foreignTrackId", UNSET))

        def _parse_foreign_recording_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_recording_id = _parse_foreign_recording_id(
            d.pop("foreignRecordingId", UNSET)
        )

        track_file_id = d.pop("trackFileId", UNSET)

        album_id = d.pop("albumId", UNSET)

        explicit = d.pop("explicit", UNSET)

        absolute_track_number = d.pop("absoluteTrackNumber", UNSET)

        def _parse_track_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        track_number = _parse_track_number(d.pop("trackNumber", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        duration = d.pop("duration", UNSET)

        _track_file = d.pop("trackFile", UNSET)
        track_file: Union[Unset, TrackFileResource]
        if isinstance(_track_file, Unset):
            track_file = UNSET
        else:
            track_file = TrackFileResource.from_dict(_track_file)

        medium_number = d.pop("mediumNumber", UNSET)

        has_file = d.pop("hasFile", UNSET)

        _artist = d.pop("artist", UNSET)
        artist: Union[Unset, ArtistResource]
        if isinstance(_artist, Unset):
            artist = UNSET
        else:
            artist = ArtistResource.from_dict(_artist)

        _ratings = d.pop("ratings", UNSET)
        ratings: Union[Unset, Ratings]
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = Ratings.from_dict(_ratings)

        track_resource = cls(
            id=id,
            artist_id=artist_id,
            foreign_track_id=foreign_track_id,
            foreign_recording_id=foreign_recording_id,
            track_file_id=track_file_id,
            album_id=album_id,
            explicit=explicit,
            absolute_track_number=absolute_track_number,
            track_number=track_number,
            title=title,
            duration=duration,
            track_file=track_file,
            medium_number=medium_number,
            has_file=has_file,
            artist=artist,
            ratings=ratings,
        )

        return track_resource
