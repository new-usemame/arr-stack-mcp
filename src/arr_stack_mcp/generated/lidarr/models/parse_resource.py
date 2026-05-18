from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_resource import AlbumResource
    from ..models.artist_resource import ArtistResource
    from ..models.custom_format_resource import CustomFormatResource
    from ..models.parsed_album_info import ParsedAlbumInfo


T = TypeVar("T", bound="ParseResource")


@_attrs_define
class ParseResource:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[None, Unset, str]):
        parsed_album_info (Union[Unset, ParsedAlbumInfo]):
        artist (Union[Unset, ArtistResource]):
        albums (Union[None, Unset, list['AlbumResource']]):
        custom_formats (Union[None, Unset, list['CustomFormatResource']]):
        custom_format_score (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    parsed_album_info: Union[Unset, "ParsedAlbumInfo"] = UNSET
    artist: Union[Unset, "ArtistResource"] = UNSET
    albums: Union[None, Unset, list["AlbumResource"]] = UNSET
    custom_formats: Union[None, Unset, list["CustomFormatResource"]] = UNSET
    custom_format_score: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        parsed_album_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parsed_album_info, Unset):
            parsed_album_info = self.parsed_album_info.to_dict()

        artist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist.to_dict()

        albums: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.albums, Unset):
            albums = UNSET
        elif isinstance(self.albums, list):
            albums = []
            for albums_type_0_item_data in self.albums:
                albums_type_0_item = albums_type_0_item_data.to_dict()
                albums.append(albums_type_0_item)

        else:
            albums = self.albums

        custom_formats: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.custom_formats, Unset):
            custom_formats = UNSET
        elif isinstance(self.custom_formats, list):
            custom_formats = []
            for custom_formats_type_0_item_data in self.custom_formats:
                custom_formats_type_0_item = custom_formats_type_0_item_data.to_dict()
                custom_formats.append(custom_formats_type_0_item)

        else:
            custom_formats = self.custom_formats

        custom_format_score = self.custom_format_score

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if parsed_album_info is not UNSET:
            field_dict["parsedAlbumInfo"] = parsed_album_info
        if artist is not UNSET:
            field_dict["artist"] = artist
        if albums is not UNSET:
            field_dict["albums"] = albums
        if custom_formats is not UNSET:
            field_dict["customFormats"] = custom_formats
        if custom_format_score is not UNSET:
            field_dict["customFormatScore"] = custom_format_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_resource import AlbumResource
        from ..models.artist_resource import ArtistResource
        from ..models.custom_format_resource import CustomFormatResource
        from ..models.parsed_album_info import ParsedAlbumInfo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        _parsed_album_info = d.pop("parsedAlbumInfo", UNSET)
        parsed_album_info: Union[Unset, ParsedAlbumInfo]
        if isinstance(_parsed_album_info, Unset):
            parsed_album_info = UNSET
        else:
            parsed_album_info = ParsedAlbumInfo.from_dict(_parsed_album_info)

        _artist = d.pop("artist", UNSET)
        artist: Union[Unset, ArtistResource]
        if isinstance(_artist, Unset):
            artist = UNSET
        else:
            artist = ArtistResource.from_dict(_artist)

        def _parse_albums(data: object) -> Union[None, Unset, list["AlbumResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                albums_type_0 = []
                _albums_type_0 = data
                for albums_type_0_item_data in _albums_type_0:
                    albums_type_0_item = AlbumResource.from_dict(
                        albums_type_0_item_data
                    )

                    albums_type_0.append(albums_type_0_item)

                return albums_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AlbumResource"]], data)

        albums = _parse_albums(d.pop("albums", UNSET))

        def _parse_custom_formats(
            data: object,
        ) -> Union[None, Unset, list["CustomFormatResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_formats_type_0 = []
                _custom_formats_type_0 = data
                for custom_formats_type_0_item_data in _custom_formats_type_0:
                    custom_formats_type_0_item = CustomFormatResource.from_dict(
                        custom_formats_type_0_item_data
                    )

                    custom_formats_type_0.append(custom_formats_type_0_item)

                return custom_formats_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["CustomFormatResource"]], data)

        custom_formats = _parse_custom_formats(d.pop("customFormats", UNSET))

        custom_format_score = d.pop("customFormatScore", UNSET)

        parse_resource = cls(
            id=id,
            title=title,
            parsed_album_info=parsed_album_info,
            artist=artist,
            albums=albums,
            custom_formats=custom_formats,
            custom_format_score=custom_format_score,
        )

        return parse_resource
