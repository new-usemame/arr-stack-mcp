from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field
    from ..models.provider_message import ProviderMessage


T = TypeVar("T", bound="NotificationResource")


@_attrs_define
class NotificationResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        fields (Union[None, Unset, list['Field']]):
        implementation_name (Union[None, Unset, str]):
        implementation (Union[None, Unset, str]):
        config_contract (Union[None, Unset, str]):
        info_link (Union[None, Unset, str]):
        message (Union[Unset, ProviderMessage]):
        tags (Union[None, Unset, list[int]]):
        presets (Union[None, Unset, list['NotificationResource']]):
        link (Union[None, Unset, str]):
        on_grab (Union[Unset, bool]):
        on_release_import (Union[Unset, bool]):
        on_upgrade (Union[Unset, bool]):
        on_rename (Union[Unset, bool]):
        on_artist_add (Union[Unset, bool]):
        on_artist_delete (Union[Unset, bool]):
        on_album_delete (Union[Unset, bool]):
        on_health_issue (Union[Unset, bool]):
        on_health_restored (Union[Unset, bool]):
        on_download_failure (Union[Unset, bool]):
        on_import_failure (Union[Unset, bool]):
        on_track_retag (Union[Unset, bool]):
        on_application_update (Union[Unset, bool]):
        supports_on_grab (Union[Unset, bool]):
        supports_on_release_import (Union[Unset, bool]):
        supports_on_upgrade (Union[Unset, bool]):
        supports_on_rename (Union[Unset, bool]):
        supports_on_artist_add (Union[Unset, bool]):
        supports_on_artist_delete (Union[Unset, bool]):
        supports_on_album_delete (Union[Unset, bool]):
        supports_on_health_issue (Union[Unset, bool]):
        supports_on_health_restored (Union[Unset, bool]):
        include_health_warnings (Union[Unset, bool]):
        supports_on_download_failure (Union[Unset, bool]):
        supports_on_import_failure (Union[Unset, bool]):
        supports_on_track_retag (Union[Unset, bool]):
        supports_on_application_update (Union[Unset, bool]):
        test_command (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    fields: Union[None, Unset, list["Field"]] = UNSET
    implementation_name: Union[None, Unset, str] = UNSET
    implementation: Union[None, Unset, str] = UNSET
    config_contract: Union[None, Unset, str] = UNSET
    info_link: Union[None, Unset, str] = UNSET
    message: Union[Unset, "ProviderMessage"] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    presets: Union[None, Unset, list["NotificationResource"]] = UNSET
    link: Union[None, Unset, str] = UNSET
    on_grab: Union[Unset, bool] = UNSET
    on_release_import: Union[Unset, bool] = UNSET
    on_upgrade: Union[Unset, bool] = UNSET
    on_rename: Union[Unset, bool] = UNSET
    on_artist_add: Union[Unset, bool] = UNSET
    on_artist_delete: Union[Unset, bool] = UNSET
    on_album_delete: Union[Unset, bool] = UNSET
    on_health_issue: Union[Unset, bool] = UNSET
    on_health_restored: Union[Unset, bool] = UNSET
    on_download_failure: Union[Unset, bool] = UNSET
    on_import_failure: Union[Unset, bool] = UNSET
    on_track_retag: Union[Unset, bool] = UNSET
    on_application_update: Union[Unset, bool] = UNSET
    supports_on_grab: Union[Unset, bool] = UNSET
    supports_on_release_import: Union[Unset, bool] = UNSET
    supports_on_upgrade: Union[Unset, bool] = UNSET
    supports_on_rename: Union[Unset, bool] = UNSET
    supports_on_artist_add: Union[Unset, bool] = UNSET
    supports_on_artist_delete: Union[Unset, bool] = UNSET
    supports_on_album_delete: Union[Unset, bool] = UNSET
    supports_on_health_issue: Union[Unset, bool] = UNSET
    supports_on_health_restored: Union[Unset, bool] = UNSET
    include_health_warnings: Union[Unset, bool] = UNSET
    supports_on_download_failure: Union[Unset, bool] = UNSET
    supports_on_import_failure: Union[Unset, bool] = UNSET
    supports_on_track_retag: Union[Unset, bool] = UNSET
    supports_on_application_update: Union[Unset, bool] = UNSET
    test_command: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        implementation_name: Union[None, Unset, str]
        if isinstance(self.implementation_name, Unset):
            implementation_name = UNSET
        else:
            implementation_name = self.implementation_name

        implementation: Union[None, Unset, str]
        if isinstance(self.implementation, Unset):
            implementation = UNSET
        else:
            implementation = self.implementation

        config_contract: Union[None, Unset, str]
        if isinstance(self.config_contract, Unset):
            config_contract = UNSET
        else:
            config_contract = self.config_contract

        info_link: Union[None, Unset, str]
        if isinstance(self.info_link, Unset):
            info_link = UNSET
        else:
            info_link = self.info_link

        message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        presets: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.presets, Unset):
            presets = UNSET
        elif isinstance(self.presets, list):
            presets = []
            for presets_type_0_item_data in self.presets:
                presets_type_0_item = presets_type_0_item_data.to_dict()
                presets.append(presets_type_0_item)

        else:
            presets = self.presets

        link: Union[None, Unset, str]
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        on_grab = self.on_grab

        on_release_import = self.on_release_import

        on_upgrade = self.on_upgrade

        on_rename = self.on_rename

        on_artist_add = self.on_artist_add

        on_artist_delete = self.on_artist_delete

        on_album_delete = self.on_album_delete

        on_health_issue = self.on_health_issue

        on_health_restored = self.on_health_restored

        on_download_failure = self.on_download_failure

        on_import_failure = self.on_import_failure

        on_track_retag = self.on_track_retag

        on_application_update = self.on_application_update

        supports_on_grab = self.supports_on_grab

        supports_on_release_import = self.supports_on_release_import

        supports_on_upgrade = self.supports_on_upgrade

        supports_on_rename = self.supports_on_rename

        supports_on_artist_add = self.supports_on_artist_add

        supports_on_artist_delete = self.supports_on_artist_delete

        supports_on_album_delete = self.supports_on_album_delete

        supports_on_health_issue = self.supports_on_health_issue

        supports_on_health_restored = self.supports_on_health_restored

        include_health_warnings = self.include_health_warnings

        supports_on_download_failure = self.supports_on_download_failure

        supports_on_import_failure = self.supports_on_import_failure

        supports_on_track_retag = self.supports_on_track_retag

        supports_on_application_update = self.supports_on_application_update

        test_command: Union[None, Unset, str]
        if isinstance(self.test_command, Unset):
            test_command = UNSET
        else:
            test_command = self.test_command

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if fields is not UNSET:
            field_dict["fields"] = fields
        if implementation_name is not UNSET:
            field_dict["implementationName"] = implementation_name
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if config_contract is not UNSET:
            field_dict["configContract"] = config_contract
        if info_link is not UNSET:
            field_dict["infoLink"] = info_link
        if message is not UNSET:
            field_dict["message"] = message
        if tags is not UNSET:
            field_dict["tags"] = tags
        if presets is not UNSET:
            field_dict["presets"] = presets
        if link is not UNSET:
            field_dict["link"] = link
        if on_grab is not UNSET:
            field_dict["onGrab"] = on_grab
        if on_release_import is not UNSET:
            field_dict["onReleaseImport"] = on_release_import
        if on_upgrade is not UNSET:
            field_dict["onUpgrade"] = on_upgrade
        if on_rename is not UNSET:
            field_dict["onRename"] = on_rename
        if on_artist_add is not UNSET:
            field_dict["onArtistAdd"] = on_artist_add
        if on_artist_delete is not UNSET:
            field_dict["onArtistDelete"] = on_artist_delete
        if on_album_delete is not UNSET:
            field_dict["onAlbumDelete"] = on_album_delete
        if on_health_issue is not UNSET:
            field_dict["onHealthIssue"] = on_health_issue
        if on_health_restored is not UNSET:
            field_dict["onHealthRestored"] = on_health_restored
        if on_download_failure is not UNSET:
            field_dict["onDownloadFailure"] = on_download_failure
        if on_import_failure is not UNSET:
            field_dict["onImportFailure"] = on_import_failure
        if on_track_retag is not UNSET:
            field_dict["onTrackRetag"] = on_track_retag
        if on_application_update is not UNSET:
            field_dict["onApplicationUpdate"] = on_application_update
        if supports_on_grab is not UNSET:
            field_dict["supportsOnGrab"] = supports_on_grab
        if supports_on_release_import is not UNSET:
            field_dict["supportsOnReleaseImport"] = supports_on_release_import
        if supports_on_upgrade is not UNSET:
            field_dict["supportsOnUpgrade"] = supports_on_upgrade
        if supports_on_rename is not UNSET:
            field_dict["supportsOnRename"] = supports_on_rename
        if supports_on_artist_add is not UNSET:
            field_dict["supportsOnArtistAdd"] = supports_on_artist_add
        if supports_on_artist_delete is not UNSET:
            field_dict["supportsOnArtistDelete"] = supports_on_artist_delete
        if supports_on_album_delete is not UNSET:
            field_dict["supportsOnAlbumDelete"] = supports_on_album_delete
        if supports_on_health_issue is not UNSET:
            field_dict["supportsOnHealthIssue"] = supports_on_health_issue
        if supports_on_health_restored is not UNSET:
            field_dict["supportsOnHealthRestored"] = supports_on_health_restored
        if include_health_warnings is not UNSET:
            field_dict["includeHealthWarnings"] = include_health_warnings
        if supports_on_download_failure is not UNSET:
            field_dict["supportsOnDownloadFailure"] = supports_on_download_failure
        if supports_on_import_failure is not UNSET:
            field_dict["supportsOnImportFailure"] = supports_on_import_failure
        if supports_on_track_retag is not UNSET:
            field_dict["supportsOnTrackRetag"] = supports_on_track_retag
        if supports_on_application_update is not UNSET:
            field_dict["supportsOnApplicationUpdate"] = supports_on_application_update
        if test_command is not UNSET:
            field_dict["testCommand"] = test_command

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field import Field
        from ..models.provider_message import ProviderMessage

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_fields(data: object) -> Union[None, Unset, list["Field"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = Field.from_dict(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Field"]], data)

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_implementation_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation_name = _parse_implementation_name(
            d.pop("implementationName", UNSET)
        )

        def _parse_implementation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation = _parse_implementation(d.pop("implementation", UNSET))

        def _parse_config_contract(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        config_contract = _parse_config_contract(d.pop("configContract", UNSET))

        def _parse_info_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_link = _parse_info_link(d.pop("infoLink", UNSET))

        _message = d.pop("message", UNSET)
        message: Union[Unset, ProviderMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = ProviderMessage.from_dict(_message)

        def _parse_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_presets(
            data: object,
        ) -> Union[None, Unset, list["NotificationResource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                presets_type_0 = []
                _presets_type_0 = data
                for presets_type_0_item_data in _presets_type_0:
                    presets_type_0_item = NotificationResource.from_dict(
                        presets_type_0_item_data
                    )

                    presets_type_0.append(presets_type_0_item)

                return presets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NotificationResource"]], data)

        presets = _parse_presets(d.pop("presets", UNSET))

        def _parse_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        link = _parse_link(d.pop("link", UNSET))

        on_grab = d.pop("onGrab", UNSET)

        on_release_import = d.pop("onReleaseImport", UNSET)

        on_upgrade = d.pop("onUpgrade", UNSET)

        on_rename = d.pop("onRename", UNSET)

        on_artist_add = d.pop("onArtistAdd", UNSET)

        on_artist_delete = d.pop("onArtistDelete", UNSET)

        on_album_delete = d.pop("onAlbumDelete", UNSET)

        on_health_issue = d.pop("onHealthIssue", UNSET)

        on_health_restored = d.pop("onHealthRestored", UNSET)

        on_download_failure = d.pop("onDownloadFailure", UNSET)

        on_import_failure = d.pop("onImportFailure", UNSET)

        on_track_retag = d.pop("onTrackRetag", UNSET)

        on_application_update = d.pop("onApplicationUpdate", UNSET)

        supports_on_grab = d.pop("supportsOnGrab", UNSET)

        supports_on_release_import = d.pop("supportsOnReleaseImport", UNSET)

        supports_on_upgrade = d.pop("supportsOnUpgrade", UNSET)

        supports_on_rename = d.pop("supportsOnRename", UNSET)

        supports_on_artist_add = d.pop("supportsOnArtistAdd", UNSET)

        supports_on_artist_delete = d.pop("supportsOnArtistDelete", UNSET)

        supports_on_album_delete = d.pop("supportsOnAlbumDelete", UNSET)

        supports_on_health_issue = d.pop("supportsOnHealthIssue", UNSET)

        supports_on_health_restored = d.pop("supportsOnHealthRestored", UNSET)

        include_health_warnings = d.pop("includeHealthWarnings", UNSET)

        supports_on_download_failure = d.pop("supportsOnDownloadFailure", UNSET)

        supports_on_import_failure = d.pop("supportsOnImportFailure", UNSET)

        supports_on_track_retag = d.pop("supportsOnTrackRetag", UNSET)

        supports_on_application_update = d.pop("supportsOnApplicationUpdate", UNSET)

        def _parse_test_command(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        test_command = _parse_test_command(d.pop("testCommand", UNSET))

        notification_resource = cls(
            id=id,
            name=name,
            fields=fields,
            implementation_name=implementation_name,
            implementation=implementation,
            config_contract=config_contract,
            info_link=info_link,
            message=message,
            tags=tags,
            presets=presets,
            link=link,
            on_grab=on_grab,
            on_release_import=on_release_import,
            on_upgrade=on_upgrade,
            on_rename=on_rename,
            on_artist_add=on_artist_add,
            on_artist_delete=on_artist_delete,
            on_album_delete=on_album_delete,
            on_health_issue=on_health_issue,
            on_health_restored=on_health_restored,
            on_download_failure=on_download_failure,
            on_import_failure=on_import_failure,
            on_track_retag=on_track_retag,
            on_application_update=on_application_update,
            supports_on_grab=supports_on_grab,
            supports_on_release_import=supports_on_release_import,
            supports_on_upgrade=supports_on_upgrade,
            supports_on_rename=supports_on_rename,
            supports_on_artist_add=supports_on_artist_add,
            supports_on_artist_delete=supports_on_artist_delete,
            supports_on_album_delete=supports_on_album_delete,
            supports_on_health_issue=supports_on_health_issue,
            supports_on_health_restored=supports_on_health_restored,
            include_health_warnings=include_health_warnings,
            supports_on_download_failure=supports_on_download_failure,
            supports_on_import_failure=supports_on_import_failure,
            supports_on_track_retag=supports_on_track_retag,
            supports_on_application_update=supports_on_application_update,
            test_command=test_command,
        )

        return notification_resource
