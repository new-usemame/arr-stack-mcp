from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncPlayQueueItem")


@_attrs_define
class SyncPlayQueueItem:
    """Class QueueItem.

    Attributes:
        item_id (Union[Unset, UUID]): Gets the item identifier.
        playlist_item_id (Union[Unset, UUID]): Gets the playlist identifier of the item.
    """

    item_id: Union[Unset, UUID] = UNSET
    playlist_item_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        item_id: Union[Unset, str] = UNSET
        if not isinstance(self.item_id, Unset):
            item_id = str(self.item_id)

        playlist_item_id: Union[Unset, str] = UNSET
        if not isinstance(self.playlist_item_id, Unset):
            playlist_item_id = str(self.playlist_item_id)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["ItemId"] = item_id
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _item_id = d.pop("ItemId", UNSET)
        item_id: Union[Unset, UUID]
        if isinstance(_item_id, Unset):
            item_id = UNSET
        else:
            item_id = UUID(_item_id)

        _playlist_item_id = d.pop("PlaylistItemId", UNSET)
        playlist_item_id: Union[Unset, UUID]
        if isinstance(_playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = UUID(_playlist_item_id)

        sync_play_queue_item = cls(
            item_id=item_id,
            playlist_item_id=playlist_item_id,
        )

        return sync_play_queue_item
