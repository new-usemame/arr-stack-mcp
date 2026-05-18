from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_resource import AlbumResource
    from ..models.artist_resource import ArtistResource


T = TypeVar("T", bound="SearchResource")


@_attrs_define
class SearchResource:
    """
    Attributes:
        id (Union[Unset, int]):
        foreign_id (Union[None, Unset, str]):
        artist (Union[Unset, ArtistResource]):
        album (Union[Unset, AlbumResource]):
    """

    id: Union[Unset, int] = UNSET
    foreign_id: Union[None, Unset, str] = UNSET
    artist: Union[Unset, "ArtistResource"] = UNSET
    album: Union[Unset, "AlbumResource"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        foreign_id: Union[None, Unset, str]
        if isinstance(self.foreign_id, Unset):
            foreign_id = UNSET
        else:
            foreign_id = self.foreign_id

        artist: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.artist, Unset):
            artist = self.artist.to_dict()

        album: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.album, Unset):
            album = self.album.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if foreign_id is not UNSET:
            field_dict["foreignId"] = foreign_id
        if artist is not UNSET:
            field_dict["artist"] = artist
        if album is not UNSET:
            field_dict["album"] = album

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_resource import AlbumResource
        from ..models.artist_resource import ArtistResource

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_foreign_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        foreign_id = _parse_foreign_id(d.pop("foreignId", UNSET))

        _artist = d.pop("artist", UNSET)
        artist: Union[Unset, ArtistResource]
        if isinstance(_artist, Unset):
            artist = UNSET
        else:
            artist = ArtistResource.from_dict(_artist)

        _album = d.pop("album", UNSET)
        album: Union[Unset, AlbumResource]
        if isinstance(_album, Unset):
            album = UNSET
        else:
            album = AlbumResource.from_dict(_album)

        search_resource = cls(
            id=id,
            foreign_id=foreign_id,
            artist=artist,
            album=album,
        )

        return search_resource
