from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagDifference")


@_attrs_define
class TagDifference:
    """
    Attributes:
        field (Union[None, Unset, str]):
        old_value (Union[None, Unset, str]):
        new_value (Union[None, Unset, str]):
    """

    field: Union[None, Unset, str] = UNSET
    old_value: Union[None, Unset, str] = UNSET
    new_value: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        field: Union[None, Unset, str]
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        old_value: Union[None, Unset, str]
        if isinstance(self.old_value, Unset):
            old_value = UNSET
        else:
            old_value = self.old_value

        new_value: Union[None, Unset, str]
        if isinstance(self.new_value, Unset):
            new_value = UNSET
        else:
            new_value = self.new_value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if new_value is not UNSET:
            field_dict["newValue"] = new_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_field(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        field = _parse_field(d.pop("field", UNSET))

        def _parse_old_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        old_value = _parse_old_value(d.pop("oldValue", UNSET))

        def _parse_new_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        new_value = _parse_new_value(d.pop("newValue", UNSET))

        tag_difference = cls(
            field=field,
            old_value=old_value,
            new_value=new_value,
        )

        return tag_difference
