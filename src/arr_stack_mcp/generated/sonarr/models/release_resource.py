import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.download_protocol import DownloadProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alternate_title_resource import AlternateTitleResource
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.language import Language
    from ..models.quality_model import QualityModel
    from ..models.release_episode_resource import ReleaseEpisodeResource


T = TypeVar("T", bound="ReleaseResource")


@_attrs_define
class ReleaseResource:
    """
    Attributes:
        id (Union[Unset, int]):
        guid (Union[None, Unset, str]):
        quality (Union[Unset, QualityModel]):
        quality_weight (Union[Unset, int]):
        age (Union[Unset, int]):
        age_hours (Union[Unset, float]):
        age_minutes (Union[Unset, float]):
        size (Union[Unset, int]):
        indexer_id (Union[Unset, int]):
        indexer (Union[None, Unset, str]):
        release_group (Union[None, Unset, str]):
        sub_group (Union[None, Unset, str]):
        release_hash (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        full_season (Union[Unset, bool]):
        scene_source (Union[Unset, bool]):
        season_number (Union[Unset, int]):
        languages (Union[None, Unset, list['Language']]):
        language_weight (Union[Unset, int]):
        air_date (Union[None, Unset, str]):
        series_title (Union[None, Unset, str]):
        episode_numbers (Union[None, Unset, list[int]]):
        absolute_episode_numbers (Union[None, Unset, list[int]]):
        mapped_season_number (Union[None, Unset, int]):
        mapped_episode_numbers (Union[None, Unset, list[int]]):
        mapped_absolute_episode_numbers (Union[None, Unset, list[int]]):
        mapped_series_id (Union[None, Unset, int]):
        mapped_episode_info (Union[None, Unset, list['ReleaseEpisodeResource']]):
        approved (Union[Unset, bool]):
        temporarily_rejected (Union[Unset, bool]):
        rejected (Union[Unset, bool]):
        tvdb_id (Union[Unset, int]):
        tv_rage_id (Union[Unset, int]):
        imdb_id (Union[None, Unset, str]):
        rejections (Union[None, Unset, list[str]]):
        publish_date (Union[Unset, datetime.datetime]):
        comment_url (Union[None, Unset, str]):
        download_url (Union[None, Unset, str]):
        info_url (Union[None, Unset, str]):
        episode_requested (Union[Unset, bool]):
        download_allowed (Union[Unset, bool]):
        release_weight (Union[Unset, int]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
        scene_mapping (Union[Unset, AlternateTitleResource]):
        magnet_url (Union[None, Unset, str]):
        info_hash (Union[None, Unset, str]):
        seeders (Union[None, Unset, int]):
        leechers (Union[None, Unset, int]):
        protocol (Union[Unset, DownloadProtocol]):
        indexer_flags (Union[Unset, int]):
        is_daily (Union[Unset, bool]):
        is_absolute_numbering (Union[Unset, bool]):
        is_possible_special_episode (Union[Unset, bool]):
        special (Union[Unset, bool]):
        series_id (Union[None, Unset, int]):
        episode_id (Union[None, Unset, int]):
        episode_ids (Union[None, Unset, list[int]]):
        download_client_id (Union[None, Unset, int]):
        download_client (Union[None, Unset, str]):
        should_override (Union[None, Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    guid: Union[None, Unset, str] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    quality_weight: Union[Unset, int] = UNSET
    age: Union[Unset, int] = UNSET
    age_hours: Union[Unset, float] = UNSET
    age_minutes: Union[Unset, float] = UNSET
    size: Union[Unset, int] = UNSET
    indexer_id: Union[Unset, int] = UNSET
    indexer: Union[None, Unset, str] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    sub_group: Union[None, Unset, str] = UNSET
    release_hash: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    full_season: Union[Unset, bool] = UNSET
    scene_source: Union[Unset, bool] = UNSET
    season_number: Union[Unset, int] = UNSET
    languages: Union[None, Unset, list["Language"]] = UNSET
    language_weight: Union[Unset, int] = UNSET
    air_date: Union[None, Unset, str] = UNSET
    series_title: Union[None, Unset, str] = UNSET
    episode_numbers: Union[None, Unset, list[int]] = UNSET
    absolute_episode_numbers: Union[None, Unset, list[int]] = UNSET
    mapped_season_number: Union[None, Unset, int] = UNSET
    mapped_episode_numbers: Union[None, Unset, list[int]] = UNSET
    mapped_absolute_episode_numbers: Union[None, Unset, list[int]] = UNSET
    mapped_series_id: Union[None, Unset, int] = UNSET
    mapped_episode_info: Union[None, Unset, list["ReleaseEpisodeResource"]] = UNSET
    approved: Union[Unset, bool] = UNSET
    temporarily_rejected: Union[Unset, bool] = UNSET
    rejected: Union[Unset, bool] = UNSET
    tvdb_id: Union[Unset, int] = UNSET
    tv_rage_id: Union[Unset, int] = UNSET
    imdb_id: Union[None, Unset, str] = UNSET
    rejections: Union[None, Unset, list[str]] = UNSET
    publish_date: Union[Unset, datetime.datetime] = UNSET
    comment_url: Union[None, Unset, str] = UNSET
    download_url: Union[None, Unset, str] = UNSET
    info_url: Union[None, Unset, str] = UNSET
    episode_requested: Union[Unset, bool] = UNSET
    download_allowed: Union[Unset, bool] = UNSET
    release_weight: Union[Unset, int] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET
    scene_mapping: Union[Unset, "AlternateTitleResource"] = UNSET
    magnet_url: Union[None, Unset, str] = UNSET
    info_hash: Union[None, Unset, str] = UNSET
    seeders: Union[None, Unset, int] = UNSET
    leechers: Union[None, Unset, int] = UNSET
    protocol: Union[Unset, DownloadProtocol] = UNSET
    indexer_flags: Union[Unset, int] = UNSET
    is_daily: Union[Unset, bool] = UNSET
    is_absolute_numbering: Union[Unset, bool] = UNSET
    is_possible_special_episode: Union[Unset, bool] = UNSET
    special: Union[Unset, bool] = UNSET
    series_id: Union[None, Unset, int] = UNSET
    episode_id: Union[None, Unset, int] = UNSET
    episode_ids: Union[None, Unset, list[int]] = UNSET
    download_client_id: Union[None, Unset, int] = UNSET
    download_client: Union[None, Unset, str] = UNSET
    should_override: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        guid: Union[None, Unset, str]
        if isinstance(self.guid, Unset):
            guid = UNSET
        else:
            guid = self.guid

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        quality_weight = self.quality_weight

        age = self.age

        age_hours = self.age_hours

        age_minutes = self.age_minutes

        size = self.size

        indexer_id = self.indexer_id

        indexer: Union[None, Unset, str]
        if isinstance(self.indexer, Unset):
            indexer = UNSET
        else:
            indexer = self.indexer

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

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

        full_season = self.full_season

        scene_source = self.scene_source

        season_number = self.season_number

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

        language_weight = self.language_weight

        air_date: Union[None, Unset, str]
        if isinstance(self.air_date, Unset):
            air_date = UNSET
        else:
            air_date = self.air_date

        series_title: Union[None, Unset, str]
        if isinstance(self.series_title, Unset):
            series_title = UNSET
        else:
            series_title = self.series_title

        episode_numbers: Union[None, Unset, list[int]]
        if isinstance(self.episode_numbers, Unset):
            episode_numbers = UNSET
        elif isinstance(self.episode_numbers, list):
            episode_numbers = self.episode_numbers

        else:
            episode_numbers = self.episode_numbers

        absolute_episode_numbers: Union[None, Unset, list[int]]
        if isinstance(self.absolute_episode_numbers, Unset):
            absolute_episode_numbers = UNSET
        elif isinstance(self.absolute_episode_numbers, list):
            absolute_episode_numbers = self.absolute_episode_numbers

        else:
            absolute_episode_numbers = self.absolute_episode_numbers

        mapped_season_number: Union[None, Unset, int]
        if isinstance(self.mapped_season_number, Unset):
            mapped_season_number = UNSET
        else:
            mapped_season_number = self.mapped_season_number

        mapped_episode_numbers: Union[None, Unset, list[int]]
        if isinstance(self.mapped_episode_numbers, Unset):
            mapped_episode_numbers = UNSET
        elif isinstance(self.mapped_episode_numbers, list):
            mapped_episode_numbers = self.mapped_episode_numbers

        else:
            mapped_episode_numbers = self.mapped_episode_numbers

        mapped_absolute_episode_numbers: Union[None, Unset, list[int]]
        if isinstance(self.mapped_absolute_episode_numbers, Unset):
            mapped_absolute_episode_numbers = UNSET
        elif isinstance(self.mapped_absolute_episode_numbers, list):
            mapped_absolute_episode_numbers = self.mapped_absolute_episode_numbers

        else:
            mapped_absolute_episode_numbers = self.mapped_absolute_episode_numbers

        mapped_series_id: Union[None, Unset, int]
        if isinstance(self.mapped_series_id, Unset):
            mapped_series_id = UNSET
        else:
            mapped_series_id = self.mapped_series_id

        mapped_episode_info: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.mapped_episode_info, Unset):
            mapped_episode_info = UNSET
        elif isinstance(self.mapped_episode_info, list):
            mapped_episode_info = []
            for mapped_episode_info_type_0_item_data in self.mapped_episode_info:
                mapped_episode_info_type_0_item = (
                    mapped_episode_info_type_0_item_data.to_dict()
                )
                mapped_episode_info.append(mapped_episode_info_type_0_item)

        else:
            mapped_episode_info = self.mapped_episode_info

        approved = self.approved

        temporarily_rejected = self.temporarily_rejected

        rejected = self.rejected

        tvdb_id = self.tvdb_id

        tv_rage_id = self.tv_rage_id

        imdb_id: Union[None, Unset, str]
        if isinstance(self.imdb_id, Unset):
            imdb_id = UNSET
        else:
            imdb_id = self.imdb_id

        rejections: Union[None, Unset, list[str]]
        if isinstance(self.rejections, Unset):
            rejections = UNSET
        elif isinstance(self.rejections, list):
            rejections = self.rejections

        else:
            rejections = self.rejections

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

        episode_requested = self.episode_requested

        download_allowed = self.download_allowed

        release_weight = self.release_weight

        custom_formats: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_formats, Unset):
            custom_formats = UNSET
        elif isinstance(self.custom_formats, list):
            custom_formats = []
            for custom_formats_type_0_item_data in self.custom_formats:
                custom_formats_type_0_item = custom_formats_type_0_item_data.to_dict()
                custom_formats.append(custom_formats_type_0_item)

        else:
            custom_formats = self.custom_formats

        custom_format_score = self.custom_format_score

        scene_mapping: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scene_mapping, Unset):
            scene_mapping = self.scene_mapping.to_dict()

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

        indexer_flags = self.indexer_flags

        is_daily = self.is_daily

        is_absolute_numbering = self.is_absolute_numbering

        is_possible_special_episode = self.is_possible_special_episode

        special = self.special

        series_id: Union[None, Unset, int]
        if isinstance(self.series_id, Unset):
            series_id = UNSET
        else:
            series_id = self.series_id

        episode_id: Union[None, Unset, int]
        if isinstance(self.episode_id, Unset):
            episode_id = UNSET
        else:
            episode_id = self.episode_id

        episode_ids: Union[None, Unset, list[int]]
        if isinstance(self.episode_ids, Unset):
            episode_ids = UNSET
        elif isinstance(self.episode_ids, list):
            episode_ids = self.episode_ids

        else:
            episode_ids = self.episode_ids

        download_client_id: Union[None, Unset, int]
        if isinstance(self.download_client_id, Unset):
            download_client_id = UNSET
        else:
            download_client_id = self.download_client_id

        download_client: Union[None, Unset, str]
        if isinstance(self.download_client, Unset):
            download_client = UNSET
        else:
            download_client = self.download_client

        should_override: Union[None, Unset, bool]
        if isinstance(self.should_override, Unset):
            should_override = UNSET
        else:
            should_override = self.should_override

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if quality is not UNSET:
            field_dict["quality"] = quality
        if quality_weight is not UNSET:
            field_dict["qualityWeight"] = quality_weight
        if age is not UNSET:
            field_dict["age"] = age
        if age_hours is not UNSET:
            field_dict["ageHours"] = age_hours
        if age_minutes is not UNSET:
            field_dict["ageMinutes"] = age_minutes
        if size is not UNSET:
            field_dict["size"] = size
        if indexer_id is not UNSET:
            field_dict["indexerId"] = indexer_id
        if indexer is not UNSET:
            field_dict["indexer"] = indexer
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if sub_group is not UNSET:
            field_dict["subGroup"] = sub_group
        if release_hash is not UNSET:
            field_dict["releaseHash"] = release_hash
        if title is not UNSET:
            field_dict["title"] = title
        if full_season is not UNSET:
            field_dict["fullSeason"] = full_season
        if scene_source is not UNSET:
            field_dict["sceneSource"] = scene_source
        if season_number is not UNSET:
            field_dict["seasonNumber"] = season_number
        if languages is not UNSET:
            field_dict["languages"] = languages
        if language_weight is not UNSET:
            field_dict["languageWeight"] = language_weight
        if air_date is not UNSET:
            field_dict["airDate"] = air_date
        if series_title is not UNSET:
            field_dict["seriesTitle"] = series_title
        if episode_numbers is not UNSET:
            field_dict["episodeNumbers"] = episode_numbers
        if absolute_episode_numbers is not UNSET:
            field_dict["absoluteEpisodeNumbers"] = absolute_episode_numbers
        if mapped_season_number is not UNSET:
            field_dict["mappedSeasonNumber"] = mapped_season_number
        if mapped_episode_numbers is not UNSET:
            field_dict["mappedEpisodeNumbers"] = mapped_episode_numbers
        if mapped_absolute_episode_numbers is not UNSET:
            field_dict["mappedAbsoluteEpisodeNumbers"] = mapped_absolute_episode_numbers
        if mapped_series_id is not UNSET:
            field_dict["mappedSeriesId"] = mapped_series_id
        if mapped_episode_info is not UNSET:
            field_dict["mappedEpisodeInfo"] = mapped_episode_info
        if approved is not UNSET:
            field_dict["approved"] = approved
        if temporarily_rejected is not UNSET:
            field_dict["temporarilyRejected"] = temporarily_rejected
        if rejected is not UNSET:
            field_dict["rejected"] = rejected
        if tvdb_id is not UNSET:
            field_dict["tvdbId"] = tvdb_id
        if tv_rage_id is not UNSET:
            field_dict["tvRageId"] = tv_rage_id
        if imdb_id is not UNSET:
            field_dict["imdbId"] = imdb_id
        if rejections is not UNSET:
            field_dict["rejections"] = rejections
        if publish_date is not UNSET:
            field_dict["publishDate"] = publish_date
        if comment_url is not UNSET:
            field_dict["commentUrl"] = comment_url
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if info_url is not UNSET:
            field_dict["infoUrl"] = info_url
        if episode_requested is not UNSET:
            field_dict["episodeRequested"] = episode_requested
        if download_allowed is not UNSET:
            field_dict["downloadAllowed"] = download_allowed
        if release_weight is not UNSET:
            field_dict["releaseWeight"] = release_weight
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score
        if scene_mapping is not UNSET:
            field_dict["sceneMapping"] = scene_mapping
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
        if indexer_flags is not UNSET:
            field_dict["indexerFlags"] = indexer_flags
        if is_daily is not UNSET:
            field_dict["isDaily"] = is_daily
        if is_absolute_numbering is not UNSET:
            field_dict["isAbsoluteNumbering"] = is_absolute_numbering
        if is_possible_special_episode is not UNSET:
            field_dict["isPossibleSpecialEpisode"] = is_possible_special_episode
        if special is not UNSET:
            field_dict["special"] = special
        if series_id is not UNSET:
            field_dict["seriesId"] = series_id
        if episode_id is not UNSET:
            field_dict["episodeId"] = episode_id
        if episode_ids is not UNSET:
            field_dict["episodeIds"] = episode_ids
        if download_client_id is not UNSET:
            field_dict["downloadClientId"] = download_client_id
        if download_client is not UNSET:
            field_dict["downloadClient"] = download_client
        if should_override is not UNSET:
            field_dict["shouldOverride"] = should_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alternate_title_resource import AlternateTitleResource
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.language import Language
        from ..models.quality_model import QualityModel
        from ..models.release_episode_resource import ReleaseEpisodeResource

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

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        quality_weight = d.pop("qualityWeight", UNSET)

        age = d.pop("age", UNSET)

        age_hours = d.pop("ageHours", UNSET)

        age_minutes = d.pop("ageMinutes", UNSET)

        size = d.pop("size", UNSET)

        indexer_id = d.pop("indexerId", UNSET)

        def _parse_indexer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        indexer = _parse_indexer(d.pop("indexer", UNSET))

        def _parse_release_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_group = _parse_release_group(d.pop("releaseGroup", UNSET))

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

        full_season = d.pop("fullSeason", UNSET)

        scene_source = d.pop("sceneSource", UNSET)

        season_number = d.pop("seasonNumber", UNSET)

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

        language_weight = d.pop("languageWeight", UNSET)

        def _parse_air_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        air_date = _parse_air_date(d.pop("airDate", UNSET))

        def _parse_series_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_title = _parse_series_title(d.pop("seriesTitle", UNSET))

        def _parse_episode_numbers(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                episode_numbers_type_0 = cast(list[int], data)

                return episode_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        episode_numbers = _parse_episode_numbers(d.pop("episodeNumbers", UNSET))

        def _parse_absolute_episode_numbers(
            data: object,
        ) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                absolute_episode_numbers_type_0 = cast(list[int], data)

                return absolute_episode_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        absolute_episode_numbers = _parse_absolute_episode_numbers(
            d.pop("absoluteEpisodeNumbers", UNSET)
        )

        def _parse_mapped_season_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mapped_season_number = _parse_mapped_season_number(
            d.pop("mappedSeasonNumber", UNSET)
        )

        def _parse_mapped_episode_numbers(
            data: object,
        ) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mapped_episode_numbers_type_0 = cast(list[int], data)

                return mapped_episode_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        mapped_episode_numbers = _parse_mapped_episode_numbers(
            d.pop("mappedEpisodeNumbers", UNSET)
        )

        def _parse_mapped_absolute_episode_numbers(
            data: object,
        ) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mapped_absolute_episode_numbers_type_0 = cast(list[int], data)

                return mapped_absolute_episode_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        mapped_absolute_episode_numbers = _parse_mapped_absolute_episode_numbers(
            d.pop("mappedAbsoluteEpisodeNumbers", UNSET)
        )

        def _parse_mapped_series_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mapped_series_id = _parse_mapped_series_id(d.pop("mappedSeriesId", UNSET))

        def _parse_mapped_episode_info(
            data: object,
        ) -> Union[None, Unset, list["ReleaseEpisodeResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mapped_episode_info_type_0 = []
                _mapped_episode_info_type_0 = data
                for mapped_episode_info_type_0_item_data in _mapped_episode_info_type_0:
                    mapped_episode_info_type_0_item = ReleaseEpisodeResource.from_dict(
                        mapped_episode_info_type_0_item_data
                    )

                    mapped_episode_info_type_0.append(mapped_episode_info_type_0_item)

                return mapped_episode_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ReleaseEpisodeResource"]], data)

        mapped_episode_info = _parse_mapped_episode_info(
            d.pop("mappedEpisodeInfo", UNSET)
        )

        approved = d.pop("approved", UNSET)

        temporarily_rejected = d.pop("temporarilyRejected", UNSET)

        rejected = d.pop("rejected", UNSET)

        tvdb_id = d.pop("tvdbId", UNSET)

        tv_rage_id = d.pop("tvRageId", UNSET)

        def _parse_imdb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        imdb_id = _parse_imdb_id(d.pop("imdbId", UNSET))

        def _parse_rejections(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rejections_type_0 = cast(list[str], data)

                return rejections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        rejections = _parse_rejections(d.pop("rejections", UNSET))

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

        episode_requested = d.pop("episodeRequested", UNSET)

        download_allowed = d.pop("downloadAllowed", UNSET)

        release_weight = d.pop("releaseWeight", UNSET)

        def _parse_custom_formats(
            data: object,
        ) -> Union[None, Unset, list["CustomFormatResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_formats_type_0 = []
                _custom_formats_type_0 = data
                for custom_formats_type_0_item_data in _custom_formats_type_0:
                    custom_formats_type_0_item = CustomFormatResource.from_dict(
                        custom_formats_type_0_item_data
                    )

                    custom_formats_type_0.append(custom_formats_type_0_item)

                return custom_formats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["CustomFormatResource"]], data)

        custom_formats = _parse_custom_formats(d.pop("customFormats", UNSET))

        custom_format_score = d.pop("customFormatScore", UNSET)

        _scene_mapping = d.pop("sceneMapping", UNSET)
        scene_mapping: Union[Unset, AlternateTitleResource]
        if isinstance(_scene_mapping, Unset):
            scene_mapping = UNSET
        else:
            scene_mapping = AlternateTitleResource.from_dict(_scene_mapping)

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

        indexer_flags = d.pop("indexerFlags", UNSET)

        is_daily = d.pop("isDaily", UNSET)

        is_absolute_numbering = d.pop("isAbsoluteNumbering", UNSET)

        is_possible_special_episode = d.pop("isPossibleSpecialEpisode", UNSET)

        special = d.pop("special", UNSET)

        def _parse_series_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        series_id = _parse_series_id(d.pop("seriesId", UNSET))

        def _parse_episode_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        episode_id = _parse_episode_id(d.pop("episodeId", UNSET))

        def _parse_episode_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                episode_ids_type_0 = cast(list[int], data)

                return episode_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        episode_ids = _parse_episode_ids(d.pop("episodeIds", UNSET))

        def _parse_download_client_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        download_client_id = _parse_download_client_id(d.pop("downloadClientId", UNSET))

        def _parse_download_client(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_client = _parse_download_client(d.pop("downloadClient", UNSET))

        def _parse_should_override(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        should_override = _parse_should_override(d.pop("shouldOverride", UNSET))

        release_resource = cls(
            id=id,
            guid=guid,
            quality=quality,
            quality_weight=quality_weight,
            age=age,
            age_hours=age_hours,
            age_minutes=age_minutes,
            size=size,
            indexer_id=indexer_id,
            indexer=indexer,
            release_group=release_group,
            sub_group=sub_group,
            release_hash=release_hash,
            title=title,
            full_season=full_season,
            scene_source=scene_source,
            season_number=season_number,
            languages=languages,
            language_weight=language_weight,
            air_date=air_date,
            series_title=series_title,
            episode_numbers=episode_numbers,
            absolute_episode_numbers=absolute_episode_numbers,
            mapped_season_number=mapped_season_number,
            mapped_episode_numbers=mapped_episode_numbers,
            mapped_absolute_episode_numbers=mapped_absolute_episode_numbers,
            mapped_series_id=mapped_series_id,
            mapped_episode_info=mapped_episode_info,
            approved=approved,
            temporarily_rejected=temporarily_rejected,
            rejected=rejected,
            tvdb_id=tvdb_id,
            tv_rage_id=tv_rage_id,
            imdb_id=imdb_id,
            rejections=rejections,
            publish_date=publish_date,
            comment_url=comment_url,
            download_url=download_url,
            info_url=info_url,
            episode_requested=episode_requested,
            download_allowed=download_allowed,
            release_weight=release_weight,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
            scene_mapping=scene_mapping,
            magnet_url=magnet_url,
            info_hash=info_hash,
            seeders=seeders,
            leechers=leechers,
            protocol=protocol,
            indexer_flags=indexer_flags,
            is_daily=is_daily,
            is_absolute_numbering=is_absolute_numbering,
            is_possible_special_episode=is_possible_special_episode,
            special=special,
            series_id=series_id,
            episode_id=episode_id,
            episode_ids=episode_ids,
            download_client_id=download_client_id,
            download_client=download_client,
            should_override=should_override,
        )

        return release_resource
