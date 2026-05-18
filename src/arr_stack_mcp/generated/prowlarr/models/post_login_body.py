from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostLoginBody")


@_attrs_define
class PostLoginBody:
    """
    Attributes:
        username (Union[Unset, str]):
        password (Union[Unset, str]):
        remember_me (Union[Unset, str]):
    """

    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    remember_me: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        remember_me = self.remember_me

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if remember_me is not UNSET:
            field_dict["rememberMe"] = remember_me

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        username = (
            self.username
            if isinstance(self.username, Unset)
            else (None, str(self.username).encode(), "text/plain")
        )

        password = (
            self.password
            if isinstance(self.password, Unset)
            else (None, str(self.password).encode(), "text/plain")
        )

        remember_me = (
            self.remember_me
            if isinstance(self.remember_me, Unset)
            else (None, str(self.remember_me).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if remember_me is not UNSET:
            field_dict["rememberMe"] = remember_me

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        remember_me = d.pop("rememberMe", UNSET)

        post_login_body = cls(
            username=username,
            password=password,
            remember_me=remember_me,
        )

        post_login_body.additional_properties = d
        return post_login_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
