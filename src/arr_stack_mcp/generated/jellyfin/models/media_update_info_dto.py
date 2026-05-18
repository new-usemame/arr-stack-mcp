from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_update_info_path_dto import MediaUpdateInfoPathDto


T = TypeVar("T", bound="MediaUpdateInfoDto")


@_attrs_define
class MediaUpdateInfoDto:
    """Media Update Info Dto.

    Attributes:
        updates (Union[Unset, list['MediaUpdateInfoPathDto']]): Gets or sets the list of updates.
    """

    updates: Union[Unset, list["MediaUpdateInfoPathDto"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        updates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.updates, Unset):
            updates = []
            for updates_item_data in self.updates:
                updates_item = updates_item_data.to_dict()
                updates.append(updates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if updates is not UNSET:
            field_dict["Updates"] = updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_update_info_path_dto import MediaUpdateInfoPathDto

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        updates = []
        _updates = d.pop("Updates", UNSET)
        for updates_item_data in _updates or []:
            updates_item = MediaUpdateInfoPathDto.from_dict(updates_item_data)

            updates.append(updates_item)

        media_update_info_dto = cls(
            updates=updates,
        )

        return media_update_info_dto
