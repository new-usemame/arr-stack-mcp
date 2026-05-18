from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.rejection_type import RejectionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportRejectionResource")


@_attrs_define
class ImportRejectionResource:
    """
    Attributes:
        reason (Union[None, Unset, str]):
        type_ (Union[Unset, RejectionType]):
    """

    reason: Union[None, Unset, str] = UNSET
    type_: Union[Unset, RejectionType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason: Union[None, Unset, str]
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason = _parse_reason(d.pop("reason", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, RejectionType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RejectionType(_type_)

        import_rejection_resource = cls(
            reason=reason,
            type_=type_,
        )

        return import_rejection_resource
