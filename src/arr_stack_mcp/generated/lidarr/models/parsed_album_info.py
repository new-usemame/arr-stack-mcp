from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artist_title_info import ArtistTitleInfo
    from ..models.quality_model import QualityModel


T = TypeVar("T", bound="ParsedAlbumInfo")


@_attrs_define
class ParsedAlbumInfo:
    """
    Attributes:
        release_title (Union[None, Unset, str]):
        album_title (Union[None, Unset, str]):
        artist_name (Union[None, Unset, str]):
        album_type (Union[None, Unset, str]):
        artist_title_info (Union[Unset, ArtistTitleInfo]):
        quality (Union[Unset, QualityModel]):
        release_date (Union[None, Unset, str]):
        discography (Union[Unset, bool]):
        discography_start (Union[Unset, int]):
        discography_end (Union[Unset, int]):
        release_group (Union[None, Unset, str]):
        release_hash (Union[None, Unset, str]):
        release_version (Union[None, Unset, str]):
    """

    release_title: Union[None, Unset, str] = UNSET
    album_title: Union[None, Unset, str] = UNSET
    artist_name: Union[None, Unset, str] = UNSET
    album_type: Union[None, Unset, str] = UNSET
    artist_title_info: Union[Unset, "ArtistTitleInfo"] = UNSET
    quality: Union[Unset, "QualityModel"] = UNSET
    release_date: Union[None, Unset, str] = UNSET
    discography: Union[Unset, bool] = UNSET
    discography_start: Union[Unset, int] = UNSET
    discography_end: Union[Unset, int] = UNSET
    release_group: Union[None, Unset, str] = UNSET
    release_hash: Union[None, Unset, str] = UNSET
    release_version: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        release_title: Union[None, Unset, str]
        if isinstance(self.release_title, Unset):
            release_title = UNSET
        else:
            release_title = self.release_title

        album_title: Union[None, Unset, str]
        if isinstance(self.album_title, Unset):
            album_title = UNSET
        else:
            album_title = self.album_title

        artist_name: Union[None, Unset, str]
        if isinstance(self.artist_name, Unset):
            artist_name = UNSET
        else:
            artist_name = self.artist_name

        album_type: Union[None, Unset, str]
        if isinstance(self.album_type, Unset):
            album_type = UNSET
        else:
            album_type = self.album_type

        artist_title_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist_title_info, Unset):
            artist_title_info = self.artist_title_info.to_dict()

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        release_date: Union[None, Unset, str]
        if isinstance(self.release_date, Unset):
            release_date = UNSET
        else:
            release_date = self.release_date

        discography = self.discography

        discography_start = self.discography_start

        discography_end = self.discography_end

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

        release_version: Union[None, Unset, str]
        if isinstance(self.release_version, Unset):
            release_version = UNSET
        else:
            release_version = self.release_version

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if release_title is not UNSET:
            field_dict["releaseTitle"] = release_title
        if album_title is not UNSET:
            field_dict["albumTitle"] = album_title
        if artist_name is not UNSET:
            field_dict["artistName"] = artist_name
        if album_type is not UNSET:
            field_dict["albumType"] = album_type
        if artist_title_info is not UNSET:
            field_dict["artistTitleInfo"] = artist_title_info
        if quality is not UNSET:
            field_dict["quality"] = quality
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if discography is not UNSET:
            field_dict["discography"] = discography
        if discography_start is not UNSET:
            field_dict["discographyStart"] = discography_start
        if discography_end is not UNSET:
            field_dict["discographyEnd"] = discography_end
        if release_group is not UNSET:
            field_dict["releaseGroup"] = release_group
        if release_hash is not UNSET:
            field_dict["releaseHash"] = release_hash
        if release_version is not UNSET:
            field_dict["releaseVersion"] = release_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artist_title_info import ArtistTitleInfo
        from ..models.quality_model import QualityModel

        d = dict(src_dict)

        def _parse_release_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_title = _parse_release_title(d.pop("releaseTitle", UNSET))

        def _parse_album_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_title = _parse_album_title(d.pop("albumTitle", UNSET))

        def _parse_artist_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        artist_name = _parse_artist_name(d.pop("artistName", UNSET))

        def _parse_album_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        album_type = _parse_album_type(d.pop("albumType", UNSET))

        _artist_title_info = d.pop("artistTitleInfo", UNSET)
        artist_title_info: Union[Unset, ArtistTitleInfo]
        if isinstance(_artist_title_info, Unset):
            artist_title_info = UNSET
        else:
            artist_title_info = ArtistTitleInfo.from_dict(_artist_title_info)

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, QualityModel]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = QualityModel.from_dict(_quality)

        def _parse_release_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_date = _parse_release_date(d.pop("releaseDate", UNSET))

        discography = d.pop("discography", UNSET)

        discography_start = d.pop("discographyStart", UNSET)

        discography_end = d.pop("discographyEnd", UNSET)

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

        def _parse_release_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        release_version = _parse_release_version(d.pop("releaseVersion", UNSET))

        parsed_album_info = cls(
            release_title=release_title,
            album_title=album_title,
            artist_name=artist_name,
            album_type=album_type,
            artist_title_info=artist_title_info,
            quality=quality,
            release_date=release_date,
            discography=discography,
            discography_start=discography_start,
            discography_end=discography_end,
            release_group=release_group,
            release_hash=release_hash,
            release_version=release_version,
        )

        return parsed_album_info
