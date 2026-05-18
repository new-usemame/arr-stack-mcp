import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_changes import UpdateChanges


T = TypeVar("T", bound="UpdateResource")


@_attrs_define
class UpdateResource:
    """
    Attributes:
        id (Union[Unset, int]):
        version (Union[None, Unset, str]):
        branch (Union[None, Unset, str]):
        release_date (Union[Unset, datetime.datetime]):
        file_name (Union[None, Unset, str]):
        url (Union[None, Unset, str]):
        installed (Union[Unset, bool]):
        installed_on (Union[None, Unset, datetime.datetime]):
        installable (Union[Unset, bool]):
        latest (Union[Unset, bool]):
        changes (Union[Unset, UpdateChanges]):
        hash_ (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    version: Union[None, Unset, str] = UNSET
    branch: Union[None, Unset, str] = UNSET
    release_date: Union[Unset, datetime.datetime] = UNSET
    file_name: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    installed: Union[Unset, bool] = UNSET
    installed_on: Union[None, Unset, datetime.datetime] = UNSET
    installable: Union[Unset, bool] = UNSET
    latest: Union[Unset, bool] = UNSET
    changes: Union[Unset, "UpdateChanges"] = UNSET
    hash_: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        branch: Union[None, Unset, str]
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        release_date: Union[Unset, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        file_name: Union[None, Unset, str]
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        installed = self.installed

        installed_on: Union[None, Unset, str]
        if isinstance(self.installed_on, Unset):
            installed_on = UNSET
        elif isinstance(self.installed_on, datetime.datetime):
            installed_on = self.installed_on.isoformat()
        else:
            installed_on = self.installed_on

        installable = self.installable

        latest = self.latest

        changes: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        hash_: Union[None, Unset, str]
        if isinstance(self.hash_, Unset):
            hash_ = UNSET
        else:
            hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if branch is not UNSET:
            field_dict["branch"] = branch
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if url is not UNSET:
            field_dict["url"] = url
        if installed is not UNSET:
            field_dict["installed"] = installed
        if installed_on is not UNSET:
            field_dict["installedOn"] = installed_on
        if installable is not UNSET:
            field_dict["installable"] = installable
        if latest is not UNSET:
            field_dict["latest"] = latest
        if changes is not UNSET:
            field_dict["changes"] = changes
        if hash_ is not UNSET:
            field_dict["hash"] = hash_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_changes import UpdateChanges

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_branch(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        branch = _parse_branch(d.pop("branch", UNSET))

        _release_date = d.pop("releaseDate", UNSET)
        release_date: Union[Unset, datetime.datetime]
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date)

        def _parse_file_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        installed = d.pop("installed", UNSET)

        def _parse_installed_on(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                installed_on_type_0 = isoparse(data)

                return installed_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        installed_on = _parse_installed_on(d.pop("installedOn", UNSET))

        installable = d.pop("installable", UNSET)

        latest = d.pop("latest", UNSET)

        _changes = d.pop("changes", UNSET)
        changes: Union[Unset, UpdateChanges]
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = UpdateChanges.from_dict(_changes)

        def _parse_hash_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hash_ = _parse_hash_(d.pop("hash", UNSET))

        update_resource = cls(
            id=id,
            version=version,
            branch=branch,
            release_date=release_date,
            file_name=file_name,
            url=url,
            installed=installed,
            installed_on=installed_on,
            installable=installable,
            latest=latest,
            changes=changes,
            hash_=hash_,
        )

        return update_resource
