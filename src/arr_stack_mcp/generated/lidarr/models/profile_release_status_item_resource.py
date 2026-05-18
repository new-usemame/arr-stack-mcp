from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.release_status import ReleaseStatus


T = TypeVar("T", bound="ProfileReleaseStatusItemResource")


@_attrs_define
class ProfileReleaseStatusItemResource:
    """
    Attributes:
        id (Union[Unset, int]):
        release_status (Union[Unset, ReleaseStatus]):
        allowed (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    release_status: Union[Unset, "ReleaseStatus"] = UNSET
    allowed: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        release_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.release_status, Unset):
            release_status = self.release_status.to_dict()

        allowed = self.allowed

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if release_status is not UNSET:
            field_dict["releaseStatus"] = release_status
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.release_status import ReleaseStatus

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _release_status = d.pop("releaseStatus", UNSET)
        release_status: Union[Unset, ReleaseStatus]
        if isinstance(_release_status, Unset):
            release_status = UNSET
        else:
            release_status = ReleaseStatus.from_dict(_release_status)

        allowed = d.pop("allowed", UNSET)

        profile_release_status_item_resource = cls(
            id=id,
            release_status=release_status,
            allowed=allowed,
        )

        return profile_release_status_item_resource
