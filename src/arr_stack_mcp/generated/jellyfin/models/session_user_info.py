from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionUserInfo")


@_attrs_define
class SessionUserInfo:
    """Class SessionUserInfo.

    Attributes:
        user_id (Union[Unset, UUID]): Gets or sets the user identifier.
        user_name (Union[None, Unset, str]): Gets or sets the name of the user.
    """

    user_id: Union[Unset, UUID] = UNSET
    user_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id: Union[Unset, str] = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _user_id = d.pop("UserId", UNSET)
        user_id: Union[Unset, UUID]
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("UserName", UNSET))

        session_user_info = cls(
            user_id=user_id,
            user_name=user_name,
        )

        return session_user_info
