from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.album_resource import AlbumResource


T = TypeVar("T", bound="AlbumStudioArtistResource")


@_attrs_define
class AlbumStudioArtistResource:
    """
    Attributes:
        id (Union[Unset, int]):
        monitored (Union[None, Unset, bool]):
        albums (Union[None, Unset, list['AlbumResource']]):
    """

    id: Union[Unset, int] = UNSET
    monitored: Union[None, Unset, bool] = UNSET
    albums: Union[None, Unset, list["AlbumResource"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        monitored: Union[None, Unset, bool]
        if isinstance(self.monitored, Unset):
            monitored = UNSET
        else:
            monitored = self.monitored

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

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if monitored is not UNSET:
            field_dict["monitored"] = monitored
        if albums is not UNSET:
            field_dict["albums"] = albums

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.album_resource import AlbumResource

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_monitored(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        monitored = _parse_monitored(d.pop("monitored", UNSET))

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

        album_studio_artist_resource = cls(
            id=id,
            monitored=monitored,
            albums=albums,
        )

        return album_studio_artist_resource
