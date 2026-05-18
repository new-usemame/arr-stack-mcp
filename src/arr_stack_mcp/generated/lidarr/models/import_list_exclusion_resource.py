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
        foreign_id (Union[None, Unset, str]):
        artist_name (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    foreign_id: Union[None, Unset, str] = UNSET
    artist_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        foreign_id: Union[None, Unset, str]
        if isinstance(self.foreign_id, Unset):
            foreign_id = UNSET
        else:
            foreign_id = self.foreign_id

        artist_name: Union[None, Unset, str]
        if isinstance(self.artist_name, Unset):
            artist_name = UNSET
        else:
            artist_name = self.artist_name

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if foreign_id is not UNSET:
            field_dict["foreignId"] = foreign_id
        if artist_name is not UNSET:
            field_dict["artistName"] = artist_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_foreign_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_id = _parse_foreign_id(d.pop("foreignId", UNSET))

        def _parse_artist_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist_name = _parse_artist_name(d.pop("artistName", UNSET))

        import_list_exclusion_resource = cls(
            id=id,
            foreign_id=foreign_id,
            artist_name=artist_name,
        )

        return import_list_exclusion_resource
