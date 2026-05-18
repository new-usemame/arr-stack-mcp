import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.media_info_resource import MediaInfoResource
    from ..models.parsed_track_info import ParsedTrackInfo
    from ..models.quality_model import QualityModel


T = TypeVar("T", bound="TrackFileResource")


@_attrs_define
class TrackFileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        artist_id (Union[Unset, int]):
        album_id (Union[Unset, int]):
        path (Union[None, Unset, str]):
        size (Union[Unset, int]):
        date_added (Union[Unset, datetime.datetime]):
        scene_name (Union[None, Unset, str]):
        release_group (Union[None, Unset, str]):
        quality (Union[Unset, QualityModel]):
        quality_weight (Union[Unset, int]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
        indexer_flags (Union[None, Unset, int]):
        media_info (Union[Unset, MediaInfoResource]):
        quality_cutoff_not_met (Union[Unset, bool]):
        audio_tags (Union[Unset, ParsedTrackInfo]):
    """

    id: Union[Unset, int] = UNSET
    artist_id: Union[Unset, int] = UNSET
    album_id: Union[Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    date_added: Union[Unset, datetime.datetime] = UNSET
    scene_name: Union[None, Unset, str] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    quality_weight: Union[Unset, int] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET
    indexer_flags: Union[None, Unset, int] = UNSET
    media_info: Union[Unset, "MediaInfoResource"] = UNSET
    quality_cutoff_not_met: Union[Unset, bool] = UNSET
    audio_tags: Union[Unset, "ParsedTrackInfo"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        artist_id = self.artist_id

        album_id = self.album_id

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        size = self.size

        date_added: Union[Unset, str] = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        scene_name: Union[None, Unset, str]
        if isinstance(self.scene_name, Unset):
            scene_name = UNSET
        else:
            scene_name = self.scene_name

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        quality_weight = self.quality_weight

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

        indexer_flags: Union[None, Unset, int]
        if isinstance(self.indexer_flags, Unset):
            indexer_flags = UNSET
        else:
            indexer_flags = self.indexer_flags

        media_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.media_info, Unset):
            media_info = self.media_info.to_dict()

        quality_cutoff_not_met = self.quality_cutoff_not_met

        audio_tags: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.audio_tags, Unset):
            audio_tags = self.audio_tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if artist_id is not UNSET:
            field_dict["artistId"] = artist_id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if path is not UNSET:
            field_dict["path"] = path
        if size is not UNSET:
            field_dict["size"] = size
        if date_added is not UNSET:
            field_dict["dateAdded"] = date_added
        if scene_name is not UNSET:
            field_dict["sceneName"] = scene_name
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if quality is not UNSET:
            field_dict["quality"] = quality
        if quality_weight is not UNSET:
            field_dict["qualityWeight"] = quality_weight
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score
        if indexer_flags is not UNSET:
            field_dict["indexerFlags"] = indexer_flags
        if media_info is not UNSET:
            field_dict["mediaInfo"] = media_info
        if quality_cutoff_not_met is not UNSET:
            field_dict["qualityCutoffNotMet"] = quality_cutoff_not_met
        if audio_tags is not UNSET:
            field_dict["audioTags"] = audio_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.media_info_resource import MediaInfoResource
        from ..models.parsed_track_info import ParsedTrackInfo
        from ..models.quality_model import QualityModel

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        artist_id = d.pop("artistId", UNSET)

        album_id = d.pop("albumId", UNSET)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        size = d.pop("size", UNSET)

        _date_added = d.pop("dateAdded", UNSET)
        date_added: Union[Unset, datetime.datetime]
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        def _parse_scene_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scene_name = _parse_scene_name(d.pop("sceneName", UNSET))

        def _parse_release_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_group = _parse_release_group(d.pop("releaseGroup", UNSET))

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        quality_weight = d.pop("qualityWeight", UNSET)

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

        def _parse_indexer_flags(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        indexer_flags = _parse_indexer_flags(d.pop("indexerFlags", UNSET))

        _media_info = d.pop("mediaInfo", UNSET)
        media_info: Union[Unset, MediaInfoResource]
        if isinstance(_media_info, Unset):
            media_info = UNSET
        else:
            media_info = MediaInfoResource.from_dict(_media_info)

        quality_cutoff_not_met = d.pop("qualityCutoffNotMet", UNSET)

        _audio_tags = d.pop("audioTags", UNSET)
        audio_tags: Union[Unset, ParsedTrackInfo]
        if isinstance(_audio_tags, Unset):
            audio_tags = UNSET
        else:
            audio_tags = ParsedTrackInfo.from_dict(_audio_tags)

        track_file_resource = cls(
            id=id,
            artist_id=artist_id,
            album_id=album_id,
            path=path,
            size=size,
            date_added=date_added,
            scene_name=scene_name,
            release_group=release_group,
            quality=quality,
            quality_weight=quality_weight,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
            indexer_flags=indexer_flags,
            media_info=media_info,
            quality_cutoff_not_met=quality_cutoff_not_met,
            audio_tags=audio_tags,
        )

        return track_file_resource
