from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.codec_type import CodecType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="CodecProfile")


@_attrs_define
class CodecProfile:
    """Defines the MediaBrowser.Model.Dlna.CodecProfile.

    Attributes:
        type_ (Union[Unset, CodecType]):
        conditions (Union[Unset, list['ProfileCondition']]): Gets or sets the list of
            MediaBrowser.Model.Dlna.ProfileCondition which this profile must meet.
        apply_conditions (Union[Unset, list['ProfileCondition']]): Gets or sets the list of
            MediaBrowser.Model.Dlna.ProfileCondition to apply if this profile is met.
        codec (Union[None, Unset, str]): Gets or sets the codec(s) that this profile applies to.
        container (Union[None, Unset, str]): Gets or sets the container(s) which this profile will be applied to.
        sub_container (Union[None, Unset, str]): Gets or sets the sub-container(s) which this profile will be applied
            to.
    """

    type_: Union[Unset, CodecType] = UNSET
    conditions: Union[Unset, list["ProfileCondition"]] = UNSET
    apply_conditions: Union[Unset, list["ProfileCondition"]] = UNSET
    codec: Union[None, Unset, str] = UNSET
    container: Union[None, Unset, str] = UNSET
    sub_container: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        apply_conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apply_conditions, Unset):
            apply_conditions = []
            for apply_conditions_item_data in self.apply_conditions:
                apply_conditions_item = apply_conditions_item_data.to_dict()
                apply_conditions.append(apply_conditions_item)

        codec: Union[None, Unset, str]
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

        container: Union[None, Unset, str]
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        sub_container: Union[None, Unset, str]
        if isinstance(self.sub_container, Unset):
            sub_container = UNSET
        else:
            sub_container = self.sub_container

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if apply_conditions is not UNSET:
            field_dict["ApplyConditions"] = apply_conditions
        if codec is not UNSET:
            field_dict["Codec"] = codec
        if container is not UNSET:
            field_dict["Container"] = container
        if sub_container is not UNSET:
            field_dict["SubContainer"] = sub_container

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = dict(src_dict)
        _type_ = d.pop("Type", UNSET)
        type_: Union[Unset, CodecType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CodecType(_type_)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ProfileCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        apply_conditions = []
        _apply_conditions = d.pop("ApplyConditions", UNSET)
        for apply_conditions_item_data in _apply_conditions or []:
            apply_conditions_item = ProfileCondition.from_dict(
                apply_conditions_item_data
            )

            apply_conditions.append(apply_conditions_item)

        def _parse_codec(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codec = _parse_codec(d.pop("Codec", UNSET))

        def _parse_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        container = _parse_container(d.pop("Container", UNSET))

        def _parse_sub_container(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sub_container = _parse_sub_container(d.pop("SubContainer", UNSET))

        codec_profile = cls(
            type_=type_,
            conditions=conditions,
            apply_conditions=apply_conditions,
            codec=codec,
            container=container,
            sub_container=sub_container,
        )

        return codec_profile
