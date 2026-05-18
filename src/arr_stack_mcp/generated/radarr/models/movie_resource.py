import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.movie_status_type import MovieStatusType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_movie_options import AddMovieOptions
    from ..models.alternative_title_resource import AlternativeTitleResource
    from ..models.language import Language
    from ..models.media_cover import MediaCover
    from ..models.movie_collection_resource import MovieCollectionResource
    from ..models.movie_file_resource import MovieFileResource
    from ..models.movie_statistics_resource import MovieStatisticsResource
    from ..models.ratings import Ratings


T = TypeVar("T", bound="MovieResource")


@_attrs_define
class MovieResource:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[None, Unset, str]):
        original_title (Union[None, Unset, str]):
        original_language (Union[Unset, Language]):
        alternate_titles (Union[None, Unset, list['AlternativeTitleResource']]):
        secondary_year (Union[None, Unset, int]):
        secondary_year_source_id (Union[Unset, int]):
        sort_title (Union[None, Unset, str]):
        size_on_disk (Union[None, Unset, int]):
        status (Union[Unset, MovieStatusType]):
        overview (Union[None, Unset, str]):
        in_cinemas (Union[None, Unset, datetime.datetime]):
        physical_release (Union[None, Unset, datetime.datetime]):
        digital_release (Union[None, Unset, datetime.datetime]):
        release_date (Union[None, Unset, datetime.datetime]):
        physical_release_note (Union[None, Unset, str]):
        images (Union[None, Unset, list['MediaCover']]):
        website (Union[None, Unset, str]):
        remote_poster (Union[None, Unset, str]):
        year (Union[Unset, int]):
        you_tube_trailer_id (Union[None, Unset, str]):
        studio (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        quality_profile_id (Union[Unset, int]):
        has_file (Union[None, Unset, bool]):
        movie_file_id (Union[Unset, int]):
        monitored (Union[Unset, bool]):
        minimum_availability (Union[Unset, MovieStatusType]):
        is_available (Union[Unset, bool]):
        folder_name (Union[None, Unset, str]):
        runtime (Union[Unset, int]):
        clean_title (Union[None, Unset, str]):
        imdb_id (Union[None, Unset, str]):
        tmdb_id (Union[Unset, int]):
        title_slug (Union[None, Unset, str]):
        root_folder_path (Union[None, Unset, str]):
        folder (Union[None, Unset, str]):
        certification (Union[None, Unset, str]):
        genres (Union[None, Unset, list[str]]):
        keywords (Union[None, Unset, list[str]]):
        tags (Union[None, Unset, list[int]]):
        added (Union[Unset, datetime.datetime]):
        add_options (Union[Unset, AddMovieOptions]):
        ratings (Union[Unset, Ratings]):
        movie_file (Union[Unset, MovieFileResource]):
        collection (Union[Unset, MovieCollectionResource]):
        popularity (Union[Unset, float]):
        last_search_time (Union[None, Unset, datetime.datetime]):
        statistics (Union[Unset, MovieStatisticsResource]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    original_title: Union[None, Unset, str] = UNSET
    original_language: Union[Unset, "Language"] = UNSET
    alternate_titles: Union[None, Unset, list["AlternativeTitleResource"]] = UNSET
    secondary_year: Union[None, Unset, int] = UNSET
    secondary_year_source_id: Union[Unset, int] = UNSET
    sort_title: Union[None, Unset, str] = UNSET
    size_on_disk: Union[None, Unset, int] = UNSET
    status: Union[Unset, MovieStatusType] = UNSET
    overview: Union[None, Unset, str] = UNSET
    in_cinemas: Union[None, Unset, datetime.datetime] = UNSET
    physical_release: Union[None, Unset, datetime.datetime] = UNSET
    digital_release: Union[None, Unset, datetime.datetime] = UNSET
    release_date: Union[None, Unset, datetime.datetime] = UNSET
    physical_release_note: Union[None, Unset, str] = UNSET
    images: Union[None, Unset, list["MediaCover"]] = UNSET
    website: Union[None, Unset, str] = UNSET
    remote_poster: Union[None, Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    you_tube_trailer_id: Union[None, Unset, str] = UNSET
    studio: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    quality_profile_id: Union[Unset, int] = UNSET
    has_file: Union[None, Unset, bool] = UNSET
    movie_file_id: Union[Unset, int] = UNSET
    monitored: Union[Unset, bool] = UNSET
    minimum_availability: Union[Unset, MovieStatusType] = UNSET
    is_available: Union[Unset, bool] = UNSET
    folder_name: Union[None, Unset, str] = UNSET
    runtime: Union[Unset, int] = UNSET
    clean_title: Union[None, Unset, str] = UNSET
    imdb_id: Union[None, Unset, str] = UNSET
    tmdb_id: Union[Unset, int] = UNSET
    title_slug: Union[None, Unset, str] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    folder: Union[None, Unset, str] = UNSET
    certification: Union[None, Unset, str] = UNSET
    genres: Union[None, Unset, list[str]] = UNSET
    keywords: Union[None, Unset, list[str]] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    add_options: Union[Unset, "AddMovieOptions"] = UNSET
    ratings: Union[Unset, "Ratings"] = UNSET
    movie_file: Union[Unset, "MovieFileResource"] = UNSET
    collection: Union[Unset, "MovieCollectionResource"] = UNSET
    popularity: Union[Unset, float] = UNSET
    last_search_time: Union[None, Unset, datetime.datetime] = UNSET
    statistics: Union[Unset, "MovieStatisticsResource"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        original_title: Union[None, Unset, str]
        if isinstance(self.original_title, Unset):
            original_title = UNSET
        else:
            original_title = self.original_title

        original_language: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.original_language, Unset):
            original_language = self.original_language.to_dict()

        alternate_titles: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.alternate_titles, Unset):
            alternate_titles = UNSET
        elif isinstance(self.alternate_titles, list):
            alternate_titles = []
            for alternate_titles_type_0_item_data in self.alternate_titles:
                alternate_titles_type_0_item = (
                    alternate_titles_type_0_item_data.to_dict()
                )
                alternate_titles.append(alternate_titles_type_0_item)

        else:
            alternate_titles = self.alternate_titles

        secondary_year: Union[None, Unset, int]
        if isinstance(self.secondary_year, Unset):
            secondary_year = UNSET
        else:
            secondary_year = self.secondary_year

        secondary_year_source_id = self.secondary_year_source_id

        sort_title: Union[None, Unset, str]
        if isinstance(self.sort_title, Unset):
            sort_title = UNSET
        else:
            sort_title = self.sort_title

        size_on_disk: Union[None, Unset, int]
        if isinstance(self.size_on_disk, Unset):
            size_on_disk = UNSET
        else:
            size_on_disk = self.size_on_disk

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        in_cinemas: Union[None, Unset, str]
        if isinstance(self.in_cinemas, Unset):
            in_cinemas = UNSET
        elif isinstance(self.in_cinemas, datetime.datetime):
            in_cinemas = self.in_cinemas.isoformat()
        else:
            in_cinemas = self.in_cinemas

        physical_release: Union[None, Unset, str]
        if isinstance(self.physical_release, Unset):
            physical_release = UNSET
        elif isinstance(self.physical_release, datetime.datetime):
            physical_release = self.physical_release.isoformat()
        else:
            physical_release = self.physical_release

        digital_release: Union[None, Unset, str]
        if isinstance(self.digital_release, Unset):
            digital_release = UNSET
        elif isinstance(self.digital_release, datetime.datetime):
            digital_release = self.digital_release.isoformat()
        else:
            digital_release = self.digital_release

        release_date: Union[None, Unset, str]
        if isinstance(self.release_date, Unset):
            release_date = UNSET
        elif isinstance(self.release_date, datetime.datetime):
            release_date = self.release_date.isoformat()
        else:
            release_date = self.release_date

        physical_release_note: Union[None, Unset, str]
        if isinstance(self.physical_release_note, Unset):
            physical_release_note = UNSET
        else:
            physical_release_note = self.physical_release_note

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

        website: Union[None, Unset, str]
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        remote_poster: Union[None, Unset, str]
        if isinstance(self.remote_poster, Unset):
            remote_poster = UNSET
        else:
            remote_poster = self.remote_poster

        year = self.year

        you_tube_trailer_id: Union[None, Unset, str]
        if isinstance(self.you_tube_trailer_id, Unset):
            you_tube_trailer_id = UNSET
        else:
            you_tube_trailer_id = self.you_tube_trailer_id

        studio: Union[None, Unset, str]
        if isinstance(self.studio, Unset):
            studio = UNSET
        else:
            studio = self.studio

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        quality_profile_id = self.quality_profile_id

        has_file: Union[None, Unset, bool]
        if isinstance(self.has_file, Unset):
            has_file = UNSET
        else:
            has_file = self.has_file

        movie_file_id = self.movie_file_id

        monitored = self.monitored

        minimum_availability: Union[Unset, str] = UNSET
        if not isinstance(self.minimum_availability, Unset):
            minimum_availability = self.minimum_availability.value

        is_available = self.is_available

        folder_name: Union[None, Unset, str]
        if isinstance(self.folder_name, Unset):
            folder_name = UNSET
        else:
            folder_name = self.folder_name

        runtime = self.runtime

        clean_title: Union[None, Unset, str]
        if isinstance(self.clean_title, Unset):
            clean_title = UNSET
        else:
            clean_title = self.clean_title

        imdb_id: Union[None, Unset, str]
        if isinstance(self.imdb_id, Unset):
            imdb_id = UNSET
        else:
            imdb_id = self.imdb_id

        tmdb_id = self.tmdb_id

        title_slug: Union[None, Unset, str]
        if isinstance(self.title_slug, Unset):
            title_slug = UNSET
        else:
            title_slug = self.title_slug

        root_folder_path: Union[None, Unset, str]
        if isinstance(self.root_folder_path, Unset):
            root_folder_path = UNSET
        else:
            root_folder_path = self.root_folder_path

        folder: Union[None, Unset, str]
        if isinstance(self.folder, Unset):
            folder = UNSET
        else:
            folder = self.folder

        certification: Union[None, Unset, str]
        if isinstance(self.certification, Unset):
            certification = UNSET
        else:
            certification = self.certification

        genres: Union[None, Unset, list[str]]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        keywords: Union[None, Unset, list[str]]
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        add_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.add_options, Unset):
            add_options = self.add_options.to_dict()

        ratings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        movie_file: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.movie_file, Unset):
            movie_file = self.movie_file.to_dict()

        collection: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.collection, Unset):
            collection = self.collection.to_dict()

        popularity = self.popularity

        last_search_time: Union[None, Unset, str]
        if isinstance(self.last_search_time, Unset):
            last_search_time = UNSET
        elif isinstance(self.last_search_time, datetime.datetime):
            last_search_time = self.last_search_time.isoformat()
        else:
            last_search_time = self.last_search_time

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if original_title is not UNSET:
            field_dict["originalTitle"] = original_title
        if original_language is not UNSET:
            field_dict["originalLanguage"] = original_language
        if alternate_titles is not UNSET:
            field_dict["alternateTitles"] = alternate_titles
        if secondary_year is not UNSET:
            field_dict["secondaryYear"] = secondary_year
        if secondary_year_source_id is not UNSET:
            field_dict["secondaryYearSourceId"] = secondary_year_source_id
        if sort_title is not UNSET:
            field_dict["sortTitle"] = sort_title
        if size_on_disk is not UNSET:
            field_dict["sizeOnDisk"] = size_on_disk
        if status is not UNSET:
            field_dict["status"] = status
        if overview is not UNSET:
            field_dict["overview"] = overview
        if in_cinemas is not UNSET:
            field_dict["inCinemas"] = in_cinemas
        if physical_release is not UNSET:
            field_dict["physicalRelease"] = physical_release
        if digital_release is not UNSET:
            field_dict["digitalRelease"] = digital_release
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if physical_release_note is not UNSET:
            field_dict["physicalReleaseNote"] = physical_release_note
        if images is not UNSET:
            field_dict["images"] = images
        if website is not UNSET:
            field_dict["website"] = website
        if remote_poster is not UNSET:
            field_dict["remotePoster"] = remote_poster
        if year is not UNSET:
            field_dict["year"] = year
        if you_tube_trailer_id is not UNSET:
            field_dict["youTubeTrailerId"] = you_tube_trailer_id
        if studio is not UNSET:
            field_dict["studio"] = studio
        if path is not UNSET:
            field_dict["path"] = path
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id
        if has_file is not UNSET:
            field_dict["hasFile"] = has_file
        if movie_file_id is not UNSET:
            field_dict["movieFileId"] = movie_file_id
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if minimum_availability is not UNSET:
            field_dict["minimumAvailability"] = minimum_availability
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available
        if folder_name is not UNSET:
            field_dict["folderName"] = folder_name
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if clean_title is not UNSET:
            field_dict["cleanTitle"] = clean_title
        if imdb_id is not UNSET:
            field_dict["imdbId"] = imdb_id
        if tmdb_id is not UNSET:
            field_dict["tmdbId"] = tmdb_id
        if title_slug is not UNSET:
            field_dict["titleSlug"] = title_slug
        if root_folder_path is not UNSET:
            field_dict["rootFolderPath"] = root_folder_path
        if folder is not UNSET:
            field_dict["folder"] = folder
        if certification is not UNSET:
            field_dict["certification"] = certification
        if genres is not UNSET:
            field_dict["genres"] = genres
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if tags is not UNSET:
            field_dict["tags"] = tags
        if added is not UNSET:
            field_dict["added"] = added
        if add_options is not UNSET:
            field_dict["addOptions"] = add_options
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if movie_file is not UNSET:
            field_dict["movieFile"] = movie_file
        if collection is not UNSET:
            field_dict["collection"] = collection
        if popularity is not UNSET:
            field_dict["popularity"] = popularity
        if last_search_time is not UNSET:
            field_dict["lastSearchTime"] = last_search_time
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_movie_options import AddMovieOptions
        from ..models.alternative_title_resource import AlternativeTitleResource
        from ..models.language import Language
        from ..models.media_cover import MediaCover
        from ..models.movie_collection_resource import MovieCollectionResource
        from ..models.movie_file_resource import MovieFileResource
        from ..models.movie_statistics_resource import MovieStatisticsResource
        from ..models.ratings import Ratings

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_original_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        original_title = _parse_original_title(d.pop("originalTitle", UNSET))

        _original_language = d.pop("originalLanguage", UNSET)
        original_language: Union[Unset, Language]
        if isinstance(_original_language, Unset):
            original_language = UNSET
        else:
            original_language = Language.from_dict(_original_language)

        def _parse_alternate_titles(
            data: object,
        ) -> Union[None, Unset, list["AlternativeTitleResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alternate_titles_type_0 = []
                _alternate_titles_type_0 = data
                for alternate_titles_type_0_item_data in _alternate_titles_type_0:
                    alternate_titles_type_0_item = AlternativeTitleResource.from_dict(
                        alternate_titles_type_0_item_data
                    )

                    alternate_titles_type_0.append(alternate_titles_type_0_item)

                return alternate_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AlternativeTitleResource"]], data)

        alternate_titles = _parse_alternate_titles(d.pop("alternateTitles", UNSET))

        def _parse_secondary_year(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        secondary_year = _parse_secondary_year(d.pop("secondaryYear", UNSET))

        secondary_year_source_id = d.pop("secondaryYearSourceId", UNSET)

        def _parse_sort_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sort_title = _parse_sort_title(d.pop("sortTitle", UNSET))

        def _parse_size_on_disk(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_on_disk = _parse_size_on_disk(d.pop("sizeOnDisk", UNSET))

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

        def _parse_in_cinemas(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                in_cinemas_type_0 = isoparse(data)

                return in_cinemas_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        in_cinemas = _parse_in_cinemas(d.pop("inCinemas", UNSET))

        def _parse_physical_release(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                physical_release_type_0 = isoparse(data)

                return physical_release_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        physical_release = _parse_physical_release(d.pop("physicalRelease", UNSET))

        def _parse_digital_release(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                digital_release_type_0 = isoparse(data)

                return digital_release_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        digital_release = _parse_digital_release(d.pop("digitalRelease", UNSET))

        def _parse_release_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                release_date_type_0 = isoparse(data)

                return release_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        release_date = _parse_release_date(d.pop("releaseDate", UNSET))

        def _parse_physical_release_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        physical_release_note = _parse_physical_release_note(
            d.pop("physicalReleaseNote", UNSET)
        )

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

        def _parse_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_remote_poster(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_poster = _parse_remote_poster(d.pop("remotePoster", UNSET))

        year = d.pop("year", UNSET)

        def _parse_you_tube_trailer_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        you_tube_trailer_id = _parse_you_tube_trailer_id(
            d.pop("youTubeTrailerId", UNSET)
        )

        def _parse_studio(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        studio = _parse_studio(d.pop("studio", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        quality_profile_id = d.pop("qualityProfileId", UNSET)

        def _parse_has_file(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_file = _parse_has_file(d.pop("hasFile", UNSET))

        movie_file_id = d.pop("movieFileId", UNSET)

        monitored = d.pop("monitored", UNSET)

        _minimum_availability = d.pop("minimumAvailability", UNSET)
        minimum_availability: Union[Unset, MovieStatusType]
        if isinstance(_minimum_availability, Unset):
            minimum_availability = UNSET
        else:
            minimum_availability = MovieStatusType(_minimum_availability)

        is_available = d.pop("isAvailable", UNSET)

        def _parse_folder_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        folder_name = _parse_folder_name(d.pop("folderName", UNSET))

        runtime = d.pop("runtime", UNSET)

        def _parse_clean_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        clean_title = _parse_clean_title(d.pop("cleanTitle", UNSET))

        def _parse_imdb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        imdb_id = _parse_imdb_id(d.pop("imdbId", UNSET))

        tmdb_id = d.pop("tmdbId", UNSET)

        def _parse_title_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title_slug = _parse_title_slug(d.pop("titleSlug", UNSET))

        def _parse_root_folder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_folder_path = _parse_root_folder_path(d.pop("rootFolderPath", UNSET))

        def _parse_folder(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        folder = _parse_folder(d.pop("folder", UNSET))

        def _parse_certification(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        certification = _parse_certification(d.pop("certification", UNSET))

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

        def _parse_keywords(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        _add_options = d.pop("addOptions", UNSET)
        add_options: Union[Unset, AddMovieOptions]
        if isinstance(_add_options, Unset):
            add_options = UNSET
        else:
            add_options = AddMovieOptions.from_dict(_add_options)

        _ratings = d.pop("ratings", UNSET)
        ratings: Union[Unset, Ratings]
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = Ratings.from_dict(_ratings)

        _movie_file = d.pop("movieFile", UNSET)
        movie_file: Union[Unset, MovieFileResource]
        if isinstance(_movie_file, Unset):
            movie_file = UNSET
        else:
            movie_file = MovieFileResource.from_dict(_movie_file)

        _collection = d.pop("collection", UNSET)
        collection: Union[Unset, MovieCollectionResource]
        if isinstance(_collection, Unset):
            collection = UNSET
        else:
            collection = MovieCollectionResource.from_dict(_collection)

        popularity = d.pop("popularity", UNSET)

        def _parse_last_search_time(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_search_time_type_0 = isoparse(data)

                return last_search_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_search_time = _parse_last_search_time(d.pop("lastSearchTime", UNSET))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, MovieStatisticsResource]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = MovieStatisticsResource.from_dict(_statistics)

        movie_resource = cls(
            id=id,
            title=title,
            original_title=original_title,
            original_language=original_language,
            alternate_titles=alternate_titles,
            secondary_year=secondary_year,
            secondary_year_source_id=secondary_year_source_id,
            sort_title=sort_title,
            size_on_disk=size_on_disk,
            status=status,
            overview=overview,
            in_cinemas=in_cinemas,
            physical_release=physical_release,
            digital_release=digital_release,
            release_date=release_date,
            physical_release_note=physical_release_note,
            images=images,
            website=website,
            remote_poster=remote_poster,
            year=year,
            you_tube_trailer_id=you_tube_trailer_id,
            studio=studio,
            path=path,
            quality_profile_id=quality_profile_id,
            has_file=has_file,
            movie_file_id=movie_file_id,
            monitored=monitored,
            minimum_availability=minimum_availability,
            is_available=is_available,
            folder_name=folder_name,
            runtime=runtime,
            clean_title=clean_title,
            imdb_id=imdb_id,
            tmdb_id=tmdb_id,
            title_slug=title_slug,
            root_folder_path=root_folder_path,
            folder=folder,
            certification=certification,
            genres=genres,
            keywords=keywords,
            tags=tags,
            added=added,
            add_options=add_options,
            ratings=ratings,
            movie_file=movie_file,
            collection=collection,
            popularity=popularity,
            last_search_time=last_search_time,
            statistics=statistics,
        )

        return movie_resource
