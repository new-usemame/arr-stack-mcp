from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language import Language


T = TypeVar("T", bound="LanguageProfileItemResource")


@_attrs_define
class LanguageProfileItemResource:
    """
    Attributes:
        id (Union[Unset, int]):
        language (Union[Unset, Language]):
        allowed (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    language: Union[Unset, "Language"] = UNSET
    allowed: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        language: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        allowed = self.allowed

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if allowed is not UNSET:
            field_dict["allowed"] = allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.language import Language

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, Language]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language.from_dict(_language)

        allowed = d.pop("allowed", UNSET)

        language_profile_item_resource = cls(
            id=id,
            language=language,
            allowed=allowed,
        )

        return language_profile_item_resource
