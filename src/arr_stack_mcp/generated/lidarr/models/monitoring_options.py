from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.monitor_types import MonitorTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonitoringOptions")


@_attrs_define
class MonitoringOptions:
    """
    Attributes:
        monitor (Union[Unset, MonitorTypes]):
        albums_to_monitor (Union[None, Unset, list[str]]):
        monitored (Union[Unset, bool]):
    """

    monitor: Union[Unset, MonitorTypes] = UNSET
    albums_to_monitor: Union[None, Unset, list[str]] = UNSET
    monitored: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        monitor: Union[Unset, str] = UNSET
        if not isinstance(self.monitor, Unset):
            monitor = self.monitor.value

        albums_to_monitor: Union[None, Unset, list[str]]
        if isinstance(self.albums_to_monitor, Unset):
            albums_to_monitor = UNSET
        elif isinstance(self.albums_to_monitor, list):
            albums_to_monitor = self.albums_to_monitor

        else:
            albums_to_monitor = self.albums_to_monitor

        monitored = self.monitored

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if albums_to_monitor is not UNSET:
            field_dict["albumsToMonitor"] = albums_to_monitor
        if monitored is not UNSET:
            field_dict["monitored"] = monitored

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _monitor = d.pop("monitor", UNSET)
        monitor: Union[Unset, MonitorTypes]
        if isinstance(_monitor, Unset):
            monitor = UNSET
        else:
            monitor = MonitorTypes(_monitor)

        def _parse_albums_to_monitor(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                albums_to_monitor_type_0 = cast(list[str], data)

                return albums_to_monitor_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        albums_to_monitor = _parse_albums_to_monitor(d.pop("albumsToMonitor", UNSET))

        monitored = d.pop("monitored", UNSET)

        monitoring_options = cls(
            monitor=monitor,
            albums_to_monitor=albums_to_monitor,
            monitored=monitored,
        )

        return monitoring_options
