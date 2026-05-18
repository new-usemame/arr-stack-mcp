import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.command_trigger import CommandTrigger
from ..types import UNSET, Unset

T = TypeVar("T", bound="Command")


@_attrs_define
class Command:
    """
    Attributes:
        send_updates_to_client (Union[Unset, bool]):
        update_scheduled_task (Union[Unset, bool]):
        completion_message (Union[None, Unset, str]):
        requires_disk_access (Union[Unset, bool]):
        is_exclusive (Union[Unset, bool]):
        is_type_exclusive (Union[Unset, bool]):
        is_long_running (Union[Unset, bool]):
        name (Union[None, Unset, str]):
        last_execution_time (Union[None, Unset, datetime.datetime]):
        last_start_time (Union[None, Unset, datetime.datetime]):
        trigger (Union[Unset, CommandTrigger]):
        suppress_messages (Union[Unset, bool]):
        client_user_agent (Union[None, Unset, str]):
    """

    send_updates_to_client: Union[Unset, bool] = UNSET
    update_scheduled_task: Union[Unset, bool] = UNSET
    completion_message: Union[None, Unset, str] = UNSET
    requires_disk_access: Union[Unset, bool] = UNSET
    is_exclusive: Union[Unset, bool] = UNSET
    is_type_exclusive: Union[Unset, bool] = UNSET
    is_long_running: Union[Unset, bool] = UNSET
    name: Union[None, Unset, str] = UNSET
    last_execution_time: Union[None, Unset, datetime.datetime] = UNSET
    last_start_time: Union[None, Unset, datetime.datetime] = UNSET
    trigger: Union[Unset, CommandTrigger] = UNSET
    suppress_messages: Union[Unset, bool] = UNSET
    client_user_agent: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        send_updates_to_client = self.send_updates_to_client

        update_scheduled_task = self.update_scheduled_task

        completion_message: Union[None, Unset, str]
        if isinstance(self.completion_message, Unset):
            completion_message = UNSET
        else:
            completion_message = self.completion_message

        requires_disk_access = self.requires_disk_access

        is_exclusive = self.is_exclusive

        is_type_exclusive = self.is_type_exclusive

        is_long_running = self.is_long_running

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        last_execution_time: Union[None, Unset, str]
        if isinstance(self.last_execution_time, Unset):
            last_execution_time = UNSET
        elif isinstance(self.last_execution_time, datetime.datetime):
            last_execution_time = self.last_execution_time.isoformat()
        else:
            last_execution_time = self.last_execution_time

        last_start_time: Union[None, Unset, str]
        if isinstance(self.last_start_time, Unset):
            last_start_time = UNSET
        elif isinstance(self.last_start_time, datetime.datetime):
            last_start_time = self.last_start_time.isoformat()
        else:
            last_start_time = self.last_start_time

        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        suppress_messages = self.suppress_messages

        client_user_agent: Union[None, Unset, str]
        if isinstance(self.client_user_agent, Unset):
            client_user_agent = UNSET
        else:
            client_user_agent = self.client_user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if send_updates_to_client is not UNSET:
            field_dict["sendUpdatesToClient"] = send_updates_to_client
        if update_scheduled_task is not UNSET:
            field_dict["updateScheduledTask"] = update_scheduled_task
        if completion_message is not UNSET:
            field_dict["completionMessage"] = completion_message
        if requires_disk_access is not UNSET:
            field_dict["requiresDiskAccess"] = requires_disk_access
        if is_exclusive is not UNSET:
            field_dict["isExclusive"] = is_exclusive
        if is_type_exclusive is not UNSET:
            field_dict["isTypeExclusive"] = is_type_exclusive
        if is_long_running is not UNSET:
            field_dict["isLongRunning"] = is_long_running
        if name is not UNSET:
            field_dict["name"] = name
        if last_execution_time is not UNSET:
            field_dict["lastExecutionTime"] = last_execution_time
        if last_start_time is not UNSET:
            field_dict["lastStartTime"] = last_start_time
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if suppress_messages is not UNSET:
            field_dict["suppressMessages"] = suppress_messages
        if client_user_agent is not UNSET:
            field_dict["clientUserAgent"] = client_user_agent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        send_updates_to_client = d.pop("sendUpdatesToClient", UNSET)

        update_scheduled_task = d.pop("updateScheduledTask", UNSET)

        def _parse_completion_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completion_message = _parse_completion_message(
            d.pop("completionMessage", UNSET)
        )

        requires_disk_access = d.pop("requiresDiskAccess", UNSET)

        is_exclusive = d.pop("isExclusive", UNSET)

        is_type_exclusive = d.pop("isTypeExclusive", UNSET)

        is_long_running = d.pop("isLongRunning", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_last_execution_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_execution_time_type_0 = isoparse(data)

                return last_execution_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_execution_time = _parse_last_execution_time(
            d.pop("lastExecutionTime", UNSET)
        )

        def _parse_last_start_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_start_time_type_0 = isoparse(data)

                return last_start_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_start_time = _parse_last_start_time(d.pop("lastStartTime", UNSET))

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, CommandTrigger]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = CommandTrigger(_trigger)

        suppress_messages = d.pop("suppressMessages", UNSET)

        def _parse_client_user_agent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_user_agent = _parse_client_user_agent(d.pop("clientUserAgent", UNSET))

        command = cls(
            send_updates_to_client=send_updates_to_client,
            update_scheduled_task=update_scheduled_task,
            completion_message=completion_message,
            requires_disk_access=requires_disk_access,
            is_exclusive=is_exclusive,
            is_type_exclusive=is_type_exclusive,
            is_long_running=is_long_running,
            name=name,
            last_execution_time=last_execution_time,
            last_start_time=last_start_time,
            trigger=trigger,
            suppress_messages=suppress_messages,
            client_user_agent=client_user_agent,
        )

        return command
