from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediumResource")


@_attrs_define
class MediumResource:
    """
    Attributes:
        medium_number (Union[Unset, int]):
        medium_name (Union[None, Unset, str]):
        medium_format (Union[None, Unset, str]):
    """

    medium_number: Union[Unset, int] = UNSET
    medium_name: Union[None, Unset, str] = UNSET
    medium_format: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        medium_number = self.medium_number

        medium_name: Union[None, Unset, str]
        if isinstance(self.medium_name, Unset):
            medium_name = UNSET
        else:
            medium_name = self.medium_name

        medium_format: Union[None, Unset, str]
        if isinstance(self.medium_format, Unset):
            medium_format = UNSET
        else:
            medium_format = self.medium_format

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if medium_number is not UNSET:
            field_dict["mediumNumber"] = medium_number
        if medium_name is not UNSET:
            field_dict["mediumName"] = medium_name
        if medium_format is not UNSET:
            field_dict["mediumFormat"] = medium_format

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        medium_number = d.pop("mediumNumber", UNSET)

        def _parse_medium_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        medium_name = _parse_medium_name(d.pop("mediumName", UNSET))

        def _parse_medium_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        medium_format = _parse_medium_format(d.pop("mediumFormat", UNSET))

        medium_resource = cls(
            medium_number=medium_number,
            medium_name=medium_name,
            medium_format=medium_format,
        )

        return medium_resource
