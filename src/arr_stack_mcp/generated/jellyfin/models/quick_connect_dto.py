from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="QuickConnectDto")


@_attrs_define
class QuickConnectDto:
    """The quick connect request body.

    Attributes:
        secret (str): Gets or sets the quick connect secret.
    """

    secret: str

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "Secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        secret = d.pop("Secret")

        quick_connect_dto = cls(
            secret=secret,
        )

        return quick_connect_dto
