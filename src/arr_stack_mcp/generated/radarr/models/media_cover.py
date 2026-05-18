from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.media_cover_types import MediaCoverTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaCover")


@_attrs_define
class MediaCover:
    """
    Attributes:
        cover_type (Union[Unset, MediaCoverTypes]):
        url (Union[None, Unset, str]):
        remote_url (Union[None, Unset, str]):
    """

    cover_type: Union[Unset, MediaCoverTypes] = UNSET
    url: Union[None, Unset, str] = UNSET
    remote_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        cover_type: Union[Unset, str] = UNSET
        if not isinstance(self.cover_type, Unset):
            cover_type = self.cover_type.value

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        remote_url: Union[None, Unset, str]
        if isinstance(self.remote_url, Unset):
            remote_url = UNSET
        else:
            remote_url = self.remote_url

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if cover_type is not UNSET:
            field_dict["coverType"] = cover_type
        if url is not UNSET:
            field_dict["url"] = url
        if remote_url is not UNSET:
            field_dict["remoteUrl"] = remote_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _cover_type = d.pop("coverType", UNSET)
        cover_type: Union[Unset, MediaCoverTypes]
        if isinstance(_cover_type, Unset):
            cover_type = UNSET
        else:
            cover_type = MediaCoverTypes(_cover_type)

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_remote_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_url = _parse_remote_url(d.pop("remoteUrl", UNSET))

        media_cover = cls(
            cover_type=cover_type,
            url=url,
            remote_url=remote_url,
        )

        return media_cover
