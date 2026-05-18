import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.send_command_type import SendCommandType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendCommand")


@_attrs_define
class SendCommand:
    """Class SendCommand.

    Attributes:
        group_id (Union[Unset, UUID]): Gets the group identifier.
        playlist_item_id (Union[Unset, UUID]): Gets the playlist identifier of the playing item.
        when (Union[Unset, datetime.datetime]): Gets or sets the UTC time when to execute the command.
        position_ticks (Union[None, Unset, int]): Gets the position ticks.
        command (Union[Unset, SendCommandType]): Enum SendCommandType.
        emitted_at (Union[Unset, datetime.datetime]): Gets the UTC time when this command has been emitted.
    """

    group_id: Union[Unset, UUID] = UNSET
    playlist_item_id: Union[Unset, UUID] = UNSET
    when: Union[Unset, datetime.datetime] = UNSET
    position_ticks: Union[None, Unset, int] = UNSET
    command: Union[Unset, SendCommandType] = UNSET
    emitted_at: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id: Union[Unset, str] = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        playlist_item_id: Union[Unset, str] = UNSET
        if not isinstance(self.playlist_item_id, Unset):
            playlist_item_id = str(self.playlist_item_id)

        when: Union[Unset, str] = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.isoformat()

        position_ticks: Union[None, Unset, int]
        if isinstance(self.position_ticks, Unset):
            position_ticks = UNSET
        else:
            position_ticks = self.position_ticks

        command: Union[Unset, str] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.value

        emitted_at: Union[Unset, str] = UNSET
        if not isinstance(self.emitted_at, Unset):
            emitted_at = self.emitted_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id
        if when is not UNSET:
            field_dict["When"] = when
        if position_ticks is not UNSET:
            field_dict["PositionTicks"] = position_ticks
        if command is not UNSET:
            field_dict["Command"] = command
        if emitted_at is not UNSET:
            field_dict["EmittedAt"] = emitted_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _group_id = d.pop("GroupId", UNSET)
        group_id: Union[Unset, UUID]
        if isinstance(_group_id, Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)

        _playlist_item_id = d.pop("PlaylistItemId", UNSET)
        playlist_item_id: Union[Unset, UUID]
        if isinstance(_playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = UUID(_playlist_item_id)

        _when = d.pop("When", UNSET)
        when: Union[Unset, datetime.datetime]
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = isoparse(_when)

        def _parse_position_ticks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position_ticks = _parse_position_ticks(d.pop("PositionTicks", UNSET))

        _command = d.pop("Command", UNSET)
        command: Union[Unset, SendCommandType]
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = SendCommandType(_command)

        _emitted_at = d.pop("EmittedAt", UNSET)
        emitted_at: Union[Unset, datetime.datetime]
        if isinstance(_emitted_at, Unset):
            emitted_at = UNSET
        else:
            emitted_at = isoparse(_emitted_at)

        send_command = cls(
            group_id=group_id,
            playlist_item_id=playlist_item_id,
            when=when,
            position_ticks=position_ticks,
            command=command,
            emitted_at=emitted_at,
        )

        return send_command
