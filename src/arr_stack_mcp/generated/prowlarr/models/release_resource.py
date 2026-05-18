import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.download_protocol import DownloadProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.indexer_category import IndexerCategory


T = TypeVar("T", bound="ReleaseResource")


@_attrs_define
class ReleaseResource:
    """
    Attributes:
        id (Union[Unset, int]):
        guid (Union[None, Unset, str]):
        age (Union[Unset, int]):
        age_hours (Union[Unset, float]):
        age_minutes (Union[Unset, float]):
        size (Union[Unset, int]):
        files (Union[None, Unset, int]):
        grabs (Union[None, Unset, int]):
        indexer_id (Union[Unset, int]):
        indexer (Union[None, Unset, str]):
        sub_group (Union[None, Unset, str]):
        release_hash (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        sort_title (Union[None, Unset, str]):
        imdb_id (Union[Unset, int]):
        tmdb_id (Union[Unset, int]):
        tvdb_id (Union[Unset, int]):
        tv_maze_id (Union[Unset, int]):
        publish_date (Union[Unset, datetime.datetime]):
        comment_url (Union[None, Unset, str]):
        download_url (Union[None, Unset, str]):
        info_url (Union[None, Unset, str]):
        poster_url (Union[None, Unset, str]):
        indexer_flags (Union[None, Unset, list[str]]):
        categories (Union[None, Unset, list['IndexerCategory']]):
        magnet_url (Union[None, Unset, str]):
        info_hash (Union[None, Unset, str]):
        seeders (Union[None, Unset, int]):
        leechers (Union[None, Unset, int]):
        protocol (Union[Unset, DownloadProtocol]):
        file_name (Union[None, Unset, str]):
        download_client_id (Union[None, Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    guid: Union[None, Unset, str] = UNSET
    age: Union[Unset, int] = UNSET
    age_hours: Union[Unset, float] = UNSET
    age_minutes: Union[Unset, float] = UNSET
    size: Union[Unset, int] = UNSET
    files: Union[None, Unset, int] = UNSET
    grabs: Union[None, Unset, int] = UNSET
    indexer_id: Union[Unset, int] = UNSET
    indexer: Union[None, Unset, str] = UNSET
    sub_group: Union[None, Unset, str] = UNSET
    release_hash: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    sort_title: Union[None, Unset, str] = UNSET
    imdb_id: Union[Unset, int] = UNSET
    tmdb_id: Union[Unset, int] = UNSET
    tvdb_id: Union[Unset, int] = UNSET
    tv_maze_id: Union[Unset, int] = UNSET
    publish_date: Union[Unset, datetime.datetime] = UNSET
    comment_url: Union[None, Unset, str] = UNSET
    download_url: Union[None, Unset, str] = UNSET
    info_url: Union[None, Unset, str] = UNSET
    poster_url: Union[None, Unset, str] = UNSET
    indexer_flags: Union[None, Unset, list[str]] = UNSET
    categories: Union[None, Unset, list["IndexerCategory"]] = UNSET
    magnet_url: Union[None, Unset, str] = UNSET
    info_hash: Union[None, Unset, str] = UNSET
    seeders: Union[None, Unset, int] = UNSET
    leechers: Union[None, Unset, int] = UNSET
    protocol: Union[Unset, DownloadProtocol] = UNSET
    file_name: Union[None, Unset, str] = UNSET
    download_client_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        guid: Union[None, Unset, str]
        if isinstance(self.guid, Unset):
            guid = UNSET
        else:
            guid = self.guid

        age = self.age

        age_hours = self.age_hours

        age_minutes = self.age_minutes

        size = self.size

        files: Union[None, Unset, int]
        if isinstance(self.files, Unset):
            files = UNSET
        else:
            files = self.files

        grabs: Union[None, Unset, int]
        if isinstance(self.grabs, Unset):
            grabs = UNSET
        else:
            grabs = self.grabs

        indexer_id = self.indexer_id

        indexer: Union[None, Unset, str]
        if isinstance(self.indexer, Unset):
            indexer = UNSET
        else:
            indexer = self.indexer

        sub_group: Union[None, Unset, str]
        if isinstance(self.sub_group, Unset):
            sub_group = UNSET
        else:
            sub_group = self.sub_group

        release_hash: Union[None, Unset, str]
        if isinstance(self.release_hash, Unset):
            release_hash = UNSET
        else:
            release_hash = self.release_hash

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        sort_title: Union[None, Unset, str]
        if isinstance(self.sort_title, Unset):
            sort_title = UNSET
        else:
            sort_title = self.sort_title

        imdb_id = self.imdb_id

        tmdb_id = self.tmdb_id

        tvdb_id = self.tvdb_id

        tv_maze_id = self.tv_maze_id

        publish_date: Union[Unset, str] = UNSET
        if not isinstance(self.publish_date, Unset):
            publish_date = self.publish_date.isoformat()

        comment_url: Union[None, Unset, str]
        if isinstance(self.comment_url, Unset):
            comment_url = UNSET
        else:
            comment_url = self.comment_url

        download_url: Union[None, Unset, str]
        if isinstance(self.download_url, Unset):
            download_url = UNSET
        else:
            download_url = self.download_url

        info_url: Union[None, Unset, str]
        if isinstance(self.info_url, Unset):
            info_url = UNSET
        else:
            info_url = self.info_url

        poster_url: Union[None, Unset, str]
        if isinstance(self.poster_url, Unset):
            poster_url = UNSET
        else:
            poster_url = self.poster_url

        indexer_flags: Union[None, Unset, list[str]]
        if isinstance(self.indexer_flags, Unset):
            indexer_flags = UNSET
        elif isinstance(self.indexer_flags, list):
            indexer_flags = self.indexer_flags

        else:
            indexer_flags = self.indexer_flags

        categories: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        magnet_url: Union[None, Unset, str]
        if isinstance(self.magnet_url, Unset):
            magnet_url = UNSET
        else:
            magnet_url = self.magnet_url

        info_hash: Union[None, Unset, str]
        if isinstance(self.info_hash, Unset):
            info_hash = UNSET
        else:
            info_hash = self.info_hash

        seeders: Union[None, Unset, int]
        if isinstance(self.seeders, Unset):
            seeders = UNSET
        else:
            seeders = self.seeders

        leechers: Union[None, Unset, int]
        if isinstance(self.leechers, Unset):
            leechers = UNSET
        else:
            leechers = self.leechers

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        file_name: Union[None, Unset, str]
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        download_client_id: Union[None, Unset, int]
        if isinstance(self.download_client_id, Unset):
            download_client_id = UNSET
        else:
            download_client_id = self.download_client_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if age is not UNSET:
            field_dict["age"] = age
        if age_hours is not UNSET:
            field_dict["ageHours"] = age_hours
        if age_minutes is not UNSET:
            field_dict["ageMinutes"] = age_minutes
        if size is not UNSET:
            field_dict["size"] = size
        if files is not UNSET:
            field_dict["files"] = files
        if grabs is not UNSET:
            field_dict["grabs"] = grabs
        if indexer_id is not UNSET:
            field_dict["indexerId"] = indexer_id
        if indexer is not UNSET:
            field_dict["indexer"] = indexer
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if release_hash is not UNSET:
            field_dict["releaseHash"] = release_hash
        if title is not UNSET:
            field_dict["title"] = title
        if sort_title is not UNSET:
            field_dict["sortTitle"] = sort_title
        if imdb_id is not UNSET:
            field_dict["imdbId"] = imdb_id
        if tmdb_id is not UNSET:
            field_dict["tmdbId"] = tmdb_id
        if tvdb_id is not UNSET:
            field_dict["tvdbId"] = tvdb_id
        if tv_maze_id is not UNSET:
            field_dict["tvMazeId"] = tv_maze_id
        if publish_date is not UNSET:
            field_dict["publishDate"] = publish_date
        if comment_url is not UNSET:
            field_dict["commentUrl"] = comment_url
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if info_url is not UNSET:
            field_dict["infoUrl"] = info_url
        if poster_url is not UNSET:
            field_dict["posterUrl"] = poster_url
        if indexer_flags is not UNSET:
            field_dict["indexerFlags"] = indexer_flags
        if categories is not UNSET:
            field_dict["categories"] = categories
        if magnet_url is not UNSET:
            field_dict["magnetUrl"] = magnet_url
        if info_hash is not UNSET:
            field_dict["infoHash"] = info_hash
        if seeders is not UNSET:
            field_dict["seeders"] = seeders
        if leechers is not UNSET:
            field_dict["leechers"] = leechers
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if download_client_id is not UNSET:
            field_dict["downloadClientId"] = download_client_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.indexer_category import IndexerCategory

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_guid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        guid = _parse_guid(d.pop("guid", UNSET))

        age = d.pop("age", UNSET)

        age_hours = d.pop("ageHours", UNSET)

        age_minutes = d.pop("ageMinutes", UNSET)

        size = d.pop("size", UNSET)

        def _parse_files(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        files = _parse_files(d.pop("files", UNSET))

        def _parse_grabs(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        grabs = _parse_grabs(d.pop("grabs", UNSET))

        indexer_id = d.pop("indexerId", UNSET)

        def _parse_indexer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        indexer = _parse_indexer(d.pop("indexer", UNSET))

        def _parse_sub_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sub_group = _parse_sub_group(d.pop("subGroup", UNSET))

        def _parse_release_hash(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_hash = _parse_release_hash(d.pop("releaseHash", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_sort_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sort_title = _parse_sort_title(d.pop("sortTitle", UNSET))

        imdb_id = d.pop("imdbId", UNSET)

        tmdb_id = d.pop("tmdbId", UNSET)

        tvdb_id = d.pop("tvdbId", UNSET)

        tv_maze_id = d.pop("tvMazeId", UNSET)

        _publish_date = d.pop("publishDate", UNSET)
        publish_date: Union[Unset, datetime.datetime]
        if isinstance(_publish_date, Unset):
            publish_date = UNSET
        else:
            publish_date = isoparse(_publish_date)

        def _parse_comment_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment_url = _parse_comment_url(d.pop("commentUrl", UNSET))

        def _parse_download_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_url = _parse_download_url(d.pop("downloadUrl", UNSET))

        def _parse_info_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_url = _parse_info_url(d.pop("infoUrl", UNSET))

        def _parse_poster_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        poster_url = _parse_poster_url(d.pop("posterUrl", UNSET))

        def _parse_indexer_flags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indexer_flags_type_0 = cast(list[str], data)

                return indexer_flags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        indexer_flags = _parse_indexer_flags(d.pop("indexerFlags", UNSET))

        def _parse_categories(
            data: object,
        ) -> Union[None, Unset, list["IndexerCategory"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = IndexerCategory.from_dict(
                        categories_type_0_item_data
                    )

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IndexerCategory"]], data)

        categories = _parse_categories(d.pop("categories", UNSET))

        def _parse_magnet_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        magnet_url = _parse_magnet_url(d.pop("magnetUrl", UNSET))

        def _parse_info_hash(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_hash = _parse_info_hash(d.pop("infoHash", UNSET))

        def _parse_seeders(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seeders = _parse_seeders(d.pop("seeders", UNSET))

        def _parse_leechers(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        leechers = _parse_leechers(d.pop("leechers", UNSET))

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, DownloadProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = DownloadProtocol(_protocol)

        def _parse_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_download_client_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        download_client_id = _parse_download_client_id(d.pop("downloadClientId", UNSET))

        release_resource = cls(
            id=id,
            guid=guid,
            age=age,
            age_hours=age_hours,
            age_minutes=age_minutes,
            size=size,
            files=files,
            grabs=grabs,
            indexer_id=indexer_id,
            indexer=indexer,
            sub_group=sub_group,
            release_hash=release_hash,
            title=title,
            sort_title=sort_title,
            imdb_id=imdb_id,
            tmdb_id=tmdb_id,
            tvdb_id=tvdb_id,
            tv_maze_id=tv_maze_id,
            publish_date=publish_date,
            comment_url=comment_url,
            download_url=download_url,
            info_url=info_url,
            poster_url=poster_url,
            indexer_flags=indexer_flags,
            categories=categories,
            magnet_url=magnet_url,
            info_hash=info_hash,
            seeders=seeders,
            leechers=leechers,
            protocol=protocol,
            file_name=file_name,
            download_client_id=download_client_id,
        )

        return release_resource
