from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeekRequestDto")


@_attrs_define
class SeekRequestDto:
    """Class SeekRequestDto.

    Attributes:
        position_ticks (Union[Unset, int]): Gets or sets the position ticks.
    """

    position_ticks: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        position_ticks = self.position_ticks

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        position_ticks = d.pop("PositionTicks", UNSET)

        seek_request_dto = cls(
            position_ticks=position_ticks,
        )

        return seek_request_dto
