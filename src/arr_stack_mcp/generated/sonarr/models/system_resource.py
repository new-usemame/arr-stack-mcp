import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.authentication_type import AuthenticationType
from ..models.database_type import DatabaseType
from ..models.runtime_mode import RuntimeMode
from ..models.update_mechanism import UpdateMechanism
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemResource")


@_attrs_define
class SystemResource:
    """
    Attributes:
        app_name (Union[None, Unset, str]):
        instance_name (Union[None, Unset, str]):
        version (Union[None, Unset, str]):
        build_time (Union[Unset, datetime.datetime]):
        is_debug (Union[Unset, bool]):
        is_production (Union[Unset, bool]):
        is_admin (Union[Unset, bool]):
        is_user_interactive (Union[Unset, bool]):
        startup_path (Union[None, Unset, str]):
        app_data (Union[None, Unset, str]):
        os_name (Union[None, Unset, str]):
        os_version (Union[None, Unset, str]):
        is_net_core (Union[Unset, bool]):
        is_linux (Union[Unset, bool]):
        is_osx (Union[Unset, bool]):
        is_windows (Union[Unset, bool]):
        is_docker (Union[Unset, bool]):
        mode (Union[Unset, RuntimeMode]):
        branch (Union[None, Unset, str]):
        authentication (Union[Unset, AuthenticationType]):
        sqlite_version (Union[None, Unset, str]):
        migration_version (Union[Unset, int]):
        url_base (Union[None, Unset, str]):
        runtime_version (Union[None, Unset, str]):
        runtime_name (Union[None, Unset, str]):
        start_time (Union[Unset, datetime.datetime]):
        package_version (Union[None, Unset, str]):
        package_author (Union[None, Unset, str]):
        package_update_mechanism (Union[Unset, UpdateMechanism]):
        package_update_mechanism_message (Union[None, Unset, str]):
        database_version (Union[None, Unset, str]):
        database_type (Union[Unset, DatabaseType]):
    """

    app_name: Union[None, Unset, str] = UNSET
    instance_name: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    build_time: Union[Unset, datetime.datetime] = UNSET
    is_debug: Union[Unset, bool] = UNSET
    is_production: Union[Unset, bool] = UNSET
    is_admin: Union[Unset, bool] = UNSET
    is_user_interactive: Union[Unset, bool] = UNSET
    startup_path: Union[None, Unset, str] = UNSET
    app_data: Union[None, Unset, str] = UNSET
    os_name: Union[None, Unset, str] = UNSET
    os_version: Union[None, Unset, str] = UNSET
    is_net_core: Union[Unset, bool] = UNSET
    is_linux: Union[Unset, bool] = UNSET
    is_osx: Union[Unset, bool] = UNSET
    is_windows: Union[Unset, bool] = UNSET
    is_docker: Union[Unset, bool] = UNSET
    mode: Union[Unset, RuntimeMode] = UNSET
    branch: Union[None, Unset, str] = UNSET
    authentication: Union[Unset, AuthenticationType] = UNSET
    sqlite_version: Union[None, Unset, str] = UNSET
    migration_version: Union[Unset, int] = UNSET
    url_base: Union[None, Unset, str] = UNSET
    runtime_version: Union[None, Unset, str] = UNSET
    runtime_name: Union[None, Unset, str] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    package_version: Union[None, Unset, str] = UNSET
    package_author: Union[None, Unset, str] = UNSET
    package_update_mechanism: Union[Unset, UpdateMechanism] = UNSET
    package_update_mechanism_message: Union[None, Unset, str] = UNSET
    database_version: Union[None, Unset, str] = UNSET
    database_type: Union[Unset, DatabaseType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        app_name: Union[None, Unset, str]
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        instance_name: Union[None, Unset, str]
        if isinstance(self.instance_name, Unset):
            instance_name = UNSET
        else:
            instance_name = self.instance_name

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        build_time: Union[Unset, str] = UNSET
        if not isinstance(self.build_time, Unset):
            build_time = self.build_time.isoformat()

        is_debug = self.is_debug

        is_production = self.is_production

        is_admin = self.is_admin

        is_user_interactive = self.is_user_interactive

        startup_path: Union[None, Unset, str]
        if isinstance(self.startup_path, Unset):
            startup_path = UNSET
        else:
            startup_path = self.startup_path

        app_data: Union[None, Unset, str]
        if isinstance(self.app_data, Unset):
            app_data = UNSET
        else:
            app_data = self.app_data

        os_name: Union[None, Unset, str]
        if isinstance(self.os_name, Unset):
            os_name = UNSET
        else:
            os_name = self.os_name

        os_version: Union[None, Unset, str]
        if isinstance(self.os_version, Unset):
            os_version = UNSET
        else:
            os_version = self.os_version

        is_net_core = self.is_net_core

        is_linux = self.is_linux

        is_osx = self.is_osx

        is_windows = self.is_windows

        is_docker = self.is_docker

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        branch: Union[None, Unset, str]
        if isinstance(self.branch, Unset):
            branch = UNSET
        else:
            branch = self.branch

        authentication: Union[Unset, str] = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.value

        sqlite_version: Union[None, Unset, str]
        if isinstance(self.sqlite_version, Unset):
            sqlite_version = UNSET
        else:
            sqlite_version = self.sqlite_version

        migration_version = self.migration_version

        url_base: Union[None, Unset, str]
        if isinstance(self.url_base, Unset):
            url_base = UNSET
        else:
            url_base = self.url_base

        runtime_version: Union[None, Unset, str]
        if isinstance(self.runtime_version, Unset):
            runtime_version = UNSET
        else:
            runtime_version = self.runtime_version

        runtime_name: Union[None, Unset, str]
        if isinstance(self.runtime_name, Unset):
            runtime_name = UNSET
        else:
            runtime_name = self.runtime_name

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        package_version: Union[None, Unset, str]
        if isinstance(self.package_version, Unset):
            package_version = UNSET
        else:
            package_version = self.package_version

        package_author: Union[None, Unset, str]
        if isinstance(self.package_author, Unset):
            package_author = UNSET
        else:
            package_author = self.package_author

        package_update_mechanism: Union[Unset, str] = UNSET
        if not isinstance(self.package_update_mechanism, Unset):
            package_update_mechanism = self.package_update_mechanism.value

        package_update_mechanism_message: Union[None, Unset, str]
        if isinstance(self.package_update_mechanism_message, Unset):
            package_update_mechanism_message = UNSET
        else:
            package_update_mechanism_message = self.package_update_mechanism_message

        database_version: Union[None, Unset, str]
        if isinstance(self.database_version, Unset):
            database_version = UNSET
        else:
            database_version = self.database_version

        database_type: Union[Unset, str] = UNSET
        if not isinstance(self.database_type, Unset):
            database_type = self.database_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if version is not UNSET:
            field_dict["version"] = version
        if build_time is not UNSET:
            field_dict["buildTime"] = build_time
        if is_debug is not UNSET:
            field_dict["isDebug"] = is_debug
        if is_production is not UNSET:
            field_dict["isProduction"] = is_production
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if is_user_interactive is not UNSET:
            field_dict["isUserInteractive"] = is_user_interactive
        if startup_path is not UNSET:
            field_dict["startupPath"] = startup_path
        if app_data is not UNSET:
            field_dict["appData"] = app_data
        if os_name is not UNSET:
            field_dict["osName"] = os_name
        if os_version is not UNSET:
            field_dict["osVersion"] = os_version
        if is_net_core is not UNSET:
            field_dict["isNetCore"] = is_net_core
        if is_linux is not UNSET:
            field_dict["isLinux"] = is_linux
        if is_osx is not UNSET:
            field_dict["isOsx"] = is_osx
        if is_windows is not UNSET:
            field_dict["isWindows"] = is_windows
        if is_docker is not UNSET:
            field_dict["isDocker"] = is_docker
        if mode is not UNSET:
            field_dict["mode"] = mode
        if branch is not UNSET:
            field_dict["branch"] = branch
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if sqlite_version is not UNSET:
            field_dict["sqliteVersion"] = sqlite_version
        if migration_version is not UNSET:
            field_dict["migrationVersion"] = migration_version
        if url_base is not UNSET:
            field_dict["urlBase"] = url_base
        if runtime_version is not UNSET:
            field_dict["runtimeVersion"] = runtime_version
        if runtime_name is not UNSET:
            field_dict["runtimeName"] = runtime_name
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if package_version is not UNSET:
            field_dict["packageVersion"] = package_version
        if package_author is not UNSET:
            field_dict["packageAuthor"] = package_author
        if package_update_mechanism is not UNSET:
            field_dict["packageUpdateMechanism"] = package_update_mechanism
        if package_update_mechanism_message is not UNSET:
            field_dict["packageUpdateMechanismMessage"] = (
                package_update_mechanism_message
            )
        if database_version is not UNSET:
            field_dict["databaseVersion"] = database_version
        if database_type is not UNSET:
            field_dict["databaseType"] = database_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_app_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_name = _parse_app_name(d.pop("appName", UNSET))

        def _parse_instance_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instance_name = _parse_instance_name(d.pop("instanceName", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        _build_time = d.pop("buildTime", UNSET)
        build_time: Union[Unset, datetime.datetime]
        if isinstance(_build_time, Unset):
            build_time = UNSET
        else:
            build_time = isoparse(_build_time)

        is_debug = d.pop("isDebug", UNSET)

        is_production = d.pop("isProduction", UNSET)

        is_admin = d.pop("isAdmin", UNSET)

        is_user_interactive = d.pop("isUserInteractive", UNSET)

        def _parse_startup_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        startup_path = _parse_startup_path(d.pop("startupPath", UNSET))

        def _parse_app_data(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_data = _parse_app_data(d.pop("appData", UNSET))

        def _parse_os_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        os_name = _parse_os_name(d.pop("osName", UNSET))

        def _parse_os_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        os_version = _parse_os_version(d.pop("osVersion", UNSET))

        is_net_core = d.pop("isNetCore", UNSET)

        is_linux = d.pop("isLinux", UNSET)

        is_osx = d.pop("isOsx", UNSET)

        is_windows = d.pop("isWindows", UNSET)

        is_docker = d.pop("isDocker", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, RuntimeMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = RuntimeMode(_mode)

        def _parse_branch(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        branch = _parse_branch(d.pop("branch", UNSET))

        _authentication = d.pop("authentication", UNSET)
        authentication: Union[Unset, AuthenticationType]
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = AuthenticationType(_authentication)

        def _parse_sqlite_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sqlite_version = _parse_sqlite_version(d.pop("sqliteVersion", UNSET))

        migration_version = d.pop("migrationVersion", UNSET)

        def _parse_url_base(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url_base = _parse_url_base(d.pop("urlBase", UNSET))

        def _parse_runtime_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        runtime_version = _parse_runtime_version(d.pop("runtimeVersion", UNSET))

        def _parse_runtime_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        runtime_name = _parse_runtime_name(d.pop("runtimeName", UNSET))

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        def _parse_package_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        package_version = _parse_package_version(d.pop("packageVersion", UNSET))

        def _parse_package_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        package_author = _parse_package_author(d.pop("packageAuthor", UNSET))

        _package_update_mechanism = d.pop("packageUpdateMechanism", UNSET)
        package_update_mechanism: Union[Unset, UpdateMechanism]
        if isinstance(_package_update_mechanism, Unset):
            package_update_mechanism = UNSET
        else:
            package_update_mechanism = UpdateMechanism(_package_update_mechanism)

        def _parse_package_update_mechanism_message(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        package_update_mechanism_message = _parse_package_update_mechanism_message(
            d.pop("packageUpdateMechanismMessage", UNSET)
        )

        def _parse_database_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        database_version = _parse_database_version(d.pop("databaseVersion", UNSET))

        _database_type = d.pop("databaseType", UNSET)
        database_type: Union[Unset, DatabaseType]
        if isinstance(_database_type, Unset):
            database_type = UNSET
        else:
            database_type = DatabaseType(_database_type)

        system_resource = cls(
            app_name=app_name,
            instance_name=instance_name,
            version=version,
            build_time=build_time,
            is_debug=is_debug,
            is_production=is_production,
            is_admin=is_admin,
            is_user_interactive=is_user_interactive,
            startup_path=startup_path,
            app_data=app_data,
            os_name=os_name,
            os_version=os_version,
            is_net_core=is_net_core,
            is_linux=is_linux,
            is_osx=is_osx,
            is_windows=is_windows,
            is_docker=is_docker,
            mode=mode,
            branch=branch,
            authentication=authentication,
            sqlite_version=sqlite_version,
            migration_version=migration_version,
            url_base=url_base,
            runtime_version=runtime_version,
            runtime_name=runtime_name,
            start_time=start_time,
            package_version=package_version,
            package_author=package_author,
            package_update_mechanism=package_update_mechanism,
            package_update_mechanism_message=package_update_mechanism_message,
            database_version=database_version,
            database_type=database_type,
        )

        return system_resource
