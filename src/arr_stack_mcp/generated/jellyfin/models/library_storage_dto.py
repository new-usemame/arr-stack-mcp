from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder_storage_dto import FolderStorageDto


T = TypeVar("T", bound="LibraryStorageDto")


@_attrs_define
class LibraryStorageDto:
    """Contains informations about a libraries storage informations.

    Attributes:
        id (Union[Unset, UUID]): Gets or sets the Library Id.
        name (Union[Unset, str]): Gets or sets the name of the library.
        folders (Union[Unset, list['FolderStorageDto']]): Gets or sets the storage informations about the folders used
            in a library.
    """

    id: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    folders: Union[Unset, list["FolderStorageDto"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        folders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()
                folders.append(folders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if name is not UNSET:
            field_dict["Name"] = name
        if folders is not UNSET:
            field_dict["Folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_storage_dto import FolderStorageDto

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        _id = d.pop("Id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("Name", UNSET)

        folders = []
        _folders = d.pop("Folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = FolderStorageDto.from_dict(folders_item_data)

            folders.append(folders_item)

        library_storage_dto = cls(
            id=id,
            name=name,
            folders=folders,
        )

        return library_storage_dto
