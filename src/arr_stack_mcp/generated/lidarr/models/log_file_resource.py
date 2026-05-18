import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogFileResource")


@_attrs_define
class LogFileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        filename (Union[None, Unset, str]):
        last_write_time (Union[Unset, datetime.datetime]):
        contents_url (Union[None, Unset, str]):
        download_url (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    filename: Union[None, Unset, str] = UNSET
    last_write_time: Union[Unset, datetime.datetime] = UNSET
    contents_url: Union[None, Unset, str] = UNSET
    download_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        filename: Union[None, Unset, str]
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        last_write_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_write_time, Unset):
            last_write_time = self.last_write_time.isoformat()

        contents_url: Union[None, Unset, str]
        if isinstance(self.contents_url, Unset):
            contents_url = UNSET
        else:
            contents_url = self.contents_url

        download_url: Union[None, Unset, str]
        if isinstance(self.download_url, Unset):
            download_url = UNSET
        else:
            download_url = self.download_url

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if last_write_time is not UNSET:
            field_dict["lastWriteTime"] = last_write_time
        if contents_url is not UNSET:
            field_dict["contentsUrl"] = contents_url
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_filename(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        filename = _parse_filename(d.pop("filename", UNSET))

        _last_write_time = d.pop("lastWriteTime", UNSET)
        last_write_time: Union[Unset, datetime.datetime]
        if isinstance(_last_write_time, Unset):
            last_write_time = UNSET
        else:
            last_write_time = isoparse(_last_write_time)

        def _parse_contents_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contents_url = _parse_contents_url(d.pop("contentsUrl", UNSET))

        def _parse_download_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_url = _parse_download_url(d.pop("downloadUrl", UNSET))

        log_file_resource = cls(
            id=id,
            filename=filename,
            last_write_time=last_write_time,
            contents_url=contents_url,
            download_url=download_url,
        )

        return log_file_resource
