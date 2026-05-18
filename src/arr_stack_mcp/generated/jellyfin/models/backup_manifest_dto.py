import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_options_dto import BackupOptionsDto


T = TypeVar("T", bound="BackupManifestDto")


@_attrs_define
class BackupManifestDto:
    """Manifest type for backups internal structure.

    Attributes:
        server_version (Union[Unset, str]): Gets or sets the jellyfin version this backup was created with.
        backup_engine_version (Union[Unset, str]): Gets or sets the backup engine version this backup was created with.
        date_created (Union[Unset, datetime.datetime]): Gets or sets the date this backup was created with.
        path (Union[Unset, str]): Gets or sets the path to the backup on the system.
        options (Union[Unset, BackupOptionsDto]): Defines the optional contents of the backup archive.
    """

    server_version: Union[Unset, str] = UNSET
    backup_engine_version: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    path: Union[Unset, str] = UNSET
    options: Union[Unset, "BackupOptionsDto"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        server_version = self.server_version

        backup_engine_version = self.backup_engine_version

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        path = self.path

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if server_version is not UNSET:
            field_dict["ServerVersion"] = server_version
        if backup_engine_version is not UNSET:
            field_dict["BackupEngineVersion"] = backup_engine_version
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if path is not UNSET:
            field_dict["Path"] = path
        if options is not UNSET:
            field_dict["Options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_options_dto import BackupOptionsDto

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        server_version = d.pop("ServerVersion", UNSET)

        backup_engine_version = d.pop("BackupEngineVersion", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        path = d.pop("Path", UNSET)

        _options = d.pop("Options", UNSET)
        options: Union[Unset, BackupOptionsDto]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BackupOptionsDto.from_dict(_options)

        backup_manifest_dto = cls(
            server_version=server_version,
            backup_engine_version=backup_engine_version,
            date_created=date_created,
            path=path,
            options=options,
        )

        return backup_manifest_dto
