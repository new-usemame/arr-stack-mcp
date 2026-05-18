from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.apply_tags import ApplyTags
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexerBulkResource")


@_attrs_define
class IndexerBulkResource:
    """
    Attributes:
        ids (Union[None, Unset, list[int]]):
        tags (Union[None, Unset, list[int]]):
        apply_tags (Union[Unset, ApplyTags]):
        enable_rss (Union[None, Unset, bool]):
        enable_automatic_search (Union[None, Unset, bool]):
        enable_interactive_search (Union[None, Unset, bool]):
        priority (Union[None, Unset, int]):
    """

    ids: Union[None, Unset, list[int]] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    apply_tags: Union[Unset, ApplyTags] = UNSET
    enable_rss: Union[None, Unset, bool] = UNSET
    enable_automatic_search: Union[None, Unset, bool] = UNSET
    enable_interactive_search: Union[None, Unset, bool] = UNSET
    priority: Union[None, Unset, int] = UNSET

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

        enable_rss: Union[None, Unset, bool]
        if isinstance(self.enable_rss, Unset):
            enable_rss = UNSET
        else:
            enable_rss = self.enable_rss

        enable_automatic_search: Union[None, Unset, bool]
        if isinstance(self.enable_automatic_search, Unset):
            enable_automatic_search = UNSET
        else:
            enable_automatic_search = self.enable_automatic_search

        enable_interactive_search: Union[None, Unset, bool]
        if isinstance(self.enable_interactive_search, Unset):
            enable_interactive_search = UNSET
        else:
            enable_interactive_search = self.enable_interactive_search

        priority: Union[None, Unset, int]
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if apply_tags is not UNSET:
            field_dict["applyTags"] = apply_tags
        if enable_rss is not UNSET:
            field_dict["enableRss"] = enable_rss
        if enable_automatic_search is not UNSET:
            field_dict["enableAutomaticSearch"] = enable_automatic_search
        if enable_interactive_search is not UNSET:
            field_dict["enableInteractiveSearch"] = enable_interactive_search
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        def _parse_enable_rss(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_rss = _parse_enable_rss(d.pop("enableRss", UNSET))

        def _parse_enable_automatic_search(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_automatic_search = _parse_enable_automatic_search(
            d.pop("enableAutomaticSearch", UNSET)
        )

        def _parse_enable_interactive_search(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_interactive_search = _parse_enable_interactive_search(
            d.pop("enableInteractiveSearch", UNSET)
        )

        def _parse_priority(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        indexer_bulk_resource = cls(
            ids=ids,
            tags=tags,
            apply_tags=apply_tags,
            enable_rss=enable_rss,
            enable_automatic_search=enable_automatic_search,
            enable_interactive_search=enable_interactive_search,
            priority=priority,
        )

        return indexer_bulk_resource
