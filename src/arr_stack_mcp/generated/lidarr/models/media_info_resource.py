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
        audio_channels (Union[Unset, float]):
        audio_bit_rate (Union[None, Unset, str]):
        audio_codec (Union[None, Unset, str]):
        audio_bits (Union[None, Unset, str]):
        audio_sample_rate (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    audio_channels: Union[Unset, float] = UNSET
    audio_bit_rate: Union[None, Unset, str] = UNSET
    audio_codec: Union[None, Unset, str] = UNSET
    audio_bits: Union[None, Unset, str] = UNSET
    audio_sample_rate: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        audio_channels = self.audio_channels

        audio_bit_rate: Union[None, Unset, str]
        if isinstance(self.audio_bit_rate, Unset):
            audio_bit_rate = UNSET
        else:
            audio_bit_rate = self.audio_bit_rate

        audio_codec: Union[None, Unset, str]
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        audio_bits: Union[None, Unset, str]
        if isinstance(self.audio_bits, Unset):
            audio_bits = UNSET
        else:
            audio_bits = self.audio_bits

        audio_sample_rate: Union[None, Unset, str]
        if isinstance(self.audio_sample_rate, Unset):
            audio_sample_rate = UNSET
        else:
            audio_sample_rate = self.audio_sample_rate

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if audio_channels is not UNSET:
            field_dict["audioChannels"] = audio_channels
        if audio_bit_rate is not UNSET:
            field_dict["audioBitRate"] = audio_bit_rate
        if audio_codec is not UNSET:
            field_dict["audioCodec"] = audio_codec
        if audio_bits is not UNSET:
            field_dict["audioBits"] = audio_bits
        if audio_sample_rate is not UNSET:
            field_dict["audioSampleRate"] = audio_sample_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        audio_channels = d.pop("audioChannels", UNSET)

        def _parse_audio_bit_rate(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_bit_rate = _parse_audio_bit_rate(d.pop("audioBitRate", UNSET))

        def _parse_audio_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_codec = _parse_audio_codec(d.pop("audioCodec", UNSET))

        def _parse_audio_bits(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_bits = _parse_audio_bits(d.pop("audioBits", UNSET))

        def _parse_audio_sample_rate(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_sample_rate = _parse_audio_sample_rate(d.pop("audioSampleRate", UNSET))

        media_info_resource = cls(
            id=id,
            audio_channels=audio_channels,
            audio_bit_rate=audio_bit_rate,
            audio_codec=audio_codec,
            audio_bits=audio_bits,
            audio_sample_rate=audio_sample_rate,
        )

        return media_info_resource
