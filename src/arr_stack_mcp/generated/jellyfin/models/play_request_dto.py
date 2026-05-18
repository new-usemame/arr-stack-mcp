from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayRequestDto")


@_attrs_define
class PlayRequestDto:
    """Class PlayRequestDto.

    Attributes:
        playing_queue (Union[Unset, list[UUID]]): Gets or sets the playing queue.
        playing_item_position (Union[Unset, int]): Gets or sets the position of the playing item in the queue.
        start_position_ticks (Union[Unset, int]): Gets or sets the start position ticks.
    """

    playing_queue: Union[Unset, list[UUID]] = UNSET
    playing_item_position: Union[Unset, int] = UNSET
    start_position_ticks: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        playing_queue: Union[Unset, list[str]] = UNSET
        if not isinstance(self.playing_queue, Unset):
            playing_queue = []
            for playing_queue_item_data in self.playing_queue:
                playing_queue_item = str(playing_queue_item_data)
                playing_queue.append(playing_queue_item)

        playing_item_position = self.playing_item_position

        start_position_ticks = self.start_position_ticks

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if playing_queue is not UNSET:
            field_dict["PlayingQueue"] = playing_queue
        if playing_item_position is not UNSET:
            field_dict["PlayingItemPosition"] = playing_item_position
        if start_position_ticks is not UNSET:
            field_dict["StartPositionTicks"] = start_position_ticks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        playing_queue = []
        _playing_queue = d.pop("PlayingQueue", UNSET)
        for playing_queue_item_data in _playing_queue or []:
            playing_queue_item = UUID(playing_queue_item_data)

            playing_queue.append(playing_queue_item)

        playing_item_position = d.pop("PlayingItemPosition", UNSET)

        start_position_ticks = d.pop("StartPositionTicks", UNSET)

        play_request_dto = cls(
            playing_queue=playing_queue,
            playing_item_position=playing_item_position,
            start_position_ticks=start_position_ticks,
        )

        return play_request_dto
