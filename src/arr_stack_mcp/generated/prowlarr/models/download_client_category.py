from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadClientCategory")


@_attrs_define
class DownloadClientCategory:
    """
    Attributes:
        client_category (Union[None, Unset, str]):
        categories (Union[None, Unset, list[int]]):
    """

    client_category: Union[None, Unset, str] = UNSET
    categories: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_category: Union[None, Unset, str]
        if isinstance(self.client_category, Unset):
            client_category = UNSET
        else:
            client_category = self.client_category

        categories: Union[None, Unset, list[int]]
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = self.categories

        else:
            categories = self.categories

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if client_category is not UNSET:
            field_dict["clientCategory"] = client_category
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_client_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_category = _parse_client_category(d.pop("clientCategory", UNSET))

        def _parse_categories(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = cast(list[int], data)

                return categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        categories = _parse_categories(d.pop("categories", UNSET))

        download_client_category = cls(
            client_category=client_category,
            categories=categories,
        )

        return download_client_category
