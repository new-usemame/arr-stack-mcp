import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.movie_history_event_type import MovieHistoryEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.history_resource_data_type_0 import HistoryResourceDataType0
    from ..models.language import Language
    from ..models.movie_resource import MovieResource
    from ..models.quality_model import QualityModel


T = TypeVar("T", bound="HistoryResource")


@_attrs_define
class HistoryResource:
    """
    Attributes:
        id (Union[Unset, int]):
        movie_id (Union[Unset, int]):
        source_title (Union[None, Unset, str]):
        languages (Union[None, Unset, list['Language']]):
        quality (Union[Unset, QualityModel]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
        quality_cutoff_not_met (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):
        download_id (Union[None, Unset, str]):
        event_type (Union[Unset, MovieHistoryEventType]):
        data (Union['HistoryResourceDataType0', None, Unset]):
        movie (Union[Unset, MovieResource]):
    """

    id: Union[Unset, int] = UNSET
    movie_id: Union[Unset, int] = UNSET
    source_title: Union[None, Unset, str] = UNSET
    languages: Union[None, Unset, list["Language"]] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET
    quality_cutoff_not_met: Union[Unset, bool] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    download_id: Union[None, Unset, str] = UNSET
    event_type: Union[Unset, MovieHistoryEventType] = UNSET
    data: Union["HistoryResourceDataType0", None, Unset] = UNSET
    movie: Union[Unset, "MovieResource"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.history_resource_data_type_0 import HistoryResourceDataType0

        id = self.id

        movie_id = self.movie_id

        source_title: Union[None, Unset, str]
        if isinstance(self.source_title, Unset):
            source_title = UNSET
        else:
            source_title = self.source_title

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

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

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

        quality_cutoff_not_met = self.quality_cutoff_not_met

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        download_id: Union[None, Unset, str]
        if isinstance(self.download_id, Unset):
            download_id = UNSET
        else:
            download_id = self.download_id

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        data: Union[None, Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, HistoryResourceDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        movie: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.movie, Unset):
            movie = self.movie.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if movie_id is not UNSET:
            field_dict["movieId"] = movie_id
        if source_title is not UNSET:
            field_dict["sourceTitle"] = source_title
        if languages is not UNSET:
            field_dict["languages"] = languages
        if quality is not UNSET:
            field_dict["quality"] = quality
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score
        if quality_cutoff_not_met is not UNSET:
            field_dict["qualityCutoffNotMet"] = quality_cutoff_not_met
        if date is not UNSET:
            field_dict["date"] = date
        if download_id is not UNSET:
            field_dict["downloadId"] = download_id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if data is not UNSET:
            field_dict["data"] = data
        if movie is not UNSET:
            field_dict["movie"] = movie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.history_resource_data_type_0 import HistoryResourceDataType0
        from ..models.language import Language
        from ..models.movie_resource import MovieResource
        from ..models.quality_model import QualityModel

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        movie_id = d.pop("movieId", UNSET)

        def _parse_source_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_title = _parse_source_title(d.pop("sourceTitle", UNSET))

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

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

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

        quality_cutoff_not_met = d.pop("qualityCutoffNotMet", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        def _parse_download_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        download_id = _parse_download_id(d.pop("downloadId", UNSET))

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, MovieHistoryEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = MovieHistoryEventType(_event_type)

        def _parse_data(data: object) -> Union["HistoryResourceDataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = HistoryResourceDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HistoryResourceDataType0", None, Unset], data)

        data = _parse_data(d.pop("data", UNSET))

        _movie = d.pop("movie", UNSET)
        movie: Union[Unset, MovieResource]
        if isinstance(_movie, Unset):
            movie = UNSET
        else:
            movie = MovieResource.from_dict(_movie)

        history_resource = cls(
            id=id,
            movie_id=movie_id,
            source_title=source_title,
            languages=languages,
            quality=quality,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
            quality_cutoff_not_met=quality_cutoff_not_met,
            date=date,
            download_id=download_id,
            event_type=event_type,
            data=data,
            movie=movie,
        )

        return history_resource
