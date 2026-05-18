from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_item_monitor_types import NewItemMonitorTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_studio_artist_resource import AlbumStudioArtistResource
    from ..models.monitoring_options import MonitoringOptions


T = TypeVar("T", bound="AlbumStudioResource")


@_attrs_define
class AlbumStudioResource:
    """
    Attributes:
        artist (Union[None, Unset, list['AlbumStudioArtistResource']]):
        monitoring_options (Union[Unset, MonitoringOptions]):
        monitor_new_items (Union[Unset, NewItemMonitorTypes]):
    """

    artist: Union[None, Unset, list["AlbumStudioArtistResource"]] = UNSET
    monitoring_options: Union[Unset, "MonitoringOptions"] = UNSET
    monitor_new_items: Union[Unset, NewItemMonitorTypes] = UNSET

    def to_dict(self) -> dict[str, Any]:
        artist: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.artist, Unset):
            artist = UNSET
        elif isinstance(self.artist, list):
            artist = []
            for artist_type_0_item_data in self.artist:
                artist_type_0_item = artist_type_0_item_data.to_dict()
                artist.append(artist_type_0_item)

        else:
            artist = self.artist

        monitoring_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monitoring_options, Unset):
            monitoring_options = self.monitoring_options.to_dict()

        monitor_new_items: Union[Unset, str] = UNSET
        if not isinstance(self.monitor_new_items, Unset):
            monitor_new_items = self.monitor_new_items.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if artist is not UNSET:
            field_dict["artist"] = artist
        if monitoring_options is not UNSET:
            field_dict["monitoringOptions"] = monitoring_options
        if monitor_new_items is not UNSET:
            field_dict["monitorNewItems"] = monitor_new_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_studio_artist_resource import AlbumStudioArtistResource
        from ..models.monitoring_options import MonitoringOptions

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_artist(
            data: object,
        ) -> Union[None, Unset, list["AlbumStudioArtistResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                artist_type_0 = []
                _artist_type_0 = data
                for artist_type_0_item_data in _artist_type_0:
                    artist_type_0_item = AlbumStudioArtistResource.from_dict(
                        artist_type_0_item_data
                    )

                    artist_type_0.append(artist_type_0_item)

                return artist_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AlbumStudioArtistResource"]], data)

        artist = _parse_artist(d.pop("artist", UNSET))

        _monitoring_options = d.pop("monitoringOptions", UNSET)
        monitoring_options: Union[Unset, MonitoringOptions]
        if isinstance(_monitoring_options, Unset):
            monitoring_options = UNSET
        else:
            monitoring_options = MonitoringOptions.from_dict(_monitoring_options)

        _monitor_new_items = d.pop("monitorNewItems", UNSET)
        monitor_new_items: Union[Unset, NewItemMonitorTypes]
        if isinstance(_monitor_new_items, Unset):
            monitor_new_items = UNSET
        else:
            monitor_new_items = NewItemMonitorTypes(_monitor_new_items)

        album_studio_resource = cls(
            artist=artist,
            monitoring_options=monitoring_options,
            monitor_new_items=monitor_new_items,
        )

        return album_studio_resource
