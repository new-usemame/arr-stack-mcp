import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.command_priority import CommandPriority
from ..models.command_result import CommandResult
from ..models.command_status import CommandStatus
from ..models.command_trigger import CommandTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.command import Command


T = TypeVar("T", bound="CommandResource")


@_attrs_define
class CommandResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        command_name (Union[None, Unset, str]):
        message (Union[None, Unset, str]):
        body (Union[Unset, Command]):
        priority (Union[Unset, CommandPriority]):
        status (Union[Unset, CommandStatus]):
        result (Union[Unset, CommandResult]):
        queued (Union[Unset, datetime.datetime]):
        started (Union[None, Unset, datetime.datetime]):
        ended (Union[None, Unset, datetime.datetime]):
        duration (Union[None, Unset, str]):
        exception (Union[None, Unset, str]):
        trigger (Union[Unset, CommandTrigger]):
        client_user_agent (Union[None, Unset, str]):
        state_change_time (Union[None, Unset, datetime.datetime]):
        send_updates_to_client (Union[Unset, bool]):
        update_scheduled_task (Union[Unset, bool]):
        last_execution_time (Union[None, Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    command_name: Union[None, Unset, str] = UNSET
    message: Union[None, Unset, str] = UNSET
    body: Union[Unset, "Command"] = UNSET
    priority: Union[Unset, CommandPriority] = UNSET
    status: Union[Unset, CommandStatus] = UNSET
    result: Union[Unset, CommandResult] = UNSET
    queued: Union[Unset, datetime.datetime] = UNSET
    started: Union[None, Unset, datetime.datetime] = UNSET
    ended: Union[None, Unset, datetime.datetime] = UNSET
    duration: Union[None, Unset, str] = UNSET
    exception: Union[None, Unset, str] = UNSET
    trigger: Union[Unset, CommandTrigger] = UNSET
    client_user_agent: Union[None, Unset, str] = UNSET
    state_change_time: Union[None, Unset, datetime.datetime] = UNSET
    send_updates_to_client: Union[Unset, bool] = UNSET
    update_scheduled_task: Union[Unset, bool] = UNSET
    last_execution_time: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        command_name: Union[None, Unset, str]
        if isinstance(self.command_name, Unset):
            command_name = UNSET
        else:
            command_name = self.command_name

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        queued: Union[Unset, str] = UNSET
        if not isinstance(self.queued, Unset):
            queued = self.queued.isoformat()

        started: Union[None, Unset, str]
        if isinstance(self.started, Unset):
            started = UNSET
        elif isinstance(self.started, datetime.datetime):
            started = self.started.isoformat()
        else:
            started = self.started

        ended: Union[None, Unset, str]
        if isinstance(self.ended, Unset):
            ended = UNSET
        elif isinstance(self.ended, datetime.datetime):
            ended = self.ended.isoformat()
        else:
            ended = self.ended

        duration: Union[None, Unset, str]
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        exception: Union[None, Unset, str]
        if isinstance(self.exception, Unset):
            exception = UNSET
        else:
            exception = self.exception

        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        client_user_agent: Union[None, Unset, str]
        if isinstance(self.client_user_agent, Unset):
            client_user_agent = UNSET
        else:
            client_user_agent = self.client_user_agent

        state_change_time: Union[None, Unset, str]
        if isinstance(self.state_change_time, Unset):
            state_change_time = UNSET
        elif isinstance(self.state_change_time, datetime.datetime):
            state_change_time = self.state_change_time.isoformat()
        else:
            state_change_time = self.state_change_time

        send_updates_to_client = self.send_updates_to_client

        update_scheduled_task = self.update_scheduled_task

        last_execution_time: Union[None, Unset, str]
        if isinstance(self.last_execution_time, Unset):
            last_execution_time = UNSET
        elif isinstance(self.last_execution_time, datetime.datetime):
            last_execution_time = self.last_execution_time.isoformat()
        else:
            last_execution_time = self.last_execution_time

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if command_name is not UNSET:
            field_dict["commandName"] = command_name
        if message is not UNSET:
            field_dict["message"] = message
        if body is not UNSET:
            field_dict["body"] = body
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if result is not UNSET:
            field_dict["result"] = result
        if queued is not UNSET:
            field_dict["queued"] = queued
        if started is not UNSET:
            field_dict["started"] = started
        if ended is not UNSET:
            field_dict["ended"] = ended
        if duration is not UNSET:
            field_dict["duration"] = duration
        if exception is not UNSET:
            field_dict["exception"] = exception
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if client_user_agent is not UNSET:
            field_dict["clientUserAgent"] = client_user_agent
        if state_change_time is not UNSET:
            field_dict["stateChangeTime"] = state_change_time
        if send_updates_to_client is not UNSET:
            field_dict["sendUpdatesToClient"] = send_updates_to_client
        if update_scheduled_task is not UNSET:
            field_dict["updateScheduledTask"] = update_scheduled_task
        if last_execution_time is not UNSET:
            field_dict["lastExecutionTime"] = last_execution_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command import Command

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_command_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        command_name = _parse_command_name(d.pop("commandName", UNSET))

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        _body = d.pop("body", UNSET)
        body: Union[Unset, Command]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = Command.from_dict(_body)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, CommandPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CommandPriority(_priority)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CommandStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CommandStatus(_status)

        _result = d.pop("result", UNSET)
        result: Union[Unset, CommandResult]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = CommandResult(_result)

        _queued = d.pop("queued", UNSET)
        queued: Union[Unset, datetime.datetime]
        if isinstance(_queued, Unset):
            queued = UNSET
        else:
            queued = isoparse(_queued)

        def _parse_started(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_type_0 = isoparse(data)

                return started_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        started = _parse_started(d.pop("started", UNSET))

        def _parse_ended(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_type_0 = isoparse(data)

                return ended_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ended = _parse_ended(d.pop("ended", UNSET))

        def _parse_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_exception(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exception = _parse_exception(d.pop("exception", UNSET))

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, CommandTrigger]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = CommandTrigger(_trigger)

        def _parse_client_user_agent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_user_agent = _parse_client_user_agent(d.pop("clientUserAgent", UNSET))

        def _parse_state_change_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_change_time_type_0 = isoparse(data)

                return state_change_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        state_change_time = _parse_state_change_time(d.pop("stateChangeTime", UNSET))

        send_updates_to_client = d.pop("sendUpdatesToClient", UNSET)

        update_scheduled_task = d.pop("updateScheduledTask", UNSET)

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

        command_resource = cls(
            id=id,
            name=name,
            command_name=command_name,
            message=message,
            body=body,
            priority=priority,
            status=status,
            result=result,
            queued=queued,
            started=started,
            ended=ended,
            duration=duration,
            exception=exception,
            trigger=trigger,
            client_user_agent=client_user_agent,
            state_change_time=state_change_time,
            send_updates_to_client=send_updates_to_client,
            update_scheduled_task=update_scheduled_task,
            last_execution_time=last_execution_time,
        )

        return command_resource
