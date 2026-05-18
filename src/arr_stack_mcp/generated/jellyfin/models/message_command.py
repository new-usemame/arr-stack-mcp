from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageCommand")


@_attrs_define
class MessageCommand:
    """
    Attributes:
        text (str):
        header (Union[None, Unset, str]):
        timeout_ms (Union[None, Unset, int]):
    """

    text: str
    header: Union[None, Unset, str] = UNSET
    timeout_ms: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        header: Union[None, Unset, str]
        if isinstance(self.header, Unset):
            header = UNSET
        else:
            header = self.header

        timeout_ms: Union[None, Unset, int]
        if isinstance(self.timeout_ms, Unset):
            timeout_ms = UNSET
        else:
            timeout_ms = self.timeout_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "Text": text,
            }
        )
        if header is not UNSET:
            field_dict["Header"] = header
        if timeout_ms is not UNSET:
            field_dict["TimeoutMs"] = timeout_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("Text")

        def _parse_header(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        header = _parse_header(d.pop("Header", UNSET))

        def _parse_timeout_ms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timeout_ms = _parse_timeout_ms(d.pop("TimeoutMs", UNSET))

        message_command = cls(
            text=text,
            header=header,
            timeout_ms=timeout_ms,
        )

        return message_command
