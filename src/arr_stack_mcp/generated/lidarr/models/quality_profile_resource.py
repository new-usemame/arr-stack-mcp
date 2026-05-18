from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_format_item_resource import ProfileFormatItemResource
    from ..models.quality_profile_quality_item_resource import (
        QualityProfileQualityItemResource,
    )


T = TypeVar("T", bound="QualityProfileResource")


@_attrs_define
class QualityProfileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        upgrade_allowed (Union[Unset, bool]):
        cutoff (Union[Unset, int]):
        items (Union[None, Unset, list['QualityProfileQualityItemResource']]):
        min_format_score (Union[Unset, int]):
        cutoff_format_score (Union[Unset, int]):
        format_items (Union[None, Unset, list['ProfileFormatItemResource']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    upgrade_allowed: Union[Unset, bool] = UNSET
    cutoff: Union[Unset, int] = UNSET
    items: Union[None, Unset, list["QualityProfileQualityItemResource"]] = UNSET
    min_format_score: Union[Unset, int] = UNSET
    cutoff_format_score: Union[Unset, int] = UNSET
    format_items: Union[None, Unset, list["ProfileFormatItemResource"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        upgrade_allowed = self.upgrade_allowed

        cutoff = self.cutoff

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

        min_format_score = self.min_format_score

        cutoff_format_score = self.cutoff_format_score

        format_items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.format_items, Unset):
            format_items = UNSET
        elif isinstance(self.format_items, list):
            format_items = []
            for format_items_type_0_item_data in self.format_items:
                format_items_type_0_item = format_items_type_0_item_data.to_dict()
                format_items.append(format_items_type_0_item)

        else:
            format_items = self.format_items

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if upgrade_allowed is not UNSET:
            field_dict["upgradeAllowed"] = upgrade_allowed
        if cutoff is not UNSET:
            field_dict["cutoff"] = cutoff
        if items is not UNSET:
            field_dict["items"] = items
        if min_format_score is not UNSET:
            field_dict["minFormatScore"] = min_format_score
        if cutoff_format_score is not UNSET:
            field_dict["cutoffFormatScore"] = cutoff_format_score
        if format_items is not UNSET:
            field_dict["formatItems"] = format_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_format_item_resource import ProfileFormatItemResource
        from ..models.quality_profile_quality_item_resource import (
            QualityProfileQualityItemResource,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        upgrade_allowed = d.pop("upgradeAllowed", UNSET)

        cutoff = d.pop("cutoff", UNSET)

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

        min_format_score = d.pop("minFormatScore", UNSET)

        cutoff_format_score = d.pop("cutoffFormatScore", UNSET)

        def _parse_format_items(
            data: object,
        ) -> Union[None, Unset, list["ProfileFormatItemResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                format_items_type_0 = []
                _format_items_type_0 = data
                for format_items_type_0_item_data in _format_items_type_0:
                    format_items_type_0_item = ProfileFormatItemResource.from_dict(
                        format_items_type_0_item_data
                    )

                    format_items_type_0.append(format_items_type_0_item)

                return format_items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ProfileFormatItemResource"]], data)

        format_items = _parse_format_items(d.pop("formatItems", UNSET))

        quality_profile_resource = cls(
            id=id,
            name=name,
            upgrade_allowed=upgrade_allowed,
            cutoff=cutoff,
            items=items,
            min_format_score=min_format_score,
            cutoff_format_score=cutoff_format_score,
            format_items=format_items,
        )

        return quality_profile_resource
