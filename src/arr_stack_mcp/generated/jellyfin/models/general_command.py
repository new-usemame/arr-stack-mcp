from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.general_command_type import GeneralCommandType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.general_command_arguments import GeneralCommandArguments


T = TypeVar("T", bound="GeneralCommand")


@_attrs_define
class GeneralCommand:
    """
    Attributes:
        name (Union[Unset, GeneralCommandType]): This exists simply to identify a set of known commands.
        controlling_user_id (Union[Unset, UUID]):
        arguments (Union[Unset, GeneralCommandArguments]):
    """

    name: Union[Unset, GeneralCommandType] = UNSET
    controlling_user_id: Union[Unset, UUID] = UNSET
    arguments: Union[Unset, "GeneralCommandArguments"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        controlling_user_id: Union[Unset, str] = UNSET
        if not isinstance(self.controlling_user_id, Unset):
            controlling_user_id = str(self.controlling_user_id)

        arguments: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if controlling_user_id is not UNSET:
            field_dict["ControllingUserId"] = controlling_user_id
        if arguments is not UNSET:
            field_dict["Arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.general_command_arguments import GeneralCommandArguments

        d = dict(src_dict)
        _name = d.pop("Name", UNSET)
        name: Union[Unset, GeneralCommandType]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = GeneralCommandType(_name)

        _controlling_user_id = d.pop("ControllingUserId", UNSET)
        controlling_user_id: Union[Unset, UUID]
        if isinstance(_controlling_user_id, Unset):
            controlling_user_id = UNSET
        else:
            controlling_user_id = UUID(_controlling_user_id)

        _arguments = d.pop("Arguments", UNSET)
        arguments: Union[Unset, GeneralCommandArguments]
        if isinstance(_arguments, Unset):
            arguments = UNSET
        else:
            arguments = GeneralCommandArguments.from_dict(_arguments)

        general_command = cls(
            name=name,
            controlling_user_id=controlling_user_id,
            arguments=arguments,
        )

        return general_command
