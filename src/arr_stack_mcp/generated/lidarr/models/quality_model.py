from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality import Quality
    from ..models.revision import Revision


T = TypeVar("T", bound="QualityModel")


@_attrs_define
class QualityModel:
    """
    Attributes:
        quality (Union[Unset, Quality]):
        revision (Union[Unset, Revision]):
    """

    quality: Union[Unset, "Quality"] = UNSET
    revision: Union[Unset, "Revision"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        revision: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.revision, Unset):
            revision = self.revision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if quality is not UNSET:
            field_dict["quality"] = quality
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quality import Quality
        from ..models.revision import Revision

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, Quality]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = Quality.from_dict(_quality)

        _revision = d.pop("revision", UNSET)
        revision: Union[Unset, Revision]
        if isinstance(_revision, Unset):
            revision = UNSET
        else:
            revision = Revision.from_dict(_revision)

        quality_model = cls(
            quality=quality,
            revision=revision,
        )

        return quality_model
