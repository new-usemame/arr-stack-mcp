from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackedDownloadStatusMessage")


@_attrs_define
class TrackedDownloadStatusMessage:
    """
    Attributes:
        title (Union[None, Unset, str]):
        messages (Union[None, Unset, list[str]]):
    """

    title: Union[None, Unset, str] = UNSET
    messages: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        messages: Union[None, Unset, list[str]]
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = self.messages

        else:
            messages = self.messages

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_messages(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = cast(list[str], data)

                return messages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        messages = _parse_messages(d.pop("messages", UNSET))

        tracked_download_status_message = cls(
            title=title,
            messages=messages,
        )

        return tracked_download_status_message
