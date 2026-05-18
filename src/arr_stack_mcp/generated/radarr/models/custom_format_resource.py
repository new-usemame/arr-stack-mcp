from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format_specification_schema import (
        CustomFormatSpecificationSchema,
    )


T = TypeVar("T", bound="CustomFormatResource")


@_attrs_define
class CustomFormatResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        include_custom_format_when_renaming (Union[None, Unset, bool]):
        specifications (Union[None, Unset, list['CustomFormatSpecificationSchema']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    include_custom_format_when_renaming: Union[None, Unset, bool] = UNSET
    specifications: Union[None, Unset, list["CustomFormatSpecificationSchema"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        include_custom_format_when_renaming: Union[None, Unset, bool]
        if isinstance(self.include_custom_format_when_renaming, Unset):
            include_custom_format_when_renaming = UNSET
        else:
            include_custom_format_when_renaming = (
                self.include_custom_format_when_renaming
            )

        specifications: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.specifications, Unset):
            specifications = UNSET
        elif isinstance(self.specifications, list):
            specifications = []
            for specifications_type_0_item_data in self.specifications:
                specifications_type_0_item = specifications_type_0_item_data.to_dict()
                specifications.append(specifications_type_0_item)

        else:
            specifications = self.specifications

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if include_custom_format_when_renaming is not UNSET:
            field_dict["includeCustomFormatWhenRenaming"] = (
                include_custom_format_when_renaming
            )
        if specifications is not UNSET:
            field_dict["specifications"] = specifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_format_specification_schema import (
            CustomFormatSpecificationSchema,
        )

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_include_custom_format_when_renaming(
            data: object,
        ) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_custom_format_when_renaming = (
            _parse_include_custom_format_when_renaming(
                d.pop("includeCustomFormatWhenRenaming", UNSET)
            )
        )

        def _parse_specifications(
            data: object,
        ) -> Union[None, Unset, list["CustomFormatSpecificationSchema"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                specifications_type_0 = []
                _specifications_type_0 = data
                for specifications_type_0_item_data in _specifications_type_0:
                    specifications_type_0_item = (
                        CustomFormatSpecificationSchema.from_dict(
                            specifications_type_0_item_data
                        )
                    )

                    specifications_type_0.append(specifications_type_0_item)

                return specifications_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["CustomFormatSpecificationSchema"]], data
            )

        specifications = _parse_specifications(d.pop("specifications", UNSET))

        custom_format_resource = cls(
            id=id,
            name=name,
            include_custom_format_when_renaming=include_custom_format_when_renaming,
            specifications=specifications,
        )

        return custom_format_resource
