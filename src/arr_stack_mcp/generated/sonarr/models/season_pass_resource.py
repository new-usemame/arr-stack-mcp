from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitoring_options import MonitoringOptions
    from ..models.season_pass_series_resource import SeasonPassSeriesResource


T = TypeVar("T", bound="SeasonPassResource")


@_attrs_define
class SeasonPassResource:
    """
    Attributes:
        series (Union[None, Unset, list['SeasonPassSeriesResource']]):
        monitoring_options (Union[Unset, MonitoringOptions]):
    """

    series: Union[None, Unset, list["SeasonPassSeriesResource"]] = UNSET
    monitoring_options: Union[Unset, "MonitoringOptions"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        series: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.series, Unset):
            series = UNSET
        elif isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)

        else:
            series = self.series

        monitoring_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monitoring_options, Unset):
            monitoring_options = self.monitoring_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if series is not UNSET:
            field_dict["series"] = series
        if monitoring_options is not UNSET:
            field_dict["monitoringOptions"] = monitoring_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitoring_options import MonitoringOptions
        from ..models.season_pass_series_resource import SeasonPassSeriesResource

        d = dict(src_dict)

        def _parse_series(
            data: object,
        ) -> Union[None, Unset, list["SeasonPassSeriesResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in _series_type_0:
                    series_type_0_item = SeasonPassSeriesResource.from_dict(
                        series_type_0_item_data
                    )

                    series_type_0.append(series_type_0_item)

                return series_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SeasonPassSeriesResource"]], data)

        series = _parse_series(d.pop("series", UNSET))

        _monitoring_options = d.pop("monitoringOptions", UNSET)
        monitoring_options: Union[Unset, MonitoringOptions]
        if isinstance(_monitoring_options, Unset):
            monitoring_options = UNSET
        else:
            monitoring_options = MonitoringOptions.from_dict(_monitoring_options)

        season_pass_resource = cls(
            series=series,
            monitoring_options=monitoring_options,
        )

        return season_pass_resource
