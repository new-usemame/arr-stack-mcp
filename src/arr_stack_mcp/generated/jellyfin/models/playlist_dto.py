from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playlist_user_permissions import PlaylistUserPermissions


T = TypeVar("T", bound="PlaylistDto")


@_attrs_define
class PlaylistDto:
    """DTO for playlists.

    Attributes:
        open_access (Union[Unset, bool]): Gets or sets a value indicating whether the playlist is publicly readable.
        shares (Union[Unset, list['PlaylistUserPermissions']]): Gets or sets the share permissions.
        item_ids (Union[Unset, list[UUID]]): Gets or sets the item ids.
    """

    open_access: Union[Unset, bool] = UNSET
    shares: Union[Unset, list["PlaylistUserPermissions"]] = UNSET
    item_ids: Union[Unset, list[UUID]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        open_access = self.open_access

        shares: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shares, Unset):
            shares = []
            for shares_item_data in self.shares:
                shares_item = shares_item_data.to_dict()
                shares.append(shares_item)

        item_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = []
            for item_ids_item_data in self.item_ids:
                item_ids_item = str(item_ids_item_data)
                item_ids.append(item_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if open_access is not UNSET:
            field_dict["OpenAccess"] = open_access
        if shares is not UNSET:
            field_dict["Shares"] = shares
        if item_ids is not UNSET:
            field_dict["ItemIds"] = item_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        open_access = d.pop("OpenAccess", UNSET)

        shares = []
        _shares = d.pop("Shares", UNSET)
        for shares_item_data in _shares or []:
            shares_item = PlaylistUserPermissions.from_dict(shares_item_data)

            shares.append(shares_item)

        item_ids = []
        _item_ids = d.pop("ItemIds", UNSET)
        for item_ids_item_data in _item_ids or []:
            item_ids_item = UUID(item_ids_item_data)

            item_ids.append(item_ids_item)

        playlist_dto = cls(
            open_access=open_access,
            shares=shares,
            item_ids=item_ids,
        )

        return playlist_dto
