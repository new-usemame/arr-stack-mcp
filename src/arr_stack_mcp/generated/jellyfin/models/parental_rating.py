from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parental_rating_score import ParentalRatingScore


T = TypeVar("T", bound="ParentalRating")


@_attrs_define
class ParentalRating:
    """Class ParentalRating.

    Attributes:
        name (Union[Unset, str]): Gets or sets the name.
        value (Union[None, Unset, int]): Gets or sets the value.
        rating_score (Union['ParentalRatingScore', None, Unset]): Gets or sets the rating score.
    """

    name: Union[Unset, str] = UNSET
    value: Union[None, Unset, int] = UNSET
    rating_score: Union["ParentalRatingScore", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.parental_rating_score import ParentalRatingScore

        name = self.name

        value: Union[None, Unset, int]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        rating_score: Union[None, Unset, dict[str, Any]]
        if isinstance(self.rating_score, Unset):
            rating_score = UNSET
        elif isinstance(self.rating_score, ParentalRatingScore):
            rating_score = self.rating_score.to_dict()
        else:
            rating_score = self.rating_score

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value
        if rating_score is not UNSET:
            field_dict["RatingScore"] = rating_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parental_rating_score import ParentalRatingScore

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        name = d.pop("Name", UNSET)

        def _parse_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        value = _parse_value(d.pop("Value", UNSET))

        def _parse_rating_score(
            data: object,
        ) -> Union["ParentalRatingScore", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rating_score_type_1 = ParentalRatingScore.from_dict(data)

                return rating_score_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ParentalRatingScore", None, Unset], data)

        rating_score = _parse_rating_score(d.pop("RatingScore", UNSET))

        parental_rating = cls(
            name=name,
            value=value,
            rating_score=rating_score,
        )

        return parental_rating
