from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDatabaseOption")


@_attrs_define
class CustomDatabaseOption:
    """The custom value option for custom database providers.

    Attributes:
        key (Union[Unset, str]): Gets or sets the key of the value.
        value (Union[Unset, str]): Gets or sets the value.
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if key is not UNSET:
            field_dict["Key"] = key
        if value is not UNSET:
            field_dict["Value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        key = d.pop("Key", UNSET)

        value = d.pop("Value", UNSET)

        custom_database_option = cls(
            key=key,
            value=value,
        )

        return custom_database_option
