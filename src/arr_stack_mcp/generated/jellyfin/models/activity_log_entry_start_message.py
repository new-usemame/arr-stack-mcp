from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.session_message_type import SessionMessageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityLogEntryStartMessage")


@_attrs_define
class ActivityLogEntryStartMessage:
    """Activity log entry start message.
    Data is the timing data encoded as "$initialDelay,$interval" in ms.

        Attributes:
            data (Union[None, Unset, str]): Gets or sets the data.
            message_type (Union[Unset, SessionMessageType]): The different kinds of messages that are used in the WebSocket
                api. Default: SessionMessageType.ACTIVITYLOGENTRYSTART.
    """

    data: Union[None, Unset, str] = UNSET
    message_type: Union[Unset, SessionMessageType] = (
        SessionMessageType.ACTIVITYLOGENTRYSTART
    )

    def to_dict(self) -> dict[str, Any]:
        data: Union[None, Unset, str]
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        message_type: Union[Unset, str] = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if data is not UNSET:
            field_dict["Data"] = data
        if message_type is not UNSET:
            field_dict["MessageType"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_data(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data = _parse_data(d.pop("Data", UNSET))

        _message_type = d.pop("MessageType", UNSET)
        message_type: Union[Unset, SessionMessageType]
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = SessionMessageType(_message_type)

        activity_log_entry_start_message = cls(
            data=data,
            message_type=message_type,
        )

        return activity_log_entry_start_message
