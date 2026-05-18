from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.apply_tags import ApplyTags
from ..models.new_item_monitor_types import NewItemMonitorTypes
from ..models.series_types import SeriesTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeriesEditorResource")


@_attrs_define
class SeriesEditorResource:
    """
    Attributes:
        series_ids (Union[None, Unset, list[int]]):
        monitored (Union[None, Unset, bool]):
        monitor_new_items (Union[Unset, NewItemMonitorTypes]):
        quality_profile_id (Union[None, Unset, int]):
        series_type (Union[Unset, SeriesTypes]):
        season_folder (Union[None, Unset, bool]):
        root_folder_path (Union[None, Unset, str]):
        tags (Union[None, Unset, list[int]]):
        apply_tags (Union[Unset, ApplyTags]):
        move_files (Union[Unset, bool]):
        delete_files (Union[Unset, bool]):
        add_import_list_exclusion (Union[Unset, bool]):
    """

    series_ids: Union[None, Unset, list[int]] = UNSET
    monitored: Union[None, Unset, bool] = UNSET
    monitor_new_items: Union[Unset, NewItemMonitorTypes] = UNSET
    quality_profile_id: Union[None, Unset, int] = UNSET
    series_type: Union[Unset, SeriesTypes] = UNSET
    season_folder: Union[None, Unset, bool] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    apply_tags: Union[Unset, ApplyTags] = UNSET
    move_files: Union[Unset, bool] = UNSET
    delete_files: Union[Unset, bool] = UNSET
    add_import_list_exclusion: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        series_ids: Union[None, Unset, list[int]]
        if isinstance(self.series_ids, Unset):
            series_ids = UNSET
        elif isinstance(self.series_ids, list):
            series_ids = self.series_ids

        else:
            series_ids = self.series_ids

        monitored: Union[None, Unset, bool]
        if isinstance(self.monitored, Unset):
            monitored = UNSET
        else:
            monitored = self.monitored

        monitor_new_items: Union[Unset, str] = UNSET
        if not isinstance(self.monitor_new_items, Unset):
            monitor_new_items = self.monitor_new_items.value

        quality_profile_id: Union[None, Unset, int]
        if isinstance(self.quality_profile_id, Unset):
            quality_profile_id = UNSET
        else:
            quality_profile_id = self.quality_profile_id

        series_type: Union[Unset, str] = UNSET
        if not isinstance(self.series_type, Unset):
            series_type = self.series_type.value

        season_folder: Union[None, Unset, bool]
        if isinstance(self.season_folder, Unset):
            season_folder = UNSET
        else:
            season_folder = self.season_folder

        root_folder_path: Union[None, Unset, str]
        if isinstance(self.root_folder_path, Unset):
            root_folder_path = UNSET
        else:
            root_folder_path = self.root_folder_path

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        apply_tags: Union[Unset, str] = UNSET
        if not isinstance(self.apply_tags, Unset):
            apply_tags = self.apply_tags.value

        move_files = self.move_files

        delete_files = self.delete_files

        add_import_list_exclusion = self.add_import_list_exclusion

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if series_ids is not UNSET:
            field_dict["seriesIds"] = series_ids
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if monitor_new_items is not UNSET:
            field_dict["monitorNewItems"] = monitor_new_items
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id
        if series_type is not UNSET:
            field_dict["seriesType"] = series_type
        if season_folder is not UNSET:
            field_dict["seasonFolder"] = season_folder
        if root_folder_path is not UNSET:
            field_dict["rootFolderPath"] = root_folder_path
        if tags is not UNSET:
            field_dict["tags"] = tags
        if apply_tags is not UNSET:
            field_dict["applyTags"] = apply_tags
        if move_files is not UNSET:
            field_dict["moveFiles"] = move_files
        if delete_files is not UNSET:
            field_dict["deleteFiles"] = delete_files
        if add_import_list_exclusion is not UNSET:
            field_dict["addImportListExclusion"] = add_import_list_exclusion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_series_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_ids_type_0 = cast(list[int], data)

                return series_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        series_ids = _parse_series_ids(d.pop("seriesIds", UNSET))

        def _parse_monitored(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        monitored = _parse_monitored(d.pop("monitored", UNSET))

        _monitor_new_items = d.pop("monitorNewItems", UNSET)
        monitor_new_items: Union[Unset, NewItemMonitorTypes]
        if isinstance(_monitor_new_items, Unset):
            monitor_new_items = UNSET
        else:
            monitor_new_items = NewItemMonitorTypes(_monitor_new_items)

        def _parse_quality_profile_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quality_profile_id = _parse_quality_profile_id(d.pop("qualityProfileId", UNSET))

        _series_type = d.pop("seriesType", UNSET)
        series_type: Union[Unset, SeriesTypes]
        if isinstance(_series_type, Unset):
            series_type = UNSET
        else:
            series_type = SeriesTypes(_series_type)

        def _parse_season_folder(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        season_folder = _parse_season_folder(d.pop("seasonFolder", UNSET))

        def _parse_root_folder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_folder_path = _parse_root_folder_path(d.pop("rootFolderPath", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        _apply_tags = d.pop("applyTags", UNSET)
        apply_tags: Union[Unset, ApplyTags]
        if isinstance(_apply_tags, Unset):
            apply_tags = UNSET
        else:
            apply_tags = ApplyTags(_apply_tags)

        move_files = d.pop("moveFiles", UNSET)

        delete_files = d.pop("deleteFiles", UNSET)

        add_import_list_exclusion = d.pop("addImportListExclusion", UNSET)

        series_editor_resource = cls(
            series_ids=series_ids,
            monitored=monitored,
            monitor_new_items=monitor_new_items,
            quality_profile_id=quality_profile_id,
            series_type=series_type,
            season_folder=season_folder,
            root_folder_path=root_folder_path,
            tags=tags,
            apply_tags=apply_tags,
            move_files=move_files,
            delete_files=delete_files,
            add_import_list_exclusion=add_import_list_exclusion,
        )

        return series_editor_resource
