from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_value_pair import NameValuePair


T = TypeVar("T", bound="ListingsProviderInfo")


@_attrs_define
class ListingsProviderInfo:
    """
    Attributes:
        id (Union[None, Unset, str]):
        type_ (Union[None, Unset, str]):
        username (Union[None, Unset, str]):
        password (Union[None, Unset, str]):
        listings_id (Union[None, Unset, str]):
        zip_code (Union[None, Unset, str]):
        country (Union[None, Unset, str]):
        path (Union[None, Unset, str]):
        enabled_tuners (Union[None, Unset, list[str]]):
        enable_all_tuners (Union[Unset, bool]):
        news_categories (Union[None, Unset, list[str]]):
        sports_categories (Union[None, Unset, list[str]]):
        kids_categories (Union[None, Unset, list[str]]):
        movie_categories (Union[None, Unset, list[str]]):
        channel_mappings (Union[None, Unset, list['NameValuePair']]):
        movie_prefix (Union[None, Unset, str]):
        preferred_language (Union[None, Unset, str]):
        user_agent (Union[None, Unset, str]):
    """

    id: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    username: Union[None, Unset, str] = UNSET
    password: Union[None, Unset, str] = UNSET
    listings_id: Union[None, Unset, str] = UNSET
    zip_code: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    enabled_tuners: Union[None, Unset, list[str]] = UNSET
    enable_all_tuners: Union[Unset, bool] = UNSET
    news_categories: Union[None, Unset, list[str]] = UNSET
    sports_categories: Union[None, Unset, list[str]] = UNSET
    kids_categories: Union[None, Unset, list[str]] = UNSET
    movie_categories: Union[None, Unset, list[str]] = UNSET
    channel_mappings: Union[None, Unset, list["NameValuePair"]] = UNSET
    movie_prefix: Union[None, Unset, str] = UNSET
    preferred_language: Union[None, Unset, str] = UNSET
    user_agent: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        username: Union[None, Unset, str]
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        password: Union[None, Unset, str]
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        listings_id: Union[None, Unset, str]
        if isinstance(self.listings_id, Unset):
            listings_id = UNSET
        else:
            listings_id = self.listings_id

        zip_code: Union[None, Unset, str]
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        enabled_tuners: Union[None, Unset, list[str]]
        if isinstance(self.enabled_tuners, Unset):
            enabled_tuners = UNSET
        elif isinstance(self.enabled_tuners, list):
            enabled_tuners = self.enabled_tuners

        else:
            enabled_tuners = self.enabled_tuners

        enable_all_tuners = self.enable_all_tuners

        news_categories: Union[None, Unset, list[str]]
        if isinstance(self.news_categories, Unset):
            news_categories = UNSET
        elif isinstance(self.news_categories, list):
            news_categories = self.news_categories

        else:
            news_categories = self.news_categories

        sports_categories: Union[None, Unset, list[str]]
        if isinstance(self.sports_categories, Unset):
            sports_categories = UNSET
        elif isinstance(self.sports_categories, list):
            sports_categories = self.sports_categories

        else:
            sports_categories = self.sports_categories

        kids_categories: Union[None, Unset, list[str]]
        if isinstance(self.kids_categories, Unset):
            kids_categories = UNSET
        elif isinstance(self.kids_categories, list):
            kids_categories = self.kids_categories

        else:
            kids_categories = self.kids_categories

        movie_categories: Union[None, Unset, list[str]]
        if isinstance(self.movie_categories, Unset):
            movie_categories = UNSET
        elif isinstance(self.movie_categories, list):
            movie_categories = self.movie_categories

        else:
            movie_categories = self.movie_categories

        channel_mappings: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.channel_mappings, Unset):
            channel_mappings = UNSET
        elif isinstance(self.channel_mappings, list):
            channel_mappings = []
            for channel_mappings_type_0_item_data in self.channel_mappings:
                channel_mappings_type_0_item = (
                    channel_mappings_type_0_item_data.to_dict()
                )
                channel_mappings.append(channel_mappings_type_0_item)

        else:
            channel_mappings = self.channel_mappings

        movie_prefix: Union[None, Unset, str]
        if isinstance(self.movie_prefix, Unset):
            movie_prefix = UNSET
        else:
            movie_prefix = self.movie_prefix

        preferred_language: Union[None, Unset, str]
        if isinstance(self.preferred_language, Unset):
            preferred_language = UNSET
        else:
            preferred_language = self.preferred_language

        user_agent: Union[None, Unset, str]
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if username is not UNSET:
            field_dict["Username"] = username
        if password is not UNSET:
            field_dict["Password"] = password
        if listings_id is not UNSET:
            field_dict["ListingsId"] = listings_id
        if zip_code is not UNSET:
            field_dict["ZipCode"] = zip_code
        if country is not UNSET:
            field_dict["Country"] = country
        if path is not UNSET:
            field_dict["Path"] = path
        if enabled_tuners is not UNSET:
            field_dict["EnabledTuners"] = enabled_tuners
        if enable_all_tuners is not UNSET:
            field_dict["EnableAllTuners"] = enable_all_tuners
        if news_categories is not UNSET:
            field_dict["NewsCategories"] = news_categories
        if sports_categories is not UNSET:
            field_dict["SportsCategories"] = sports_categories
        if kids_categories is not UNSET:
            field_dict["KidsCategories"] = kids_categories
        if movie_categories is not UNSET:
            field_dict["MovieCategories"] = movie_categories
        if channel_mappings is not UNSET:
            field_dict["ChannelMappings"] = channel_mappings
        if movie_prefix is not UNSET:
            field_dict["MoviePrefix"] = movie_prefix
        if preferred_language is not UNSET:
            field_dict["PreferredLanguage"] = preferred_language
        if user_agent is not UNSET:
            field_dict["UserAgent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.name_value_pair import NameValuePair

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        username = _parse_username(d.pop("Username", UNSET))

        def _parse_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        password = _parse_password(d.pop("Password", UNSET))

        def _parse_listings_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        listings_id = _parse_listings_id(d.pop("ListingsId", UNSET))

        def _parse_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zip_code = _parse_zip_code(d.pop("ZipCode", UNSET))

        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("Country", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("Path", UNSET))

        def _parse_enabled_tuners(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                enabled_tuners_type_0 = cast(list[str], data)

                return enabled_tuners_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        enabled_tuners = _parse_enabled_tuners(d.pop("EnabledTuners", UNSET))

        enable_all_tuners = d.pop("EnableAllTuners", UNSET)

        def _parse_news_categories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                news_categories_type_0 = cast(list[str], data)

                return news_categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        news_categories = _parse_news_categories(d.pop("NewsCategories", UNSET))

        def _parse_sports_categories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sports_categories_type_0 = cast(list[str], data)

                return sports_categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        sports_categories = _parse_sports_categories(d.pop("SportsCategories", UNSET))

        def _parse_kids_categories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kids_categories_type_0 = cast(list[str], data)

                return kids_categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        kids_categories = _parse_kids_categories(d.pop("KidsCategories", UNSET))

        def _parse_movie_categories(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                movie_categories_type_0 = cast(list[str], data)

                return movie_categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        movie_categories = _parse_movie_categories(d.pop("MovieCategories", UNSET))

        def _parse_channel_mappings(
            data: object,
        ) -> Union[None, Unset, list["NameValuePair"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channel_mappings_type_0 = []
                _channel_mappings_type_0 = data
                for channel_mappings_type_0_item_data in _channel_mappings_type_0:
                    channel_mappings_type_0_item = NameValuePair.from_dict(
                        channel_mappings_type_0_item_data
                    )

                    channel_mappings_type_0.append(channel_mappings_type_0_item)

                return channel_mappings_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NameValuePair"]], data)

        channel_mappings = _parse_channel_mappings(d.pop("ChannelMappings", UNSET))

        def _parse_movie_prefix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        movie_prefix = _parse_movie_prefix(d.pop("MoviePrefix", UNSET))

        def _parse_preferred_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_language = _parse_preferred_language(
            d.pop("PreferredLanguage", UNSET)
        )

        def _parse_user_agent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_agent = _parse_user_agent(d.pop("UserAgent", UNSET))

        listings_provider_info = cls(
            id=id,
            type_=type_,
            username=username,
            password=password,
            listings_id=listings_id,
            zip_code=zip_code,
            country=country,
            path=path,
            enabled_tuners=enabled_tuners,
            enable_all_tuners=enable_all_tuners,
            news_categories=news_categories,
            sports_categories=sports_categories,
            kids_categories=kids_categories,
            movie_categories=movie_categories,
            channel_mappings=channel_mappings,
            movie_prefix=movie_prefix,
            preferred_language=preferred_language,
            user_agent=user_agent,
        )

        return listings_provider_info
