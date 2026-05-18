from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.movie_status_type import MovieStatusType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionUpdateResource")


@_attrs_define
class CollectionUpdateResource:
    """
    Attributes:
        collection_ids (Union[None, Unset, list[int]]):
        monitored (Union[None, Unset, bool]):
        monitor_movies (Union[None, Unset, bool]):
        search_on_add (Union[None, Unset, bool]):
        quality_profile_id (Union[None, Unset, int]):
        root_folder_path (Union[None, Unset, str]):
        minimum_availability (Union[Unset, MovieStatusType]):
    """

    collection_ids: Union[None, Unset, list[int]] = UNSET
    monitored: Union[None, Unset, bool] = UNSET
    monitor_movies: Union[None, Unset, bool] = UNSET
    search_on_add: Union[None, Unset, bool] = UNSET
    quality_profile_id: Union[None, Unset, int] = UNSET
    root_folder_path: Union[None, Unset, str] = UNSET
    minimum_availability: Union[Unset, MovieStatusType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        collection_ids: Union[None, Unset, list[int]]
        if isinstance(self.collection_ids, Unset):
            collection_ids = UNSET
        elif isinstance(self.collection_ids, list):
            collection_ids = self.collection_ids

        else:
            collection_ids = self.collection_ids

        monitored: Union[None, Unset, bool]
        if isinstance(self.monitored, Unset):
            monitored = UNSET
        else:
            monitored = self.monitored

        monitor_movies: Union[None, Unset, bool]
        if isinstance(self.monitor_movies, Unset):
            monitor_movies = UNSET
        else:
            monitor_movies = self.monitor_movies

        search_on_add: Union[None, Unset, bool]
        if isinstance(self.search_on_add, Unset):
            search_on_add = UNSET
        else:
            search_on_add = self.search_on_add

        quality_profile_id: Union[None, Unset, int]
        if isinstance(self.quality_profile_id, Unset):
            quality_profile_id = UNSET
        else:
            quality_profile_id = self.quality_profile_id

        root_folder_path: Union[None, Unset, str]
        if isinstance(self.root_folder_path, Unset):
            root_folder_path = UNSET
        else:
            root_folder_path = self.root_folder_path

        minimum_availability: Union[Unset, str] = UNSET
        if not isinstance(self.minimum_availability, Unset):
            minimum_availability = self.minimum_availability.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if collection_ids is not UNSET:
            field_dict["collectionIds"] = collection_ids
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if monitor_movies is not UNSET:
            field_dict["monitorMovies"] = monitor_movies
        if search_on_add is not UNSET:
            field_dict["searchOnAdd"] = search_on_add
        if quality_profile_id is not UNSET:
            field_dict["qualityProfileId"] = quality_profile_id
        if root_folder_path is not UNSET:
            field_dict["rootFolderPath"] = root_folder_path
        if minimum_availability is not UNSET:
            field_dict["minimumAvailability"] = minimum_availability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_collection_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collection_ids_type_0 = cast(list[int], data)

                return collection_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        collection_ids = _parse_collection_ids(d.pop("collectionIds", UNSET))

        def _parse_monitored(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        monitored = _parse_monitored(d.pop("monitored", UNSET))

        def _parse_monitor_movies(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        monitor_movies = _parse_monitor_movies(d.pop("monitorMovies", UNSET))

        def _parse_search_on_add(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        search_on_add = _parse_search_on_add(d.pop("searchOnAdd", UNSET))

        def _parse_quality_profile_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quality_profile_id = _parse_quality_profile_id(d.pop("qualityProfileId", UNSET))

        def _parse_root_folder_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        root_folder_path = _parse_root_folder_path(d.pop("rootFolderPath", UNSET))

        _minimum_availability = d.pop("minimumAvailability", UNSET)
        minimum_availability: Union[Unset, MovieStatusType]
        if isinstance(_minimum_availability, Unset):
            minimum_availability = UNSET
        else:
            minimum_availability = MovieStatusType(_minimum_availability)

        collection_update_resource = cls(
            collection_ids=collection_ids,
            monitored=monitored,
            monitor_movies=monitor_movies,
            search_on_add=search_on_add,
            quality_profile_id=quality_profile_id,
            root_folder_path=root_folder_path,
            minimum_availability=minimum_availability,
        )

        return collection_update_resource
