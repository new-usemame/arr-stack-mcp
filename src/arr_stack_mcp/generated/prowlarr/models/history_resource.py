import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.history_event_type import HistoryEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.history_resource_data_type_0 import HistoryResourceDataType0


T = TypeVar("T", bound="HistoryResource")


@_attrs_define
class HistoryResource:
    """
    Attributes:
        id (Union[Unset, int]):
        indexer_id (Union[Unset, int]):
        date (Union[Unset, datetime.datetime]):
        download_id (Union[None, Unset, str]):
        successful (Union[Unset, bool]):
        event_type (Union[Unset, HistoryEventType]):
        data (Union['HistoryResourceDataType0', None, Unset]):
    """

    id: Union[Unset, int] = UNSET
    indexer_id: Union[Unset, int] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    download_id: Union[None, Unset, str] = UNSET
    successful: Union[Unset, bool] = UNSET
    event_type: Union[Unset, HistoryEventType] = UNSET
    data: Union["HistoryResourceDataType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.history_resource_data_type_0 import HistoryResourceDataType0

        id = self.id

        indexer_id = self.indexer_id

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        successful = self.successful

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, HistoryResourceDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if indexer_id is not UNSET:
            field_dict["indexerId"] = indexer_id
        if date is not UNSET:
            field_dict["date"] = date
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if successful is not UNSET:
            field_dict["successful"] = successful
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.history_resource_data_type_0 import HistoryResourceDataType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        indexer_id = d.pop("indexerId", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        successful = d.pop("successful", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, HistoryEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = HistoryEventType(_event_type)

        def _parse_data(data: object) -> Union["HistoryResourceDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = HistoryResourceDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HistoryResourceDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        history_resource = cls(
            id=id,
            indexer_id=indexer_id,
            date=date,
            download_id=download_id,
            successful=successful,
            event_type=event_type,
            data=data,
        )

        return history_resource
