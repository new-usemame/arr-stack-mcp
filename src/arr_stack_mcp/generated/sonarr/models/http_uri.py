from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpUri")


@_attrs_define
class HttpUri:
    """
    Attributes:
        full_uri (Union[None, Unset, str]):
        scheme (Union[None, Unset, str]):
        host (Union[None, Unset, str]):
        port (Union[None, Unset, int]):
        path (Union[None, Unset, str]):
        query (Union[None, Unset, str]):
        fragment (Union[None, Unset, str]):
    """

    full_uri: Union[None, Unset, str] = UNSET
    scheme: Union[None, Unset, str] = UNSET
    host: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    query: Union[None, Unset, str] = UNSET
    fragment: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        full_uri: Union[None, Unset, str]
        if isinstance(self.full_uri, Unset):
            full_uri = UNSET
        else:
            full_uri = self.full_uri

        scheme: Union[None, Unset, str]
        if isinstance(self.scheme, Unset):
            scheme = UNSET
        else:
            scheme = self.scheme

        host: Union[None, Unset, str]
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        query: Union[None, Unset, str]
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        fragment: Union[None, Unset, str]
        if isinstance(self.fragment, Unset):
            fragment = UNSET
        else:
            fragment = self.fragment

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if full_uri is not UNSET:
            field_dict["fullUri"] = full_uri
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query
        if fragment is not UNSET:
            field_dict["fragment"] = fragment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict):
        # ARRSTACK_HTTPURI_STR_OK — Servarr family serializes some HttpUri
        # fields as plain strings even though the spec models them as objects.
        if isinstance(src_dict, str):
            return cls(full_uri=src_dict)
        d = dict(src_dict)

        def _parse_full_uri(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        full_uri = _parse_full_uri(d.pop("fullUri", UNSET))

        def _parse_scheme(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scheme = _parse_scheme(d.pop("scheme", UNSET))

        def _parse_host(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_query(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_fragment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fragment = _parse_fragment(d.pop("fragment", UNSET))

        http_uri = cls(
            full_uri=full_uri,
            scheme=scheme,
            host=host,
            port=port,
            path=path,
            query=query,
            fragment=fragment,
        )

        return http_uri
