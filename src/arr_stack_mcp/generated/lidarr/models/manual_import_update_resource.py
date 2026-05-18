from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality_model import QualityModel
    from ..models.rejection import Rejection
    from ..models.track_resource import TrackResource


T = TypeVar("T", bound="ManualImportUpdateResource")


@_attrs_define
class ManualImportUpdateResource:
    """
    Attributes:
        id (Union[Unset, int]):
        path (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        artist_id (Union[None, Unset, int]):
        album_id (Union[None, Unset, int]):
        album_release_id (Union[None, Unset, int]):
        tracks (Union[None, Unset, list['TrackResource']]):
        track_ids (Union[None, Unset, list[int]]):
        quality (Union[Unset, QualityModel]):
        release_group (Union[None, Unset, str]):
        indexer_flags (Union[Unset, int]):
        download_id (Union[None, Unset, str]):
        additional_file (Union[Unset, bool]):
        replace_existing_files (Union[Unset, bool]):
        disable_release_switching (Union[Unset, bool]):
        rejections (Union[None, Unset, list['Rejection']]):
    """

    id: Union[Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    artist_id: Union[None, Unset, int] = UNSET
    album_id: Union[None, Unset, int] = UNSET
    album_release_id: Union[None, Unset, int] = UNSET
    tracks: Union[None, Unset, list["TrackResource"]] = UNSET
    track_ids: Union[None, Unset, list[int]] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    indexer_flags: Union[Unset, int] = UNSET
    download_id: Union[None, Unset, str] = UNSET
    additional_file: Union[Unset, bool] = UNSET
    replace_existing_files: Union[Unset, bool] = UNSET
    disable_release_switching: Union[Unset, bool] = UNSET
    rejections: Union[None, Unset, list["Rejection"]] = UNSET

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

        album_release_id: Union[None, Unset, int]
        if isinstance(self.album_release_id, Unset):
            album_release_id = UNSET
        else:
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

        track_ids: Union[None, Unset, list[int]]
        if isinstance(self.track_ids, Unset):
            track_ids = UNSET
        elif isinstance(self.track_ids, list):
            track_ids = self.track_ids

        else:
            track_ids = self.track_ids

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

        indexer_flags = self.indexer_flags

        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        additional_file = self.additional_file

        replace_existing_files = self.replace_existing_files

        disable_release_switching = self.disable_release_switching

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

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path
        if name is not UNSET:
            field_dict["name"] = name
        if artist_id is not UNSET:
            field_dict["artistId"] = artist_id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if album_release_id is not UNSET:
            field_dict["albumReleaseId"] = album_release_id
        if tracks is not UNSET:
            field_dict["tracks"] = tracks
        if track_ids is not UNSET:
            field_dict["trackIds"] = track_ids
        if quality is not UNSET:
            field_dict["quality"] = quality
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if indexer_flags is not UNSET:
            field_dict["indexerFlags"] = indexer_flags
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if additional_file is not UNSET:
            field_dict["additionalFile"] = additional_file
        if replace_existing_files is not UNSET:
            field_dict["replaceExistingFiles"] = replace_existing_files
        if disable_release_switching is not UNSET:
            field_dict["disableReleaseSwitching"] = disable_release_switching
        if rejections is not UNSET:
            field_dict["rejections"] = rejections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        def _parse_album_release_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        album_release_id = _parse_album_release_id(d.pop("albumReleaseId", UNSET))

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

        def _parse_track_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                track_ids_type_0 = cast(list[int], data)

                return track_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        track_ids = _parse_track_ids(d.pop("trackIds", UNSET))

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

        indexer_flags = d.pop("indexerFlags", UNSET)

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        additional_file = d.pop("additionalFile", UNSET)

        replace_existing_files = d.pop("replaceExistingFiles", UNSET)

        disable_release_switching = d.pop("disableReleaseSwitching", UNSET)

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

        manual_import_update_resource = cls(
            id=id,
            path=path,
            name=name,
            artist_id=artist_id,
            album_id=album_id,
            album_release_id=album_release_id,
            tracks=tracks,
            track_ids=track_ids,
            quality=quality,
            release_group=release_group,
            indexer_flags=indexer_flags,
            download_id=download_id,
            additional_file=additional_file,
            replace_existing_files=replace_existing_files,
            disable_release_switching=disable_release_switching,
            rejections=rejections,
        )

        return manual_import_update_resource
