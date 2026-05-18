from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_database_option import CustomDatabaseOption


T = TypeVar("T", bound="CustomDatabaseOptions")


@_attrs_define
class CustomDatabaseOptions:
    """Defines the options for a custom database connector.

    Attributes:
        plugin_name (Union[Unset, str]): Gets or sets the Plugin name to search for database providers.
        plugin_assembly (Union[Unset, str]): Gets or sets the plugin assembly to search for providers.
        connection_string (Union[Unset, str]): Gets or sets the connection string for the custom database provider.
        options (Union[Unset, list['CustomDatabaseOption']]): Gets or sets the list of extra options for the custom
            provider.
    """

    plugin_name: Union[Unset, str] = UNSET
    plugin_assembly: Union[Unset, str] = UNSET
    connection_string: Union[Unset, str] = UNSET
    options: Union[Unset, list["CustomDatabaseOption"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        plugin_name = self.plugin_name

        plugin_assembly = self.plugin_assembly

        connection_string = self.connection_string

        options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if plugin_name is not UNSET:
            field_dict["PluginName"] = plugin_name
        if plugin_assembly is not UNSET:
            field_dict["PluginAssembly"] = plugin_assembly
        if connection_string is not UNSET:
            field_dict["ConnectionString"] = connection_string
        if options is not UNSET:
            field_dict["Options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_database_option import CustomDatabaseOption

        d = dict(src_dict)
        plugin_name = d.pop("PluginName", UNSET)

        plugin_assembly = d.pop("PluginAssembly", UNSET)

        connection_string = d.pop("ConnectionString", UNSET)

        options = []
        _options = d.pop("Options", UNSET)
        for options_item_data in _options or []:
            options_item = CustomDatabaseOption.from_dict(options_item_data)

            options.append(options_item)

        custom_database_options = cls(
            plugin_name=plugin_name,
            plugin_assembly=plugin_assembly,
            connection_string=connection_string,
            options=options,
        )

        return custom_database_options
