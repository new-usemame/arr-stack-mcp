from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemotePathMappingResource")


@_attrs_define
class RemotePathMappingResource:
    """
    Attributes:
        id (Union[Unset, int]):
        host (Union[None, Unset, str]):
        remote_path (Union[None, Unset, str]):
        local_path (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    host: Union[None, Unset, str] = UNSET
    remote_path: Union[None, Unset, str] = UNSET
    local_path: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        host: Union[None, Unset, str]
        if isinstance(self.host, Unset):
            host = UNSET
        else:
            host = self.host

        remote_path: Union[None, Unset, str]
        if isinstance(self.remote_path, Unset):
            remote_path = UNSET
        else:
            remote_path = self.remote_path

        local_path: Union[None, Unset, str]
        if isinstance(self.local_path, Unset):
            local_path = UNSET
        else:
            local_path = self.local_path

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if host is not UNSET:
            field_dict["host"] = host
        if remote_path is not UNSET:
            field_dict["remotePath"] = remote_path
        if local_path is not UNSET:
            field_dict["localPath"] = local_path

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_host(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host = _parse_host(d.pop("host", UNSET))

        def _parse_remote_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_path = _parse_remote_path(d.pop("remotePath", UNSET))

        def _parse_local_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        local_path = _parse_local_path(d.pop("localPath", UNSET))

        remote_path_mapping_resource = cls(
            id=id,
            host=host,
            remote_path=remote_path,
            local_path=local_path,
        )

        return remote_path_mapping_resource
