from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_info_dto import DeviceInfoDto


T = TypeVar("T", bound="DeviceInfoDtoQueryResult")


@_attrs_define
class DeviceInfoDtoQueryResult:
    """Query result container.

    Attributes:
        items (Union[Unset, list['DeviceInfoDto']]): Gets or sets the items.
        total_record_count (Union[Unset, int]): Gets or sets the total number of records available.
        start_index (Union[Unset, int]): Gets or sets the index of the first record in Items.
    """

    items: Union[Unset, list["DeviceInfoDto"]] = UNSET
    total_record_count: Union[Unset, int] = UNSET
    start_index: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        total_record_count = self.total_record_count

        start_index = self.start_index

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if items is not UNSET:
            field_dict["Items"] = items
        if total_record_count is not UNSET:
            field_dict["TotalRecordCount"] = total_record_count
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_info_dto import DeviceInfoDto

        d = dict(src_dict)
        items = []
        _items = d.pop("Items", UNSET)
        for items_item_data in _items or []:
            items_item = DeviceInfoDto.from_dict(items_item_data)

            items.append(items_item)

        total_record_count = d.pop("TotalRecordCount", UNSET)

        start_index = d.pop("StartIndex", UNSET)

        device_info_dto_query_result = cls(
            items=items,
            total_record_count=total_record_count,
            start_index=start_index,
        )

        return device_info_dto_query_result
