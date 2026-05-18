from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrickplayInfoDto")


@_attrs_define
class TrickplayInfoDto:
    """The trickplay api model.

    Attributes:
        width (Union[Unset, int]): Gets the width of an individual thumbnail.
        height (Union[Unset, int]): Gets the height of an individual thumbnail.
        tile_width (Union[Unset, int]): Gets the amount of thumbnails per row.
        tile_height (Union[Unset, int]): Gets the amount of thumbnails per column.
        thumbnail_count (Union[Unset, int]): Gets the total amount of non-black thumbnails.
        interval (Union[Unset, int]): Gets the interval in milliseconds between each trickplay thumbnail.
        bandwidth (Union[Unset, int]): Gets the peak bandwidth usage in bits per second.
    """

    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    tile_width: Union[Unset, int] = UNSET
    tile_height: Union[Unset, int] = UNSET
    thumbnail_count: Union[Unset, int] = UNSET
    interval: Union[Unset, int] = UNSET
    bandwidth: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        tile_width = self.tile_width

        tile_height = self.tile_height

        thumbnail_count = self.thumbnail_count

        interval = self.interval

        bandwidth = self.bandwidth

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if width is not UNSET:
            field_dict["Width"] = width
        if height is not UNSET:
            field_dict["Height"] = height
        if tile_width is not UNSET:
            field_dict["TileWidth"] = tile_width
        if tile_height is not UNSET:
            field_dict["TileHeight"] = tile_height
        if thumbnail_count is not UNSET:
            field_dict["ThumbnailCount"] = thumbnail_count
        if interval is not UNSET:
            field_dict["Interval"] = interval
        if bandwidth is not UNSET:
            field_dict["Bandwidth"] = bandwidth

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        width = d.pop("Width", UNSET)

        height = d.pop("Height", UNSET)

        tile_width = d.pop("TileWidth", UNSET)

        tile_height = d.pop("TileHeight", UNSET)

        thumbnail_count = d.pop("ThumbnailCount", UNSET)

        interval = d.pop("Interval", UNSET)

        bandwidth = d.pop("Bandwidth", UNSET)

        trickplay_info_dto = cls(
            width=width,
            height=height,
            tile_width=tile_width,
            tile_height=tile_height,
            thumbnail_count=thumbnail_count,
            interval=interval,
            bandwidth=bandwidth,
        )

        return trickplay_info_dto
