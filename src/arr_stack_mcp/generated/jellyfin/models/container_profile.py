from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="ContainerProfile")


@_attrs_define
class ContainerProfile:
    """Defines the MediaBrowser.Model.Dlna.ContainerProfile.

    Attributes:
        type_ (Union[Unset, DlnaProfileType]):
        conditions (Union[Unset, list['ProfileCondition']]): Gets or sets the list of
            MediaBrowser.Model.Dlna.ProfileCondition which this container will be applied to.
        container (Union[None, Unset, str]): Gets or sets the container(s) which this container must meet.
        sub_container (Union[None, Unset, str]): Gets or sets the sub container(s) which this container must meet.
    """

    type_: Union[Unset, DlnaProfileType] = UNSET
    conditions: Union[Unset, list["ProfileCondition"]] = UNSET
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
        type_: Union[Unset, DlnaProfileType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DlnaProfileType(_type_)

        conditions = []
        _conditions = d.pop("Conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = ProfileCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

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

        container_profile = cls(
            type_=type_,
            conditions=conditions,
            container=container,
            sub_container=sub_container,
        )

        return container_profile
