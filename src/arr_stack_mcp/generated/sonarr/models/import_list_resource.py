from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.import_list_type import ImportListType
from ..models.monitor_types import MonitorTypes
from ..models.new_item_monitor_types import NewItemMonitorTypes
from ..models.series_types import SeriesTypes
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
        enable_automatic_add (Union[Unset, bool]):
        search_for_missing_episodes (Union[Unset, bool]):
        should_monitor (Union[Unset, MonitorTypes]):
        monitor_new_items (Union[Unset, NewItemMonitorTypes]):
        root_folder_path (Union[None, Unset, str]):
        quality_profile_id (Union[Unset, int]):
        series_type (Union[Unset, SeriesTypes]):
        season_folder (Union[Unset, bool]):
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
    enable_automatic_add: Union[Unset, bool] = UNSET
    search_for_missing_episodes: Union[Unset, bool] = UNSET
    should_monitor: Union[Unset, MonitorTypes] = UNSET
    monitor_new_items: Union[Unset, NewItemMonitorTypes] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    quality_profile_id: Union[Unset, int] = UNSET
    series_type: Union[Unset, SeriesTypes] = UNSET
    season_folder: Union[Unset, bool] = UNSET
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

        enable_automatic_add = self.enable_automatic_add

        search_for_missing_episodes = self.search_for_missing_episodes

        should_monitor: Union[Unset, str] = UNSET
        if not isinstance(self.should_monitor, Unset):
            should_monitor = self.should_monitor.value

        monitor_new_items: Union[Unset, str] = UNSET
        if not isinstance(self.monitor_new_items, Unset):
            monitor_new_items = self.monitor_new_items.value

        root_folder_path: Union[None, Unset, str]
        if isinstance(self.root_folder_path, Unset):
            root_folder_path = UNSET
        else:
            root_folder_path = self.root_folder_path

        quality_profile_id = self.quality_profile_id

        series_type: Union[Unset, str] = UNSET
        if not isinstance(self.series_type, Unset):
            series_type = self.series_type.value

        season_folder = self.season_folder

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
        if enable_automatic_add is not UNSET:
            field_dict["enableAutomaticAdd"] = enable_automatic_add
        if search_for_missing_episodes is not UNSET:
            field_dict["searchForMissingEpisodes"] = search_for_missing_episodes
        if should_monitor is not UNSET:
            field_dict["shouldMonitor"] = should_monitor
        if monitor_new_items is not UNSET:
            field_dict["monitorNewItems"] = monitor_new_items
        if root_folder_path is not UNSET:
            field_dict["rootFolderPath"] = root_folder_path
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id
        if series_type is not UNSET:
            field_dict["seriesType"] = series_type
        if season_folder is not UNSET:
            field_dict["seasonFolder"] = season_folder
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

        enable_automatic_add = d.pop("enableAutomaticAdd", UNSET)

        search_for_missing_episodes = d.pop("searchForMissingEpisodes", UNSET)

        _should_monitor = d.pop("shouldMonitor", UNSET)
        should_monitor: Union[Unset, MonitorTypes]
        if isinstance(_should_monitor, Unset):
            should_monitor = UNSET
        else:
            should_monitor = MonitorTypes(_should_monitor)

        _monitor_new_items = d.pop("monitorNewItems", UNSET)
        monitor_new_items: Union[Unset, NewItemMonitorTypes]
        if isinstance(_monitor_new_items, Unset):
            monitor_new_items = UNSET
        else:
            monitor_new_items = NewItemMonitorTypes(_monitor_new_items)

        def _parse_root_folder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_folder_path = _parse_root_folder_path(d.pop("rootFolderPath", UNSET))

        quality_profile_id = d.pop("qualityProfileId", UNSET)

        _series_type = d.pop("seriesType", UNSET)
        series_type: Union[Unset, SeriesTypes]
        if isinstance(_series_type, Unset):
            series_type = UNSET
        else:
            series_type = SeriesTypes(_series_type)

        season_folder = d.pop("seasonFolder", UNSET)

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
            enable_automatic_add=enable_automatic_add,
            search_for_missing_episodes=search_for_missing_episodes,
            should_monitor=should_monitor,
            monitor_new_items=monitor_new_items,
            root_folder_path=root_folder_path,
            quality_profile_id=quality_profile_id,
            series_type=series_type,
            season_folder=season_folder,
            list_type=list_type,
            list_order=list_order,
            min_refresh_interval=min_refresh_interval,
        )

        return import_list_resource
