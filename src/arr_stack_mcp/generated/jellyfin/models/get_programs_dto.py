import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.image_type import ImageType
from ..models.item_fields import ItemFields
from ..models.item_sort_by import ItemSortBy
from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProgramsDto")


@_attrs_define
class GetProgramsDto:
    """Get programs dto.

    Attributes:
        channel_ids (Union[None, Unset, list[UUID]]): Gets or sets the channels to return guide information for.
        user_id (Union[None, UUID, Unset]): Gets or sets optional. Filter by user id.
        min_start_date (Union[None, Unset, datetime.datetime]): Gets or sets the minimum premiere start date.
        has_aired (Union[None, Unset, bool]): Gets or sets filter by programs that have completed airing, or not.
        is_airing (Union[None, Unset, bool]): Gets or sets filter by programs that are currently airing, or not.
        max_start_date (Union[None, Unset, datetime.datetime]): Gets or sets the maximum premiere start date.
        min_end_date (Union[None, Unset, datetime.datetime]): Gets or sets the minimum premiere end date.
        max_end_date (Union[None, Unset, datetime.datetime]): Gets or sets the maximum premiere end date.
        is_movie (Union[None, Unset, bool]): Gets or sets filter for movies.
        is_series (Union[None, Unset, bool]): Gets or sets filter for series.
        is_news (Union[None, Unset, bool]): Gets or sets filter for news.
        is_kids (Union[None, Unset, bool]): Gets or sets filter for kids.
        is_sports (Union[None, Unset, bool]): Gets or sets filter for sports.
        start_index (Union[None, Unset, int]): Gets or sets the record index to start at. All items with a lower index
            will be dropped from the results.
        limit (Union[None, Unset, int]): Gets or sets the maximum number of records to return.
        sort_by (Union[None, Unset, list[ItemSortBy]]): Gets or sets specify one or more sort orders, comma delimited.
            Options: Name, StartDate.
        sort_order (Union[None, Unset, list[SortOrder]]): Gets or sets sort order.
        genres (Union[None, Unset, list[str]]): Gets or sets the genres to return guide information for.
        genre_ids (Union[None, Unset, list[UUID]]): Gets or sets the genre ids to return guide information for.
        enable_images (Union[None, Unset, bool]): Gets or sets include image information in output.
        enable_total_record_count (Union[Unset, bool]): Gets or sets a value indicating whether retrieve total record
            count. Default: True.
        image_type_limit (Union[None, Unset, int]): Gets or sets the max number of images to return, per image type.
        enable_image_types (Union[None, Unset, list[ImageType]]): Gets or sets the image types to include in the output.
        enable_user_data (Union[None, Unset, bool]): Gets or sets include user data.
        series_timer_id (Union[None, Unset, str]): Gets or sets filter by series timer id.
        library_series_id (Union[None, UUID, Unset]): Gets or sets filter by library series id.
        fields (Union[None, Unset, list[ItemFields]]): Gets or sets specify additional fields of information to return
            in the output.
    """

    channel_ids: Union[None, Unset, list[UUID]] = UNSET
    user_id: Union[None, UUID, Unset] = UNSET
    min_start_date: Union[None, Unset, datetime.datetime] = UNSET
    has_aired: Union[None, Unset, bool] = UNSET
    is_airing: Union[None, Unset, bool] = UNSET
    max_start_date: Union[None, Unset, datetime.datetime] = UNSET
    min_end_date: Union[None, Unset, datetime.datetime] = UNSET
    max_end_date: Union[None, Unset, datetime.datetime] = UNSET
    is_movie: Union[None, Unset, bool] = UNSET
    is_series: Union[None, Unset, bool] = UNSET
    is_news: Union[None, Unset, bool] = UNSET
    is_kids: Union[None, Unset, bool] = UNSET
    is_sports: Union[None, Unset, bool] = UNSET
    start_index: Union[None, Unset, int] = UNSET
    limit: Union[None, Unset, int] = UNSET
    sort_by: Union[None, Unset, list[ItemSortBy]] = UNSET
    sort_order: Union[None, Unset, list[SortOrder]] = UNSET
    genres: Union[None, Unset, list[str]] = UNSET
    genre_ids: Union[None, Unset, list[UUID]] = UNSET
    enable_images: Union[None, Unset, bool] = UNSET
    enable_total_record_count: Union[Unset, bool] = True
    image_type_limit: Union[None, Unset, int] = UNSET
    enable_image_types: Union[None, Unset, list[ImageType]] = UNSET
    enable_user_data: Union[None, Unset, bool] = UNSET
    series_timer_id: Union[None, Unset, str] = UNSET
    library_series_id: Union[None, UUID, Unset] = UNSET
    fields: Union[None, Unset, list[ItemFields]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel_ids: Union[None, Unset, list[str]]
        if isinstance(self.channel_ids, Unset):
            channel_ids = UNSET
        elif isinstance(self.channel_ids, list):
            channel_ids = []
            for channel_ids_type_0_item_data in self.channel_ids:
                channel_ids_type_0_item = str(channel_ids_type_0_item_data)
                channel_ids.append(channel_ids_type_0_item)

        else:
            channel_ids = self.channel_ids

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        min_start_date: Union[None, Unset, str]
        if isinstance(self.min_start_date, Unset):
            min_start_date = UNSET
        elif isinstance(self.min_start_date, datetime.datetime):
            min_start_date = self.min_start_date.isoformat()
        else:
            min_start_date = self.min_start_date

        has_aired: Union[None, Unset, bool]
        if isinstance(self.has_aired, Unset):
            has_aired = UNSET
        else:
            has_aired = self.has_aired

        is_airing: Union[None, Unset, bool]
        if isinstance(self.is_airing, Unset):
            is_airing = UNSET
        else:
            is_airing = self.is_airing

        max_start_date: Union[None, Unset, str]
        if isinstance(self.max_start_date, Unset):
            max_start_date = UNSET
        elif isinstance(self.max_start_date, datetime.datetime):
            max_start_date = self.max_start_date.isoformat()
        else:
            max_start_date = self.max_start_date

        min_end_date: Union[None, Unset, str]
        if isinstance(self.min_end_date, Unset):
            min_end_date = UNSET
        elif isinstance(self.min_end_date, datetime.datetime):
            min_end_date = self.min_end_date.isoformat()
        else:
            min_end_date = self.min_end_date

        max_end_date: Union[None, Unset, str]
        if isinstance(self.max_end_date, Unset):
            max_end_date = UNSET
        elif isinstance(self.max_end_date, datetime.datetime):
            max_end_date = self.max_end_date.isoformat()
        else:
            max_end_date = self.max_end_date

        is_movie: Union[None, Unset, bool]
        if isinstance(self.is_movie, Unset):
            is_movie = UNSET
        else:
            is_movie = self.is_movie

        is_series: Union[None, Unset, bool]
        if isinstance(self.is_series, Unset):
            is_series = UNSET
        else:
            is_series = self.is_series

        is_news: Union[None, Unset, bool]
        if isinstance(self.is_news, Unset):
            is_news = UNSET
        else:
            is_news = self.is_news

        is_kids: Union[None, Unset, bool]
        if isinstance(self.is_kids, Unset):
            is_kids = UNSET
        else:
            is_kids = self.is_kids

        is_sports: Union[None, Unset, bool]
        if isinstance(self.is_sports, Unset):
            is_sports = UNSET
        else:
            is_sports = self.is_sports

        start_index: Union[None, Unset, int]
        if isinstance(self.start_index, Unset):
            start_index = UNSET
        else:
            start_index = self.start_index

        limit: Union[None, Unset, int]
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        sort_by: Union[None, Unset, list[str]]
        if isinstance(self.sort_by, Unset):
            sort_by = UNSET
        elif isinstance(self.sort_by, list):
            sort_by = []
            for sort_by_type_0_item_data in self.sort_by:
                sort_by_type_0_item = sort_by_type_0_item_data.value
                sort_by.append(sort_by_type_0_item)

        else:
            sort_by = self.sort_by

        sort_order: Union[None, Unset, list[str]]
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        elif isinstance(self.sort_order, list):
            sort_order = []
            for sort_order_type_0_item_data in self.sort_order:
                sort_order_type_0_item = sort_order_type_0_item_data.value
                sort_order.append(sort_order_type_0_item)

        else:
            sort_order = self.sort_order

        genres: Union[None, Unset, list[str]]
        if isinstance(self.genres, Unset):
            genres = UNSET
        elif isinstance(self.genres, list):
            genres = self.genres

        else:
            genres = self.genres

        genre_ids: Union[None, Unset, list[str]]
        if isinstance(self.genre_ids, Unset):
            genre_ids = UNSET
        elif isinstance(self.genre_ids, list):
            genre_ids = []
            for genre_ids_type_0_item_data in self.genre_ids:
                genre_ids_type_0_item = str(genre_ids_type_0_item_data)
                genre_ids.append(genre_ids_type_0_item)

        else:
            genre_ids = self.genre_ids

        enable_images: Union[None, Unset, bool]
        if isinstance(self.enable_images, Unset):
            enable_images = UNSET
        else:
            enable_images = self.enable_images

        enable_total_record_count = self.enable_total_record_count

        image_type_limit: Union[None, Unset, int]
        if isinstance(self.image_type_limit, Unset):
            image_type_limit = UNSET
        else:
            image_type_limit = self.image_type_limit

        enable_image_types: Union[None, Unset, list[str]]
        if isinstance(self.enable_image_types, Unset):
            enable_image_types = UNSET
        elif isinstance(self.enable_image_types, list):
            enable_image_types = []
            for enable_image_types_type_0_item_data in self.enable_image_types:
                enable_image_types_type_0_item = (
                    enable_image_types_type_0_item_data.value
                )
                enable_image_types.append(enable_image_types_type_0_item)

        else:
            enable_image_types = self.enable_image_types

        enable_user_data: Union[None, Unset, bool]
        if isinstance(self.enable_user_data, Unset):
            enable_user_data = UNSET
        else:
            enable_user_data = self.enable_user_data

        series_timer_id: Union[None, Unset, str]
        if isinstance(self.series_timer_id, Unset):
            series_timer_id = UNSET
        else:
            series_timer_id = self.series_timer_id

        library_series_id: Union[None, Unset, str]
        if isinstance(self.library_series_id, Unset):
            library_series_id = UNSET
        elif isinstance(self.library_series_id, UUID):
            library_series_id = str(self.library_series_id)
        else:
            library_series_id = self.library_series_id

        fields: Union[None, Unset, list[str]]
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.value
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if channel_ids is not UNSET:
            field_dict["ChannelIds"] = channel_ids
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if min_start_date is not UNSET:
            field_dict["MinStartDate"] = min_start_date
        if has_aired is not UNSET:
            field_dict["HasAired"] = has_aired
        if is_airing is not UNSET:
            field_dict["IsAiring"] = is_airing
        if max_start_date is not UNSET:
            field_dict["MaxStartDate"] = max_start_date
        if min_end_date is not UNSET:
            field_dict["MinEndDate"] = min_end_date
        if max_end_date is not UNSET:
            field_dict["MaxEndDate"] = max_end_date
        if is_movie is not UNSET:
            field_dict["IsMovie"] = is_movie
        if is_series is not UNSET:
            field_dict["IsSeries"] = is_series
        if is_news is not UNSET:
            field_dict["IsNews"] = is_news
        if is_kids is not UNSET:
            field_dict["IsKids"] = is_kids
        if is_sports is not UNSET:
            field_dict["IsSports"] = is_sports
        if start_index is not UNSET:
            field_dict["StartIndex"] = start_index
        if limit is not UNSET:
            field_dict["Limit"] = limit
        if sort_by is not UNSET:
            field_dict["SortBy"] = sort_by
        if sort_order is not UNSET:
            field_dict["SortOrder"] = sort_order
        if genres is not UNSET:
            field_dict["Genres"] = genres
        if genre_ids is not UNSET:
            field_dict["GenreIds"] = genre_ids
        if enable_images is not UNSET:
            field_dict["EnableImages"] = enable_images
        if enable_total_record_count is not UNSET:
            field_dict["EnableTotalRecordCount"] = enable_total_record_count
        if image_type_limit is not UNSET:
            field_dict["ImageTypeLimit"] = image_type_limit
        if enable_image_types is not UNSET:
            field_dict["EnableImageTypes"] = enable_image_types
        if enable_user_data is not UNSET:
            field_dict["EnableUserData"] = enable_user_data
        if series_timer_id is not UNSET:
            field_dict["SeriesTimerId"] = series_timer_id
        if library_series_id is not UNSET:
            field_dict["LibrarySeriesId"] = library_series_id
        if fields is not UNSET:
            field_dict["Fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_channel_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channel_ids_type_0 = []
                _channel_ids_type_0 = data
                for channel_ids_type_0_item_data in _channel_ids_type_0:
                    channel_ids_type_0_item = UUID(channel_ids_type_0_item_data)

                    channel_ids_type_0.append(channel_ids_type_0_item)

                return channel_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        channel_ids = _parse_channel_ids(d.pop("ChannelIds", UNSET))

        def _parse_user_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        def _parse_min_start_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                min_start_date_type_0 = isoparse(data)

                return min_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        min_start_date = _parse_min_start_date(d.pop("MinStartDate", UNSET))

        def _parse_has_aired(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_aired = _parse_has_aired(d.pop("HasAired", UNSET))

        def _parse_is_airing(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_airing = _parse_is_airing(d.pop("IsAiring", UNSET))

        def _parse_max_start_date(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                max_start_date_type_0 = isoparse(data)

                return max_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        max_start_date = _parse_max_start_date(d.pop("MaxStartDate", UNSET))

        def _parse_min_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                min_end_date_type_0 = isoparse(data)

                return min_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        min_end_date = _parse_min_end_date(d.pop("MinEndDate", UNSET))

        def _parse_max_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                max_end_date_type_0 = isoparse(data)

                return max_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        max_end_date = _parse_max_end_date(d.pop("MaxEndDate", UNSET))

        def _parse_is_movie(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_movie = _parse_is_movie(d.pop("IsMovie", UNSET))

        def _parse_is_series(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_series = _parse_is_series(d.pop("IsSeries", UNSET))

        def _parse_is_news(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_news = _parse_is_news(d.pop("IsNews", UNSET))

        def _parse_is_kids(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_kids = _parse_is_kids(d.pop("IsKids", UNSET))

        def _parse_is_sports(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_sports = _parse_is_sports(d.pop("IsSports", UNSET))

        def _parse_start_index(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        start_index = _parse_start_index(d.pop("StartIndex", UNSET))

        def _parse_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limit = _parse_limit(d.pop("Limit", UNSET))

        def _parse_sort_by(data: object) -> Union[None, Unset, list[ItemSortBy]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_by_type_0 = []
                _sort_by_type_0 = data
                for sort_by_type_0_item_data in _sort_by_type_0:
                    sort_by_type_0_item = ItemSortBy(sort_by_type_0_item_data)

                    sort_by_type_0.append(sort_by_type_0_item)

                return sort_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[ItemSortBy]], data)

        sort_by = _parse_sort_by(d.pop("SortBy", UNSET))

        def _parse_sort_order(data: object) -> Union[None, Unset, list[SortOrder]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_order_type_0 = []
                _sort_order_type_0 = data
                for sort_order_type_0_item_data in _sort_order_type_0:
                    sort_order_type_0_item = SortOrder(sort_order_type_0_item_data)

                    sort_order_type_0.append(sort_order_type_0_item)

                return sort_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[SortOrder]], data)

        sort_order = _parse_sort_order(d.pop("SortOrder", UNSET))

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

        genres = _parse_genres(d.pop("Genres", UNSET))

        def _parse_genre_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                genre_ids_type_0 = []
                _genre_ids_type_0 = data
                for genre_ids_type_0_item_data in _genre_ids_type_0:
                    genre_ids_type_0_item = UUID(genre_ids_type_0_item_data)

                    genre_ids_type_0.append(genre_ids_type_0_item)

                return genre_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        genre_ids = _parse_genre_ids(d.pop("GenreIds", UNSET))

        def _parse_enable_images(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_images = _parse_enable_images(d.pop("EnableImages", UNSET))

        enable_total_record_count = d.pop("EnableTotalRecordCount", UNSET)

        def _parse_image_type_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        image_type_limit = _parse_image_type_limit(d.pop("ImageTypeLimit", UNSET))

        def _parse_enable_image_types(
            data: object,
        ) -> Union[None, Unset, list[ImageType]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enable_image_types_type_0 = []
                _enable_image_types_type_0 = data
                for enable_image_types_type_0_item_data in _enable_image_types_type_0:
                    enable_image_types_type_0_item = ImageType(
                        enable_image_types_type_0_item_data
                    )

                    enable_image_types_type_0.append(enable_image_types_type_0_item)

                return enable_image_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[ImageType]], data)

        enable_image_types = _parse_enable_image_types(d.pop("EnableImageTypes", UNSET))

        def _parse_enable_user_data(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_user_data = _parse_enable_user_data(d.pop("EnableUserData", UNSET))

        def _parse_series_timer_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_timer_id = _parse_series_timer_id(d.pop("SeriesTimerId", UNSET))

        def _parse_library_series_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                library_series_id_type_0 = UUID(data)

                return library_series_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        library_series_id = _parse_library_series_id(d.pop("LibrarySeriesId", UNSET))

        def _parse_fields(data: object) -> Union[None, Unset, list[ItemFields]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = ItemFields(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[ItemFields]], data)

        fields = _parse_fields(d.pop("Fields", UNSET))

        get_programs_dto = cls(
            channel_ids=channel_ids,
            user_id=user_id,
            min_start_date=min_start_date,
            has_aired=has_aired,
            is_airing=is_airing,
            max_start_date=max_start_date,
            min_end_date=min_end_date,
            max_end_date=max_end_date,
            is_movie=is_movie,
            is_series=is_series,
            is_news=is_news,
            is_kids=is_kids,
            is_sports=is_sports,
            start_index=start_index,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            genres=genres,
            genre_ids=genre_ids,
            enable_images=enable_images,
            enable_total_record_count=enable_total_record_count,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
            series_timer_id=series_timer_id,
            library_series_id=library_series_id,
            fields=fields,
        )

        return get_programs_dto
