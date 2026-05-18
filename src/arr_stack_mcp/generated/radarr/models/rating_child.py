from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.rating_type import RatingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RatingChild")


@_attrs_define
class RatingChild:
    """
    Attributes:
        votes (Union[Unset, int]):
        value (Union[Unset, float]):
        type_ (Union[Unset, RatingType]):
    """

    votes: Union[Unset, int] = UNSET
    value: Union[Unset, float] = UNSET
    type_: Union[Unset, RatingType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        votes = self.votes

        value = self.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if votes is not UNSET:
            field_dict["votes"] = votes
        if value is not UNSET:
            field_dict["value"] = value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        votes = d.pop("votes", UNSET)

        value = d.pop("value", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, RatingType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RatingType(_type_)

        rating_child = cls(
            votes=votes,
            value=value,
            type_=type_,
        )

        return rating_child
