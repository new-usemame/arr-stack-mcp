from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_filter_resource_filters_type_0_item import (
        CustomFilterResourceFiltersType0Item,
    )


T = TypeVar("T", bound="CustomFilterResource")


@_attrs_define
class CustomFilterResource:
    """
    Attributes:
        id (Union[Unset, int]):
        type_ (Union[None, Unset, str]):
        label (Union[None, Unset, str]):
        filters (Union[None, Unset, list['CustomFilterResourceFiltersType0Item']]):
    """

    id: Union[Unset, int] = UNSET
    type_: Union[None, Unset, str] = UNSET
    label: Union[None, Unset, str] = UNSET
    filters: Union[None, Unset, list["CustomFilterResourceFiltersType0Item"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        filters: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_filter_resource_filters_type_0_item import (
            CustomFilterResourceFiltersType0Item,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_filters(
            data: object,
        ) -> Union[None, Unset, list["CustomFilterResourceFiltersType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = (
                        CustomFilterResourceFiltersType0Item.from_dict(
                            filters_type_0_item_data
                        )
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["CustomFilterResourceFiltersType0Item"]], data
            )

        filters = _parse_filters(d.pop("filters", UNSET))

        custom_filter_resource = cls(
            id=id,
            type_=type_,
            label=label,
            filters=filters,
        )

        return custom_filter_resource
