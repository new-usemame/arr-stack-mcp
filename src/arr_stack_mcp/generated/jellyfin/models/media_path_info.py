from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaPathInfo")


@_attrs_define
class MediaPathInfo:
    """
    Attributes:
        path (Union[Unset, str]):
    """

    path: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        path = d.pop("Path", UNSET)

        media_path_info = cls(
            path=path,
        )

        return media_path_info
