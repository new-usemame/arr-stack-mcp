from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.primary_album_type import PrimaryAlbumType


T = TypeVar("T", bound="ProfilePrimaryAlbumTypeItemResource")


@_attrs_define
class ProfilePrimaryAlbumTypeItemResource:
    """
    Attributes:
        id (Union[Unset, int]):
        album_type (Union[Unset, PrimaryAlbumType]):
        allowed (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    album_type: Union[Unset, "PrimaryAlbumType"] = UNSET
    allowed: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        album_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.album_type, Unset):
            album_type = self.album_type.to_dict()

        allowed = self.allowed

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if album_type is not UNSET:
            field_dict["albumType"] = album_type
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.primary_album_type import PrimaryAlbumType

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _album_type = d.pop("albumType", UNSET)
        album_type: Union[Unset, PrimaryAlbumType]
        if isinstance(_album_type, Unset):
            album_type = UNSET
        else:
            album_type = PrimaryAlbumType.from_dict(_album_type)

        allowed = d.pop("allowed", UNSET)

        profile_primary_album_type_item_resource = cls(
            id=id,
            album_type=album_type,
            allowed=allowed,
        )

        return profile_primary_album_type_item_resource
