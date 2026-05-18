from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaInfoModel")


@_attrs_define
class MediaInfoModel:
    """
    Attributes:
        audio_format (Union[None, Unset, str]):
        audio_bitrate (Union[Unset, int]):
        audio_channels (Union[Unset, int]):
        audio_bits (Union[Unset, int]):
        audio_sample_rate (Union[Unset, int]):
    """

    audio_format: Union[None, Unset, str] = UNSET
    audio_bitrate: Union[Unset, int] = UNSET
    audio_channels: Union[Unset, int] = UNSET
    audio_bits: Union[Unset, int] = UNSET
    audio_sample_rate: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_format: Union[None, Unset, str]
        if isinstance(self.audio_format, Unset):
            audio_format = UNSET
        else:
            audio_format = self.audio_format

        audio_bitrate = self.audio_bitrate

        audio_channels = self.audio_channels

        audio_bits = self.audio_bits

        audio_sample_rate = self.audio_sample_rate

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if audio_format is not UNSET:
            field_dict["audioFormat"] = audio_format
        if audio_bitrate is not UNSET:
            field_dict["audioBitrate"] = audio_bitrate
        if audio_channels is not UNSET:
            field_dict["audioChannels"] = audio_channels
        if audio_bits is not UNSET:
            field_dict["audioBits"] = audio_bits
        if audio_sample_rate is not UNSET:
            field_dict["audioSampleRate"] = audio_sample_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_format = _parse_audio_format(d.pop("audioFormat", UNSET))

        audio_bitrate = d.pop("audioBitrate", UNSET)

        audio_channels = d.pop("audioChannels", UNSET)

        audio_bits = d.pop("audioBits", UNSET)

        audio_sample_rate = d.pop("audioSampleRate", UNSET)

        media_info_model = cls(
            audio_format=audio_format,
            audio_bitrate=audio_bitrate,
            audio_channels=audio_channels,
            audio_bits=audio_bits,
            audio_sample_rate=audio_sample_rate,
        )

        return media_info_model
