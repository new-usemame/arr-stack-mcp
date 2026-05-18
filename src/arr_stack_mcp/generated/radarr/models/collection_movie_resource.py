from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.movie_status_type import MovieStatusType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_cover import MediaCover
    from ..models.ratings import Ratings


T = TypeVar("T", bound="CollectionMovieResource")


@_attrs_define
class CollectionMovieResource:
    """
    Attributes:
        tmdb_id (Union[Unset, int]):
        imdb_id (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        clean_title (Union[None, Unset, str]):
        sort_title (Union[None, Unset, str]):
        status (Union[Unset, MovieStatusType]):
        overview (Union[None, Unset, str]):
        runtime (Union[Unset, int]):
        images (Union[None, Unset, list['MediaCover']]):
        year (Union[Unset, int]):
        ratings (Union[Unset, Ratings]):
        genres (Union[None, Unset, list[str]]):
        folder (Union[None, Unset, str]):
        is_existing (Union[Unset, bool]):
        is_excluded (Union[Unset, bool]):
    """

    tmdb_id: Union[Unset, int] = UNSET
    imdb_id: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    clean_title: Union[None, Unset, str] = UNSET
    sort_title: Union[None, Unset, str] = UNSET
    status: Union[Unset, MovieStatusType] = UNSET
    overview: Union[None, Unset, str] = UNSET
    runtime: Union[Unset, int] = UNSET
    images: Union[None, Unset, list["MediaCover"]] = UNSET
    year: Union[Unset, int] = UNSET
    ratings: Union[Unset, "Ratings"] = UNSET
    genres: Union[None, Unset, list[str]] = UNSET
    folder: Union[None, Unset, str] = UNSET
    is_existing: Union[Unset, bool] = UNSET
    is_excluded: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        tmdb_id = self.tmdb_id

        imdb_id: Union[None, Unset, str]
        if isinstance(self.imdb_id, Unset):
            imdb_id = UNSET
        else:
            imdb_id = self.imdb_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        clean_title: Union[None, Unset, str]
        if isinstance(self.clean_title, Unset):
            clean_title = UNSET
        else:
            clean_title = self.clean_title

        sort_title: Union[None, Unset, str]
        if isinstance(self.sort_title, Unset):
            sort_title = UNSET
        else:
            sort_title = self.sort_title

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        runtime = self.runtime

        images: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.images, Unset):
            images = UNSET
        elif isinstance(self.images, list):
            images = []
            for images_type_0_item_data in self.images:
                images_type_0_item = images_type_0_item_data.to_dict()
                images.append(images_type_0_item)

        else:
            images = self.images

        year = self.year

        ratings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        genres: Union[None, Unset, list[str]]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        folder: Union[None, Unset, str]
        if isinstance(self.folder, Unset):
            folder = UNSET
        else:
            folder = self.folder

        is_existing = self.is_existing

        is_excluded = self.is_excluded

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if tmdb_id is not UNSET:
            field_dict["tmdbId"] = tmdb_id
        if imdb_id is not UNSET:
            field_dict["imdbId"] = imdb_id
        if title is not UNSET:
            field_dict["title"] = title
        if clean_title is not UNSET:
            field_dict["cleanTitle"] = clean_title
        if sort_title is not UNSET:
            field_dict["sortTitle"] = sort_title
        if status is not UNSET:
            field_dict["status"] = status
        if overview is not UNSET:
            field_dict["overview"] = overview
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if images is not UNSET:
            field_dict["images"] = images
        if year is not UNSET:
            field_dict["year"] = year
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if genres is not UNSET:
            field_dict["genres"] = genres
        if folder is not UNSET:
            field_dict["folder"] = folder
        if is_existing is not UNSET:
            field_dict["isExisting"] = is_existing
        if is_excluded is not UNSET:
            field_dict["isExcluded"] = is_excluded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_cover import MediaCover
        from ..models.ratings import Ratings

        d = dict(src_dict)
        tmdb_id = d.pop("tmdbId", UNSET)

        def _parse_imdb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        imdb_id = _parse_imdb_id(d.pop("imdbId", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_clean_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        clean_title = _parse_clean_title(d.pop("cleanTitle", UNSET))

        def _parse_sort_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sort_title = _parse_sort_title(d.pop("sortTitle", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, MovieStatusType]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MovieStatusType(_status)

        def _parse_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        overview = _parse_overview(d.pop("overview", UNSET))

        runtime = d.pop("runtime", UNSET)

        def _parse_images(data: object) -> Union[None, Unset, list["MediaCover"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                images_type_0 = []
                _images_type_0 = data
                for images_type_0_item_data in _images_type_0:
                    images_type_0_item = MediaCover.from_dict(images_type_0_item_data)

                    images_type_0.append(images_type_0_item)

                return images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MediaCover"]], data)

        images = _parse_images(d.pop("images", UNSET))

        year = d.pop("year", UNSET)

        _ratings = d.pop("ratings", UNSET)
        ratings: Union[Unset, Ratings]
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = Ratings.from_dict(_ratings)

        def _parse_genres(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genres_type_0 = cast(list[str], data)

                return genres_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        genres = _parse_genres(d.pop("genres", UNSET))

        def _parse_folder(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        folder = _parse_folder(d.pop("folder", UNSET))

        is_existing = d.pop("isExisting", UNSET)

        is_excluded = d.pop("isExcluded", UNSET)

        collection_movie_resource = cls(
            tmdb_id=tmdb_id,
            imdb_id=imdb_id,
            title=title,
            clean_title=clean_title,
            sort_title=sort_title,
            status=status,
            overview=overview,
            runtime=runtime,
            images=images,
            year=year,
            ratings=ratings,
            genres=genres,
            folder=folder,
            is_existing=is_existing,
            is_excluded=is_excluded,
        )

        return collection_movie_resource
