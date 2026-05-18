from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexerConfigResource")


@_attrs_define
class IndexerConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        minimum_age (Union[Unset, int]):
        retention (Union[Unset, int]):
        maximum_size (Union[Unset, int]):
        rss_sync_interval (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    minimum_age: Union[Unset, int] = UNSET
    retention: Union[Unset, int] = UNSET
    maximum_size: Union[Unset, int] = UNSET
    rss_sync_interval: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        minimum_age = self.minimum_age

        retention = self.retention

        maximum_size = self.maximum_size

        rss_sync_interval = self.rss_sync_interval

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if minimum_age is not UNSET:
            field_dict["minimumAge"] = minimum_age
        if retention is not UNSET:
            field_dict["retention"] = retention
        if maximum_size is not UNSET:
            field_dict["maximumSize"] = maximum_size
        if rss_sync_interval is not UNSET:
            field_dict["rssSyncInterval"] = rss_sync_interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        minimum_age = d.pop("minimumAge", UNSET)

        retention = d.pop("retention", UNSET)

        maximum_size = d.pop("maximumSize", UNSET)

        rss_sync_interval = d.pop("rssSyncInterval", UNSET)

        indexer_config_resource = cls(
            id=id,
            minimum_age=minimum_age,
            retention=retention,
            maximum_size=maximum_size,
            rss_sync_interval=rss_sync_interval,
        )

        return indexer_config_resource
