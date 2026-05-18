from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unmapped_folder import UnmappedFolder


T = TypeVar("T", bound="RootFolderResource")


@_attrs_define
class RootFolderResource:
    """
    Attributes:
        id (Union[Unset, int]):
        path (Union[None, Unset, str]):
        accessible (Union[Unset, bool]):
        free_space (Union[None, Unset, int]):
        unmapped_folders (Union[None, Unset, list['UnmappedFolder']]):
    """

    id: Union[Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    accessible: Union[Unset, bool] = UNSET
    free_space: Union[None, Unset, int] = UNSET
    unmapped_folders: Union[None, Unset, list["UnmappedFolder"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        accessible = self.accessible

        free_space: Union[None, Unset, int]
        if isinstance(self.free_space, Unset):
            free_space = UNSET
        else:
            free_space = self.free_space

        unmapped_folders: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.unmapped_folders, Unset):
            unmapped_folders = UNSET
        elif isinstance(self.unmapped_folders, list):
            unmapped_folders = []
            for unmapped_folders_type_0_item_data in self.unmapped_folders:
                unmapped_folders_type_0_item = (
                    unmapped_folders_type_0_item_data.to_dict()
                )
                unmapped_folders.append(unmapped_folders_type_0_item)

        else:
            unmapped_folders = self.unmapped_folders

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path
        if accessible is not UNSET:
            field_dict["accessible"] = accessible
        if free_space is not UNSET:
            field_dict["freeSpace"] = free_space
        if unmapped_folders is not UNSET:
            field_dict["unmappedFolders"] = unmapped_folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unmapped_folder import UnmappedFolder

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        accessible = d.pop("accessible", UNSET)

        def _parse_free_space(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space = _parse_free_space(d.pop("freeSpace", UNSET))

        def _parse_unmapped_folders(
            data: object,
        ) -> Union[None, Unset, list["UnmappedFolder"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                unmapped_folders_type_0 = []
                _unmapped_folders_type_0 = data
                for unmapped_folders_type_0_item_data in _unmapped_folders_type_0:
                    unmapped_folders_type_0_item = UnmappedFolder.from_dict(
                        unmapped_folders_type_0_item_data
                    )

                    unmapped_folders_type_0.append(unmapped_folders_type_0_item)

                return unmapped_folders_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UnmappedFolder"]], data)

        unmapped_folders = _parse_unmapped_folders(d.pop("unmappedFolders", UNSET))

        root_folder_resource = cls(
            id=id,
            path=path,
            accessible=accessible,
            free_space=free_space,
            unmapped_folders=unmapped_folders,
        )

        return root_folder_resource
