import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_capabilities_dto import ClientCapabilitiesDto


T = TypeVar("T", bound="DeviceInfoDto")


@_attrs_define
class DeviceInfoDto:
    """A DTO representing device information.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        custom_name (Union[None, Unset, str]): Gets or sets the custom name.
        access_token (Union[None, Unset, str]): Gets or sets the access token.
        id (Union[None, Unset, str]): Gets or sets the identifier.
        last_user_name (Union[None, Unset, str]): Gets or sets the last name of the user.
        app_name (Union[None, Unset, str]): Gets or sets the name of the application.
        app_version (Union[None, Unset, str]): Gets or sets the application version.
        last_user_id (Union[None, UUID, Unset]): Gets or sets the last user identifier.
        date_last_activity (Union[None, Unset, datetime.datetime]): Gets or sets the date last modified.
        capabilities (Union[Unset, ClientCapabilitiesDto]): Client capabilities dto.
        icon_url (Union[None, Unset, str]): Gets or sets the icon URL.
    """

    name: Union[None, Unset, str] = UNSET
    custom_name: Union[None, Unset, str] = UNSET
    access_token: Union[None, Unset, str] = UNSET
    id: Union[None, Unset, str] = UNSET
    last_user_name: Union[None, Unset, str] = UNSET
    app_name: Union[None, Unset, str] = UNSET
    app_version: Union[None, Unset, str] = UNSET
    last_user_id: Union[None, UUID, Unset] = UNSET
    date_last_activity: Union[None, Unset, datetime.datetime] = UNSET
    capabilities: Union[Unset, "ClientCapabilitiesDto"] = UNSET
    icon_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        custom_name: Union[None, Unset, str]
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        access_token: Union[None, Unset, str]
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        last_user_name: Union[None, Unset, str]
        if isinstance(self.last_user_name, Unset):
            last_user_name = UNSET
        else:
            last_user_name = self.last_user_name

        app_name: Union[None, Unset, str]
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        app_version: Union[None, Unset, str]
        if isinstance(self.app_version, Unset):
            app_version = UNSET
        else:
            app_version = self.app_version

        last_user_id: Union[None, Unset, str]
        if isinstance(self.last_user_id, Unset):
            last_user_id = UNSET
        elif isinstance(self.last_user_id, UUID):
            last_user_id = str(self.last_user_id)
        else:
            last_user_id = self.last_user_id

        date_last_activity: Union[None, Unset, str]
        if isinstance(self.date_last_activity, Unset):
            date_last_activity = UNSET
        elif isinstance(self.date_last_activity, datetime.datetime):
            date_last_activity = self.date_last_activity.isoformat()
        else:
            date_last_activity = self.date_last_activity

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        icon_url: Union[None, Unset, str]
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if custom_name is not UNSET:
            field_dict["CustomName"] = custom_name
        if access_token is not UNSET:
            field_dict["AccessToken"] = access_token
        if id is not UNSET:
            field_dict["Id"] = id
        if last_user_name is not UNSET:
            field_dict["LastUserName"] = last_user_name
        if app_name is not UNSET:
            field_dict["AppName"] = app_name
        if app_version is not UNSET:
            field_dict["AppVersion"] = app_version
        if last_user_id is not UNSET:
            field_dict["LastUserId"] = last_user_id
        if date_last_activity is not UNSET:
            field_dict["DateLastActivity"] = date_last_activity
        if capabilities is not UNSET:
            field_dict["Capabilities"] = capabilities
        if icon_url is not UNSET:
            field_dict["IconUrl"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_capabilities_dto import ClientCapabilitiesDto

        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        def _parse_custom_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_name = _parse_custom_name(d.pop("CustomName", UNSET))

        def _parse_access_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        access_token = _parse_access_token(d.pop("AccessToken", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_last_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_user_name = _parse_last_user_name(d.pop("LastUserName", UNSET))

        def _parse_app_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_name = _parse_app_name(d.pop("AppName", UNSET))

        def _parse_app_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_version = _parse_app_version(d.pop("AppVersion", UNSET))

        def _parse_last_user_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_user_id_type_0 = UUID(data)

                return last_user_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        last_user_id = _parse_last_user_id(d.pop("LastUserId", UNSET))

        def _parse_date_last_activity(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_last_activity_type_0 = isoparse(data)

                return date_last_activity_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_last_activity = _parse_date_last_activity(d.pop("DateLastActivity", UNSET))

        _capabilities = d.pop("Capabilities", UNSET)
        capabilities: Union[Unset, ClientCapabilitiesDto]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = ClientCapabilitiesDto.from_dict(_capabilities)

        def _parse_icon_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        icon_url = _parse_icon_url(d.pop("IconUrl", UNSET))

        device_info_dto = cls(
            name=name,
            custom_name=custom_name,
            access_token=access_token,
            id=id,
            last_user_name=last_user_name,
            app_name=app_name,
            app_version=app_version,
            last_user_id=last_user_id,
            date_last_activity=date_last_activity,
            capabilities=capabilities,
            icon_url=icon_url,
        )

        return device_info_dto
