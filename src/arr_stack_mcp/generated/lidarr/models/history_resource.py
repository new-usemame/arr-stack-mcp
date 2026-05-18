import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.entity_history_event_type import EntityHistoryEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_resource import AlbumResource
    from ..models.artist_resource import ArtistResource
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.history_resource_data_type_0 import HistoryResourceDataType0
    from ..models.quality_model import QualityModel
    from ..models.track_resource import TrackResource


T = TypeVar("T", bound="HistoryResource")


@_attrs_define
class HistoryResource:
    """
    Attributes:
        id (Union[Unset, int]):
        album_id (Union[Unset, int]):
        artist_id (Union[Unset, int]):
        track_id (Union[Unset, int]):
        source_title (Union[None, Unset, str]):
        quality (Union[Unset, QualityModel]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
        quality_cutoff_not_met (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):
        download_id (Union[None, Unset, str]):
        event_type (Union[Unset, EntityHistoryEventType]):
        data (Union['HistoryResourceDataType0', None, Unset]):
        album (Union[Unset, AlbumResource]):
        artist (Union[Unset, ArtistResource]):
        track (Union[Unset, TrackResource]):
    """

    id: Union[Unset, int] = UNSET
    album_id: Union[Unset, int] = UNSET
    artist_id: Union[Unset, int] = UNSET
    track_id: Union[Unset, int] = UNSET
    source_title: Union[None, Unset, str] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET
    quality_cutoff_not_met: Union[Unset, bool] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    download_id: Union[None, Unset, str] = UNSET
    event_type: Union[Unset, EntityHistoryEventType] = UNSET
    data: Union["HistoryResourceDataType0", None, Unset] = UNSET
    album: Union[Unset, "AlbumResource"] = UNSET
    artist: Union[Unset, "ArtistResource"] = UNSET
    track: Union[Unset, "TrackResource"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.history_resource_data_type_0 import HistoryResourceDataType0

        id = self.id

        album_id = self.album_id

        artist_id = self.artist_id

        track_id = self.track_id

        source_title: Union[None, Unset, str]
        if isinstance(self.source_title, Unset):
            source_title = UNSET
        else:
            source_title = self.source_title

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        custom_formats: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_formats, Unset):
            custom_formats = UNSET
        elif isinstance(self.custom_formats, list):
            custom_formats = []
            for custom_formats_type_0_item_data in self.custom_formats:
                custom_formats_type_0_item = custom_formats_type_0_item_data.to_dict()
                custom_formats.append(custom_formats_type_0_item)

        else:
            custom_formats = self.custom_formats

        custom_format_score = self.custom_format_score

        quality_cutoff_not_met = self.quality_cutoff_not_met

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, HistoryResourceDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        album: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        artist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist.to_dict()

        track: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.track, Unset):
            track = self.track.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if artist_id is not UNSET:
            field_dict["artistId"] = artist_id
        if track_id is not UNSET:
            field_dict["trackId"] = track_id
        if source_title is not UNSET:
            field_dict["sourceTitle"] = source_title
        if quality is not UNSET:
            field_dict["quality"] = quality
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score
        if quality_cutoff_not_met is not UNSET:
            field_dict["qualityCutoffNotMet"] = quality_cutoff_not_met
        if date is not UNSET:
            field_dict["date"] = date
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if data is not UNSET:
            field_dict["data"] = data
        if album is not UNSET:
            field_dict["album"] = album
        if artist is not UNSET:
            field_dict["artist"] = artist
        if track is not UNSET:
            field_dict["track"] = track

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_resource import AlbumResource
        from ..models.artist_resource import ArtistResource
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.history_resource_data_type_0 import HistoryResourceDataType0
        from ..models.quality_model import QualityModel
        from ..models.track_resource import TrackResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        album_id = d.pop("albumId", UNSET)

        artist_id = d.pop("artistId", UNSET)

        track_id = d.pop("trackId", UNSET)

        def _parse_source_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_title = _parse_source_title(d.pop("sourceTitle", UNSET))

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        def _parse_custom_formats(
            data: object,
        ) -> Union[None, Unset, list["CustomFormatResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_formats_type_0 = []
                _custom_formats_type_0 = data
                for custom_formats_type_0_item_data in _custom_formats_type_0:
                    custom_formats_type_0_item = CustomFormatResource.from_dict(
                        custom_formats_type_0_item_data
                    )

                    custom_formats_type_0.append(custom_formats_type_0_item)

                return custom_formats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["CustomFormatResource"]], data)

        custom_formats = _parse_custom_formats(d.pop("customFormats", UNSET))

        custom_format_score = d.pop("customFormatScore", UNSET)

        quality_cutoff_not_met = d.pop("qualityCutoffNotMet", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, EntityHistoryEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = EntityHistoryEventType(_event_type)

        def _parse_data(data: object) -> Union["HistoryResourceDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = HistoryResourceDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HistoryResourceDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        _album = d.pop("album", UNSET)
        album: Union[Unset, AlbumResource]
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = AlbumResource.from_dict(_album)

        _artist = d.pop("artist", UNSET)
        artist: Union[Unset, ArtistResource]
        if isinstance(_artist, Unset):
            artist = UNSET
        else:
            artist = ArtistResource.from_dict(_artist)

        _track = d.pop("track", UNSET)
        track: Union[Unset, TrackResource]
        if isinstance(_track, Unset):
            track = UNSET
        else:
            track = TrackResource.from_dict(_track)

        history_resource = cls(
            id=id,
            album_id=album_id,
            artist_id=artist_id,
            track_id=track_id,
            source_title=source_title,
            quality=quality,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
            quality_cutoff_not_met=quality_cutoff_not_met,
            date=date,
            download_id=download_id,
            event_type=event_type,
            data=data,
            album=album,
            artist=artist,
            track=track,
        )

        return history_resource
