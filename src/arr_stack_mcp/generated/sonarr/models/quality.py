from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.quality_source import QualitySource
from ..types import UNSET, Unset

T = TypeVar("T", bound="Quality")


@_attrs_define
class Quality:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        source (Union[Unset, QualitySource]):
        resolution (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    source: Union[Unset, QualitySource] = UNSET
    resolution: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        resolution = self.resolution

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if resolution is not UNSET:
            field_dict["resolution"] = resolution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _source = d.pop("source", UNSET)
        source: Union[Unset, QualitySource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = QualitySource(_source)

        resolution = d.pop("resolution", UNSET)

        quality = cls(
            id=id,
            name=name,
            source=source,
            resolution=resolution,
        )

        return quality
