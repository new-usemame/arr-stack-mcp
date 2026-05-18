from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.image_type import ImageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageOption")


@_attrs_define
class ImageOption:
    """
    Attributes:
        type_ (Union[Unset, ImageType]): Enum ImageType.
        limit (Union[Unset, int]): Gets or sets the limit.
        min_width (Union[Unset, int]): Gets or sets the minimum width.
    """

    type_: Union[Unset, ImageType] = UNSET
    limit: Union[Unset, int] = UNSET
    min_width: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        limit = self.limit

        min_width = self.min_width

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if limit is not UNSET:
            field_dict["Limit"] = limit
        if min_width is not UNSET:
            field_dict["MinWidth"] = min_width

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _type_ = d.pop("Type", UNSET)
        type_: Union[Unset, ImageType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ImageType(_type_)

        limit = d.pop("Limit", UNSET)

        min_width = d.pop("MinWidth", UNSET)

        image_option = cls(
            type_=type_,
            limit=limit,
            min_width=min_width,
        )

        return image_option
