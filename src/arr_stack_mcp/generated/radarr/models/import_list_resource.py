from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.import_list_type import ImportListType
from ..models.monitor_types import MonitorTypes
from ..models.movie_status_type import MovieStatusType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field
    from ..models.provider_message import ProviderMessage


T = TypeVar("T", bound="ImportListResource")


@_attrs_define
class ImportListResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        fields (Union[None, Unset, list['Field']]):
        implementation_name (Union[None, Unset, str]):
        implementation (Union[None, Unset, str]):
        config_contract (Union[None, Unset, str]):
        info_link (Union[None, Unset, str]):
        message (Union[Unset, ProviderMessage]):
        tags (Union[None, Unset, list[int]]):
        presets (Union[None, Unset, list['ImportListResource']]):
        enabled (Union[Unset, bool]):
        enable_auto (Union[Unset, bool]):
        monitor (Union[Unset, MonitorTypes]):
        root_folder_path (Union[None, Unset, str]):
        quality_profile_id (Union[Unset, int]):
        search_on_add (Union[Unset, bool]):
        minimum_availability (Union[Unset, MovieStatusType]):
        list_type (Union[Unset, ImportListType]):
        list_order (Union[Unset, int]):
        min_refresh_interval (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    fields: Union[None, Unset, list["Field"]] = UNSET
    implementation_name: Union[None, Unset, str] = UNSET
    implementation: Union[None, Unset, str] = UNSET
    config_contract: Union[None, Unset, str] = UNSET
    info_link: Union[None, Unset, str] = UNSET
    message: Union[Unset, "ProviderMessage"] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    presets: Union[None, Unset, list["ImportListResource"]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    enable_auto: Union[Unset, bool] = UNSET
    monitor: Union[Unset, MonitorTypes] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    quality_profile_id: Union[Unset, int] = UNSET
    search_on_add: Union[Unset, bool] = UNSET
    minimum_availability: Union[Unset, MovieStatusType] = UNSET
    list_type: Union[Unset, ImportListType] = UNSET
    list_order: Union[Unset, int] = UNSET
    min_refresh_interval: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        implementation_name: Union[None, Unset, str]
        if isinstance(self.implementation_name, Unset):
            implementation_name = UNSET
        else:
            implementation_name = self.implementation_name

        implementation: Union[None, Unset, str]
        if isinstance(self.implementation, Unset):
            implementation = UNSET
        else:
            implementation = self.implementation

        config_contract: Union[None, Unset, str]
        if isinstance(self.config_contract, Unset):
            config_contract = UNSET
        else:
            config_contract = self.config_contract

        info_link: Union[None, Unset, str]
        if isinstance(self.info_link, Unset):
            info_link = UNSET
        else:
            info_link = self.info_link

        message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        presets: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.presets, Unset):
            presets = UNSET
        elif isinstance(self.presets, list):
            presets = []
            for presets_type_0_item_data in self.presets:
                presets_type_0_item = presets_type_0_item_data.to_dict()
                presets.append(presets_type_0_item)

        else:
            presets = self.presets

        enabled = self.enabled

        enable_auto = self.enable_auto

        monitor: Union[Unset, str] = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.value

        root_folder_path: Union[None, Unset, str]
        if isinstance(self.root_folder_path, Unset):
            root_folder_path = UNSET
        else:
            root_folder_path = self.root_folder_path

        quality_profile_id = self.quality_profile_id

        search_on_add = self.search_on_add

        minimum_availability: Union[Unset, str] = UNSET
        if not isinstance(self.minimum_availability, Unset):
            minimum_availability = self.minimum_availability.value

        list_type: Union[Unset, str] = UNSET
        if not isinstance(self.list_type, Unset):
            list_type = self.list_type.value

        list_order = self.list_order

        min_refresh_interval = self.min_refresh_interval

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if fields is not UNSET:
            field_dict["fields"] = fields
        if implementation_name is not UNSET:
            field_dict["implementationName"] = implementation_name
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if config_contract is not UNSET:
            field_dict["configContract"] = config_contract
        if info_link is not UNSET:
            field_dict["infoLink"] = info_link
        if message is not UNSET:
            field_dict["message"] = message
        if tags is not UNSET:
            field_dict["tags"] = tags
        if presets is not UNSET:
            field_dict["presets"] = presets
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enable_auto is not UNSET:
            field_dict["enableAuto"] = enable_auto
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if root_folder_path is not UNSET:
            field_dict["rootFolderPath"] = root_folder_path
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id
        if search_on_add is not UNSET:
            field_dict["searchOnAdd"] = search_on_add
        if minimum_availability is not UNSET:
            field_dict["minimumAvailability"] = minimum_availability
        if list_type is not UNSET:
            field_dict["listType"] = list_type
        if list_order is not UNSET:
            field_dict["listOrder"] = list_order
        if min_refresh_interval is not UNSET:
            field_dict["minRefreshInterval"] = min_refresh_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field import Field
        from ..models.provider_message import ProviderMessage

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_fields(data: object) -> Union[None, Unset, list["Field"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = Field.from_dict(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Field"]], data)

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_implementation_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation_name = _parse_implementation_name(
            d.pop("implementationName", UNSET)
        )

        def _parse_implementation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation = _parse_implementation(d.pop("implementation", UNSET))

        def _parse_config_contract(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        config_contract = _parse_config_contract(d.pop("configContract", UNSET))

        def _parse_info_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_link = _parse_info_link(d.pop("infoLink", UNSET))

        _message = d.pop("message", UNSET)
        message: Union[Unset, ProviderMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = ProviderMessage.from_dict(_message)

        def _parse_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_presets(
            data: object,
        ) -> Union[None, Unset, list["ImportListResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                presets_type_0 = []
                _presets_type_0 = data
                for presets_type_0_item_data in _presets_type_0:
                    presets_type_0_item = ImportListResource.from_dict(
                        presets_type_0_item_data
                    )

                    presets_type_0.append(presets_type_0_item)

                return presets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ImportListResource"]], data)

        presets = _parse_presets(d.pop("presets", UNSET))

        enabled = d.pop("enabled", UNSET)

        enable_auto = d.pop("enableAuto", UNSET)

        _monitor = d.pop("monitor", UNSET)
        monitor: Union[Unset, MonitorTypes]
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = MonitorTypes(_monitor)

        def _parse_root_folder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_folder_path = _parse_root_folder_path(d.pop("rootFolderPath", UNSET))

        quality_profile_id = d.pop("qualityProfileId", UNSET)

        search_on_add = d.pop("searchOnAdd", UNSET)

        _minimum_availability = d.pop("minimumAvailability", UNSET)
        minimum_availability: Union[Unset, MovieStatusType]
        if isinstance(_minimum_availability, Unset):
            minimum_availability = UNSET
        else:
            minimum_availability = MovieStatusType(_minimum_availability)

        _list_type = d.pop("listType", UNSET)
        list_type: Union[Unset, ImportListType]
        if isinstance(_list_type, Unset):
            list_type = UNSET
        else:
            list_type = ImportListType(_list_type)

        list_order = d.pop("listOrder", UNSET)

        min_refresh_interval = d.pop("minRefreshInterval", UNSET)

        import_list_resource = cls(
            id=id,
            name=name,
            fields=fields,
            implementation_name=implementation_name,
            implementation=implementation,
            config_contract=config_contract,
            info_link=info_link,
            message=message,
            tags=tags,
            presets=presets,
            enabled=enabled,
            enable_auto=enable_auto,
            monitor=monitor,
            root_folder_path=root_folder_path,
            quality_profile_id=quality_profile_id,
            search_on_add=search_on_add,
            minimum_availability=minimum_availability,
            list_type=list_type,
            list_order=list_order,
            min_refresh_interval=min_refresh_interval,
        )

        return import_list_resource
