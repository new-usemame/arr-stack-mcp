from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFormatBulkResource")


@_attrs_define
class CustomFormatBulkResource:
    """
    Attributes:
        ids (Union[None, Unset, list[int]]):
        include_custom_format_when_renaming (Union[None, Unset, bool]):
    """

    ids: Union[None, Unset, list[int]] = UNSET
    include_custom_format_when_renaming: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ids: Union[None, Unset, list[int]]
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = self.ids

        else:
            ids = self.ids

        include_custom_format_when_renaming: Union[None, Unset, bool]
        if isinstance(self.include_custom_format_when_renaming, Unset):
            include_custom_format_when_renaming = UNSET
        else:
            include_custom_format_when_renaming = (
                self.include_custom_format_when_renaming
            )

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if include_custom_format_when_renaming is not UNSET:
            field_dict["includeCustomFormatWhenRenaming"] = (
                include_custom_format_when_renaming
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = cast(list[int], data)

                return ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        ids = _parse_ids(d.pop("ids", UNSET))

        def _parse_include_custom_format_when_renaming(
            data: object,
        ) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_custom_format_when_renaming = (
            _parse_include_custom_format_when_renaming(
                d.pop("includeCustomFormatWhenRenaming", UNSET)
            )
        )

        custom_format_bulk_resource = cls(
            ids=ids,
            include_custom_format_when_renaming=include_custom_format_when_renaming,
        )

        return custom_format_bulk_resource
