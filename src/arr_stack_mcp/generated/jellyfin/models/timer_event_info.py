from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimerEventInfo")


@_attrs_define
class TimerEventInfo:
    """
    Attributes:
        id (Union[Unset, str]):
        program_id (Union[None, UUID, Unset]):
    """

    id: Union[Unset, str] = UNSET
    program_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        program_id: Union[None, Unset, str]
        if isinstance(self.program_id, Unset):
            program_id = UNSET
        elif isinstance(self.program_id, UUID):
            program_id = str(self.program_id)
        else:
            program_id = self.program_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if program_id is not UNSET:
            field_dict["ProgramId"] = program_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        def _parse_program_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                program_id_type_0 = UUID(data)

                return program_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        program_id = _parse_program_id(d.pop("ProgramId", UNSET))

        timer_event_info = cls(
            id=id,
            program_id=program_id,
        )

        return timer_event_info
