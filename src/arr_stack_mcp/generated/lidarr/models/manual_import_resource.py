from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_resource import AlbumResource
    from ..models.artist_resource import ArtistResource
    from ..models.parsed_track_info import ParsedTrackInfo
    from ..models.quality_model import QualityModel
    from ..models.rejection import Rejection
    from ..models.track_resource import TrackResource


T = TypeVar("T", bound="ManualImportResource")


@_attrs_define
class ManualImportResource:
    """
    Attributes:
        id (Union[Unset, int]):
        path (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        size (Union[Unset, int]):
        artist (Union[Unset, ArtistResource]):
        album (Union[Unset, AlbumResource]):
        album_release_id (Union[Unset, int]):
        tracks (Union[None, Unset, list['TrackResource']]):
        quality (Union[Unset, QualityModel]):
        release_group (Union[None, Unset, str]):
        quality_weight (Union[Unset, int]):
        download_id (Union[None, Unset, str]):
        indexer_flags (Union[Unset, int]):
        rejections (Union[None, Unset, list['Rejection']]):
        audio_tags (Union[Unset, ParsedTrackInfo]):
        additional_file (Union[Unset, bool]):
        replace_existing_files (Union[Unset, bool]):
        disable_release_switching (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    artist: Union[Unset, "ArtistResource"] = UNSET
    album: Union[Unset, "AlbumResource"] = UNSET
    album_release_id: Union[Unset, int] = UNSET
    tracks: Union[None, Unset, list["TrackResource"]] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    quality_weight: Union[Unset, int] = UNSET
    download_id: Union[None, Unset, str] = UNSET
    indexer_flags: Union[Unset, int] = UNSET
    rejections: Union[None, Unset, list["Rejection"]] = UNSET
    audio_tags: Union[Unset, "ParsedTrackInfo"] = UNSET
    additional_file: Union[Unset, bool] = UNSET
    replace_existing_files: Union[Unset, bool] = UNSET
    disable_release_switching: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        size = self.size

        artist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist.to_dict()

        album: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        album_release_id = self.album_release_id

        tracks: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.tracks, Unset):
            tracks = UNSET
        elif isinstance(self.tracks, list):
            tracks = []
            for tracks_type_0_item_data in self.tracks:
                tracks_type_0_item = tracks_type_0_item_data.to_dict()
                tracks.append(tracks_type_0_item)

        else:
            tracks = self.tracks

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

        quality_weight = self.quality_weight

        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        indexer_flags = self.indexer_flags

        rejections: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.rejections, Unset):
            rejections = UNSET
        elif isinstance(self.rejections, list):
            rejections = []
            for rejections_type_0_item_data in self.rejections:
                rejections_type_0_item = rejections_type_0_item_data.to_dict()
                rejections.append(rejections_type_0_item)

        else:
            rejections = self.rejections

        audio_tags: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.audio_tags, Unset):
            audio_tags = self.audio_tags.to_dict()

        additional_file = self.additional_file

        replace_existing_files = self.replace_existing_files

        disable_release_switching = self.disable_release_switching

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if artist is not UNSET:
            field_dict["artist"] = artist
        if album is not UNSET:
            field_dict["album"] = album
        if album_release_id is not UNSET:
            field_dict["albumReleaseId"] = album_release_id
        if tracks is not UNSET:
            field_dict["tracks"] = tracks
        if quality is not UNSET:
            field_dict["quality"] = quality
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if quality_weight is not UNSET:
            field_dict["qualityWeight"] = quality_weight
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if indexer_flags is not UNSET:
            field_dict["indexerFlags"] = indexer_flags
        if rejections is not UNSET:
            field_dict["rejections"] = rejections
        if audio_tags is not UNSET:
            field_dict["audioTags"] = audio_tags
        if additional_file is not UNSET:
            field_dict["additionalFile"] = additional_file
        if replace_existing_files is not UNSET:
            field_dict["replaceExistingFiles"] = replace_existing_files
        if disable_release_switching is not UNSET:
            field_dict["disableReleaseSwitching"] = disable_release_switching

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_resource import AlbumResource
        from ..models.artist_resource import ArtistResource
        from ..models.parsed_track_info import ParsedTrackInfo
        from ..models.quality_model import QualityModel
        from ..models.rejection import Rejection
        from ..models.track_resource import TrackResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        size = d.pop("size", UNSET)

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

        album_release_id = d.pop("albumReleaseId", UNSET)

        def _parse_tracks(data: object) -> Union[None, Unset, list["TrackResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tracks_type_0 = []
                _tracks_type_0 = data
                for tracks_type_0_item_data in _tracks_type_0:
                    tracks_type_0_item = TrackResource.from_dict(
                        tracks_type_0_item_data
                    )

                    tracks_type_0.append(tracks_type_0_item)

                return tracks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TrackResource"]], data)

        tracks = _parse_tracks(d.pop("tracks", UNSET))

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        def _parse_release_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_group = _parse_release_group(d.pop("releaseGroup", UNSET))

        quality_weight = d.pop("qualityWeight", UNSET)

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        indexer_flags = d.pop("indexerFlags", UNSET)

        def _parse_rejections(data: object) -> Union[None, Unset, list["Rejection"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rejections_type_0 = []
                _rejections_type_0 = data
                for rejections_type_0_item_data in _rejections_type_0:
                    rejections_type_0_item = Rejection.from_dict(
                        rejections_type_0_item_data
                    )

                    rejections_type_0.append(rejections_type_0_item)

                return rejections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Rejection"]], data)

        rejections = _parse_rejections(d.pop("rejections", UNSET))

        _audio_tags = d.pop("audioTags", UNSET)
        audio_tags: Union[Unset, ParsedTrackInfo]
        if isinstance(_audio_tags, Unset):
            audio_tags = UNSET
        else:
            audio_tags = ParsedTrackInfo.from_dict(_audio_tags)

        additional_file = d.pop("additionalFile", UNSET)

        replace_existing_files = d.pop("replaceExistingFiles", UNSET)

        disable_release_switching = d.pop("disableReleaseSwitching", UNSET)

        manual_import_resource = cls(
            id=id,
            path=path,
            name=name,
            size=size,
            artist=artist,
            album=album,
            album_release_id=album_release_id,
            tracks=tracks,
            quality=quality,
            release_group=release_group,
            quality_weight=quality_weight,
            download_id=download_id,
            indexer_flags=indexer_flags,
            rejections=rejections,
            audio_tags=audio_tags,
            additional_file=additional_file,
            replace_existing_files=replace_existing_files,
            disable_release_switching=disable_release_switching,
        )

        return manual_import_resource
