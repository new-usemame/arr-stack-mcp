from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueStatusResource")


@_attrs_define
class QueueStatusResource:
    """
    Attributes:
        id (Union[Unset, int]):
        total_count (Union[Unset, int]):
        count (Union[Unset, int]):
        unknown_count (Union[Unset, int]):
        errors (Union[Unset, bool]):
        warnings (Union[Unset, bool]):
        unknown_errors (Union[Unset, bool]):
        unknown_warnings (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    total_count: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    unknown_count: Union[Unset, int] = UNSET
    errors: Union[Unset, bool] = UNSET
    warnings: Union[Unset, bool] = UNSET
    unknown_errors: Union[Unset, bool] = UNSET
    unknown_warnings: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        total_count = self.total_count

        count = self.count

        unknown_count = self.unknown_count

        errors = self.errors

        warnings = self.warnings

        unknown_errors = self.unknown_errors

        unknown_warnings = self.unknown_warnings

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if count is not UNSET:
            field_dict["count"] = count
        if unknown_count is not UNSET:
            field_dict["unknownCount"] = unknown_count
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if unknown_errors is not UNSET:
            field_dict["unknownErrors"] = unknown_errors
        if unknown_warnings is not UNSET:
            field_dict["unknownWarnings"] = unknown_warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        total_count = d.pop("totalCount", UNSET)

        count = d.pop("count", UNSET)

        unknown_count = d.pop("unknownCount", UNSET)

        errors = d.pop("errors", UNSET)

        warnings = d.pop("warnings", UNSET)

        unknown_errors = d.pop("unknownErrors", UNSET)

        unknown_warnings = d.pop("unknownWarnings", UNSET)

        queue_status_resource = cls(
            id=id,
            total_count=total_count,
            count=count,
            unknown_count=unknown_count,
            errors=errors,
            warnings=warnings,
            unknown_errors=unknown_errors,
            unknown_warnings=unknown_warnings,
        )

        return queue_status_resource
