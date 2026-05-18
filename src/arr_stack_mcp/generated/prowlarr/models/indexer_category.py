from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexerCategory")


@_attrs_define
class IndexerCategory:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        sub_categories (Union[None, Unset, list['IndexerCategory']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    sub_categories: Union[None, Unset, list["IndexerCategory"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        sub_categories: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.sub_categories, Unset):
            sub_categories = UNSET
        elif isinstance(self.sub_categories, list):
            sub_categories = []
            for sub_categories_type_0_item_data in self.sub_categories:
                sub_categories_type_0_item = sub_categories_type_0_item_data.to_dict()
                sub_categories.append(sub_categories_type_0_item)

        else:
            sub_categories = self.sub_categories

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if sub_categories is not UNSET:
            field_dict["subCategories"] = sub_categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_sub_categories(
            data: object,
        ) -> Union[None, Unset, list["IndexerCategory"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sub_categories_type_0 = []
                _sub_categories_type_0 = data
                for sub_categories_type_0_item_data in _sub_categories_type_0:
                    sub_categories_type_0_item = IndexerCategory.from_dict(
                        sub_categories_type_0_item_data
                    )

                    sub_categories_type_0.append(sub_categories_type_0_item)

                return sub_categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IndexerCategory"]], data)

        sub_categories = _parse_sub_categories(d.pop("subCategories", UNSET))

        indexer_category = cls(
            id=id,
            name=name,
            description=description,
            sub_categories=sub_categories,
        )

        return indexer_category
