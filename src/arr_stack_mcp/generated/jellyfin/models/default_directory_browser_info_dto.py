from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultDirectoryBrowserInfoDto")


@_attrs_define
class DefaultDirectoryBrowserInfoDto:
    """Default directory browser info.

    Attributes:
        path (Union[None, Unset, str]): Gets or sets the path.
    """

    path: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
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

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        default_directory_browser_info_dto = cls(
            path=path,
        )

        return default_directory_browser_info_dto
