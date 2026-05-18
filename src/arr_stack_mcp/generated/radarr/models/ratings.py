from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rating_child import RatingChild


T = TypeVar("T", bound="Ratings")


@_attrs_define
class Ratings:
    """
    Attributes:
        imdb (Union[Unset, RatingChild]):
        tmdb (Union[Unset, RatingChild]):
        metacritic (Union[Unset, RatingChild]):
        rotten_tomatoes (Union[Unset, RatingChild]):
        trakt (Union[Unset, RatingChild]):
    """

    imdb: Union[Unset, "RatingChild"] = UNSET
    tmdb: Union[Unset, "RatingChild"] = UNSET
    metacritic: Union[Unset, "RatingChild"] = UNSET
    rotten_tomatoes: Union[Unset, "RatingChild"] = UNSET
    trakt: Union[Unset, "RatingChild"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        imdb: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.imdb, Unset):
            imdb = self.imdb.to_dict()

        tmdb: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tmdb, Unset):
            tmdb = self.tmdb.to_dict()

        metacritic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metacritic, Unset):
            metacritic = self.metacritic.to_dict()

        rotten_tomatoes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rotten_tomatoes, Unset):
            rotten_tomatoes = self.rotten_tomatoes.to_dict()

        trakt: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.trakt, Unset):
            trakt = self.trakt.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if imdb is not UNSET:
            field_dict["imdb"] = imdb
        if tmdb is not UNSET:
            field_dict["tmdb"] = tmdb
        if metacritic is not UNSET:
            field_dict["metacritic"] = metacritic
        if rotten_tomatoes is not UNSET:
            field_dict["rottenTomatoes"] = rotten_tomatoes
        if trakt is not UNSET:
            field_dict["trakt"] = trakt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rating_child import RatingChild

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _imdb = d.pop("imdb", UNSET)
        imdb: Union[Unset, RatingChild]
        if isinstance(_imdb, Unset):
            imdb = UNSET
        else:
            imdb = RatingChild.from_dict(_imdb)

        _tmdb = d.pop("tmdb", UNSET)
        tmdb: Union[Unset, RatingChild]
        if isinstance(_tmdb, Unset):
            tmdb = UNSET
        else:
            tmdb = RatingChild.from_dict(_tmdb)

        _metacritic = d.pop("metacritic", UNSET)
        metacritic: Union[Unset, RatingChild]
        if isinstance(_metacritic, Unset):
            metacritic = UNSET
        else:
            metacritic = RatingChild.from_dict(_metacritic)

        _rotten_tomatoes = d.pop("rottenTomatoes", UNSET)
        rotten_tomatoes: Union[Unset, RatingChild]
        if isinstance(_rotten_tomatoes, Unset):
            rotten_tomatoes = UNSET
        else:
            rotten_tomatoes = RatingChild.from_dict(_rotten_tomatoes)

        _trakt = d.pop("trakt", UNSET)
        trakt: Union[Unset, RatingChild]
        if isinstance(_trakt, Unset):
            trakt = UNSET
        else:
            trakt = RatingChild.from_dict(_trakt)

        ratings = cls(
            imdb=imdb,
            tmdb=tmdb,
            metacritic=metacritic,
            rotten_tomatoes=rotten_tomatoes,
            trakt=trakt,
        )

        return ratings
