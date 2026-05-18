from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.apply_tags import ApplyTags
from ..models.new_item_monitor_types import NewItemMonitorTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtistEditorResource")


@_attrs_define
class ArtistEditorResource:
    """
    Attributes:
        artist_ids (Union[None, Unset, list[int]]):
        monitored (Union[None, Unset, bool]):
        monitor_new_items (Union[Unset, NewItemMonitorTypes]):
        quality_profile_id (Union[None, Unset, int]):
        metadata_profile_id (Union[None, Unset, int]):
        root_folder_path (Union[None, Unset, str]):
        tags (Union[None, Unset, list[int]]):
        apply_tags (Union[Unset, ApplyTags]):
        move_files (Union[Unset, bool]):
        delete_files (Union[Unset, bool]):
        add_import_list_exclusion (Union[Unset, bool]):
    """

    artist_ids: Union[None, Unset, list[int]] = UNSET
    monitored: Union[None, Unset, bool] = UNSET
    monitor_new_items: Union[Unset, NewItemMonitorTypes] = UNSET
    quality_profile_id: Union[None, Unset, int] = UNSET
    metadata_profile_id: Union[None, Unset, int] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    apply_tags: Union[Unset, ApplyTags] = UNSET
    move_files: Union[Unset, bool] = UNSET
    delete_files: Union[Unset, bool] = UNSET
    add_import_list_exclusion: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        artist_ids: Union[None, Unset, list[int]]
        if isinstance(self.artist_ids, Unset):
            artist_ids = UNSET
        elif isinstance(self.artist_ids, list):
            artist_ids = self.artist_ids

        else:
            artist_ids = self.artist_ids

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

        metadata_profile_id: Union[None, Unset, int]
        if isinstance(self.metadata_profile_id, Unset):
            metadata_profile_id = UNSET
        else:
            metadata_profile_id = self.metadata_profile_id

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
        if artist_ids is not UNSET:
            field_dict["artistIds"] = artist_ids
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if monitor_new_items is not UNSET:
            field_dict["monitorNewItems"] = monitor_new_items
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id
        if metadata_profile_id is not UNSET:
            field_dict["metadataProfileId"] = metadata_profile_id
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
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_artist_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                artist_ids_type_0 = cast(list[int], data)

                return artist_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        artist_ids = _parse_artist_ids(d.pop("artistIds", UNSET))

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

        def _parse_metadata_profile_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        metadata_profile_id = _parse_metadata_profile_id(
            d.pop("metadataProfileId", UNSET)
        )

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

        artist_editor_resource = cls(
            artist_ids=artist_ids,
            monitored=monitored,
            monitor_new_items=monitor_new_items,
            quality_profile_id=quality_profile_id,
            metadata_profile_id=metadata_profile_id,
            root_folder_path=root_folder_path,
            tags=tags,
            apply_tags=apply_tags,
            move_files=move_files,
            delete_files=delete_files,
            add_import_list_exclusion=add_import_list_exclusion,
        )

        return artist_editor_resource
