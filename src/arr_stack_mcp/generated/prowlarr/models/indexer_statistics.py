from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexerStatistics")


@_attrs_define
class IndexerStatistics:
    """
    Attributes:
        indexer_id (Union[Unset, int]):
        indexer_name (Union[None, Unset, str]):
        average_response_time (Union[Unset, int]):
        average_grab_response_time (Union[Unset, int]):
        number_of_queries (Union[Unset, int]):
        number_of_grabs (Union[Unset, int]):
        number_of_rss_queries (Union[Unset, int]):
        number_of_auth_queries (Union[Unset, int]):
        number_of_failed_queries (Union[Unset, int]):
        number_of_failed_grabs (Union[Unset, int]):
        number_of_failed_rss_queries (Union[Unset, int]):
        number_of_failed_auth_queries (Union[Unset, int]):
    """

    indexer_id: Union[Unset, int] = UNSET
    indexer_name: Union[None, Unset, str] = UNSET
    average_response_time: Union[Unset, int] = UNSET
    average_grab_response_time: Union[Unset, int] = UNSET
    number_of_queries: Union[Unset, int] = UNSET
    number_of_grabs: Union[Unset, int] = UNSET
    number_of_rss_queries: Union[Unset, int] = UNSET
    number_of_auth_queries: Union[Unset, int] = UNSET
    number_of_failed_queries: Union[Unset, int] = UNSET
    number_of_failed_grabs: Union[Unset, int] = UNSET
    number_of_failed_rss_queries: Union[Unset, int] = UNSET
    number_of_failed_auth_queries: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        indexer_id = self.indexer_id

        indexer_name: Union[None, Unset, str]
        if isinstance(self.indexer_name, Unset):
            indexer_name = UNSET
        else:
            indexer_name = self.indexer_name

        average_response_time = self.average_response_time

        average_grab_response_time = self.average_grab_response_time

        number_of_queries = self.number_of_queries

        number_of_grabs = self.number_of_grabs

        number_of_rss_queries = self.number_of_rss_queries

        number_of_auth_queries = self.number_of_auth_queries

        number_of_failed_queries = self.number_of_failed_queries

        number_of_failed_grabs = self.number_of_failed_grabs

        number_of_failed_rss_queries = self.number_of_failed_rss_queries

        number_of_failed_auth_queries = self.number_of_failed_auth_queries

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if indexer_id is not UNSET:
            field_dict["indexerId"] = indexer_id
        if indexer_name is not UNSET:
            field_dict["indexerName"] = indexer_name
        if average_response_time is not UNSET:
            field_dict["averageResponseTime"] = average_response_time
        if average_grab_response_time is not UNSET:
            field_dict["averageGrabResponseTime"] = average_grab_response_time
        if number_of_queries is not UNSET:
            field_dict["numberOfQueries"] = number_of_queries
        if number_of_grabs is not UNSET:
            field_dict["numberOfGrabs"] = number_of_grabs
        if number_of_rss_queries is not UNSET:
            field_dict["numberOfRssQueries"] = number_of_rss_queries
        if number_of_auth_queries is not UNSET:
            field_dict["numberOfAuthQueries"] = number_of_auth_queries
        if number_of_failed_queries is not UNSET:
            field_dict["numberOfFailedQueries"] = number_of_failed_queries
        if number_of_failed_grabs is not UNSET:
            field_dict["numberOfFailedGrabs"] = number_of_failed_grabs
        if number_of_failed_rss_queries is not UNSET:
            field_dict["numberOfFailedRssQueries"] = number_of_failed_rss_queries
        if number_of_failed_auth_queries is not UNSET:
            field_dict["numberOfFailedAuthQueries"] = number_of_failed_auth_queries

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        indexer_id = d.pop("indexerId", UNSET)

        def _parse_indexer_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        indexer_name = _parse_indexer_name(d.pop("indexerName", UNSET))

        average_response_time = d.pop("averageResponseTime", UNSET)

        average_grab_response_time = d.pop("averageGrabResponseTime", UNSET)

        number_of_queries = d.pop("numberOfQueries", UNSET)

        number_of_grabs = d.pop("numberOfGrabs", UNSET)

        number_of_rss_queries = d.pop("numberOfRssQueries", UNSET)

        number_of_auth_queries = d.pop("numberOfAuthQueries", UNSET)

        number_of_failed_queries = d.pop("numberOfFailedQueries", UNSET)

        number_of_failed_grabs = d.pop("numberOfFailedGrabs", UNSET)

        number_of_failed_rss_queries = d.pop("numberOfFailedRssQueries", UNSET)

        number_of_failed_auth_queries = d.pop("numberOfFailedAuthQueries", UNSET)

        indexer_statistics = cls(
            indexer_id=indexer_id,
            indexer_name=indexer_name,
            average_response_time=average_response_time,
            average_grab_response_time=average_grab_response_time,
            number_of_queries=number_of_queries,
            number_of_grabs=number_of_grabs,
            number_of_rss_queries=number_of_rss_queries,
            number_of_auth_queries=number_of_auth_queries,
            number_of_failed_queries=number_of_failed_queries,
            number_of_failed_grabs=number_of_failed_grabs,
            number_of_failed_rss_queries=number_of_failed_rss_queries,
            number_of_failed_auth_queries=number_of_failed_auth_queries,
        )

        return indexer_statistics
