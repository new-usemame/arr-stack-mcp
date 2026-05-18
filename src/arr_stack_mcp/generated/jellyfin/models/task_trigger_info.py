from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.task_trigger_info_day_of_week import TaskTriggerInfoDayOfWeek
from ..models.task_trigger_info_type import TaskTriggerInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskTriggerInfo")


@_attrs_define
class TaskTriggerInfo:
    """Class TaskTriggerInfo.

    Attributes:
        type_ (Union[Unset, TaskTriggerInfoType]): Enum TaskTriggerInfoType.
        time_of_day_ticks (Union[None, Unset, int]): Gets or sets the time of day.
        interval_ticks (Union[None, Unset, int]): Gets or sets the interval.
        day_of_week (Union[Unset, TaskTriggerInfoDayOfWeek]): Gets or sets the day of week.
        max_runtime_ticks (Union[None, Unset, int]): Gets or sets the maximum runtime ticks.
    """

    type_: Union[Unset, TaskTriggerInfoType] = UNSET
    time_of_day_ticks: Union[None, Unset, int] = UNSET
    interval_ticks: Union[None, Unset, int] = UNSET
    day_of_week: Union[Unset, TaskTriggerInfoDayOfWeek] = UNSET
    max_runtime_ticks: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        time_of_day_ticks: Union[None, Unset, int]
        if isinstance(self.time_of_day_ticks, Unset):
            time_of_day_ticks = UNSET
        else:
            time_of_day_ticks = self.time_of_day_ticks

        interval_ticks: Union[None, Unset, int]
        if isinstance(self.interval_ticks, Unset):
            interval_ticks = UNSET
        else:
            interval_ticks = self.interval_ticks

        day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        max_runtime_ticks: Union[None, Unset, int]
        if isinstance(self.max_runtime_ticks, Unset):
            max_runtime_ticks = UNSET
        else:
            max_runtime_ticks = self.max_runtime_ticks

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if time_of_day_ticks is not UNSET:
            field_dict["TimeOfDayTicks"] = time_of_day_ticks
        if interval_ticks is not UNSET:
            field_dict["IntervalTicks"] = interval_ticks
        if day_of_week is not UNSET:
            field_dict["DayOfWeek"] = day_of_week
        if max_runtime_ticks is not UNSET:
            field_dict["MaxRuntimeTicks"] = max_runtime_ticks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _type_ = d.pop("Type", UNSET)
        type_: Union[Unset, TaskTriggerInfoType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TaskTriggerInfoType(_type_)

        def _parse_time_of_day_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        time_of_day_ticks = _parse_time_of_day_ticks(d.pop("TimeOfDayTicks", UNSET))

        def _parse_interval_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        interval_ticks = _parse_interval_ticks(d.pop("IntervalTicks", UNSET))

        _day_of_week = d.pop("DayOfWeek", UNSET)
        day_of_week: Union[Unset, TaskTriggerInfoDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = TaskTriggerInfoDayOfWeek(_day_of_week)

        def _parse_max_runtime_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_runtime_ticks = _parse_max_runtime_ticks(d.pop("MaxRuntimeTicks", UNSET))

        task_trigger_info = cls(
            type_=type_,
            time_of_day_ticks=time_of_day_ticks,
            interval_ticks=interval_ticks,
            day_of_week=day_of_week,
            max_runtime_ticks=max_runtime_ticks,
        )

        return task_trigger_info
