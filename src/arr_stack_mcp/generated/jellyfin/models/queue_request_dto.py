from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.group_queue_mode import GroupQueueMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueRequestDto")


@_attrs_define
class QueueRequestDto:
    """Class QueueRequestDto.

    Attributes:
        item_ids (Union[Unset, list[UUID]]): Gets or sets the items to enqueue.
        mode (Union[Unset, GroupQueueMode]): Enum GroupQueueMode.
    """

    item_ids: Union[Unset, list[UUID]] = UNSET
    mode: Union[Unset, GroupQueueMode] = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = []
            for item_ids_item_data in self.item_ids:
                item_ids_item = str(item_ids_item_data)
                item_ids.append(item_ids_item)

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        item_ids = []
        _item_ids = d.pop("ItemIds", UNSET)
        for item_ids_item_data in _item_ids or []:
            item_ids_item = UUID(item_ids_item_data)

            item_ids.append(item_ids_item)

        _mode = d.pop("Mode", UNSET)
        mode: Union[Unset, GroupQueueMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GroupQueueMode(_mode)

        queue_request_dto = cls(
            item_ids=item_ids,
            mode=mode,
        )

        return queue_request_dto
