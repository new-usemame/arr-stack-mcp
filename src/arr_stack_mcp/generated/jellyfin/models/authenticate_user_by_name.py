from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticateUserByName")


@_attrs_define
class AuthenticateUserByName:
    """The authenticate user by name request body.

    Attributes:
        username (Union[None, Unset, str]): Gets or sets the username.
        pw (Union[None, Unset, str]): Gets or sets the plain text password.
    """

    username: Union[None, Unset, str] = UNSET
    pw: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        pw: Union[None, Unset, str]
        if isinstance(self.pw, Unset):
            pw = UNSET
        else:
            pw = self.pw

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if username is not UNSET:
            field_dict["Username"] = username
        if pw is not UNSET:
            field_dict["Pw"] = pw

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("Username", UNSET))

        def _parse_pw(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pw = _parse_pw(d.pop("Pw", UNSET))

        authenticate_user_by_name = cls(
            username=username,
            pw=pw,
        )

        return authenticate_user_by_name
