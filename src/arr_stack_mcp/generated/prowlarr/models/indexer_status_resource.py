import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexerStatusResource")


@_attrs_define
class IndexerStatusResource:
    """
    Attributes:
        id (Union[Unset, int]):
        indexer_id (Union[Unset, int]):
        disabled_till (Union[None, Unset, datetime.datetime]):
        most_recent_failure (Union[None, Unset, datetime.datetime]):
        initial_failure (Union[None, Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    indexer_id: Union[Unset, int] = UNSET
    disabled_till: Union[None, Unset, datetime.datetime] = UNSET
    most_recent_failure: Union[None, Unset, datetime.datetime] = UNSET
    initial_failure: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        indexer_id = self.indexer_id

        disabled_till: Union[None, Unset, str]
        if isinstance(self.disabled_till, Unset):
            disabled_till = UNSET
        elif isinstance(self.disabled_till, datetime.datetime):
            disabled_till = self.disabled_till.isoformat()
        else:
            disabled_till = self.disabled_till

        most_recent_failure: Union[None, Unset, str]
        if isinstance(self.most_recent_failure, Unset):
            most_recent_failure = UNSET
        elif isinstance(self.most_recent_failure, datetime.datetime):
            most_recent_failure = self.most_recent_failure.isoformat()
        else:
            most_recent_failure = self.most_recent_failure

        initial_failure: Union[None, Unset, str]
        if isinstance(self.initial_failure, Unset):
            initial_failure = UNSET
        elif isinstance(self.initial_failure, datetime.datetime):
            initial_failure = self.initial_failure.isoformat()
        else:
            initial_failure = self.initial_failure

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if indexer_id is not UNSET:
            field_dict["indexerId"] = indexer_id
        if disabled_till is not UNSET:
            field_dict["disabledTill"] = disabled_till
        if most_recent_failure is not UNSET:
            field_dict["mostRecentFailure"] = most_recent_failure
        if initial_failure is not UNSET:
            field_dict["initialFailure"] = initial_failure

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        indexer_id = d.pop("indexerId", UNSET)

        def _parse_disabled_till(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_till_type_0 = isoparse(data)

                return disabled_till_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        disabled_till = _parse_disabled_till(d.pop("disabledTill", UNSET))

        def _parse_most_recent_failure(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                most_recent_failure_type_0 = isoparse(data)

                return most_recent_failure_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        most_recent_failure = _parse_most_recent_failure(
            d.pop("mostRecentFailure", UNSET)
        )

        def _parse_initial_failure(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                initial_failure_type_0 = isoparse(data)

                return initial_failure_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        initial_failure = _parse_initial_failure(d.pop("initialFailure", UNSET))

        indexer_status_resource = cls(
            id=id,
            indexer_id=indexer_id,
            disabled_till=disabled_till,
            most_recent_failure=most_recent_failure,
            initial_failure=initial_failure,
        )

        return indexer_status_resource
