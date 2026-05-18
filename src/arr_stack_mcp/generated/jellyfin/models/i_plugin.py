from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPlugin")


@_attrs_define
class IPlugin:
    """Defines the MediaBrowser.Common.Plugins.IPlugin.

    Attributes:
        name (Union[None, Unset, str]): Gets the name of the plugin.
        description (Union[None, Unset, str]): Gets the Description.
        id (Union[Unset, UUID]): Gets the unique id.
        version (Union[None, Unset, str]): Gets the plugin version.
        assembly_file_path (Union[None, Unset, str]): Gets the path to the assembly file.
        can_uninstall (Union[Unset, bool]): Gets a value indicating whether the plugin can be uninstalled.
        data_folder_path (Union[None, Unset, str]): Gets the full path to the data folder, where the plugin can store
            any miscellaneous files needed.
    """

    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    id: Union[Unset, UUID] = UNSET
    version: Union[None, Unset, str] = UNSET
    assembly_file_path: Union[None, Unset, str] = UNSET
    can_uninstall: Union[Unset, bool] = UNSET
    data_folder_path: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        assembly_file_path: Union[None, Unset, str]
        if isinstance(self.assembly_file_path, Unset):
            assembly_file_path = UNSET
        else:
            assembly_file_path = self.assembly_file_path

        can_uninstall = self.can_uninstall

        data_folder_path: Union[None, Unset, str]
        if isinstance(self.data_folder_path, Unset):
            data_folder_path = UNSET
        else:
            data_folder_path = self.data_folder_path

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if id is not UNSET:
            field_dict["Id"] = id
        if version is not UNSET:
            field_dict["Version"] = version
        if assembly_file_path is not UNSET:
            field_dict["AssemblyFilePath"] = assembly_file_path
        if can_uninstall is not UNSET:
            field_dict["CanUninstall"] = can_uninstall
        if data_folder_path is not UNSET:
            field_dict["DataFolderPath"] = data_folder_path

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("Description", UNSET))

        _id = d.pop("Id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("Version", UNSET))

        def _parse_assembly_file_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        assembly_file_path = _parse_assembly_file_path(d.pop("AssemblyFilePath", UNSET))

        can_uninstall = d.pop("CanUninstall", UNSET)

        def _parse_data_folder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data_folder_path = _parse_data_folder_path(d.pop("DataFolderPath", UNSET))

        i_plugin = cls(
            name=name,
            description=description,
            id=id,
            version=version,
            assembly_file_path=assembly_file_path,
            can_uninstall=can_uninstall,
            data_folder_path=data_folder_path,
        )

        return i_plugin
