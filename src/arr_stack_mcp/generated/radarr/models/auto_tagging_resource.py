from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_tagging_specification_schema import (
        AutoTaggingSpecificationSchema,
    )


T = TypeVar("T", bound="AutoTaggingResource")


@_attrs_define
class AutoTaggingResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        remove_tags_automatically (Union[Unset, bool]):
        tags (Union[None, Unset, list[int]]):
        specifications (Union[None, Unset, list['AutoTaggingSpecificationSchema']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    remove_tags_automatically: Union[Unset, bool] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    specifications: Union[None, Unset, list["AutoTaggingSpecificationSchema"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        remove_tags_automatically = self.remove_tags_automatically

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

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
        if remove_tags_automatically is not UNSET:
            field_dict["removeTagsAutomatically"] = remove_tags_automatically
        if tags is not UNSET:
            field_dict["tags"] = tags
        if specifications is not UNSET:
            field_dict["specifications"] = specifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_tagging_specification_schema import (
            AutoTaggingSpecificationSchema,
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

        remove_tags_automatically = d.pop("removeTagsAutomatically", UNSET)

        def _parse_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_specifications(
            data: object,
        ) -> Union[None, Unset, list["AutoTaggingSpecificationSchema"]]:
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
                        AutoTaggingSpecificationSchema.from_dict(
                            specifications_type_0_item_data
                        )
                    )

                    specifications_type_0.append(specifications_type_0_item)

                return specifications_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["AutoTaggingSpecificationSchema"]], data
            )

        specifications = _parse_specifications(d.pop("specifications", UNSET))

        auto_tagging_resource = cls(
            id=id,
            name=name,
            remove_tags_automatically=remove_tags_automatically,
            tags=tags,
            specifications=specifications,
        )

        return auto_tagging_resource
