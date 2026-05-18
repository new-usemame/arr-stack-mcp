from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevelopmentConfigResource")


@_attrs_define
class DevelopmentConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        console_log_level (Union[None, Unset, str]):
        log_sql (Union[Unset, bool]):
        log_indexer_response (Union[Unset, bool]):
        log_rotate (Union[Unset, int]):
        filter_sentry_events (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    console_log_level: Union[None, Unset, str] = UNSET
    log_sql: Union[Unset, bool] = UNSET
    log_indexer_response: Union[Unset, bool] = UNSET
    log_rotate: Union[Unset, int] = UNSET
    filter_sentry_events: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        console_log_level: Union[None, Unset, str]
        if isinstance(self.console_log_level, Unset):
            console_log_level = UNSET
        else:
            console_log_level = self.console_log_level

        log_sql = self.log_sql

        log_indexer_response = self.log_indexer_response

        log_rotate = self.log_rotate

        filter_sentry_events = self.filter_sentry_events

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if console_log_level is not UNSET:
            field_dict["consoleLogLevel"] = console_log_level
        if log_sql is not UNSET:
            field_dict["logSql"] = log_sql
        if log_indexer_response is not UNSET:
            field_dict["logIndexerResponse"] = log_indexer_response
        if log_rotate is not UNSET:
            field_dict["logRotate"] = log_rotate
        if filter_sentry_events is not UNSET:
            field_dict["filterSentryEvents"] = filter_sentry_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_console_log_level(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        console_log_level = _parse_console_log_level(d.pop("consoleLogLevel", UNSET))

        log_sql = d.pop("logSql", UNSET)

        log_indexer_response = d.pop("logIndexerResponse", UNSET)

        log_rotate = d.pop("logRotate", UNSET)

        filter_sentry_events = d.pop("filterSentryEvents", UNSET)

        development_config_resource = cls(
            id=id,
            console_log_level=console_log_level,
            log_sql=log_sql,
            log_indexer_response=log_indexer_response,
            log_rotate=log_rotate,
            filter_sentry_events=filter_sentry_events,
        )

        return development_config_resource
