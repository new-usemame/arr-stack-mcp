from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportListConfigResource")


@_attrs_define
class ImportListConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        list_sync_level (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    list_sync_level: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        list_sync_level: Union[None, Unset, str]
        if isinstance(self.list_sync_level, Unset):
            list_sync_level = UNSET
        else:
            list_sync_level = self.list_sync_level

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if list_sync_level is not UNSET:
            field_dict["listSyncLevel"] = list_sync_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_list_sync_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        list_sync_level = _parse_list_sync_level(d.pop("listSyncLevel", UNSET))

        import_list_config_resource = cls(
            id=id,
            list_sync_level=list_sync_level,
        )

        return import_list_config_resource
