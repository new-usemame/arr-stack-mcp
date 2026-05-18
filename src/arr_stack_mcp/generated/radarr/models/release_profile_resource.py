from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReleaseProfileResource")


@_attrs_define
class ReleaseProfileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        enabled (Union[Unset, bool]):
        required (Union[Unset, Any]):
        ignored (Union[Unset, Any]):
        indexer_id (Union[Unset, int]):
        tags (Union[None, Unset, list[int]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    required: Union[Unset, Any] = UNSET
    ignored: Union[Unset, Any] = UNSET
    indexer_id: Union[Unset, int] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        enabled = self.enabled

        required = self.required

        ignored = self.ignored

        indexer_id = self.indexer_id

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if required is not UNSET:
            field_dict["required"] = required
        if ignored is not UNSET:
            field_dict["ignored"] = ignored
        if indexer_id is not UNSET:
            field_dict["indexerId"] = indexer_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        enabled = d.pop("enabled", UNSET)

        required = d.pop("required", UNSET)

        ignored = d.pop("ignored", UNSET)

        indexer_id = d.pop("indexerId", UNSET)

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

        release_profile_resource = cls(
            id=id,
            name=name,
            enabled=enabled,
            required=required,
            ignored=ignored,
            indexer_id=indexer_id,
            tags=tags,
        )

        return release_profile_resource
