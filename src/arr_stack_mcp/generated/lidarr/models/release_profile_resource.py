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
        enabled (Union[Unset, bool]):
        required (Union[None, Unset, list[str]]):
        ignored (Union[None, Unset, list[str]]):
        indexer_id (Union[Unset, int]):
        tags (Union[None, Unset, list[int]]):
    """

    id: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    required: Union[None, Unset, list[str]] = UNSET
    ignored: Union[None, Unset, list[str]] = UNSET
    indexer_id: Union[Unset, int] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enabled = self.enabled

        required: Union[None, Unset, list[str]]
        if isinstance(self.required, Unset):
            required = UNSET
        elif isinstance(self.required, list):
            required = self.required

        else:
            required = self.required

        ignored: Union[None, Unset, list[str]]
        if isinstance(self.ignored, Unset):
            ignored = UNSET
        elif isinstance(self.ignored, list):
            ignored = self.ignored

        else:
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_required(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_type_0 = cast(list[str], data)

                return required_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        required = _parse_required(d.pop("required", UNSET))

        def _parse_ignored(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ignored_type_0 = cast(list[str], data)

                return ignored_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ignored = _parse_ignored(d.pop("ignored", UNSET))

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
            enabled=enabled,
            required=required,
            ignored=ignored,
            indexer_id=indexer_id,
            tags=tags,
        )

        return release_profile_resource
