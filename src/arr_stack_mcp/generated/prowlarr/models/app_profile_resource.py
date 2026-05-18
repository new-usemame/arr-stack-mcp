from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppProfileResource")


@_attrs_define
class AppProfileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        enable_rss (Union[Unset, bool]):
        enable_automatic_search (Union[Unset, bool]):
        enable_interactive_search (Union[Unset, bool]):
        minimum_seeders (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    enable_rss: Union[Unset, bool] = UNSET
    enable_automatic_search: Union[Unset, bool] = UNSET
    enable_interactive_search: Union[Unset, bool] = UNSET
    minimum_seeders: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        enable_rss = self.enable_rss

        enable_automatic_search = self.enable_automatic_search

        enable_interactive_search = self.enable_interactive_search

        minimum_seeders = self.minimum_seeders

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enable_rss is not UNSET:
            field_dict["enableRss"] = enable_rss
        if enable_automatic_search is not UNSET:
            field_dict["enableAutomaticSearch"] = enable_automatic_search
        if enable_interactive_search is not UNSET:
            field_dict["enableInteractiveSearch"] = enable_interactive_search
        if minimum_seeders is not UNSET:
            field_dict["minimumSeeders"] = minimum_seeders

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

        enable_rss = d.pop("enableRss", UNSET)

        enable_automatic_search = d.pop("enableAutomaticSearch", UNSET)

        enable_interactive_search = d.pop("enableInteractiveSearch", UNSET)

        minimum_seeders = d.pop("minimumSeeders", UNSET)

        app_profile_resource = cls(
            id=id,
            name=name,
            enable_rss=enable_rss,
            enable_automatic_search=enable_automatic_search,
            enable_interactive_search=enable_interactive_search,
            minimum_seeders=minimum_seeders,
        )

        return app_profile_resource
