from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportListExclusionResource")


@_attrs_define
class ImportListExclusionResource:
    """
    Attributes:
        id (Union[Unset, int]):
        tvdb_id (Union[Unset, int]):
        title (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    tvdb_id: Union[Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tvdb_id = self.tvdb_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tvdb_id is not UNSET:
            field_dict["tvdbId"] = tvdb_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tvdb_id = d.pop("tvdbId", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        import_list_exclusion_resource = cls(
            id=id,
            tvdb_id=tvdb_id,
            title=title,
        )

        return import_list_exclusion_resource
