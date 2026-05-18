from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.allow_fingerprinting import AllowFingerprinting
from ..models.file_date_type import FileDateType
from ..models.proper_download_types import ProperDownloadTypes
from ..models.rescan_after_refresh_type import RescanAfterRefreshType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaManagementConfigResource")


@_attrs_define
class MediaManagementConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        auto_unmonitor_previously_downloaded_tracks (Union[Unset, bool]):
        recycle_bin (Union[None, Unset, str]):
        recycle_bin_cleanup_days (Union[Unset, int]):
        download_propers_and_repacks (Union[Unset, ProperDownloadTypes]):
        create_empty_artist_folders (Union[Unset, bool]):
        delete_empty_folders (Union[Unset, bool]):
        file_date (Union[Unset, FileDateType]):
        watch_library_for_changes (Union[Unset, bool]):
        rescan_after_refresh (Union[Unset, RescanAfterRefreshType]):
        allow_fingerprinting (Union[Unset, AllowFingerprinting]):
        set_permissions_linux (Union[Unset, bool]):
        chmod_folder (Union[None, Unset, str]):
        chown_group (Union[None, Unset, str]):
        skip_free_space_check_when_importing (Union[Unset, bool]):
        minimum_free_space_when_importing (Union[Unset, int]):
        copy_using_hardlinks (Union[Unset, bool]):
        enable_media_info (Union[Unset, bool]):
        use_script_import (Union[Unset, bool]):
        script_import_path (Union[None, Unset, str]):
        import_extra_files (Union[Unset, bool]):
        extra_file_extensions (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    auto_unmonitor_previously_downloaded_tracks: Union[Unset, bool] = UNSET
    recycle_bin: Union[None, Unset, str] = UNSET
    recycle_bin_cleanup_days: Union[Unset, int] = UNSET
    download_propers_and_repacks: Union[Unset, ProperDownloadTypes] = UNSET
    create_empty_artist_folders: Union[Unset, bool] = UNSET
    delete_empty_folders: Union[Unset, bool] = UNSET
    file_date: Union[Unset, FileDateType] = UNSET
    watch_library_for_changes: Union[Unset, bool] = UNSET
    rescan_after_refresh: Union[Unset, RescanAfterRefreshType] = UNSET
    allow_fingerprinting: Union[Unset, AllowFingerprinting] = UNSET
    set_permissions_linux: Union[Unset, bool] = UNSET
    chmod_folder: Union[None, Unset, str] = UNSET
    chown_group: Union[None, Unset, str] = UNSET
    skip_free_space_check_when_importing: Union[Unset, bool] = UNSET
    minimum_free_space_when_importing: Union[Unset, int] = UNSET
    copy_using_hardlinks: Union[Unset, bool] = UNSET
    enable_media_info: Union[Unset, bool] = UNSET
    use_script_import: Union[Unset, bool] = UNSET
    script_import_path: Union[None, Unset, str] = UNSET
    import_extra_files: Union[Unset, bool] = UNSET
    extra_file_extensions: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        auto_unmonitor_previously_downloaded_tracks = (
            self.auto_unmonitor_previously_downloaded_tracks
        )

        recycle_bin: Union[None, Unset, str]
        if isinstance(self.recycle_bin, Unset):
            recycle_bin = UNSET
        else:
            recycle_bin = self.recycle_bin

        recycle_bin_cleanup_days = self.recycle_bin_cleanup_days

        download_propers_and_repacks: Union[Unset, str] = UNSET
        if not isinstance(self.download_propers_and_repacks, Unset):
            download_propers_and_repacks = self.download_propers_and_repacks.value

        create_empty_artist_folders = self.create_empty_artist_folders

        delete_empty_folders = self.delete_empty_folders

        file_date: Union[Unset, str] = UNSET
        if not isinstance(self.file_date, Unset):
            file_date = self.file_date.value

        watch_library_for_changes = self.watch_library_for_changes

        rescan_after_refresh: Union[Unset, str] = UNSET
        if not isinstance(self.rescan_after_refresh, Unset):
            rescan_after_refresh = self.rescan_after_refresh.value

        allow_fingerprinting: Union[Unset, str] = UNSET
        if not isinstance(self.allow_fingerprinting, Unset):
            allow_fingerprinting = self.allow_fingerprinting.value

        set_permissions_linux = self.set_permissions_linux

        chmod_folder: Union[None, Unset, str]
        if isinstance(self.chmod_folder, Unset):
            chmod_folder = UNSET
        else:
            chmod_folder = self.chmod_folder

        chown_group: Union[None, Unset, str]
        if isinstance(self.chown_group, Unset):
            chown_group = UNSET
        else:
            chown_group = self.chown_group

        skip_free_space_check_when_importing = self.skip_free_space_check_when_importing

        minimum_free_space_when_importing = self.minimum_free_space_when_importing

        copy_using_hardlinks = self.copy_using_hardlinks

        enable_media_info = self.enable_media_info

        use_script_import = self.use_script_import

        script_import_path: Union[None, Unset, str]
        if isinstance(self.script_import_path, Unset):
            script_import_path = UNSET
        else:
            script_import_path = self.script_import_path

        import_extra_files = self.import_extra_files

        extra_file_extensions: Union[None, Unset, str]
        if isinstance(self.extra_file_extensions, Unset):
            extra_file_extensions = UNSET
        else:
            extra_file_extensions = self.extra_file_extensions

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if auto_unmonitor_previously_downloaded_tracks is not UNSET:
            field_dict["autoUnmonitorPreviouslyDownloadedTracks"] = (
                auto_unmonitor_previously_downloaded_tracks
            )
        if recycle_bin is not UNSET:
            field_dict["recycleBin"] = recycle_bin
        if recycle_bin_cleanup_days is not UNSET:
            field_dict["recycleBinCleanupDays"] = recycle_bin_cleanup_days
        if download_propers_and_repacks is not UNSET:
            field_dict["downloadPropersAndRepacks"] = download_propers_and_repacks
        if create_empty_artist_folders is not UNSET:
            field_dict["createEmptyArtistFolders"] = create_empty_artist_folders
        if delete_empty_folders is not UNSET:
            field_dict["deleteEmptyFolders"] = delete_empty_folders
        if file_date is not UNSET:
            field_dict["fileDate"] = file_date
        if watch_library_for_changes is not UNSET:
            field_dict["watchLibraryForChanges"] = watch_library_for_changes
        if rescan_after_refresh is not UNSET:
            field_dict["rescanAfterRefresh"] = rescan_after_refresh
        if allow_fingerprinting is not UNSET:
            field_dict["allowFingerprinting"] = allow_fingerprinting
        if set_permissions_linux is not UNSET:
            field_dict["setPermissionsLinux"] = set_permissions_linux
        if chmod_folder is not UNSET:
            field_dict["chmodFolder"] = chmod_folder
        if chown_group is not UNSET:
            field_dict["chownGroup"] = chown_group
        if skip_free_space_check_when_importing is not UNSET:
            field_dict["skipFreeSpaceCheckWhenImporting"] = (
                skip_free_space_check_when_importing
            )
        if minimum_free_space_when_importing is not UNSET:
            field_dict["minimumFreeSpaceWhenImporting"] = (
                minimum_free_space_when_importing
            )
        if copy_using_hardlinks is not UNSET:
            field_dict["copyUsingHardlinks"] = copy_using_hardlinks
        if enable_media_info is not UNSET:
            field_dict["enableMediaInfo"] = enable_media_info
        if use_script_import is not UNSET:
            field_dict["useScriptImport"] = use_script_import
        if script_import_path is not UNSET:
            field_dict["scriptImportPath"] = script_import_path
        if import_extra_files is not UNSET:
            field_dict["importExtraFiles"] = import_extra_files
        if extra_file_extensions is not UNSET:
            field_dict["extraFileExtensions"] = extra_file_extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        auto_unmonitor_previously_downloaded_tracks = d.pop(
            "autoUnmonitorPreviouslyDownloadedTracks", UNSET
        )

        def _parse_recycle_bin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recycle_bin = _parse_recycle_bin(d.pop("recycleBin", UNSET))

        recycle_bin_cleanup_days = d.pop("recycleBinCleanupDays", UNSET)

        _download_propers_and_repacks = d.pop("downloadPropersAndRepacks", UNSET)
        download_propers_and_repacks: Union[Unset, ProperDownloadTypes]
        if isinstance(_download_propers_and_repacks, Unset):
            download_propers_and_repacks = UNSET
        else:
            download_propers_and_repacks = ProperDownloadTypes(
                _download_propers_and_repacks
            )

        create_empty_artist_folders = d.pop("createEmptyArtistFolders", UNSET)

        delete_empty_folders = d.pop("deleteEmptyFolders", UNSET)

        _file_date = d.pop("fileDate", UNSET)
        file_date: Union[Unset, FileDateType]
        if isinstance(_file_date, Unset):
            file_date = UNSET
        else:
            file_date = FileDateType(_file_date)

        watch_library_for_changes = d.pop("watchLibraryForChanges", UNSET)

        _rescan_after_refresh = d.pop("rescanAfterRefresh", UNSET)
        rescan_after_refresh: Union[Unset, RescanAfterRefreshType]
        if isinstance(_rescan_after_refresh, Unset):
            rescan_after_refresh = UNSET
        else:
            rescan_after_refresh = RescanAfterRefreshType(_rescan_after_refresh)

        _allow_fingerprinting = d.pop("allowFingerprinting", UNSET)
        allow_fingerprinting: Union[Unset, AllowFingerprinting]
        if isinstance(_allow_fingerprinting, Unset):
            allow_fingerprinting = UNSET
        else:
            allow_fingerprinting = AllowFingerprinting(_allow_fingerprinting)

        set_permissions_linux = d.pop("setPermissionsLinux", UNSET)

        def _parse_chmod_folder(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chmod_folder = _parse_chmod_folder(d.pop("chmodFolder", UNSET))

        def _parse_chown_group(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        chown_group = _parse_chown_group(d.pop("chownGroup", UNSET))

        skip_free_space_check_when_importing = d.pop(
            "skipFreeSpaceCheckWhenImporting", UNSET
        )

        minimum_free_space_when_importing = d.pop(
            "minimumFreeSpaceWhenImporting", UNSET
        )

        copy_using_hardlinks = d.pop("copyUsingHardlinks", UNSET)

        enable_media_info = d.pop("enableMediaInfo", UNSET)

        use_script_import = d.pop("useScriptImport", UNSET)

        def _parse_script_import_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        script_import_path = _parse_script_import_path(d.pop("scriptImportPath", UNSET))

        import_extra_files = d.pop("importExtraFiles", UNSET)

        def _parse_extra_file_extensions(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        extra_file_extensions = _parse_extra_file_extensions(
            d.pop("extraFileExtensions", UNSET)
        )

        media_management_config_resource = cls(
            id=id,
            auto_unmonitor_previously_downloaded_tracks=auto_unmonitor_previously_downloaded_tracks,
            recycle_bin=recycle_bin,
            recycle_bin_cleanup_days=recycle_bin_cleanup_days,
            download_propers_and_repacks=download_propers_and_repacks,
            create_empty_artist_folders=create_empty_artist_folders,
            delete_empty_folders=delete_empty_folders,
            file_date=file_date,
            watch_library_for_changes=watch_library_for_changes,
            rescan_after_refresh=rescan_after_refresh,
            allow_fingerprinting=allow_fingerprinting,
            set_permissions_linux=set_permissions_linux,
            chmod_folder=chmod_folder,
            chown_group=chown_group,
            skip_free_space_check_when_importing=skip_free_space_check_when_importing,
            minimum_free_space_when_importing=minimum_free_space_when_importing,
            copy_using_hardlinks=copy_using_hardlinks,
            enable_media_info=enable_media_info,
            use_script_import=use_script_import,
            script_import_path=script_import_path,
            import_extra_files=import_extra_files,
            extra_file_extensions=extra_file_extensions,
        )

        return media_management_config_resource
