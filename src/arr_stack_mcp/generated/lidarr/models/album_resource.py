import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_album_options import AddAlbumOptions
    from ..models.album_release_resource import AlbumReleaseResource
    from ..models.album_statistics_resource import AlbumStatisticsResource
    from ..models.artist_resource import ArtistResource
    from ..models.links import Links
    from ..models.media_cover import MediaCover
    from ..models.medium_resource import MediumResource
    from ..models.ratings import Ratings


T = TypeVar("T", bound="AlbumResource")


@_attrs_define
class AlbumResource:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[None, Unset, str]):
        disambiguation (Union[None, Unset, str]):
        overview (Union[None, Unset, str]):
        artist_id (Union[Unset, int]):
        foreign_album_id (Union[None, Unset, str]):
        monitored (Union[Unset, bool]):
        any_release_ok (Union[Unset, bool]):
        profile_id (Union[Unset, int]):
        duration (Union[Unset, int]):
        album_type (Union[None, Unset, str]):
        secondary_types (Union[None, Unset, list[str]]):
        medium_count (Union[Unset, int]):
        ratings (Union[Unset, Ratings]):
        release_date (Union[None, Unset, datetime.datetime]):
        releases (Union[None, Unset, list['AlbumReleaseResource']]):
        genres (Union[None, Unset, list[str]]):
        media (Union[None, Unset, list['MediumResource']]):
        artist (Union[Unset, ArtistResource]):
        images (Union[None, Unset, list['MediaCover']]):
        links (Union[None, Unset, list['Links']]):
        last_search_time (Union[None, Unset, datetime.datetime]):
        statistics (Union[Unset, AlbumStatisticsResource]):
        add_options (Union[Unset, AddAlbumOptions]):
        remote_cover (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    disambiguation: Union[None, Unset, str] = UNSET
    overview: Union[None, Unset, str] = UNSET
    artist_id: Union[Unset, int] = UNSET
    foreign_album_id: Union[None, Unset, str] = UNSET
    monitored: Union[Unset, bool] = UNSET
    any_release_ok: Union[Unset, bool] = UNSET
    profile_id: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    album_type: Union[None, Unset, str] = UNSET
    secondary_types: Union[None, Unset, list[str]] = UNSET
    medium_count: Union[Unset, int] = UNSET
    ratings: Union[Unset, "Ratings"] = UNSET
    release_date: Union[None, Unset, datetime.datetime] = UNSET
    releases: Union[None, Unset, list["AlbumReleaseResource"]] = UNSET
    genres: Union[None, Unset, list[str]] = UNSET
    media: Union[None, Unset, list["MediumResource"]] = UNSET
    artist: Union[Unset, "ArtistResource"] = UNSET
    images: Union[None, Unset, list["MediaCover"]] = UNSET
    links: Union[None, Unset, list["Links"]] = UNSET
    last_search_time: Union[None, Unset, datetime.datetime] = UNSET
    statistics: Union[Unset, "AlbumStatisticsResource"] = UNSET
    add_options: Union[Unset, "AddAlbumOptions"] = UNSET
    remote_cover: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        disambiguation: Union[None, Unset, str]
        if isinstance(self.disambiguation, Unset):
            disambiguation = UNSET
        else:
            disambiguation = self.disambiguation

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        artist_id = self.artist_id

        foreign_album_id: Union[None, Unset, str]
        if isinstance(self.foreign_album_id, Unset):
            foreign_album_id = UNSET
        else:
            foreign_album_id = self.foreign_album_id

        monitored = self.monitored

        any_release_ok = self.any_release_ok

        profile_id = self.profile_id

        duration = self.duration

        album_type: Union[None, Unset, str]
        if isinstance(self.album_type, Unset):
            album_type = UNSET
        else:
            album_type = self.album_type

        secondary_types: Union[None, Unset, list[str]]
        if isinstance(self.secondary_types, Unset):
            secondary_types = UNSET
        elif isinstance(self.secondary_types, list):
            secondary_types = self.secondary_types

        else:
            secondary_types = self.secondary_types

        medium_count = self.medium_count

        ratings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        release_date: Union[None, Unset, str]
        if isinstance(self.release_date, Unset):
            release_date = UNSET
        elif isinstance(self.release_date, datetime.datetime):
            release_date = self.release_date.isoformat()
        else:
            release_date = self.release_date

        releases: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.releases, Unset):
            releases = UNSET
        elif isinstance(self.releases, list):
            releases = []
            for releases_type_0_item_data in self.releases:
                releases_type_0_item = releases_type_0_item_data.to_dict()
                releases.append(releases_type_0_item)

        else:
            releases = self.releases

        genres: Union[None, Unset, list[str]]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        media: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.media, Unset):
            media = UNSET
        elif isinstance(self.media, list):
            media = []
            for media_type_0_item_data in self.media:
                media_type_0_item = media_type_0_item_data.to_dict()
                media.append(media_type_0_item)

        else:
            media = self.media

        artist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist.to_dict()

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

        links: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)

        else:
            links = self.links

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

        add_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.add_options, Unset):
            add_options = self.add_options.to_dict()

        remote_cover: Union[None, Unset, str]
        if isinstance(self.remote_cover, Unset):
            remote_cover = UNSET
        else:
            remote_cover = self.remote_cover

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if disambiguation is not UNSET:
            field_dict["disambiguation"] = disambiguation
        if overview is not UNSET:
            field_dict["overview"] = overview
        if artist_id is not UNSET:
            field_dict["artistId"] = artist_id
        if foreign_album_id is not UNSET:
            field_dict["foreignAlbumId"] = foreign_album_id
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if any_release_ok is not UNSET:
            field_dict["anyReleaseOk"] = any_release_ok
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if album_type is not UNSET:
            field_dict["albumType"] = album_type
        if secondary_types is not UNSET:
            field_dict["secondaryTypes"] = secondary_types
        if medium_count is not UNSET:
            field_dict["mediumCount"] = medium_count
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if releases is not UNSET:
            field_dict["releases"] = releases
        if genres is not UNSET:
            field_dict["genres"] = genres
        if media is not UNSET:
            field_dict["media"] = media
        if artist is not UNSET:
            field_dict["artist"] = artist
        if images is not UNSET:
            field_dict["images"] = images
        if links is not UNSET:
            field_dict["links"] = links
        if last_search_time is not UNSET:
            field_dict["lastSearchTime"] = last_search_time
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if add_options is not UNSET:
            field_dict["addOptions"] = add_options
        if remote_cover is not UNSET:
            field_dict["remoteCover"] = remote_cover

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_album_options import AddAlbumOptions
        from ..models.album_release_resource import AlbumReleaseResource
        from ..models.album_statistics_resource import AlbumStatisticsResource
        from ..models.artist_resource import ArtistResource
        from ..models.links import Links
        from ..models.media_cover import MediaCover
        from ..models.medium_resource import MediumResource
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

        def _parse_disambiguation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disambiguation = _parse_disambiguation(d.pop("disambiguation", UNSET))

        def _parse_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        overview = _parse_overview(d.pop("overview", UNSET))

        artist_id = d.pop("artistId", UNSET)

        def _parse_foreign_album_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_album_id = _parse_foreign_album_id(d.pop("foreignAlbumId", UNSET))

        monitored = d.pop("monitored", UNSET)

        any_release_ok = d.pop("anyReleaseOk", UNSET)

        profile_id = d.pop("profileId", UNSET)

        duration = d.pop("duration", UNSET)

        def _parse_album_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_type = _parse_album_type(d.pop("albumType", UNSET))

        def _parse_secondary_types(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                secondary_types_type_0 = cast(list[str], data)

                return secondary_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        secondary_types = _parse_secondary_types(d.pop("secondaryTypes", UNSET))

        medium_count = d.pop("mediumCount", UNSET)

        _ratings = d.pop("ratings", UNSET)
        ratings: Union[Unset, Ratings]
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = Ratings.from_dict(_ratings)

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

        def _parse_releases(
            data: object,
        ) -> Union[None, Unset, list["AlbumReleaseResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                releases_type_0 = []
                _releases_type_0 = data
                for releases_type_0_item_data in _releases_type_0:
                    releases_type_0_item = AlbumReleaseResource.from_dict(
                        releases_type_0_item_data
                    )

                    releases_type_0.append(releases_type_0_item)

                return releases_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AlbumReleaseResource"]], data)

        releases = _parse_releases(d.pop("releases", UNSET))

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

        def _parse_media(data: object) -> Union[None, Unset, list["MediumResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_type_0 = []
                _media_type_0 = data
                for media_type_0_item_data in _media_type_0:
                    media_type_0_item = MediumResource.from_dict(media_type_0_item_data)

                    media_type_0.append(media_type_0_item)

                return media_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MediumResource"]], data)

        media = _parse_media(d.pop("media", UNSET))

        _artist = d.pop("artist", UNSET)
        artist: Union[Unset, ArtistResource]
        if isinstance(_artist, Unset):
            artist = UNSET
        else:
            artist = ArtistResource.from_dict(_artist)

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

        def _parse_links(data: object) -> Union[None, Unset, list["Links"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in _links_type_0:
                    links_type_0_item = Links.from_dict(links_type_0_item_data)

                    links_type_0.append(links_type_0_item)

                return links_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Links"]], data)

        links = _parse_links(d.pop("links", UNSET))

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
        statistics: Union[Unset, AlbumStatisticsResource]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = AlbumStatisticsResource.from_dict(_statistics)

        _add_options = d.pop("addOptions", UNSET)
        add_options: Union[Unset, AddAlbumOptions]
        if isinstance(_add_options, Unset):
            add_options = UNSET
        else:
            add_options = AddAlbumOptions.from_dict(_add_options)

        def _parse_remote_cover(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_cover = _parse_remote_cover(d.pop("remoteCover", UNSET))

        album_resource = cls(
            id=id,
            title=title,
            disambiguation=disambiguation,
            overview=overview,
            artist_id=artist_id,
            foreign_album_id=foreign_album_id,
            monitored=monitored,
            any_release_ok=any_release_ok,
            profile_id=profile_id,
            duration=duration,
            album_type=album_type,
            secondary_types=secondary_types,
            medium_count=medium_count,
            ratings=ratings,
            release_date=release_date,
            releases=releases,
            genres=genres,
            media=media,
            artist=artist,
            images=images,
            links=links,
            last_search_time=last_search_time,
            statistics=statistics,
            add_options=add_options,
            remote_cover=remote_cover,
        )

        return album_resource
