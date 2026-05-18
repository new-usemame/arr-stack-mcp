from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.album_add_type import AlbumAddType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddAlbumOptions")


@_attrs_define
class AddAlbumOptions:
    """
    Attributes:
        add_type (Union[Unset, AlbumAddType]):
        search_for_new_album (Union[Unset, bool]):
    """

    add_type: Union[Unset, AlbumAddType] = UNSET
    search_for_new_album: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        add_type: Union[Unset, str] = UNSET
        if not isinstance(self.add_type, Unset):
            add_type = self.add_type.value

        search_for_new_album = self.search_for_new_album

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if add_type is not UNSET:
            field_dict["addType"] = add_type
        if search_for_new_album is not UNSET:
            field_dict["searchForNewAlbum"] = search_for_new_album

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _add_type = d.pop("addType", UNSET)
        add_type: Union[Unset, AlbumAddType]
        if isinstance(_add_type, Unset):
            add_type = UNSET
        else:
            add_type = AlbumAddType(_add_type)

        search_for_new_album = d.pop("searchForNewAlbum", UNSET)

        add_album_options = cls(
            add_type=add_type,
            search_for_new_album=search_for_new_album,
        )

        return add_album_options
