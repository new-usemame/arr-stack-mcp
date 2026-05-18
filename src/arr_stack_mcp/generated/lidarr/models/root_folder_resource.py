from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.monitor_types import MonitorTypes
from ..models.new_item_monitor_types import NewItemMonitorTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="RootFolderResource")


@_attrs_define
class RootFolderResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        default_metadata_profile_id (Union[Unset, int]):
        default_quality_profile_id (Union[Unset, int]):
        default_monitor_option (Union[Unset, MonitorTypes]):
        default_new_item_monitor_option (Union[Unset, NewItemMonitorTypes]):
        default_tags (Union[None, Unset, list[int]]):
        accessible (Union[Unset, bool]):
        free_space (Union[None, Unset, int]):
        total_space (Union[None, Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    default_metadata_profile_id: Union[Unset, int] = UNSET
    default_quality_profile_id: Union[Unset, int] = UNSET
    default_monitor_option: Union[Unset, MonitorTypes] = UNSET
    default_new_item_monitor_option: Union[Unset, NewItemMonitorTypes] = UNSET
    default_tags: Union[None, Unset, list[int]] = UNSET
    accessible: Union[Unset, bool] = UNSET
    free_space: Union[None, Unset, int] = UNSET
    total_space: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        default_metadata_profile_id = self.default_metadata_profile_id

        default_quality_profile_id = self.default_quality_profile_id

        default_monitor_option: Union[Unset, str] = UNSET
        if not isinstance(self.default_monitor_option, Unset):
            default_monitor_option = self.default_monitor_option.value

        default_new_item_monitor_option: Union[Unset, str] = UNSET
        if not isinstance(self.default_new_item_monitor_option, Unset):
            default_new_item_monitor_option = self.default_new_item_monitor_option.value

        default_tags: Union[None, Unset, list[int]]
        if isinstance(self.default_tags, Unset):
            default_tags = UNSET
        elif isinstance(self.default_tags, list):
            default_tags = self.default_tags

        else:
            default_tags = self.default_tags

        accessible = self.accessible

        free_space: Union[None, Unset, int]
        if isinstance(self.free_space, Unset):
            free_space = UNSET
        else:
            free_space = self.free_space

        total_space: Union[None, Unset, int]
        if isinstance(self.total_space, Unset):
            total_space = UNSET
        else:
            total_space = self.total_space

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if default_metadata_profile_id is not UNSET:
            field_dict["defaultMetadataProfileId"] = default_metadata_profile_id
        if default_quality_profile_id is not UNSET:
            field_dict["defaultQualityProfileId"] = default_quality_profile_id
        if default_monitor_option is not UNSET:
            field_dict["defaultMonitorOption"] = default_monitor_option
        if default_new_item_monitor_option is not UNSET:
            field_dict["defaultNewItemMonitorOption"] = default_new_item_monitor_option
        if default_tags is not UNSET:
            field_dict["defaultTags"] = default_tags
        if accessible is not UNSET:
            field_dict["accessible"] = accessible
        if free_space is not UNSET:
            field_dict["freeSpace"] = free_space
        if total_space is not UNSET:
            field_dict["totalSpace"] = total_space

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

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        default_metadata_profile_id = d.pop("defaultMetadataProfileId", UNSET)

        default_quality_profile_id = d.pop("defaultQualityProfileId", UNSET)

        _default_monitor_option = d.pop("defaultMonitorOption", UNSET)
        default_monitor_option: Union[Unset, MonitorTypes]
        if isinstance(_default_monitor_option, Unset):
            default_monitor_option = UNSET
        else:
            default_monitor_option = MonitorTypes(_default_monitor_option)

        _default_new_item_monitor_option = d.pop("defaultNewItemMonitorOption", UNSET)
        default_new_item_monitor_option: Union[Unset, NewItemMonitorTypes]
        if isinstance(_default_new_item_monitor_option, Unset):
            default_new_item_monitor_option = UNSET
        else:
            default_new_item_monitor_option = NewItemMonitorTypes(
                _default_new_item_monitor_option
            )

        def _parse_default_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                default_tags_type_0 = cast(list[int], data)

                return default_tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        default_tags = _parse_default_tags(d.pop("defaultTags", UNSET))

        accessible = d.pop("accessible", UNSET)

        def _parse_free_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space = _parse_free_space(d.pop("freeSpace", UNSET))

        def _parse_total_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_space = _parse_total_space(d.pop("totalSpace", UNSET))

        root_folder_resource = cls(
            id=id,
            name=name,
            path=path,
            default_metadata_profile_id=default_metadata_profile_id,
            default_quality_profile_id=default_quality_profile_id,
            default_monitor_option=default_monitor_option,
            default_new_item_monitor_option=default_new_item_monitor_option,
            default_tags=default_tags,
            accessible=accessible,
            free_space=free_space,
            total_space=total_space,
        )

        return root_folder_resource
