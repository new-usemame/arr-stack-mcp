from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality_model import QualityModel


T = TypeVar("T", bound="TrackFileListResource")


@_attrs_define
class TrackFileListResource:
    """
    Attributes:
        track_file_ids (Union[None, Unset, list[int]]):
        quality (Union[Unset, QualityModel]):
        scene_name (Union[None, Unset, str]):
        release_group (Union[None, Unset, str]):
    """

    track_file_ids: Union[None, Unset, list[int]] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    scene_name: Union[None, Unset, str] = UNSET
    release_group: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        track_file_ids: Union[None, Unset, list[int]]
        if isinstance(self.track_file_ids, Unset):
            track_file_ids = UNSET
        elif isinstance(self.track_file_ids, list):
            track_file_ids = self.track_file_ids

        else:
            track_file_ids = self.track_file_ids

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        scene_name: Union[None, Unset, str]
        if isinstance(self.scene_name, Unset):
            scene_name = UNSET
        else:
            scene_name = self.scene_name

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if track_file_ids is not UNSET:
            field_dict["trackFileIds"] = track_file_ids
        if quality is not UNSET:
            field_dict["quality"] = quality
        if scene_name is not UNSET:
            field_dict["sceneName"] = scene_name
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quality_model import QualityModel

        d = dict(src_dict)

        def _parse_track_file_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                track_file_ids_type_0 = cast(list[int], data)

                return track_file_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        track_file_ids = _parse_track_file_ids(d.pop("trackFileIds", UNSET))

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        def _parse_scene_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scene_name = _parse_scene_name(d.pop("sceneName", UNSET))

        def _parse_release_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_group = _parse_release_group(d.pop("releaseGroup", UNSET))

        track_file_list_resource = cls(
            track_file_ids=track_file_ids,
            quality=quality,
            scene_name=scene_name,
            release_group=release_group,
        )

        return track_file_list_resource
