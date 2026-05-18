from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.file_system_entry_type import FileSystemEntryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSystemEntryInfo")


@_attrs_define
class FileSystemEntryInfo:
    """Class FileSystemEntryInfo.

    Attributes:
        name (Union[Unset, str]): Gets the name.
        path (Union[Unset, str]): Gets the path.
        type_ (Union[Unset, FileSystemEntryType]): Enum FileSystemEntryType.
    """

    name: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    type_: Union[Unset, FileSystemEntryType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if path is not UNSET:
            field_dict["Path"] = path
        if type_ is not UNSET:
            field_dict["Type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        path = d.pop("Path", UNSET)

        _type_ = d.pop("Type", UNSET)
        type_: Union[Unset, FileSystemEntryType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FileSystemEntryType(_type_)

        file_system_entry_info = cls(
            name=name,
            path=path,
            type_=type_,
        )

        return file_system_entry_info
