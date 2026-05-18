from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.apply_tags import ApplyTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportListBulkResource")


@_attrs_define
class ImportListBulkResource:
    """
    Attributes:
        ids (Union[None, Unset, list[int]]):
        tags (Union[None, Unset, list[int]]):
        apply_tags (Union[Unset, ApplyTags]):
        enable_automatic_add (Union[None, Unset, bool]):
        root_folder_path (Union[None, Unset, str]):
        quality_profile_id (Union[None, Unset, int]):
    """

    ids: Union[None, Unset, list[int]] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    apply_tags: Union[Unset, ApplyTags] = UNSET
    enable_automatic_add: Union[None, Unset, bool] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    quality_profile_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ids: Union[None, Unset, list[int]]
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = self.ids

        else:
            ids = self.ids

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

        enable_automatic_add: Union[None, Unset, bool]
        if isinstance(self.enable_automatic_add, Unset):
            enable_automatic_add = UNSET
        else:
            enable_automatic_add = self.enable_automatic_add

        root_folder_path: Union[None, Unset, str]
        if isinstance(self.root_folder_path, Unset):
            root_folder_path = UNSET
        else:
            root_folder_path = self.root_folder_path

        quality_profile_id: Union[None, Unset, int]
        if isinstance(self.quality_profile_id, Unset):
            quality_profile_id = UNSET
        else:
            quality_profile_id = self.quality_profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if apply_tags is not UNSET:
            field_dict["applyTags"] = apply_tags
        if enable_automatic_add is not UNSET:
            field_dict["enableAutomaticAdd"] = enable_automatic_add
        if root_folder_path is not UNSET:
            field_dict["rootFolderPath"] = root_folder_path
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = cast(list[int], data)

                return ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        ids = _parse_ids(d.pop("ids", UNSET))

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

        def _parse_enable_automatic_add(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_automatic_add = _parse_enable_automatic_add(
            d.pop("enableAutomaticAdd", UNSET)
        )

        def _parse_root_folder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_folder_path = _parse_root_folder_path(d.pop("rootFolderPath", UNSET))

        def _parse_quality_profile_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quality_profile_id = _parse_quality_profile_id(d.pop("qualityProfileId", UNSET))

        import_list_bulk_resource = cls(
            ids=ids,
            tags=tags,
            apply_tags=apply_tags,
            enable_automatic_add=enable_automatic_add,
            root_folder_path=root_folder_path,
            quality_profile_id=quality_profile_id,
        )

        return import_list_bulk_resource
