from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality import Quality


T = TypeVar("T", bound="QualityProfileQualityItemResource")


@_attrs_define
class QualityProfileQualityItemResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        quality (Union[Unset, Quality]):
        items (Union[None, Unset, list['QualityProfileQualityItemResource']]):
        allowed (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    quality: Union[Unset, "Quality"] = UNSET
    items: Union[None, Unset, list["QualityProfileQualityItemResource"]] = UNSET
    allowed: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        allowed = self.allowed

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if quality is not UNSET:
            field_dict["quality"] = quality
        if items is not UNSET:
            field_dict["items"] = items
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quality import Quality

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, Quality]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = Quality.from_dict(_quality)

        def _parse_items(
            data: object,
        ) -> Union[None, Unset, list["QualityProfileQualityItemResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = QualityProfileQualityItemResource.from_dict(
                        items_type_0_item_data
                    )

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["QualityProfileQualityItemResource"]], data
            )

        items = _parse_items(d.pop("items", UNSET))

        allowed = d.pop("allowed", UNSET)

        quality_profile_quality_item_resource = cls(
            id=id,
            name=name,
            quality=quality,
            items=items,
            allowed=allowed,
        )

        return quality_profile_quality_item_resource
