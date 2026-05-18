from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.health_check_result import HealthCheckResult
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_uri import HttpUri


T = TypeVar("T", bound="HealthResource")


@_attrs_define
class HealthResource:
    """
    Attributes:
        id (Union[Unset, int]):
        source (Union[None, Unset, str]):
        type_ (Union[Unset, HealthCheckResult]):
        message (Union[None, Unset, str]):
        wiki_url (Union[Unset, HttpUri]):
    """

    id: Union[Unset, int] = UNSET
    source: Union[None, Unset, str] = UNSET
    type_: Union[Unset, HealthCheckResult] = UNSET
    message: Union[None, Unset, str] = UNSET
    wiki_url: Union[Unset, "HttpUri"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        wiki_url: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.wiki_url, Unset):
            wiki_url = self.wiki_url.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_
        if message is not UNSET:
            field_dict["message"] = message
        if wiki_url is not UNSET:
            field_dict["wikiUrl"] = wiki_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_uri import HttpUri

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, HealthCheckResult]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = HealthCheckResult(_type_)

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        _wiki_url = d.pop("wikiUrl", UNSET)
        wiki_url: Union[Unset, HttpUri]
        if isinstance(_wiki_url, Unset):
            wiki_url = UNSET
        else:
            wiki_url = HttpUri.from_dict(_wiki_url)

        health_resource = cls(
            id=id,
            source=source,
            type_=type_,
            message=message,
            wiki_url=wiki_url,
        )

        return health_resource
