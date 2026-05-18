from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadClientConfigResource")


@_attrs_define
class DownloadClientConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        download_client_config_resource = cls(
            id=id,
        )

        return download_client_config_resource
