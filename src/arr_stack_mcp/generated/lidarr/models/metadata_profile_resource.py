from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_primary_album_type_item_resource import (
        ProfilePrimaryAlbumTypeItemResource,
    )
    from ..models.profile_release_status_item_resource import (
        ProfileReleaseStatusItemResource,
    )
    from ..models.profile_secondary_album_type_item_resource import (
        ProfileSecondaryAlbumTypeItemResource,
    )


T = TypeVar("T", bound="MetadataProfileResource")


@_attrs_define
class MetadataProfileResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        primary_album_types (Union[None, Unset, list['ProfilePrimaryAlbumTypeItemResource']]):
        secondary_album_types (Union[None, Unset, list['ProfileSecondaryAlbumTypeItemResource']]):
        release_statuses (Union[None, Unset, list['ProfileReleaseStatusItemResource']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    primary_album_types: Union[
        None, Unset, list["ProfilePrimaryAlbumTypeItemResource"]
    ] = UNSET
    secondary_album_types: Union[
        None, Unset, list["ProfileSecondaryAlbumTypeItemResource"]
    ] = UNSET
    release_statuses: Union[None, Unset, list["ProfileReleaseStatusItemResource"]] = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        primary_album_types: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.primary_album_types, Unset):
            primary_album_types = UNSET
        elif isinstance(self.primary_album_types, list):
            primary_album_types = []
            for primary_album_types_type_0_item_data in self.primary_album_types:
                primary_album_types_type_0_item = (
                    primary_album_types_type_0_item_data.to_dict()
                )
                primary_album_types.append(primary_album_types_type_0_item)

        else:
            primary_album_types = self.primary_album_types

        secondary_album_types: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.secondary_album_types, Unset):
            secondary_album_types = UNSET
        elif isinstance(self.secondary_album_types, list):
            secondary_album_types = []
            for secondary_album_types_type_0_item_data in self.secondary_album_types:
                secondary_album_types_type_0_item = (
                    secondary_album_types_type_0_item_data.to_dict()
                )
                secondary_album_types.append(secondary_album_types_type_0_item)

        else:
            secondary_album_types = self.secondary_album_types

        release_statuses: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.release_statuses, Unset):
            release_statuses = UNSET
        elif isinstance(self.release_statuses, list):
            release_statuses = []
            for release_statuses_type_0_item_data in self.release_statuses:
                release_statuses_type_0_item = (
                    release_statuses_type_0_item_data.to_dict()
                )
                release_statuses.append(release_statuses_type_0_item)

        else:
            release_statuses = self.release_statuses

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if primary_album_types is not UNSET:
            field_dict["primaryAlbumTypes"] = primary_album_types
        if secondary_album_types is not UNSET:
            field_dict["secondaryAlbumTypes"] = secondary_album_types
        if release_statuses is not UNSET:
            field_dict["releaseStatuses"] = release_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.profile_primary_album_type_item_resource import (
            ProfilePrimaryAlbumTypeItemResource,
        )
        from ..models.profile_release_status_item_resource import (
            ProfileReleaseStatusItemResource,
        )
        from ..models.profile_secondary_album_type_item_resource import (
            ProfileSecondaryAlbumTypeItemResource,
        )

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_primary_album_types(
            data: object,
        ) -> Union[None, Unset, list["ProfilePrimaryAlbumTypeItemResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primary_album_types_type_0 = []
                _primary_album_types_type_0 = data
                for primary_album_types_type_0_item_data in _primary_album_types_type_0:
                    primary_album_types_type_0_item = (
                        ProfilePrimaryAlbumTypeItemResource.from_dict(
                            primary_album_types_type_0_item_data
                        )
                    )

                    primary_album_types_type_0.append(primary_album_types_type_0_item)

                return primary_album_types_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["ProfilePrimaryAlbumTypeItemResource"]], data
            )

        primary_album_types = _parse_primary_album_types(
            d.pop("primaryAlbumTypes", UNSET)
        )

        def _parse_secondary_album_types(
            data: object,
        ) -> Union[None, Unset, list["ProfileSecondaryAlbumTypeItemResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                secondary_album_types_type_0 = []
                _secondary_album_types_type_0 = data
                for (
                    secondary_album_types_type_0_item_data
                ) in _secondary_album_types_type_0:
                    secondary_album_types_type_0_item = (
                        ProfileSecondaryAlbumTypeItemResource.from_dict(
                            secondary_album_types_type_0_item_data
                        )
                    )

                    secondary_album_types_type_0.append(
                        secondary_album_types_type_0_item
                    )

                return secondary_album_types_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["ProfileSecondaryAlbumTypeItemResource"]], data
            )

        secondary_album_types = _parse_secondary_album_types(
            d.pop("secondaryAlbumTypes", UNSET)
        )

        def _parse_release_statuses(
            data: object,
        ) -> Union[None, Unset, list["ProfileReleaseStatusItemResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                release_statuses_type_0 = []
                _release_statuses_type_0 = data
                for release_statuses_type_0_item_data in _release_statuses_type_0:
                    release_statuses_type_0_item = (
                        ProfileReleaseStatusItemResource.from_dict(
                            release_statuses_type_0_item_data
                        )
                    )

                    release_statuses_type_0.append(release_statuses_type_0_item)

                return release_statuses_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["ProfileReleaseStatusItemResource"]], data
            )

        release_statuses = _parse_release_statuses(d.pop("releaseStatuses", UNSET))

        metadata_profile_resource = cls(
            id=id,
            name=name,
            primary_album_types=primary_album_types,
            secondary_album_types=secondary_album_types,
            release_statuses=release_statuses,
        )

        return metadata_profile_resource
