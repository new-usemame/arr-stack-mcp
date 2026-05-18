from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IgnoreWaitRequestDto")


@_attrs_define
class IgnoreWaitRequestDto:
    """Class IgnoreWaitRequestDto.

    Attributes:
        ignore_wait (Union[Unset, bool]): Gets or sets a value indicating whether the client should be ignored.
    """

    ignore_wait: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ignore_wait = self.ignore_wait

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ignore_wait is not UNSET:
            field_dict["IgnoreWait"] = ignore_wait

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        ignore_wait = d.pop("IgnoreWait", UNSET)

        ignore_wait_request_dto = cls(
            ignore_wait=ignore_wait,
        )

        return ignore_wait_request_dto
