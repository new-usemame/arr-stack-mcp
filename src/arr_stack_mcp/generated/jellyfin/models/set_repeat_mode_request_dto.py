from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.group_repeat_mode import GroupRepeatMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetRepeatModeRequestDto")


@_attrs_define
class SetRepeatModeRequestDto:
    """Class SetRepeatModeRequestDto.

    Attributes:
        mode (Union[Unset, GroupRepeatMode]): Enum GroupRepeatMode.
    """

    mode: Union[Unset, GroupRepeatMode] = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _mode = d.pop("Mode", UNSET)
        mode: Union[Unset, GroupRepeatMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GroupRepeatMode(_mode)

        set_repeat_mode_request_dto = cls(
            mode=mode,
        )

        return set_repeat_mode_request_dto
