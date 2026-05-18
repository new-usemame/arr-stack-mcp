from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.group_update_type import GroupUpdateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncPlayGroupDoesNotExistUpdate")


@_attrs_define
class SyncPlayGroupDoesNotExistUpdate:
    """
    Attributes:
        group_id (Union[Unset, UUID]): Gets the group identifier.
        data (Union[Unset, str]): Gets the update data.
        type_ (Union[Unset, GroupUpdateType]): Enum GroupUpdateType. Default: GroupUpdateType.GROUPDOESNOTEXIST.
    """

    group_id: Union[Unset, UUID] = UNSET
    data: Union[Unset, str] = UNSET
    type_: Union[Unset, GroupUpdateType] = GroupUpdateType.GROUPDOESNOTEXIST

    def to_dict(self) -> dict[str, Any]:
        group_id: Union[Unset, str] = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        data = self.data

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id
        if data is not UNSET:
            field_dict["Data"] = data
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _group_id = d.pop("GroupId", UNSET)
        group_id: Union[Unset, UUID]
        if isinstance(_group_id, Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)

        data = d.pop("Data", UNSET)

        _type_ = d.pop("Type", UNSET)
        type_: Union[Unset, GroupUpdateType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GroupUpdateType(_type_)

        sync_play_group_does_not_exist_update = cls(
            group_id=group_id,
            data=data,
            type_=type_,
        )

        return sync_play_group_does_not_exist_update
