from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.episode_resource import EpisodeResource
    from ..models.language import Language
    from ..models.parsed_episode_info import ParsedEpisodeInfo
    from ..models.series_resource import SeriesResource


T = TypeVar("T", bound="ParseResource")


@_attrs_define
class ParseResource:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[None, Unset, str]):
        parsed_episode_info (Union[Unset, ParsedEpisodeInfo]):
        series (Union[Unset, SeriesResource]):
        episodes (Union[None, Unset, list['EpisodeResource']]):
        languages (Union[None, Unset, list['Language']]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    parsed_episode_info: Union[Unset, "ParsedEpisodeInfo"] = UNSET
    series: Union[Unset, "SeriesResource"] = UNSET
    episodes: Union[None, Unset, list["EpisodeResource"]] = UNSET
    languages: Union[None, Unset, list["Language"]] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        parsed_episode_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parsed_episode_info, Unset):
            parsed_episode_info = self.parsed_episode_info.to_dict()

        series: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        episodes: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.episodes, Unset):
            episodes = UNSET
        elif isinstance(self.episodes, list):
            episodes = []
            for episodes_type_0_item_data in self.episodes:
                episodes_type_0_item = episodes_type_0_item_data.to_dict()
                episodes.append(episodes_type_0_item)

        else:
            episodes = self.episodes

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

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if parsed_episode_info is not UNSET:
            field_dict["parsedEpisodeInfo"] = parsed_episode_info
        if series is not UNSET:
            field_dict["series"] = series
        if episodes is not UNSET:
            field_dict["episodes"] = episodes
        if languages is not UNSET:
            field_dict["languages"] = languages
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.episode_resource import EpisodeResource
        from ..models.language import Language
        from ..models.parsed_episode_info import ParsedEpisodeInfo
        from ..models.series_resource import SeriesResource

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        _parsed_episode_info = d.pop("parsedEpisodeInfo", UNSET)
        parsed_episode_info: Union[Unset, ParsedEpisodeInfo]
        if isinstance(_parsed_episode_info, Unset):
            parsed_episode_info = UNSET
        else:
            parsed_episode_info = ParsedEpisodeInfo.from_dict(_parsed_episode_info)

        _series = d.pop("series", UNSET)
        series: Union[Unset, SeriesResource]
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = SeriesResource.from_dict(_series)

        def _parse_episodes(
            data: object,
        ) -> Union[None, Unset, list["EpisodeResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                episodes_type_0 = []
                _episodes_type_0 = data
                for episodes_type_0_item_data in _episodes_type_0:
                    episodes_type_0_item = EpisodeResource.from_dict(
                        episodes_type_0_item_data
                    )

                    episodes_type_0.append(episodes_type_0_item)

                return episodes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["EpisodeResource"]], data)

        episodes = _parse_episodes(d.pop("episodes", UNSET))

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

        parse_resource = cls(
            id=id,
            title=title,
            parsed_episode_info=parsed_episode_info,
            series=series,
            episodes=episodes,
            languages=languages,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
        )

        return parse_resource
