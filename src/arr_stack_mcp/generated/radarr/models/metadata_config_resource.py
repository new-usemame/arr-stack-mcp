from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.tm_db_country_code import TMDbCountryCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataConfigResource")


@_attrs_define
class MetadataConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        certification_country (Union[Unset, TMDbCountryCode]):
    """

    id: Union[Unset, int] = UNSET
    certification_country: Union[Unset, TMDbCountryCode] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        certification_country: Union[Unset, str] = UNSET
        if not isinstance(self.certification_country, Unset):
            certification_country = self.certification_country.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if certification_country is not UNSET:
            field_dict["certificationCountry"] = certification_country

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _certification_country = d.pop("certificationCountry", UNSET)
        certification_country: Union[Unset, TMDbCountryCode]
        if isinstance(_certification_country, Unset):
            certification_country = UNSET
        else:
            certification_country = TMDbCountryCode(_certification_country)

        metadata_config_resource = cls(
            id=id,
            certification_country=certification_country,
        )

        return metadata_config_resource
