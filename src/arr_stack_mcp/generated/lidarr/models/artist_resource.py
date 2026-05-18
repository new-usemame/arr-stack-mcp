import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.artist_status_type import ArtistStatusType
from ..models.new_item_monitor_types import NewItemMonitorTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_artist_options import AddArtistOptions
    from ..models.album_resource import AlbumResource
    from ..models.artist_statistics_resource import ArtistStatisticsResource
    from ..models.links import Links
    from ..models.media_cover import MediaCover
    from ..models.member import Member
    from ..models.ratings import Ratings


T = TypeVar("T", bound="ArtistResource")


@_attrs_define
class ArtistResource:
    """
    Attributes:
        id (Union[Unset, int]):
        status (Union[Unset, ArtistStatusType]):
        ended (Union[Unset, bool]):
        artist_name (Union[None, Unset, str]):
        foreign_artist_id (Union[None, Unset, str]):
        mb_id (Union[None, Unset, str]):
        tadb_id (Union[Unset, int]):
        discogs_id (Union[Unset, int]):
        all_music_id (Union[None, Unset, str]):
        overview (Union[None, Unset, str]):
        artist_type (Union[None, Unset, str]):
        disambiguation (Union[None, Unset, str]):
        links (Union[None, Unset, list['Links']]):
        next_album (Union[Unset, AlbumResource]):
        last_album (Union[Unset, AlbumResource]):
        images (Union[None, Unset, list['MediaCover']]):
        members (Union[None, Unset, list['Member']]):
        remote_poster (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        quality_profile_id (Union[Unset, int]):
        metadata_profile_id (Union[Unset, int]):
        monitored (Union[Unset, bool]):
        monitor_new_items (Union[Unset, NewItemMonitorTypes]):
        root_folder_path (Union[None, Unset, str]):
        folder (Union[None, Unset, str]):
        genres (Union[None, Unset, list[str]]):
        clean_name (Union[None, Unset, str]):
        sort_name (Union[None, Unset, str]):
        tags (Union[None, Unset, list[int]]):
        added (Union[Unset, datetime.datetime]):
        add_options (Union[Unset, AddArtistOptions]):
        ratings (Union[Unset, Ratings]):
        statistics (Union[Unset, ArtistStatisticsResource]):
    """

    id: Union[Unset, int] = UNSET
    status: Union[Unset, ArtistStatusType] = UNSET
    ended: Union[Unset, bool] = UNSET
    artist_name: Union[None, Unset, str] = UNSET
    foreign_artist_id: Union[None, Unset, str] = UNSET
    mb_id: Union[None, Unset, str] = UNSET
    tadb_id: Union[Unset, int] = UNSET
    discogs_id: Union[Unset, int] = UNSET
    all_music_id: Union[None, Unset, str] = UNSET
    overview: Union[None, Unset, str] = UNSET
    artist_type: Union[None, Unset, str] = UNSET
    disambiguation: Union[None, Unset, str] = UNSET
    links: Union[None, Unset, list["Links"]] = UNSET
    next_album: Union[Unset, "AlbumResource"] = UNSET
    last_album: Union[Unset, "AlbumResource"] = UNSET
    images: Union[None, Unset, list["MediaCover"]] = UNSET
    members: Union[None, Unset, list["Member"]] = UNSET
    remote_poster: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    quality_profile_id: Union[Unset, int] = UNSET
    metadata_profile_id: Union[Unset, int] = UNSET
    monitored: Union[Unset, bool] = UNSET
    monitor_new_items: Union[Unset, NewItemMonitorTypes] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    folder: Union[None, Unset, str] = UNSET
    genres: Union[None, Unset, list[str]] = UNSET
    clean_name: Union[None, Unset, str] = UNSET
    sort_name: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    add_options: Union[Unset, "AddArtistOptions"] = UNSET
    ratings: Union[Unset, "Ratings"] = UNSET
    statistics: Union[Unset, "ArtistStatisticsResource"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        ended = self.ended

        artist_name: Union[None, Unset, str]
        if isinstance(self.artist_name, Unset):
            artist_name = UNSET
        else:
            artist_name = self.artist_name

        foreign_artist_id: Union[None, Unset, str]
        if isinstance(self.foreign_artist_id, Unset):
            foreign_artist_id = UNSET
        else:
            foreign_artist_id = self.foreign_artist_id

        mb_id: Union[None, Unset, str]
        if isinstance(self.mb_id, Unset):
            mb_id = UNSET
        else:
            mb_id = self.mb_id

        tadb_id = self.tadb_id

        discogs_id = self.discogs_id

        all_music_id: Union[None, Unset, str]
        if isinstance(self.all_music_id, Unset):
            all_music_id = UNSET
        else:
            all_music_id = self.all_music_id

        overview: Union[None, Unset, str]
        if isinstance(self.overview, Unset):
            overview = UNSET
        else:
            overview = self.overview

        artist_type: Union[None, Unset, str]
        if isinstance(self.artist_type, Unset):
            artist_type = UNSET
        else:
            artist_type = self.artist_type

        disambiguation: Union[None, Unset, str]
        if isinstance(self.disambiguation, Unset):
            disambiguation = UNSET
        else:
            disambiguation = self.disambiguation

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

        next_album: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_album, Unset):
            next_album = self.next_album.to_dict()

        last_album: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_album, Unset):
            last_album = self.last_album.to_dict()

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

        members: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)

        else:
            members = self.members

        remote_poster: Union[None, Unset, str]
        if isinstance(self.remote_poster, Unset):
            remote_poster = UNSET
        else:
            remote_poster = self.remote_poster

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        quality_profile_id = self.quality_profile_id

        metadata_profile_id = self.metadata_profile_id

        monitored = self.monitored

        monitor_new_items: Union[Unset, str] = UNSET
        if not isinstance(self.monitor_new_items, Unset):
            monitor_new_items = self.monitor_new_items.value

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

        genres: Union[None, Unset, list[str]]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        clean_name: Union[None, Unset, str]
        if isinstance(self.clean_name, Unset):
            clean_name = UNSET
        else:
            clean_name = self.clean_name

        sort_name: Union[None, Unset, str]
        if isinstance(self.sort_name, Unset):
            sort_name = UNSET
        else:
            sort_name = self.sort_name

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

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if ended is not UNSET:
            field_dict["ended"] = ended
        if artist_name is not UNSET:
            field_dict["artistName"] = artist_name
        if foreign_artist_id is not UNSET:
            field_dict["foreignArtistId"] = foreign_artist_id
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if tadb_id is not UNSET:
            field_dict["tadbId"] = tadb_id
        if discogs_id is not UNSET:
            field_dict["discogsId"] = discogs_id
        if all_music_id is not UNSET:
            field_dict["allMusicId"] = all_music_id
        if overview is not UNSET:
            field_dict["overview"] = overview
        if artist_type is not UNSET:
            field_dict["artistType"] = artist_type
        if disambiguation is not UNSET:
            field_dict["disambiguation"] = disambiguation
        if links is not UNSET:
            field_dict["links"] = links
        if next_album is not UNSET:
            field_dict["nextAlbum"] = next_album
        if last_album is not UNSET:
            field_dict["lastAlbum"] = last_album
        if images is not UNSET:
            field_dict["images"] = images
        if members is not UNSET:
            field_dict["members"] = members
        if remote_poster is not UNSET:
            field_dict["remotePoster"] = remote_poster
        if path is not UNSET:
            field_dict["path"] = path
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id
        if metadata_profile_id is not UNSET:
            field_dict["metadataProfileId"] = metadata_profile_id
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if monitor_new_items is not UNSET:
            field_dict["monitorNewItems"] = monitor_new_items
        if root_folder_path is not UNSET:
            field_dict["rootFolderPath"] = root_folder_path
        if folder is not UNSET:
            field_dict["folder"] = folder
        if genres is not UNSET:
            field_dict["genres"] = genres
        if clean_name is not UNSET:
            field_dict["cleanName"] = clean_name
        if sort_name is not UNSET:
            field_dict["sortName"] = sort_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if added is not UNSET:
            field_dict["added"] = added
        if add_options is not UNSET:
            field_dict["addOptions"] = add_options
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_artist_options import AddArtistOptions
        from ..models.album_resource import AlbumResource
        from ..models.artist_statistics_resource import ArtistStatisticsResource
        from ..models.links import Links
        from ..models.media_cover import MediaCover
        from ..models.member import Member
        from ..models.ratings import Ratings

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ArtistStatusType]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ArtistStatusType(_status)

        ended = d.pop("ended", UNSET)

        def _parse_artist_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist_name = _parse_artist_name(d.pop("artistName", UNSET))

        def _parse_foreign_artist_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_artist_id = _parse_foreign_artist_id(d.pop("foreignArtistId", UNSET))

        def _parse_mb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mb_id = _parse_mb_id(d.pop("mbId", UNSET))

        tadb_id = d.pop("tadbId", UNSET)

        discogs_id = d.pop("discogsId", UNSET)

        def _parse_all_music_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        all_music_id = _parse_all_music_id(d.pop("allMusicId", UNSET))

        def _parse_overview(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        overview = _parse_overview(d.pop("overview", UNSET))

        def _parse_artist_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist_type = _parse_artist_type(d.pop("artistType", UNSET))

        def _parse_disambiguation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disambiguation = _parse_disambiguation(d.pop("disambiguation", UNSET))

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

        _next_album = d.pop("nextAlbum", UNSET)
        next_album: Union[Unset, AlbumResource]
        if isinstance(_next_album, Unset):
            next_album = UNSET
        else:
            next_album = AlbumResource.from_dict(_next_album)

        _last_album = d.pop("lastAlbum", UNSET)
        last_album: Union[Unset, AlbumResource]
        if isinstance(_last_album, Unset):
            last_album = UNSET
        else:
            last_album = AlbumResource.from_dict(_last_album)

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

        def _parse_members(data: object) -> Union[None, Unset, list["Member"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in _members_type_0:
                    members_type_0_item = Member.from_dict(members_type_0_item_data)

                    members_type_0.append(members_type_0_item)

                return members_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Member"]], data)

        members = _parse_members(d.pop("members", UNSET))

        def _parse_remote_poster(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remote_poster = _parse_remote_poster(d.pop("remotePoster", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        quality_profile_id = d.pop("qualityProfileId", UNSET)

        metadata_profile_id = d.pop("metadataProfileId", UNSET)

        monitored = d.pop("monitored", UNSET)

        _monitor_new_items = d.pop("monitorNewItems", UNSET)
        monitor_new_items: Union[Unset, NewItemMonitorTypes]
        if isinstance(_monitor_new_items, Unset):
            monitor_new_items = UNSET
        else:
            monitor_new_items = NewItemMonitorTypes(_monitor_new_items)

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

        def _parse_clean_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        clean_name = _parse_clean_name(d.pop("cleanName", UNSET))

        def _parse_sort_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sort_name = _parse_sort_name(d.pop("sortName", UNSET))

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
        add_options: Union[Unset, AddArtistOptions]
        if isinstance(_add_options, Unset):
            add_options = UNSET
        else:
            add_options = AddArtistOptions.from_dict(_add_options)

        _ratings = d.pop("ratings", UNSET)
        ratings: Union[Unset, Ratings]
        if isinstance(_ratings, Unset):
            ratings = UNSET
        else:
            ratings = Ratings.from_dict(_ratings)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, ArtistStatisticsResource]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = ArtistStatisticsResource.from_dict(_statistics)

        artist_resource = cls(
            id=id,
            status=status,
            ended=ended,
            artist_name=artist_name,
            foreign_artist_id=foreign_artist_id,
            mb_id=mb_id,
            tadb_id=tadb_id,
            discogs_id=discogs_id,
            all_music_id=all_music_id,
            overview=overview,
            artist_type=artist_type,
            disambiguation=disambiguation,
            links=links,
            next_album=next_album,
            last_album=last_album,
            images=images,
            members=members,
            remote_poster=remote_poster,
            path=path,
            quality_profile_id=quality_profile_id,
            metadata_profile_id=metadata_profile_id,
            monitored=monitored,
            monitor_new_items=monitor_new_items,
            root_folder_path=root_folder_path,
            folder=folder,
            genres=genres,
            clean_name=clean_name,
            sort_name=sort_name,
            tags=tags,
            added=added,
            add_options=add_options,
            ratings=ratings,
            statistics=statistics,
        )

        return artist_resource
