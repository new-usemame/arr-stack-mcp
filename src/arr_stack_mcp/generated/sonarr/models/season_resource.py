from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_cover import MediaCover
    from ..models.season_statistics_resource import SeasonStatisticsResource


T = TypeVar("T", bound="SeasonResource")


@_attrs_define
class SeasonResource:
    """
    Attributes:
        season_number (Union[Unset, int]):
        monitored (Union[Unset, bool]):
        statistics (Union[Unset, SeasonStatisticsResource]):
        images (Union[None, Unset, list['MediaCover']]):
    """

    season_number: Union[Unset, int] = UNSET
    monitored: Union[Unset, bool] = UNSET
    statistics: Union[Unset, "SeasonStatisticsResource"] = UNSET
    images: Union[None, Unset, list["MediaCover"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_number = self.season_number

        monitored = self.monitored

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if season_number is not UNSET:
            field_dict["seasonNumber"] = season_number
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_cover import MediaCover
        from ..models.season_statistics_resource import SeasonStatisticsResource

        d = dict(src_dict)
        season_number = d.pop("seasonNumber", UNSET)

        monitored = d.pop("monitored", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SeasonStatisticsResource]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SeasonStatisticsResource.from_dict(_statistics)

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

        season_resource = cls(
            season_number=season_number,
            monitored=monitored,
            statistics=statistics,
            images=images,
        )

        return season_resource
