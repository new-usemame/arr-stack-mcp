from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.book_search_param import BookSearchParam
from ..models.movie_search_param import MovieSearchParam
from ..models.music_search_param import MusicSearchParam
from ..models.search_param import SearchParam
from ..models.tv_search_param import TvSearchParam
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.indexer_category import IndexerCategory


T = TypeVar("T", bound="IndexerCapabilityResource")


@_attrs_define
class IndexerCapabilityResource:
    """
    Attributes:
        id (Union[Unset, int]):
        limits_max (Union[None, Unset, int]):
        limits_default (Union[None, Unset, int]):
        categories (Union[None, Unset, list['IndexerCategory']]):
        supports_raw_search (Union[Unset, bool]):
        search_params (Union[None, Unset, list[SearchParam]]):
        tv_search_params (Union[None, Unset, list[TvSearchParam]]):
        movie_search_params (Union[None, Unset, list[MovieSearchParam]]):
        music_search_params (Union[None, Unset, list[MusicSearchParam]]):
        book_search_params (Union[None, Unset, list[BookSearchParam]]):
    """

    id: Union[Unset, int] = UNSET
    limits_max: Union[None, Unset, int] = UNSET
    limits_default: Union[None, Unset, int] = UNSET
    categories: Union[None, Unset, list["IndexerCategory"]] = UNSET
    supports_raw_search: Union[Unset, bool] = UNSET
    search_params: Union[None, Unset, list[SearchParam]] = UNSET
    tv_search_params: Union[None, Unset, list[TvSearchParam]] = UNSET
    movie_search_params: Union[None, Unset, list[MovieSearchParam]] = UNSET
    music_search_params: Union[None, Unset, list[MusicSearchParam]] = UNSET
    book_search_params: Union[None, Unset, list[BookSearchParam]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        limits_max: Union[None, Unset, int]
        if isinstance(self.limits_max, Unset):
            limits_max = UNSET
        else:
            limits_max = self.limits_max

        limits_default: Union[None, Unset, int]
        if isinstance(self.limits_default, Unset):
            limits_default = UNSET
        else:
            limits_default = self.limits_default

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

        supports_raw_search = self.supports_raw_search

        search_params: Union[None, Unset, list[str]]
        if isinstance(self.search_params, Unset):
            search_params = UNSET
        elif isinstance(self.search_params, list):
            search_params = []
            for search_params_type_0_item_data in self.search_params:
                search_params_type_0_item = search_params_type_0_item_data.value
                search_params.append(search_params_type_0_item)

        else:
            search_params = self.search_params

        tv_search_params: Union[None, Unset, list[str]]
        if isinstance(self.tv_search_params, Unset):
            tv_search_params = UNSET
        elif isinstance(self.tv_search_params, list):
            tv_search_params = []
            for tv_search_params_type_0_item_data in self.tv_search_params:
                tv_search_params_type_0_item = tv_search_params_type_0_item_data.value
                tv_search_params.append(tv_search_params_type_0_item)

        else:
            tv_search_params = self.tv_search_params

        movie_search_params: Union[None, Unset, list[str]]
        if isinstance(self.movie_search_params, Unset):
            movie_search_params = UNSET
        elif isinstance(self.movie_search_params, list):
            movie_search_params = []
            for movie_search_params_type_0_item_data in self.movie_search_params:
                movie_search_params_type_0_item = (
                    movie_search_params_type_0_item_data.value
                )
                movie_search_params.append(movie_search_params_type_0_item)

        else:
            movie_search_params = self.movie_search_params

        music_search_params: Union[None, Unset, list[str]]
        if isinstance(self.music_search_params, Unset):
            music_search_params = UNSET
        elif isinstance(self.music_search_params, list):
            music_search_params = []
            for music_search_params_type_0_item_data in self.music_search_params:
                music_search_params_type_0_item = (
                    music_search_params_type_0_item_data.value
                )
                music_search_params.append(music_search_params_type_0_item)

        else:
            music_search_params = self.music_search_params

        book_search_params: Union[None, Unset, list[str]]
        if isinstance(self.book_search_params, Unset):
            book_search_params = UNSET
        elif isinstance(self.book_search_params, list):
            book_search_params = []
            for book_search_params_type_0_item_data in self.book_search_params:
                book_search_params_type_0_item = (
                    book_search_params_type_0_item_data.value
                )
                book_search_params.append(book_search_params_type_0_item)

        else:
            book_search_params = self.book_search_params

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if limits_max is not UNSET:
            field_dict["limitsMax"] = limits_max
        if limits_default is not UNSET:
            field_dict["limitsDefault"] = limits_default
        if categories is not UNSET:
            field_dict["categories"] = categories
        if supports_raw_search is not UNSET:
            field_dict["supportsRawSearch"] = supports_raw_search
        if search_params is not UNSET:
            field_dict["searchParams"] = search_params
        if tv_search_params is not UNSET:
            field_dict["tvSearchParams"] = tv_search_params
        if movie_search_params is not UNSET:
            field_dict["movieSearchParams"] = movie_search_params
        if music_search_params is not UNSET:
            field_dict["musicSearchParams"] = music_search_params
        if book_search_params is not UNSET:
            field_dict["bookSearchParams"] = book_search_params

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

        def _parse_limits_max(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limits_max = _parse_limits_max(d.pop("limitsMax", UNSET))

        def _parse_limits_default(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limits_default = _parse_limits_default(d.pop("limitsDefault", UNSET))

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

        supports_raw_search = d.pop("supportsRawSearch", UNSET)

        def _parse_search_params(data: object) -> Union[None, Unset, list[SearchParam]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                search_params_type_0 = []
                _search_params_type_0 = data
                for search_params_type_0_item_data in _search_params_type_0:
                    search_params_type_0_item = SearchParam(
                        search_params_type_0_item_data
                    )

                    search_params_type_0.append(search_params_type_0_item)

                return search_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[SearchParam]], data)

        search_params = _parse_search_params(d.pop("searchParams", UNSET))

        def _parse_tv_search_params(
            data: object,
        ) -> Union[None, Unset, list[TvSearchParam]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tv_search_params_type_0 = []
                _tv_search_params_type_0 = data
                for tv_search_params_type_0_item_data in _tv_search_params_type_0:
                    tv_search_params_type_0_item = TvSearchParam(
                        tv_search_params_type_0_item_data
                    )

                    tv_search_params_type_0.append(tv_search_params_type_0_item)

                return tv_search_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[TvSearchParam]], data)

        tv_search_params = _parse_tv_search_params(d.pop("tvSearchParams", UNSET))

        def _parse_movie_search_params(
            data: object,
        ) -> Union[None, Unset, list[MovieSearchParam]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                movie_search_params_type_0 = []
                _movie_search_params_type_0 = data
                for movie_search_params_type_0_item_data in _movie_search_params_type_0:
                    movie_search_params_type_0_item = MovieSearchParam(
                        movie_search_params_type_0_item_data
                    )

                    movie_search_params_type_0.append(movie_search_params_type_0_item)

                return movie_search_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[MovieSearchParam]], data)

        movie_search_params = _parse_movie_search_params(
            d.pop("movieSearchParams", UNSET)
        )

        def _parse_music_search_params(
            data: object,
        ) -> Union[None, Unset, list[MusicSearchParam]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                music_search_params_type_0 = []
                _music_search_params_type_0 = data
                for music_search_params_type_0_item_data in _music_search_params_type_0:
                    music_search_params_type_0_item = MusicSearchParam(
                        music_search_params_type_0_item_data
                    )

                    music_search_params_type_0.append(music_search_params_type_0_item)

                return music_search_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[MusicSearchParam]], data)

        music_search_params = _parse_music_search_params(
            d.pop("musicSearchParams", UNSET)
        )

        def _parse_book_search_params(
            data: object,
        ) -> Union[None, Unset, list[BookSearchParam]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                book_search_params_type_0 = []
                _book_search_params_type_0 = data
                for book_search_params_type_0_item_data in _book_search_params_type_0:
                    book_search_params_type_0_item = BookSearchParam(
                        book_search_params_type_0_item_data
                    )

                    book_search_params_type_0.append(book_search_params_type_0_item)

                return book_search_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[BookSearchParam]], data)

        book_search_params = _parse_book_search_params(d.pop("bookSearchParams", UNSET))

        indexer_capability_resource = cls(
            id=id,
            limits_max=limits_max,
            limits_default=limits_default,
            categories=categories,
            supports_raw_search=supports_raw_search,
            search_params=search_params,
            tv_search_params=tv_search_params,
            movie_search_params=movie_search_params,
            music_search_params=music_search_params,
            book_search_params=book_search_params,
        )

        return indexer_capability_resource
