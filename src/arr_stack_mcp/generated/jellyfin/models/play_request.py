from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.play_command import PlayCommand
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayRequest")


@_attrs_define
class PlayRequest:
    """Class PlayRequest.

    Attributes:
        item_ids (Union[None, Unset, list[UUID]]): Gets or sets the item ids.
        start_position_ticks (Union[None, Unset, int]): Gets or sets the start position ticks that the first item should
            be played at.
        play_command (Union[Unset, PlayCommand]): Enum PlayCommand.
        controlling_user_id (Union[Unset, UUID]): Gets or sets the controlling user identifier.
        subtitle_stream_index (Union[None, Unset, int]):
        audio_stream_index (Union[None, Unset, int]):
        media_source_id (Union[None, Unset, str]):
        start_index (Union[None, Unset, int]):
    """

    item_ids: Union[None, Unset, list[UUID]] = UNSET
    start_position_ticks: Union[None, Unset, int] = UNSET
    play_command: Union[Unset, PlayCommand] = UNSET
    controlling_user_id: Union[Unset, UUID] = UNSET
    subtitle_stream_index: Union[None, Unset, int] = UNSET
    audio_stream_index: Union[None, Unset, int] = UNSET
    media_source_id: Union[None, Unset, str] = UNSET
    start_index: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_ids: Union[None, Unset, list[str]]
        if isinstance(self.item_ids, Unset):
            item_ids = UNSET
        elif isinstance(self.item_ids, list):
            item_ids = []
            for item_ids_type_0_item_data in self.item_ids:
                item_ids_type_0_item = str(item_ids_type_0_item_data)
                item_ids.append(item_ids_type_0_item)

        else:
            item_ids = self.item_ids

        start_position_ticks: Union[None, Unset, int]
        if isinstance(self.start_position_ticks, Unset):
            start_position_ticks = UNSET
        else:
            start_position_ticks = self.start_position_ticks

        play_command: Union[Unset, str] = UNSET
        if not isinstance(self.play_command, Unset):
            play_command = self.play_command.value

        controlling_user_id: Union[Unset, str] = UNSET
        if not isinstance(self.controlling_user_id, Unset):
            controlling_user_id = str(self.controlling_user_id)

        subtitle_stream_index: Union[None, Unset, int]
        if isinstance(self.subtitle_stream_index, Unset):
            subtitle_stream_index = UNSET
        else:
            subtitle_stream_index = self.subtitle_stream_index

        audio_stream_index: Union[None, Unset, int]
        if isinstance(self.audio_stream_index, Unset):
            audio_stream_index = UNSET
        else:
            audio_stream_index = self.audio_stream_index

        media_source_id: Union[None, Unset, str]
        if isinstance(self.media_source_id, Unset):
            media_source_id = UNSET
        else:
            media_source_id = self.media_source_id

        start_index: Union[None, Unset, int]
        if isinstance(self.start_index, Unset):
            start_index = UNSET
        else:
            start_index = self.start_index

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks
        if play_command is not UNSET:
            field_dict["PlayCommand"] = play_command
        if controlling_user_id is not UNSET:
            field_dict["ControllingUserId"] = controlling_user_id
        if subtitle_stream_index is not UNSET:
            field_dict["SubtitleStreamIndex"] = subtitle_stream_index
        if audio_stream_index is not UNSET:
            field_dict["AudioStreamIndex"] = audio_stream_index
        if media_source_id is not UNSET:
            field_dict["MediaSourceId"] = media_source_id
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_item_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                item_ids_type_0 = []
                _item_ids_type_0 = data
                for item_ids_type_0_item_data in _item_ids_type_0:
                    item_ids_type_0_item = UUID(item_ids_type_0_item_data)

                    item_ids_type_0.append(item_ids_type_0_item)

                return item_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        item_ids = _parse_item_ids(d.pop("ItemIds", UNSET))

        def _parse_start_position_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        start_position_ticks = _parse_start_position_ticks(
            d.pop("StartPositionTicks", UNSET)
        )

        _play_command = d.pop("PlayCommand", UNSET)
        play_command: Union[Unset, PlayCommand]
        if isinstance(_play_command, Unset):
            play_command = UNSET
        else:
            play_command = PlayCommand(_play_command)

        _controlling_user_id = d.pop("ControllingUserId", UNSET)
        controlling_user_id: Union[Unset, UUID]
        if isinstance(_controlling_user_id, Unset):
            controlling_user_id = UNSET
        else:
            controlling_user_id = UUID(_controlling_user_id)

        def _parse_subtitle_stream_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        subtitle_stream_index = _parse_subtitle_stream_index(
            d.pop("SubtitleStreamIndex", UNSET)
        )

        def _parse_audio_stream_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        audio_stream_index = _parse_audio_stream_index(d.pop("AudioStreamIndex", UNSET))

        def _parse_media_source_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        media_source_id = _parse_media_source_id(d.pop("MediaSourceId", UNSET))

        def _parse_start_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        start_index = _parse_start_index(d.pop("StartIndex", UNSET))

        play_request = cls(
            item_ids=item_ids,
            start_position_ticks=start_position_ticks,
            play_command=play_command,
            controlling_user_id=controlling_user_id,
            subtitle_stream_index=subtitle_stream_index,
            audio_stream_index=audio_stream_index,
            media_source_id=media_source_id,
            start_index=start_index,
        )

        return play_request
