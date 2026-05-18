from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language import Language
    from ..models.language_profile_item_resource import LanguageProfileItemResource


T = TypeVar("T", bound="LanguageProfileResource")


@_attrs_define
class LanguageProfileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        upgrade_allowed (Union[Unset, bool]):
        cutoff (Union[Unset, Language]):
        languages (Union[None, Unset, list['LanguageProfileItemResource']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    upgrade_allowed: Union[Unset, bool] = UNSET
    cutoff: Union[Unset, "Language"] = UNSET
    languages: Union[None, Unset, list["LanguageProfileItemResource"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        upgrade_allowed = self.upgrade_allowed

        cutoff: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cutoff, Unset):
            cutoff = self.cutoff.to_dict()

        languages: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.languages, Unset):
            languages = UNSET
        elif isinstance(self.languages, list):
            languages = []
            for languages_type_0_item_data in self.languages:
                languages_type_0_item = languages_type_0_item_data.to_dict()
                languages.append(languages_type_0_item)

        else:
            languages = self.languages

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if upgrade_allowed is not UNSET:
            field_dict["upgradeAllowed"] = upgrade_allowed
        if cutoff is not UNSET:
            field_dict["cutoff"] = cutoff
        if languages is not UNSET:
            field_dict["languages"] = languages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.language import Language
        from ..models.language_profile_item_resource import LanguageProfileItemResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        upgrade_allowed = d.pop("upgradeAllowed", UNSET)

        _cutoff = d.pop("cutoff", UNSET)
        cutoff: Union[Unset, Language]
        if isinstance(_cutoff, Unset):
            cutoff = UNSET
        else:
            cutoff = Language.from_dict(_cutoff)

        def _parse_languages(
            data: object,
        ) -> Union[None, Unset, list["LanguageProfileItemResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                languages_type_0 = []
                _languages_type_0 = data
                for languages_type_0_item_data in _languages_type_0:
                    languages_type_0_item = LanguageProfileItemResource.from_dict(
                        languages_type_0_item_data
                    )

                    languages_type_0.append(languages_type_0_item)

                return languages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["LanguageProfileItemResource"]], data)

        languages = _parse_languages(d.pop("languages", UNSET))

        language_profile_resource = cls(
            id=id,
            name=name,
            upgrade_allowed=upgrade_allowed,
            cutoff=cutoff,
            languages=languages,
        )

        return language_profile_resource
