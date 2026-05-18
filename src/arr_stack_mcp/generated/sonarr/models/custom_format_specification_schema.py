from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field


T = TypeVar("T", bound="CustomFormatSpecificationSchema")


@_attrs_define
class CustomFormatSpecificationSchema:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        implementation (Union[None, Unset, str]):
        implementation_name (Union[None, Unset, str]):
        info_link (Union[None, Unset, str]):
        negate (Union[Unset, bool]):
        required (Union[Unset, bool]):
        fields (Union[None, Unset, list['Field']]):
        presets (Union[None, Unset, list['CustomFormatSpecificationSchema']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    implementation: Union[None, Unset, str] = UNSET
    implementation_name: Union[None, Unset, str] = UNSET
    info_link: Union[None, Unset, str] = UNSET
    negate: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    fields: Union[None, Unset, list["Field"]] = UNSET
    presets: Union[None, Unset, list["CustomFormatSpecificationSchema"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        implementation: Union[None, Unset, str]
        if isinstance(self.implementation, Unset):
            implementation = UNSET
        else:
            implementation = self.implementation

        implementation_name: Union[None, Unset, str]
        if isinstance(self.implementation_name, Unset):
            implementation_name = UNSET
        else:
            implementation_name = self.implementation_name

        info_link: Union[None, Unset, str]
        if isinstance(self.info_link, Unset):
            info_link = UNSET
        else:
            info_link = self.info_link

        negate = self.negate

        required = self.required

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

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if implementation_name is not UNSET:
            field_dict["implementationName"] = implementation_name
        if info_link is not UNSET:
            field_dict["infoLink"] = info_link
        if negate is not UNSET:
            field_dict["negate"] = negate
        if required is not UNSET:
            field_dict["required"] = required
        if fields is not UNSET:
            field_dict["fields"] = fields
        if presets is not UNSET:
            field_dict["presets"] = presets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field import Field

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_implementation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation = _parse_implementation(d.pop("implementation", UNSET))

        def _parse_implementation_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation_name = _parse_implementation_name(
            d.pop("implementationName", UNSET)
        )

        def _parse_info_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_link = _parse_info_link(d.pop("infoLink", UNSET))

        negate = d.pop("negate", UNSET)

        required = d.pop("required", UNSET)

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

        def _parse_presets(
            data: object,
        ) -> Union[None, Unset, list["CustomFormatSpecificationSchema"]]:
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
                    presets_type_0_item = CustomFormatSpecificationSchema.from_dict(
                        presets_type_0_item_data
                    )

                    presets_type_0.append(presets_type_0_item)

                return presets_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["CustomFormatSpecificationSchema"]], data
            )

        presets = _parse_presets(d.pop("presets", UNSET))

        custom_format_specification_schema = cls(
            id=id,
            name=name,
            implementation=implementation,
            implementation_name=implementation_name,
            info_link=info_link,
            negate=negate,
            required=required,
            fields=fields,
            presets=presets,
        )

        return custom_format_specification_schema
