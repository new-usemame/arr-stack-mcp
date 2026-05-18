from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CastReceiverApplication")


@_attrs_define
class CastReceiverApplication:
    """The cast receiver application model.

    Attributes:
        id (Union[Unset, str]): Gets or sets the cast receiver application id.
        name (Union[Unset, str]): Gets or sets the cast receiver application name.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        name = d.pop("Name", UNSET)

        cast_receiver_application = cls(
            id=id,
            name=name,
        )

        return cast_receiver_application
