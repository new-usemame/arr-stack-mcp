from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiInfoResource")


@_attrs_define
class ApiInfoResource:
    """
    Attributes:
        current (Union[None, Unset, str]):
        deprecated (Union[None, Unset, list[str]]):
    """

    current: Union[None, Unset, str] = UNSET
    deprecated: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        current: Union[None, Unset, str]
        if isinstance(self.current, Unset):
            current = UNSET
        else:
            current = self.current

        deprecated: Union[None, Unset, list[str]]
        if isinstance(self.deprecated, Unset):
            deprecated = UNSET
        elif isinstance(self.deprecated, list):
            deprecated = self.deprecated

        else:
            deprecated = self.deprecated

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if current is not UNSET:
            field_dict["current"] = current
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_current(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        current = _parse_current(d.pop("current", UNSET))

        def _parse_deprecated(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deprecated_type_0 = cast(list[str], data)

                return deprecated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        deprecated = _parse_deprecated(d.pop("deprecated", UNSET))

        api_info_resource = cls(
            current=current,
            deprecated=deprecated,
        )

        return api_info_resource
