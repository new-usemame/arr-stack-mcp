import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.download_protocol import DownloadProtocol
from ..models.tracked_download_state import TrackedDownloadState
from ..models.tracked_download_status import TrackedDownloadStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_resource import AlbumResource
    from ..models.artist_resource import ArtistResource
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.quality_model import QualityModel
    from ..models.tracked_download_status_message import TrackedDownloadStatusMessage


T = TypeVar("T", bound="QueueResource")


@_attrs_define
class QueueResource:
    """
    Attributes:
        id (Union[Unset, int]):
        artist_id (Union[None, Unset, int]):
        album_id (Union[None, Unset, int]):
        artist (Union[Unset, ArtistResource]):
        album (Union[Unset, AlbumResource]):
        quality (Union[Unset, QualityModel]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
        size (Union[Unset, float]):
        title (Union[None, Unset, str]):
        sizeleft (Union[Unset, float]):
        timeleft (Union[None, Unset, str]):
        estimated_completion_time (Union[None, Unset, datetime.datetime]):
        added (Union[None, Unset, datetime.datetime]):
        status (Union[None, Unset, str]):
        tracked_download_status (Union[Unset, TrackedDownloadStatus]):
        tracked_download_state (Union[Unset, TrackedDownloadState]):
        status_messages (Union[None, Unset, list['TrackedDownloadStatusMessage']]):
        error_message (Union[None, Unset, str]):
        download_id (Union[None, Unset, str]):
        protocol (Union[Unset, DownloadProtocol]):
        download_client (Union[None, Unset, str]):
        download_client_has_post_import_category (Union[Unset, bool]):
        indexer (Union[None, Unset, str]):
        output_path (Union[None, Unset, str]):
        track_file_count (Union[Unset, int]):
        track_has_file_count (Union[Unset, int]):
        download_forced (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    artist_id: Union[None, Unset, int] = UNSET
    album_id: Union[None, Unset, int] = UNSET
    artist: Union[Unset, "ArtistResource"] = UNSET
    album: Union[Unset, "AlbumResource"] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET
    size: Union[Unset, float] = UNSET
    title: Union[None, Unset, str] = UNSET
    sizeleft: Union[Unset, float] = UNSET
    timeleft: Union[None, Unset, str] = UNSET
    estimated_completion_time: Union[None, Unset, datetime.datetime] = UNSET
    added: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[None, Unset, str] = UNSET
    tracked_download_status: Union[Unset, TrackedDownloadStatus] = UNSET
    tracked_download_state: Union[Unset, TrackedDownloadState] = UNSET
    status_messages: Union[None, Unset, list["TrackedDownloadStatusMessage"]] = UNSET
    error_message: Union[None, Unset, str] = UNSET
    download_id: Union[None, Unset, str] = UNSET
    protocol: Union[Unset, DownloadProtocol] = UNSET
    download_client: Union[None, Unset, str] = UNSET
    download_client_has_post_import_category: Union[Unset, bool] = UNSET
    indexer: Union[None, Unset, str] = UNSET
    output_path: Union[None, Unset, str] = UNSET
    track_file_count: Union[Unset, int] = UNSET
    track_has_file_count: Union[Unset, int] = UNSET
    download_forced: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        artist_id: Union[None, Unset, int]
        if isinstance(self.artist_id, Unset):
            artist_id = UNSET
        else:
            artist_id = self.artist_id

        album_id: Union[None, Unset, int]
        if isinstance(self.album_id, Unset):
            album_id = UNSET
        else:
            album_id = self.album_id

        artist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist.to_dict()

        album: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

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

        size = self.size

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        sizeleft = self.sizeleft

        timeleft: Union[None, Unset, str]
        if isinstance(self.timeleft, Unset):
            timeleft = UNSET
        else:
            timeleft = self.timeleft

        estimated_completion_time: Union[None, Unset, str]
        if isinstance(self.estimated_completion_time, Unset):
            estimated_completion_time = UNSET
        elif isinstance(self.estimated_completion_time, datetime.datetime):
            estimated_completion_time = self.estimated_completion_time.isoformat()
        else:
            estimated_completion_time = self.estimated_completion_time

        added: Union[None, Unset, str]
        if isinstance(self.added, Unset):
            added = UNSET
        elif isinstance(self.added, datetime.datetime):
            added = self.added.isoformat()
        else:
            added = self.added

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        tracked_download_status: Union[Unset, str] = UNSET
        if not isinstance(self.tracked_download_status, Unset):
            tracked_download_status = self.tracked_download_status.value

        tracked_download_state: Union[Unset, str] = UNSET
        if not isinstance(self.tracked_download_state, Unset):
            tracked_download_state = self.tracked_download_state.value

        status_messages: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.status_messages, Unset):
            status_messages = UNSET
        elif isinstance(self.status_messages, list):
            status_messages = []
            for status_messages_type_0_item_data in self.status_messages:
                status_messages_type_0_item = status_messages_type_0_item_data.to_dict()
                status_messages.append(status_messages_type_0_item)

        else:
            status_messages = self.status_messages

        error_message: Union[None, Unset, str]
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        download_client: Union[None, Unset, str]
        if isinstance(self.download_client, Unset):
            download_client = UNSET
        else:
            download_client = self.download_client

        download_client_has_post_import_category = (
            self.download_client_has_post_import_category
        )

        indexer: Union[None, Unset, str]
        if isinstance(self.indexer, Unset):
            indexer = UNSET
        else:
            indexer = self.indexer

        output_path: Union[None, Unset, str]
        if isinstance(self.output_path, Unset):
            output_path = UNSET
        else:
            output_path = self.output_path

        track_file_count = self.track_file_count

        track_has_file_count = self.track_has_file_count

        download_forced = self.download_forced

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if artist_id is not UNSET:
            field_dict["artistId"] = artist_id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if artist is not UNSET:
            field_dict["artist"] = artist
        if album is not UNSET:
            field_dict["album"] = album
        if quality is not UNSET:
            field_dict["quality"] = quality
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score
        if size is not UNSET:
            field_dict["size"] = size
        if title is not UNSET:
            field_dict["title"] = title
        if sizeleft is not UNSET:
            field_dict["sizeleft"] = sizeleft
        if timeleft is not UNSET:
            field_dict["timeleft"] = timeleft
        if estimated_completion_time is not UNSET:
            field_dict["estimatedCompletionTime"] = estimated_completion_time
        if added is not UNSET:
            field_dict["added"] = added
        if status is not UNSET:
            field_dict["status"] = status
        if tracked_download_status is not UNSET:
            field_dict["trackedDownloadStatus"] = tracked_download_status
        if tracked_download_state is not UNSET:
            field_dict["trackedDownloadState"] = tracked_download_state
        if status_messages is not UNSET:
            field_dict["statusMessages"] = status_messages
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if download_client is not UNSET:
            field_dict["downloadClient"] = download_client
        if download_client_has_post_import_category is not UNSET:
            field_dict["downloadClientHasPostImportCategory"] = (
                download_client_has_post_import_category
            )
        if indexer is not UNSET:
            field_dict["indexer"] = indexer
        if output_path is not UNSET:
            field_dict["outputPath"] = output_path
        if track_file_count is not UNSET:
            field_dict["trackFileCount"] = track_file_count
        if track_has_file_count is not UNSET:
            field_dict["trackHasFileCount"] = track_has_file_count
        if download_forced is not UNSET:
            field_dict["downloadForced"] = download_forced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_resource import AlbumResource
        from ..models.artist_resource import ArtistResource
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.quality_model import QualityModel
        from ..models.tracked_download_status_message import (
            TrackedDownloadStatusMessage,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_artist_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        artist_id = _parse_artist_id(d.pop("artistId", UNSET))

        def _parse_album_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        album_id = _parse_album_id(d.pop("albumId", UNSET))

        _artist = d.pop("artist", UNSET)
        artist: Union[Unset, ArtistResource]
        if isinstance(_artist, Unset):
            artist = UNSET
        else:
            artist = ArtistResource.from_dict(_artist)

        _album = d.pop("album", UNSET)
        album: Union[Unset, AlbumResource]
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = AlbumResource.from_dict(_album)

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

        size = d.pop("size", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        sizeleft = d.pop("sizeleft", UNSET)

        def _parse_timeleft(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        timeleft = _parse_timeleft(d.pop("timeleft", UNSET))

        def _parse_estimated_completion_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                estimated_completion_time_type_0 = isoparse(data)

                return estimated_completion_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        estimated_completion_time = _parse_estimated_completion_time(
            d.pop("estimatedCompletionTime", UNSET)
        )

        def _parse_added(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                added_type_0 = isoparse(data)

                return added_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        added = _parse_added(d.pop("added", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        _tracked_download_status = d.pop("trackedDownloadStatus", UNSET)
        tracked_download_status: Union[Unset, TrackedDownloadStatus]
        if isinstance(_tracked_download_status, Unset):
            tracked_download_status = UNSET
        else:
            tracked_download_status = TrackedDownloadStatus(_tracked_download_status)

        _tracked_download_state = d.pop("trackedDownloadState", UNSET)
        tracked_download_state: Union[Unset, TrackedDownloadState]
        if isinstance(_tracked_download_state, Unset):
            tracked_download_state = UNSET
        else:
            tracked_download_state = TrackedDownloadState(_tracked_download_state)

        def _parse_status_messages(
            data: object,
        ) -> Union[None, Unset, list["TrackedDownloadStatusMessage"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_messages_type_0 = []
                _status_messages_type_0 = data
                for status_messages_type_0_item_data in _status_messages_type_0:
                    status_messages_type_0_item = (
                        TrackedDownloadStatusMessage.from_dict(
                            status_messages_type_0_item_data
                        )
                    )

                    status_messages_type_0.append(status_messages_type_0_item)

                return status_messages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TrackedDownloadStatusMessage"]], data)

        status_messages = _parse_status_messages(d.pop("statusMessages", UNSET))

        def _parse_error_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, DownloadProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = DownloadProtocol(_protocol)

        def _parse_download_client(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_client = _parse_download_client(d.pop("downloadClient", UNSET))

        download_client_has_post_import_category = d.pop(
            "downloadClientHasPostImportCategory", UNSET
        )

        def _parse_indexer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        indexer = _parse_indexer(d.pop("indexer", UNSET))

        def _parse_output_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        output_path = _parse_output_path(d.pop("outputPath", UNSET))

        track_file_count = d.pop("trackFileCount", UNSET)

        track_has_file_count = d.pop("trackHasFileCount", UNSET)

        download_forced = d.pop("downloadForced", UNSET)

        queue_resource = cls(
            id=id,
            artist_id=artist_id,
            album_id=album_id,
            artist=artist,
            album=album,
            quality=quality,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
            size=size,
            title=title,
            sizeleft=sizeleft,
            timeleft=timeleft,
            estimated_completion_time=estimated_completion_time,
            added=added,
            status=status,
            tracked_download_status=tracked_download_status,
            tracked_download_state=tracked_download_state,
            status_messages=status_messages,
            error_message=error_message,
            download_id=download_id,
            protocol=protocol,
            download_client=download_client,
            download_client_has_post_import_category=download_client_has_post_import_category,
            indexer=indexer,
            output_path=output_path,
            track_file_count=track_file_count,
            track_has_file_count=track_has_file_count,
            download_forced=download_forced,
        )

        return queue_resource
