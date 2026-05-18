from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MovieStatisticsResource")


@_attrs_define
class MovieStatisticsResource:
    """
    Attributes:
        movie_file_count (Union[Unset, int]):
        size_on_disk (Union[Unset, int]):
        release_groups (Union[None, Unset, list[str]]):
    """

    movie_file_count: Union[Unset, int] = UNSET
    size_on_disk: Union[Unset, int] = UNSET
    release_groups: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        movie_file_count = self.movie_file_count

        size_on_disk = self.size_on_disk

        release_groups: Union[None, Unset, list[str]]
        if isinstance(self.release_groups, Unset):
            release_groups = UNSET
        elif isinstance(self.release_groups, list):
            release_groups = self.release_groups

        else:
            release_groups = self.release_groups

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if movie_file_count is not UNSET:
            field_dict["movieFileCount"] = movie_file_count
        if size_on_disk is not UNSET:
            field_dict["sizeOnDisk"] = size_on_disk
        if release_groups is not UNSET:
            field_dict["releaseGroups"] = release_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        movie_file_count = d.pop("movieFileCount", UNSET)

        size_on_disk = d.pop("sizeOnDisk", UNSET)

        def _parse_release_groups(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                release_groups_type_0 = cast(list[str], data)

                return release_groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        release_groups = _parse_release_groups(d.pop("releaseGroups", UNSET))

        movie_statistics_resource = cls(
            movie_file_count=movie_file_count,
            size_on_disk=size_on_disk,
            release_groups=release_groups,
        )

        return movie_statistics_resource
