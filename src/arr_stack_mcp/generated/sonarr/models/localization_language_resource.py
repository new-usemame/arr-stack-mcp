from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalizationLanguageResource")


@_attrs_define
class LocalizationLanguageResource:
    """
    Attributes:
        identifier (Union[None, Unset, str]):
    """

    identifier: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        identifier: Union[None, Unset, str]
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        localization_language_resource = cls(
            identifier=identifier,
        )

        return localization_language_resource
