from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectPlayProfile")


@_attrs_define
class DirectPlayProfile:
    """Defines the MediaBrowser.Model.Dlna.DirectPlayProfile.

    Attributes:
        container (Union[Unset, str]): Gets or sets the container.
        audio_codec (Union[None, Unset, str]): Gets or sets the audio codec.
        video_codec (Union[None, Unset, str]): Gets or sets the video codec.
        type_ (Union[Unset, DlnaProfileType]):
    """

    container: Union[Unset, str] = UNSET
    audio_codec: Union[None, Unset, str] = UNSET
    video_codec: Union[None, Unset, str] = UNSET
    type_: Union[Unset, DlnaProfileType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        container = self.container

        audio_codec: Union[None, Unset, str]
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        video_codec: Union[None, Unset, str]
        if isinstance(self.video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = self.video_codec

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if container is not UNSET:
            field_dict["Container"] = container
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        container = d.pop("Container", UNSET)

        def _parse_audio_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        audio_codec = _parse_audio_codec(d.pop("AudioCodec", UNSET))

        def _parse_video_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        video_codec = _parse_video_codec(d.pop("VideoCodec", UNSET))

        _type_ = d.pop("Type", UNSET)
        type_: Union[Unset, DlnaProfileType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DlnaProfileType(_type_)

        direct_play_profile = cls(
            container=container,
            audio_codec=audio_codec,
            video_codec=video_codec,
            type_=type_,
        )

        return direct_play_profile
