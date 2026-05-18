from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.modifier import Modifier
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
        modifier (Union[Unset, Modifier]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    source: Union[Unset, QualitySource] = UNSET
    resolution: Union[Unset, int] = UNSET
    modifier: Union[Unset, Modifier] = UNSET

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

        modifier: Union[Unset, str] = UNSET
        if not isinstance(self.modifier, Unset):
            modifier = self.modifier.value

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
        if modifier is not UNSET:
            field_dict["modifier"] = modifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        _modifier = d.pop("modifier", UNSET)
        modifier: Union[Unset, Modifier]
        if isinstance(_modifier, Unset):
            modifier = UNSET
        else:
            modifier = Modifier(_modifier)

        quality = cls(
            id=id,
            name=name,
            source=source,
            resolution=resolution,
            modifier=modifier,
        )

        return quality
