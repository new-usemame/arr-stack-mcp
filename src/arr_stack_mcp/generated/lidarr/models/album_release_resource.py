from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.medium_resource import MediumResource


T = TypeVar("T", bound="AlbumReleaseResource")


@_attrs_define
class AlbumReleaseResource:
    """
    Attributes:
        id (Union[Unset, int]):
        album_id (Union[Unset, int]):
        foreign_release_id (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        status (Union[None, Unset, str]):
        duration (Union[Unset, int]):
        track_count (Union[Unset, int]):
        media (Union[None, Unset, list['MediumResource']]):
        medium_count (Union[Unset, int]):
        disambiguation (Union[None, Unset, str]):
        country (Union[None, Unset, list[str]]):
        label (Union[None, Unset, list[str]]):
        format_ (Union[None, Unset, str]):
        monitored (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    album_id: Union[Unset, int] = UNSET
    foreign_release_id: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    track_count: Union[Unset, int] = UNSET
    media: Union[None, Unset, list["MediumResource"]] = UNSET
    medium_count: Union[Unset, int] = UNSET
    disambiguation: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, list[str]] = UNSET
    label: Union[None, Unset, list[str]] = UNSET
    format_: Union[None, Unset, str] = UNSET
    monitored: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        album_id = self.album_id

        foreign_release_id: Union[None, Unset, str]
        if isinstance(self.foreign_release_id, Unset):
            foreign_release_id = UNSET
        else:
            foreign_release_id = self.foreign_release_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        duration = self.duration

        track_count = self.track_count

        media: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.media, Unset):
            media = UNSET
        elif isinstance(self.media, list):
            media = []
            for media_type_0_item_data in self.media:
                media_type_0_item = media_type_0_item_data.to_dict()
                media.append(media_type_0_item)

        else:
            media = self.media

        medium_count = self.medium_count

        disambiguation: Union[None, Unset, str]
        if isinstance(self.disambiguation, Unset):
            disambiguation = UNSET
        else:
            disambiguation = self.disambiguation

        country: Union[None, Unset, list[str]]
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, list):
            country = self.country

        else:
            country = self.country

        label: Union[None, Unset, list[str]]
        if isinstance(self.label, Unset):
            label = UNSET
        elif isinstance(self.label, list):
            label = self.label

        else:
            label = self.label

        format_: Union[None, Unset, str]
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        monitored = self.monitored

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if album_id is not UNSET:
            field_dict["albumId"] = album_id
        if foreign_release_id is not UNSET:
            field_dict["foreignReleaseId"] = foreign_release_id
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if duration is not UNSET:
            field_dict["duration"] = duration
        if track_count is not UNSET:
            field_dict["trackCount"] = track_count
        if media is not UNSET:
            field_dict["media"] = media
        if medium_count is not UNSET:
            field_dict["mediumCount"] = medium_count
        if disambiguation is not UNSET:
            field_dict["disambiguation"] = disambiguation
        if country is not UNSET:
            field_dict["country"] = country
        if label is not UNSET:
            field_dict["label"] = label
        if format_ is not UNSET:
            field_dict["format"] = format_
        if monitored is not UNSET:
            field_dict["monitored"] = monitored

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.medium_resource import MediumResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        album_id = d.pop("albumId", UNSET)

        def _parse_foreign_release_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_release_id = _parse_foreign_release_id(d.pop("foreignReleaseId", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        duration = d.pop("duration", UNSET)

        track_count = d.pop("trackCount", UNSET)

        def _parse_media(data: object) -> Union[None, Unset, list["MediumResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                media_type_0 = []
                _media_type_0 = data
                for media_type_0_item_data in _media_type_0:
                    media_type_0_item = MediumResource.from_dict(media_type_0_item_data)

                    media_type_0.append(media_type_0_item)

                return media_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MediumResource"]], data)

        media = _parse_media(d.pop("media", UNSET))

        medium_count = d.pop("mediumCount", UNSET)

        def _parse_disambiguation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disambiguation = _parse_disambiguation(d.pop("disambiguation", UNSET))

        def _parse_country(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                country_type_0 = cast(list[str], data)

                return country_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_label(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                label_type_0 = cast(list[str], data)

                return label_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_format_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        format_ = _parse_format_(d.pop("format", UNSET))

        monitored = d.pop("monitored", UNSET)

        album_release_resource = cls(
            id=id,
            album_id=album_id,
            foreign_release_id=foreign_release_id,
            title=title,
            status=status,
            duration=duration,
            track_count=track_count,
            media=media,
            medium_count=medium_count,
            disambiguation=disambiguation,
            country=country,
            label=label,
            format_=format_,
            monitored=monitored,
        )

        return album_release_resource
