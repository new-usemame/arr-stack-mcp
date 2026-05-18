from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaInfoResource")


@_attrs_define
class MediaInfoResource:
    """
    Attributes:
        id (Union[Unset, int]):
        audio_bitrate (Union[Unset, int]):
        audio_channels (Union[Unset, float]):
        audio_codec (Union[None, Unset, str]):
        audio_languages (Union[None, Unset, str]):
        audio_stream_count (Union[Unset, int]):
        video_bit_depth (Union[Unset, int]):
        video_bitrate (Union[Unset, int]):
        video_codec (Union[None, Unset, str]):
        video_fps (Union[Unset, float]):
        video_dynamic_range (Union[None, Unset, str]):
        video_dynamic_range_type (Union[None, Unset, str]):
        resolution (Union[None, Unset, str]):
        run_time (Union[None, Unset, str]):
        scan_type (Union[None, Unset, str]):
        subtitles (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    audio_bitrate: Union[Unset, int] = UNSET
    audio_channels: Union[Unset, float] = UNSET
    audio_codec: Union[None, Unset, str] = UNSET
    audio_languages: Union[None, Unset, str] = UNSET
    audio_stream_count: Union[Unset, int] = UNSET
    video_bit_depth: Union[Unset, int] = UNSET
    video_bitrate: Union[Unset, int] = UNSET
    video_codec: Union[None, Unset, str] = UNSET
    video_fps: Union[Unset, float] = UNSET
    video_dynamic_range: Union[None, Unset, str] = UNSET
    video_dynamic_range_type: Union[None, Unset, str] = UNSET
    resolution: Union[None, Unset, str] = UNSET
    run_time: Union[None, Unset, str] = UNSET
    scan_type: Union[None, Unset, str] = UNSET
    subtitles: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        audio_bitrate = self.audio_bitrate

        audio_channels = self.audio_channels

        audio_codec: Union[None, Unset, str]
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        audio_languages: Union[None, Unset, str]
        if isinstance(self.audio_languages, Unset):
            audio_languages = UNSET
        else:
            audio_languages = self.audio_languages

        audio_stream_count = self.audio_stream_count

        video_bit_depth = self.video_bit_depth

        video_bitrate = self.video_bitrate

        video_codec: Union[None, Unset, str]
        if isinstance(self.video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = self.video_codec

        video_fps = self.video_fps

        video_dynamic_range: Union[None, Unset, str]
        if isinstance(self.video_dynamic_range, Unset):
            video_dynamic_range = UNSET
        else:
            video_dynamic_range = self.video_dynamic_range

        video_dynamic_range_type: Union[None, Unset, str]
        if isinstance(self.video_dynamic_range_type, Unset):
            video_dynamic_range_type = UNSET
        else:
            video_dynamic_range_type = self.video_dynamic_range_type

        resolution: Union[None, Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        else:
            resolution = self.resolution

        run_time: Union[None, Unset, str]
        if isinstance(self.run_time, Unset):
            run_time = UNSET
        else:
            run_time = self.run_time

        scan_type: Union[None, Unset, str]
        if isinstance(self.scan_type, Unset):
            scan_type = UNSET
        else:
            scan_type = self.scan_type

        subtitles: Union[None, Unset, str]
        if isinstance(self.subtitles, Unset):
            subtitles = UNSET
        else:
            subtitles = self.subtitles

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if audio_bitrate is not UNSET:
            field_dict["audioBitrate"] = audio_bitrate
        if audio_channels is not UNSET:
            field_dict["audioChannels"] = audio_channels
        if audio_codec is not UNSET:
            field_dict["audioCodec"] = audio_codec
        if audio_languages is not UNSET:
            field_dict["audioLanguages"] = audio_languages
        if audio_stream_count is not UNSET:
            field_dict["audioStreamCount"] = audio_stream_count
        if video_bit_depth is not UNSET:
            field_dict["videoBitDepth"] = video_bit_depth
        if video_bitrate is not UNSET:
            field_dict["videoBitrate"] = video_bitrate
        if video_codec is not UNSET:
            field_dict["videoCodec"] = video_codec
        if video_fps is not UNSET:
            field_dict["videoFps"] = video_fps
        if video_dynamic_range is not UNSET:
            field_dict["videoDynamicRange"] = video_dynamic_range
        if video_dynamic_range_type is not UNSET:
            field_dict["videoDynamicRangeType"] = video_dynamic_range_type
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if run_time is not UNSET:
            field_dict["runTime"] = run_time
        if scan_type is not UNSET:
            field_dict["scanType"] = scan_type
        if subtitles is not UNSET:
            field_dict["subtitles"] = subtitles

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        audio_bitrate = d.pop("audioBitrate", UNSET)

        audio_channels = d.pop("audioChannels", UNSET)

        def _parse_audio_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_codec = _parse_audio_codec(d.pop("audioCodec", UNSET))

        def _parse_audio_languages(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_languages = _parse_audio_languages(d.pop("audioLanguages", UNSET))

        audio_stream_count = d.pop("audioStreamCount", UNSET)

        video_bit_depth = d.pop("videoBitDepth", UNSET)

        video_bitrate = d.pop("videoBitrate", UNSET)

        def _parse_video_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_codec = _parse_video_codec(d.pop("videoCodec", UNSET))

        video_fps = d.pop("videoFps", UNSET)

        def _parse_video_dynamic_range(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_dynamic_range = _parse_video_dynamic_range(
            d.pop("videoDynamicRange", UNSET)
        )

        def _parse_video_dynamic_range_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_dynamic_range_type = _parse_video_dynamic_range_type(
            d.pop("videoDynamicRangeType", UNSET)
        )

        def _parse_resolution(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_run_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        run_time = _parse_run_time(d.pop("runTime", UNSET))

        def _parse_scan_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scan_type = _parse_scan_type(d.pop("scanType", UNSET))

        def _parse_subtitles(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subtitles = _parse_subtitles(d.pop("subtitles", UNSET))

        media_info_resource = cls(
            id=id,
            audio_bitrate=audio_bitrate,
            audio_channels=audio_channels,
            audio_codec=audio_codec,
            audio_languages=audio_languages,
            audio_stream_count=audio_stream_count,
            video_bit_depth=video_bit_depth,
            video_bitrate=video_bitrate,
            video_codec=video_codec,
            video_fps=video_fps,
            video_dynamic_range=video_dynamic_range,
            video_dynamic_range_type=video_dynamic_range_type,
            resolution=resolution,
            run_time=run_time,
            scan_type=scan_type,
            subtitles=subtitles,
        )

        return media_info_resource
