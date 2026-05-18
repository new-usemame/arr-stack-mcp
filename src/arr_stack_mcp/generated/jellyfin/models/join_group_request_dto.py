from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="JoinGroupRequestDto")


@_attrs_define
class JoinGroupRequestDto:
    """Class JoinGroupRequestDto.

    Attributes:
        group_id (Union[Unset, UUID]): Gets or sets the group identifier.
    """

    group_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id: Union[Unset, str] = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _group_id = d.pop("GroupId", UNSET)
        group_id: Union[Unset, UUID]
        if isinstance(_group_id, Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)

        join_group_request_dto = cls(
            group_id=group_id,
        )

        return join_group_request_dto
