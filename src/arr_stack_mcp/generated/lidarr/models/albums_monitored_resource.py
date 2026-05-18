from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumsMonitoredResource")


@_attrs_define
class AlbumsMonitoredResource:
    """
    Attributes:
        album_ids (Union[None, Unset, list[int]]):
        monitored (Union[Unset, bool]):
    """

    album_ids: Union[None, Unset, list[int]] = UNSET
    monitored: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        album_ids: Union[None, Unset, list[int]]
        if isinstance(self.album_ids, Unset):
            album_ids = UNSET
        elif isinstance(self.album_ids, list):
            album_ids = self.album_ids

        else:
            album_ids = self.album_ids

        monitored = self.monitored

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if album_ids is not UNSET:
            field_dict["albumIds"] = album_ids
        if monitored is not UNSET:
            field_dict["monitored"] = monitored

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_album_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                album_ids_type_0 = cast(list[int], data)

                return album_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        album_ids = _parse_album_ids(d.pop("albumIds", UNSET))

        monitored = d.pop("monitored", UNSET)

        albums_monitored_resource = cls(
            album_ids=album_ids,
            monitored=monitored,
        )

        return albums_monitored_resource
