from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IsoCountry")


@_attrs_define
class IsoCountry:
    """
    Attributes:
        two_letter_code (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
    """

    two_letter_code: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        two_letter_code: Union[None, Unset, str]
        if isinstance(self.two_letter_code, Unset):
            two_letter_code = UNSET
        else:
            two_letter_code = self.two_letter_code

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if two_letter_code is not UNSET:
            field_dict["twoLetterCode"] = two_letter_code
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_two_letter_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        two_letter_code = _parse_two_letter_code(d.pop("twoLetterCode", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        iso_country = cls(
            two_letter_code=two_letter_code,
            name=name,
        )

        return iso_country
