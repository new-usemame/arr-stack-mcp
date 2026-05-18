from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ForgotPasswordDto")


@_attrs_define
class ForgotPasswordDto:
    """Forgot Password request body DTO.

    Attributes:
        entered_username (str): Gets or sets the entered username to have its password reset.
    """

    entered_username: str

    def to_dict(self) -> dict[str, Any]:
        entered_username = self.entered_username

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "EnteredUsername": entered_username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        entered_username = d.pop("EnteredUsername")

        forgot_password_dto = cls(
            entered_username=entered_username,
        )

        return forgot_password_dto
