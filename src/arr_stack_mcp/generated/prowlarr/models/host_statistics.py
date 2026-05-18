from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostStatistics")


@_attrs_define
class HostStatistics:
    """
    Attributes:
        host (Union[None, Unset, str]):
        number_of_queries (Union[Unset, int]):
        number_of_grabs (Union[Unset, int]):
    """

    host: Union[None, Unset, str] = UNSET
    number_of_queries: Union[Unset, int] = UNSET
    number_of_grabs: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        host: Union[None, Unset, str]
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        number_of_queries = self.number_of_queries

        number_of_grabs = self.number_of_grabs

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if number_of_queries is not UNSET:
            field_dict["numberOfQueries"] = number_of_queries
        if number_of_grabs is not UNSET:
            field_dict["numberOfGrabs"] = number_of_grabs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_host(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host = _parse_host(d.pop("host", UNSET))

        number_of_queries = d.pop("numberOfQueries", UNSET)

        number_of_grabs = d.pop("numberOfGrabs", UNSET)

        host_statistics = cls(
            host=host,
            number_of_queries=number_of_queries,
            number_of_grabs=number_of_grabs,
        )

        return host_statistics
