from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playlist_user_permissions import PlaylistUserPermissions


T = TypeVar("T", bound="UpdatePlaylistDto")


@_attrs_define
class UpdatePlaylistDto:
    """Update existing playlist dto. Fields set to `null` will not be updated and keep their current values.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name of the new playlist.
        ids (Union[None, Unset, list[UUID]]): Gets or sets item ids of the playlist.
        users (Union[None, Unset, list['PlaylistUserPermissions']]): Gets or sets the playlist users.
        is_public (Union[None, Unset, bool]): Gets or sets a value indicating whether the playlist is public.
    """

    name: Union[None, Unset, str] = UNSET
    ids: Union[None, Unset, list[UUID]] = UNSET
    users: Union[None, Unset, list["PlaylistUserPermissions"]] = UNSET
    is_public: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        ids: Union[None, Unset, list[str]]
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = []
            for ids_type_0_item_data in self.ids:
                ids_type_0_item = str(ids_type_0_item_data)
                ids.append(ids_type_0_item)

        else:
            ids = self.ids

        users: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)

        else:
            users = self.users

        is_public: Union[None, Unset, bool]
        if isinstance(self.is_public, Unset):
            is_public = UNSET
        else:
            is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if users is not UNSET:
            field_dict["Users"] = users
        if is_public is not UNSET:
            field_dict["IsPublic"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playlist_user_permissions import PlaylistUserPermissions

        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = []
                _ids_type_0 = data
                for ids_type_0_item_data in _ids_type_0:
                    ids_type_0_item = UUID(ids_type_0_item_data)

                    ids_type_0.append(ids_type_0_item)

                return ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        ids = _parse_ids(d.pop("Ids", UNSET))

        def _parse_users(
            data: object,
        ) -> Union[None, Unset, list["PlaylistUserPermissions"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in _users_type_0:
                    users_type_0_item = PlaylistUserPermissions.from_dict(
                        users_type_0_item_data
                    )

                    users_type_0.append(users_type_0_item)

                return users_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["PlaylistUserPermissions"]], data)

        users = _parse_users(d.pop("Users", UNSET))

        def _parse_is_public(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_public = _parse_is_public(d.pop("IsPublic", UNSET))

        update_playlist_dto = cls(
            name=name,
            ids=ids,
            users=users,
            is_public=is_public,
        )

        return update_playlist_dto
