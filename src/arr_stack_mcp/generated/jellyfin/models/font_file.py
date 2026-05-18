import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FontFile")


@_attrs_define
class FontFile:
    """Class FontFile.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        size (Union[Unset, int]): Gets or sets the size.
        date_created (Union[Unset, datetime.datetime]): Gets or sets the date created.
        date_modified (Union[Unset, datetime.datetime]): Gets or sets the date modified.
    """

    name: Union[None, Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_modified: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        size = self.size

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: Union[Unset, str] = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if size is not UNSET:
            field_dict["Size"] = size
        if date_created is not UNSET:
            field_dict["DateCreated"] = date_created
        if date_modified is not UNSET:
            field_dict["DateModified"] = date_modified

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("Name", UNSET))

        size = d.pop("Size", UNSET)

        _date_created = d.pop("DateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_modified = d.pop("DateModified", UNSET)
        date_modified: Union[Unset, datetime.datetime]
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        font_file = cls(
            name=name,
            size=size,
            date_created=date_created,
            date_modified=date_modified,
        )

        return font_file
