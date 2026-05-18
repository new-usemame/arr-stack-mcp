from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artist_title_info import ArtistTitleInfo
    from ..models.iso_country import IsoCountry
    from ..models.media_info_model import MediaInfoModel
    from ..models.quality_model import QualityModel


T = TypeVar("T", bound="ParsedTrackInfo")


@_attrs_define
class ParsedTrackInfo:
    """
    Attributes:
        title (Union[None, Unset, str]):
        clean_title (Union[None, Unset, str]):
        artist_title (Union[None, Unset, str]):
        album_title (Union[None, Unset, str]):
        artist_title_info (Union[Unset, ArtistTitleInfo]):
        artist_mb_id (Union[None, Unset, str]):
        album_mb_id (Union[None, Unset, str]):
        release_mb_id (Union[None, Unset, str]):
        recording_mb_id (Union[None, Unset, str]):
        track_mb_id (Union[None, Unset, str]):
        disc_number (Union[Unset, int]):
        disc_count (Union[Unset, int]):
        country (Union[Unset, IsoCountry]):
        year (Union[Unset, int]):
        label (Union[None, Unset, str]):
        catalog_number (Union[None, Unset, str]):
        disambiguation (Union[None, Unset, str]):
        duration (Union[Unset, str]):
        quality (Union[Unset, QualityModel]):
        media_info (Union[Unset, MediaInfoModel]):
        track_numbers (Union[None, Unset, list[int]]):
        release_group (Union[None, Unset, str]):
        release_hash (Union[None, Unset, str]):
    """

    title: Union[None, Unset, str] = UNSET
    clean_title: Union[None, Unset, str] = UNSET
    artist_title: Union[None, Unset, str] = UNSET
    album_title: Union[None, Unset, str] = UNSET
    artist_title_info: Union[Unset, "ArtistTitleInfo"] = UNSET
    artist_mb_id: Union[None, Unset, str] = UNSET
    album_mb_id: Union[None, Unset, str] = UNSET
    release_mb_id: Union[None, Unset, str] = UNSET
    recording_mb_id: Union[None, Unset, str] = UNSET
    track_mb_id: Union[None, Unset, str] = UNSET
    disc_number: Union[Unset, int] = UNSET
    disc_count: Union[Unset, int] = UNSET
    country: Union[Unset, "IsoCountry"] = UNSET
    year: Union[Unset, int] = UNSET
    label: Union[None, Unset, str] = UNSET
    catalog_number: Union[None, Unset, str] = UNSET
    disambiguation: Union[None, Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    media_info: Union[Unset, "MediaInfoModel"] = UNSET
    track_numbers: Union[None, Unset, list[int]] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    release_hash: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        clean_title: Union[None, Unset, str]
        if isinstance(self.clean_title, Unset):
            clean_title = UNSET
        else:
            clean_title = self.clean_title

        artist_title: Union[None, Unset, str]
        if isinstance(self.artist_title, Unset):
            artist_title = UNSET
        else:
            artist_title = self.artist_title

        album_title: Union[None, Unset, str]
        if isinstance(self.album_title, Unset):
            album_title = UNSET
        else:
            album_title = self.album_title

        artist_title_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist_title_info, Unset):
            artist_title_info = self.artist_title_info.to_dict()

        artist_mb_id: Union[None, Unset, str]
        if isinstance(self.artist_mb_id, Unset):
            artist_mb_id = UNSET
        else:
            artist_mb_id = self.artist_mb_id

        album_mb_id: Union[None, Unset, str]
        if isinstance(self.album_mb_id, Unset):
            album_mb_id = UNSET
        else:
            album_mb_id = self.album_mb_id

        release_mb_id: Union[None, Unset, str]
        if isinstance(self.release_mb_id, Unset):
            release_mb_id = UNSET
        else:
            release_mb_id = self.release_mb_id

        recording_mb_id: Union[None, Unset, str]
        if isinstance(self.recording_mb_id, Unset):
            recording_mb_id = UNSET
        else:
            recording_mb_id = self.recording_mb_id

        track_mb_id: Union[None, Unset, str]
        if isinstance(self.track_mb_id, Unset):
            track_mb_id = UNSET
        else:
            track_mb_id = self.track_mb_id

        disc_number = self.disc_number

        disc_count = self.disc_count

        country: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        year = self.year

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        catalog_number: Union[None, Unset, str]
        if isinstance(self.catalog_number, Unset):
            catalog_number = UNSET
        else:
            catalog_number = self.catalog_number

        disambiguation: Union[None, Unset, str]
        if isinstance(self.disambiguation, Unset):
            disambiguation = UNSET
        else:
            disambiguation = self.disambiguation

        duration = self.duration

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        media_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.media_info, Unset):
            media_info = self.media_info.to_dict()

        track_numbers: Union[None, Unset, list[int]]
        if isinstance(self.track_numbers, Unset):
            track_numbers = UNSET
        elif isinstance(self.track_numbers, list):
            track_numbers = self.track_numbers

        else:
            track_numbers = self.track_numbers

        release_group: Union[None, Unset, str]
        if isinstance(self.release_group, Unset):
            release_group = UNSET
        else:
            release_group = self.release_group

        release_hash: Union[None, Unset, str]
        if isinstance(self.release_hash, Unset):
            release_hash = UNSET
        else:
            release_hash = self.release_hash

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if clean_title is not UNSET:
            field_dict["cleanTitle"] = clean_title
        if artist_title is not UNSET:
            field_dict["artistTitle"] = artist_title
        if album_title is not UNSET:
            field_dict["albumTitle"] = album_title
        if artist_title_info is not UNSET:
            field_dict["artistTitleInfo"] = artist_title_info
        if artist_mb_id is not UNSET:
            field_dict["artistMBId"] = artist_mb_id
        if album_mb_id is not UNSET:
            field_dict["albumMBId"] = album_mb_id
        if release_mb_id is not UNSET:
            field_dict["releaseMBId"] = release_mb_id
        if recording_mb_id is not UNSET:
            field_dict["recordingMBId"] = recording_mb_id
        if track_mb_id is not UNSET:
            field_dict["trackMBId"] = track_mb_id
        if disc_number is not UNSET:
            field_dict["discNumber"] = disc_number
        if disc_count is not UNSET:
            field_dict["discCount"] = disc_count
        if country is not UNSET:
            field_dict["country"] = country
        if year is not UNSET:
            field_dict["year"] = year
        if label is not UNSET:
            field_dict["label"] = label
        if catalog_number is not UNSET:
            field_dict["catalogNumber"] = catalog_number
        if disambiguation is not UNSET:
            field_dict["disambiguation"] = disambiguation
        if duration is not UNSET:
            field_dict["duration"] = duration
        if quality is not UNSET:
            field_dict["quality"] = quality
        if media_info is not UNSET:
            field_dict["mediaInfo"] = media_info
        if track_numbers is not UNSET:
            field_dict["trackNumbers"] = track_numbers
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if release_hash is not UNSET:
            field_dict["releaseHash"] = release_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artist_title_info import ArtistTitleInfo
        from ..models.iso_country import IsoCountry
        from ..models.media_info_model import MediaInfoModel
        from ..models.quality_model import QualityModel

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_clean_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        clean_title = _parse_clean_title(d.pop("cleanTitle", UNSET))

        def _parse_artist_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist_title = _parse_artist_title(d.pop("artistTitle", UNSET))

        def _parse_album_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_title = _parse_album_title(d.pop("albumTitle", UNSET))

        _artist_title_info = d.pop("artistTitleInfo", UNSET)
        artist_title_info: Union[Unset, ArtistTitleInfo]
        if isinstance(_artist_title_info, Unset):
            artist_title_info = UNSET
        else:
            artist_title_info = ArtistTitleInfo.from_dict(_artist_title_info)

        def _parse_artist_mb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist_mb_id = _parse_artist_mb_id(d.pop("artistMBId", UNSET))

        def _parse_album_mb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_mb_id = _parse_album_mb_id(d.pop("albumMBId", UNSET))

        def _parse_release_mb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_mb_id = _parse_release_mb_id(d.pop("releaseMBId", UNSET))

        def _parse_recording_mb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recording_mb_id = _parse_recording_mb_id(d.pop("recordingMBId", UNSET))

        def _parse_track_mb_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        track_mb_id = _parse_track_mb_id(d.pop("trackMBId", UNSET))

        disc_number = d.pop("discNumber", UNSET)

        disc_count = d.pop("discCount", UNSET)

        _country = d.pop("country", UNSET)
        country: Union[Unset, IsoCountry]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = IsoCountry.from_dict(_country)

        year = d.pop("year", UNSET)

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_catalog_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        catalog_number = _parse_catalog_number(d.pop("catalogNumber", UNSET))

        def _parse_disambiguation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disambiguation = _parse_disambiguation(d.pop("disambiguation", UNSET))

        duration = d.pop("duration", UNSET)

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        _media_info = d.pop("mediaInfo", UNSET)
        media_info: Union[Unset, MediaInfoModel]
        if isinstance(_media_info, Unset):
            media_info = UNSET
        else:
            media_info = MediaInfoModel.from_dict(_media_info)

        def _parse_track_numbers(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                track_numbers_type_0 = cast(list[int], data)

                return track_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        track_numbers = _parse_track_numbers(d.pop("trackNumbers", UNSET))

        def _parse_release_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_group = _parse_release_group(d.pop("releaseGroup", UNSET))

        def _parse_release_hash(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_hash = _parse_release_hash(d.pop("releaseHash", UNSET))

        parsed_track_info = cls(
            title=title,
            clean_title=clean_title,
            artist_title=artist_title,
            album_title=album_title,
            artist_title_info=artist_title_info,
            artist_mb_id=artist_mb_id,
            album_mb_id=album_mb_id,
            release_mb_id=release_mb_id,
            recording_mb_id=recording_mb_id,
            track_mb_id=track_mb_id,
            disc_number=disc_number,
            disc_count=disc_count,
            country=country,
            year=year,
            label=label,
            catalog_number=catalog_number,
            disambiguation=disambiguation,
            duration=duration,
            quality=quality,
            media_info=media_info,
            track_numbers=track_numbers,
            release_group=release_group,
            release_hash=release_hash,
        )

        return parsed_track_info
