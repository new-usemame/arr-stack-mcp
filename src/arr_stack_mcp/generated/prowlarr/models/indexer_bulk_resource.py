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
        enable (Union[None, Unset, bool]):
        app_profile_id (Union[None, Unset, int]):
        priority (Union[None, Unset, int]):
        minimum_seeders (Union[None, Unset, int]):
        seed_ratio (Union[None, Unset, float]):
        seed_time (Union[None, Unset, int]):
        pack_seed_time (Union[None, Unset, int]):
        prefer_magnet_url (Union[None, Unset, bool]):
    """

    ids: Union[None, Unset, list[int]] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    apply_tags: Union[Unset, ApplyTags] = UNSET
    enable: Union[None, Unset, bool] = UNSET
    app_profile_id: Union[None, Unset, int] = UNSET
    priority: Union[None, Unset, int] = UNSET
    minimum_seeders: Union[None, Unset, int] = UNSET
    seed_ratio: Union[None, Unset, float] = UNSET
    seed_time: Union[None, Unset, int] = UNSET
    pack_seed_time: Union[None, Unset, int] = UNSET
    prefer_magnet_url: Union[None, Unset, bool] = UNSET

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

        enable: Union[None, Unset, bool]
        if isinstance(self.enable, Unset):
            enable = UNSET
        else:
            enable = self.enable

        app_profile_id: Union[None, Unset, int]
        if isinstance(self.app_profile_id, Unset):
            app_profile_id = UNSET
        else:
            app_profile_id = self.app_profile_id

        priority: Union[None, Unset, int]
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        minimum_seeders: Union[None, Unset, int]
        if isinstance(self.minimum_seeders, Unset):
            minimum_seeders = UNSET
        else:
            minimum_seeders = self.minimum_seeders

        seed_ratio: Union[None, Unset, float]
        if isinstance(self.seed_ratio, Unset):
            seed_ratio = UNSET
        else:
            seed_ratio = self.seed_ratio

        seed_time: Union[None, Unset, int]
        if isinstance(self.seed_time, Unset):
            seed_time = UNSET
        else:
            seed_time = self.seed_time

        pack_seed_time: Union[None, Unset, int]
        if isinstance(self.pack_seed_time, Unset):
            pack_seed_time = UNSET
        else:
            pack_seed_time = self.pack_seed_time

        prefer_magnet_url: Union[None, Unset, bool]
        if isinstance(self.prefer_magnet_url, Unset):
            prefer_magnet_url = UNSET
        else:
            prefer_magnet_url = self.prefer_magnet_url

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if tags is not UNSET:
            field_dict["tags"] = tags
        if apply_tags is not UNSET:
            field_dict["applyTags"] = apply_tags
        if enable is not UNSET:
            field_dict["enable"] = enable
        if app_profile_id is not UNSET:
            field_dict["appProfileId"] = app_profile_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if minimum_seeders is not UNSET:
            field_dict["minimumSeeders"] = minimum_seeders
        if seed_ratio is not UNSET:
            field_dict["seedRatio"] = seed_ratio
        if seed_time is not UNSET:
            field_dict["seedTime"] = seed_time
        if pack_seed_time is not UNSET:
            field_dict["packSeedTime"] = pack_seed_time
        if prefer_magnet_url is not UNSET:
            field_dict["preferMagnetUrl"] = prefer_magnet_url

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

        def _parse_enable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable = _parse_enable(d.pop("enable", UNSET))

        def _parse_app_profile_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        app_profile_id = _parse_app_profile_id(d.pop("appProfileId", UNSET))

        def _parse_priority(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_minimum_seeders(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        minimum_seeders = _parse_minimum_seeders(d.pop("minimumSeeders", UNSET))

        def _parse_seed_ratio(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seed_ratio = _parse_seed_ratio(d.pop("seedRatio", UNSET))

        def _parse_seed_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seed_time = _parse_seed_time(d.pop("seedTime", UNSET))

        def _parse_pack_seed_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pack_seed_time = _parse_pack_seed_time(d.pop("packSeedTime", UNSET))

        def _parse_prefer_magnet_url(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        prefer_magnet_url = _parse_prefer_magnet_url(d.pop("preferMagnetUrl", UNSET))

        indexer_bulk_resource = cls(
            ids=ids,
            tags=tags,
            apply_tags=apply_tags,
            enable=enable,
            app_profile_id=app_profile_id,
            priority=priority,
            minimum_seeders=minimum_seeders,
            seed_ratio=seed_ratio,
            seed_time=seed_time,
            pack_seed_time=pack_seed_time,
            prefer_magnet_url=prefer_magnet_url,
        )

        return indexer_bulk_resource
