from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateChanges")


@_attrs_define
class UpdateChanges:
    """
    Attributes:
        new (Union[None, Unset, list[str]]):
        fixed (Union[None, Unset, list[str]]):
    """

    new: Union[None, Unset, list[str]] = UNSET
    fixed: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        new: Union[None, Unset, list[str]]
        if isinstance(self.new, Unset):
            new = UNSET
        elif isinstance(self.new, list):
            new = self.new

        else:
            new = self.new

        fixed: Union[None, Unset, list[str]]
        if isinstance(self.fixed, Unset):
            fixed = UNSET
        elif isinstance(self.fixed, list):
            fixed = self.fixed

        else:
            fixed = self.fixed

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if new is not UNSET:
            field_dict["new"] = new
        if fixed is not UNSET:
            field_dict["fixed"] = fixed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_new(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                new_type_0 = cast(list[str], data)

                return new_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        new = _parse_new(d.pop("new", UNSET))

        def _parse_fixed(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fixed_type_0 = cast(list[str], data)

                return fixed_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        fixed = _parse_fixed(d.pop("fixed", UNSET))

        update_changes = cls(
            new=new,
            fixed=fixed,
        )

        return update_changes
