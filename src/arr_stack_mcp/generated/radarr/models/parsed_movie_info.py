from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language import Language
    from ..models.quality_model import QualityModel


T = TypeVar("T", bound="ParsedMovieInfo")


@_attrs_define
class ParsedMovieInfo:
    """
    Attributes:
        movie_titles (Union[None, Unset, list[str]]):
        original_title (Union[None, Unset, str]):
        release_title (Union[None, Unset, str]):
        simple_release_title (Union[None, Unset, str]):
        quality (Union[Unset, QualityModel]):
        languages (Union[None, Unset, list['Language']]):
        release_group (Union[None, Unset, str]):
        release_hash (Union[None, Unset, str]):
        edition (Union[None, Unset, str]):
        year (Union[Unset, int]):
        imdb_id (Union[None, Unset, str]):
        tmdb_id (Union[Unset, int]):
        hardcoded_subs (Union[None, Unset, str]):
        movie_title (Union[None, Unset, str]):
        primary_movie_title (Union[None, Unset, str]):
    """

    movie_titles: Union[None, Unset, list[str]] = UNSET
    original_title: Union[None, Unset, str] = UNSET
    release_title: Union[None, Unset, str] = UNSET
    simple_release_title: Union[None, Unset, str] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    languages: Union[None, Unset, list["Language"]] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    release_hash: Union[None, Unset, str] = UNSET
    edition: Union[None, Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    imdb_id: Union[None, Unset, str] = UNSET
    tmdb_id: Union[Unset, int] = UNSET
    hardcoded_subs: Union[None, Unset, str] = UNSET
    movie_title: Union[None, Unset, str] = UNSET
    primary_movie_title: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        movie_titles: Union[None, Unset, list[str]]
        if isinstance(self.movie_titles, Unset):
            movie_titles = UNSET
        elif isinstance(self.movie_titles, list):
            movie_titles = self.movie_titles

        else:
            movie_titles = self.movie_titles

        original_title: Union[None, Unset, str]
        if isinstance(self.original_title, Unset):
            original_title = UNSET
        else:
            original_title = self.original_title

        release_title: Union[None, Unset, str]
        if isinstance(self.release_title, Unset):
            release_title = UNSET
        else:
            release_title = self.release_title

        simple_release_title: Union[None, Unset, str]
        if isinstance(self.simple_release_title, Unset):
            simple_release_title = UNSET
        else:
            simple_release_title = self.simple_release_title

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

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

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

        release_hash: Union[None, Unset, str]
        if isinstance(self.release_hash, Unset):
            release_hash = UNSET
        else:
            release_hash = self.release_hash

        edition: Union[None, Unset, str]
        if isinstance(self.edition, Unset):
            edition = UNSET
        else:
            edition = self.edition

        year = self.year

        imdb_id: Union[None, Unset, str]
        if isinstance(self.imdb_id, Unset):
            imdb_id = UNSET
        else:
            imdb_id = self.imdb_id

        tmdb_id = self.tmdb_id

        hardcoded_subs: Union[None, Unset, str]
        if isinstance(self.hardcoded_subs, Unset):
            hardcoded_subs = UNSET
        else:
            hardcoded_subs = self.hardcoded_subs

        movie_title: Union[None, Unset, str]
        if isinstance(self.movie_title, Unset):
            movie_title = UNSET
        else:
            movie_title = self.movie_title

        primary_movie_title: Union[None, Unset, str]
        if isinstance(self.primary_movie_title, Unset):
            primary_movie_title = UNSET
        else:
            primary_movie_title = self.primary_movie_title

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if movie_titles is not UNSET:
            field_dict["movieTitles"] = movie_titles
        if original_title is not UNSET:
            field_dict["originalTitle"] = original_title
        if release_title is not UNSET:
            field_dict["releaseTitle"] = release_title
        if simple_release_title is not UNSET:
            field_dict["simpleReleaseTitle"] = simple_release_title
        if quality is not UNSET:
            field_dict["quality"] = quality
        if languages is not UNSET:
            field_dict["languages"] = languages
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if release_hash is not UNSET:
            field_dict["releaseHash"] = release_hash
        if edition is not UNSET:
            field_dict["edition"] = edition
        if year is not UNSET:
            field_dict["year"] = year
        if imdb_id is not UNSET:
            field_dict["imdbId"] = imdb_id
        if tmdb_id is not UNSET:
            field_dict["tmdbId"] = tmdb_id
        if hardcoded_subs is not UNSET:
            field_dict["hardcodedSubs"] = hardcoded_subs
        if movie_title is not UNSET:
            field_dict["movieTitle"] = movie_title
        if primary_movie_title is not UNSET:
            field_dict["primaryMovieTitle"] = primary_movie_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.language import Language
        from ..models.quality_model import QualityModel

        d = dict(src_dict)

        def _parse_movie_titles(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                movie_titles_type_0 = cast(list[str], data)

                return movie_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        movie_titles = _parse_movie_titles(d.pop("movieTitles", UNSET))

        def _parse_original_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        original_title = _parse_original_title(d.pop("originalTitle", UNSET))

        def _parse_release_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_title = _parse_release_title(d.pop("releaseTitle", UNSET))

        def _parse_simple_release_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        simple_release_title = _parse_simple_release_title(
            d.pop("simpleReleaseTitle", UNSET)
        )

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        def _parse_languages(data: object) -> Union[None, Unset, list["Language"]]:
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
                    languages_type_0_item = Language.from_dict(
                        languages_type_0_item_data
                    )

                    languages_type_0.append(languages_type_0_item)

                return languages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Language"]], data)

        languages = _parse_languages(d.pop("languages", UNSET))

        def _parse_release_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_group = _parse_release_group(d.pop("releaseGroup", UNSET))

        def _parse_release_hash(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_hash = _parse_release_hash(d.pop("releaseHash", UNSET))

        def _parse_edition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        edition = _parse_edition(d.pop("edition", UNSET))

        year = d.pop("year", UNSET)

        def _parse_imdb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        imdb_id = _parse_imdb_id(d.pop("imdbId", UNSET))

        tmdb_id = d.pop("tmdbId", UNSET)

        def _parse_hardcoded_subs(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hardcoded_subs = _parse_hardcoded_subs(d.pop("hardcodedSubs", UNSET))

        def _parse_movie_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        movie_title = _parse_movie_title(d.pop("movieTitle", UNSET))

        def _parse_primary_movie_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_movie_title = _parse_primary_movie_title(
            d.pop("primaryMovieTitle", UNSET)
        )

        parsed_movie_info = cls(
            movie_titles=movie_titles,
            original_title=original_title,
            release_title=release_title,
            simple_release_title=simple_release_title,
            quality=quality,
            languages=languages,
            release_group=release_group,
            release_hash=release_hash,
            edition=edition,
            year=year,
            imdb_id=imdb_id,
            tmdb_id=tmdb_id,
            hardcoded_subs=hardcoded_subs,
            movie_title=movie_title,
            primary_movie_title=primary_movie_title,
        )

        return parsed_movie_info
