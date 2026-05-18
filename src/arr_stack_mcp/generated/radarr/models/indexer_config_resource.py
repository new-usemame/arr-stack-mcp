from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexerConfigResource")


@_attrs_define
class IndexerConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        minimum_age (Union[Unset, int]):
        maximum_size (Union[Unset, int]):
        retention (Union[Unset, int]):
        rss_sync_interval (Union[Unset, int]):
        prefer_indexer_flags (Union[Unset, bool]):
        availability_delay (Union[Unset, int]):
        allow_hardcoded_subs (Union[Unset, bool]):
        whitelisted_hardcoded_subs (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    minimum_age: Union[Unset, int] = UNSET
    maximum_size: Union[Unset, int] = UNSET
    retention: Union[Unset, int] = UNSET
    rss_sync_interval: Union[Unset, int] = UNSET
    prefer_indexer_flags: Union[Unset, bool] = UNSET
    availability_delay: Union[Unset, int] = UNSET
    allow_hardcoded_subs: Union[Unset, bool] = UNSET
    whitelisted_hardcoded_subs: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        minimum_age = self.minimum_age

        maximum_size = self.maximum_size

        retention = self.retention

        rss_sync_interval = self.rss_sync_interval

        prefer_indexer_flags = self.prefer_indexer_flags

        availability_delay = self.availability_delay

        allow_hardcoded_subs = self.allow_hardcoded_subs

        whitelisted_hardcoded_subs: Union[None, Unset, str]
        if isinstance(self.whitelisted_hardcoded_subs, Unset):
            whitelisted_hardcoded_subs = UNSET
        else:
            whitelisted_hardcoded_subs = self.whitelisted_hardcoded_subs

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if minimum_age is not UNSET:
            field_dict["minimumAge"] = minimum_age
        if maximum_size is not UNSET:
            field_dict["maximumSize"] = maximum_size
        if retention is not UNSET:
            field_dict["retention"] = retention
        if rss_sync_interval is not UNSET:
            field_dict["rssSyncInterval"] = rss_sync_interval
        if prefer_indexer_flags is not UNSET:
            field_dict["preferIndexerFlags"] = prefer_indexer_flags
        if availability_delay is not UNSET:
            field_dict["availabilityDelay"] = availability_delay
        if allow_hardcoded_subs is not UNSET:
            field_dict["allowHardcodedSubs"] = allow_hardcoded_subs
        if whitelisted_hardcoded_subs is not UNSET:
            field_dict["whitelistedHardcodedSubs"] = whitelisted_hardcoded_subs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        minimum_age = d.pop("minimumAge", UNSET)

        maximum_size = d.pop("maximumSize", UNSET)

        retention = d.pop("retention", UNSET)

        rss_sync_interval = d.pop("rssSyncInterval", UNSET)

        prefer_indexer_flags = d.pop("preferIndexerFlags", UNSET)

        availability_delay = d.pop("availabilityDelay", UNSET)

        allow_hardcoded_subs = d.pop("allowHardcodedSubs", UNSET)

        def _parse_whitelisted_hardcoded_subs(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        whitelisted_hardcoded_subs = _parse_whitelisted_hardcoded_subs(
            d.pop("whitelistedHardcodedSubs", UNSET)
        )

        indexer_config_resource = cls(
            id=id,
            minimum_age=minimum_age,
            maximum_size=maximum_size,
            retention=retention,
            rss_sync_interval=rss_sync_interval,
            prefer_indexer_flags=prefer_indexer_flags,
            availability_delay=availability_delay,
            allow_hardcoded_subs=allow_hardcoded_subs,
            whitelisted_hardcoded_subs=whitelisted_hardcoded_subs,
        )

        return indexer_config_resource
