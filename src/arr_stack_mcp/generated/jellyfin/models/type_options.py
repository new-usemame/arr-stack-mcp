from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_option import ImageOption


T = TypeVar("T", bound="TypeOptions")


@_attrs_define
class TypeOptions:
    """
    Attributes:
        type_ (Union[None, Unset, str]):
        metadata_fetchers (Union[None, Unset, list[str]]):
        metadata_fetcher_order (Union[None, Unset, list[str]]):
        image_fetchers (Union[None, Unset, list[str]]):
        image_fetcher_order (Union[None, Unset, list[str]]):
        image_options (Union[None, Unset, list['ImageOption']]):
    """

    type_: Union[None, Unset, str] = UNSET
    metadata_fetchers: Union[None, Unset, list[str]] = UNSET
    metadata_fetcher_order: Union[None, Unset, list[str]] = UNSET
    image_fetchers: Union[None, Unset, list[str]] = UNSET
    image_fetcher_order: Union[None, Unset, list[str]] = UNSET
    image_options: Union[None, Unset, list["ImageOption"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        metadata_fetchers: Union[None, Unset, list[str]]
        if isinstance(self.metadata_fetchers, Unset):
            metadata_fetchers = UNSET
        elif isinstance(self.metadata_fetchers, list):
            metadata_fetchers = self.metadata_fetchers

        else:
            metadata_fetchers = self.metadata_fetchers

        metadata_fetcher_order: Union[None, Unset, list[str]]
        if isinstance(self.metadata_fetcher_order, Unset):
            metadata_fetcher_order = UNSET
        elif isinstance(self.metadata_fetcher_order, list):
            metadata_fetcher_order = self.metadata_fetcher_order

        else:
            metadata_fetcher_order = self.metadata_fetcher_order

        image_fetchers: Union[None, Unset, list[str]]
        if isinstance(self.image_fetchers, Unset):
            image_fetchers = UNSET
        elif isinstance(self.image_fetchers, list):
            image_fetchers = self.image_fetchers

        else:
            image_fetchers = self.image_fetchers

        image_fetcher_order: Union[None, Unset, list[str]]
        if isinstance(self.image_fetcher_order, Unset):
            image_fetcher_order = UNSET
        elif isinstance(self.image_fetcher_order, list):
            image_fetcher_order = self.image_fetcher_order

        else:
            image_fetcher_order = self.image_fetcher_order

        image_options: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.image_options, Unset):
            image_options = UNSET
        elif isinstance(self.image_options, list):
            image_options = []
            for image_options_type_0_item_data in self.image_options:
                image_options_type_0_item = image_options_type_0_item_data.to_dict()
                image_options.append(image_options_type_0_item)

        else:
            image_options = self.image_options

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if metadata_fetchers is not UNSET:
            field_dict["MetadataFetchers"] = metadata_fetchers
        if metadata_fetcher_order is not UNSET:
            field_dict["MetadataFetcherOrder"] = metadata_fetcher_order
        if image_fetchers is not UNSET:
            field_dict["ImageFetchers"] = image_fetchers
        if image_fetcher_order is not UNSET:
            field_dict["ImageFetcherOrder"] = image_fetcher_order
        if image_options is not UNSET:
            field_dict["ImageOptions"] = image_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_option import ImageOption

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_metadata_fetchers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_fetchers_type_0 = cast(list[str], data)

                return metadata_fetchers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        metadata_fetchers = _parse_metadata_fetchers(d.pop("MetadataFetchers", UNSET))

        def _parse_metadata_fetcher_order(
            data: object,
        ) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metadata_fetcher_order_type_0 = cast(list[str], data)

                return metadata_fetcher_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        metadata_fetcher_order = _parse_metadata_fetcher_order(
            d.pop("MetadataFetcherOrder", UNSET)
        )

        def _parse_image_fetchers(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_fetchers_type_0 = cast(list[str], data)

                return image_fetchers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        image_fetchers = _parse_image_fetchers(d.pop("ImageFetchers", UNSET))

        def _parse_image_fetcher_order(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_fetcher_order_type_0 = cast(list[str], data)

                return image_fetcher_order_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        image_fetcher_order = _parse_image_fetcher_order(
            d.pop("ImageFetcherOrder", UNSET)
        )

        def _parse_image_options(
            data: object,
        ) -> Union[None, Unset, list["ImageOption"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_options_type_0 = []
                _image_options_type_0 = data
                for image_options_type_0_item_data in _image_options_type_0:
                    image_options_type_0_item = ImageOption.from_dict(
                        image_options_type_0_item_data
                    )

                    image_options_type_0.append(image_options_type_0_item)

                return image_options_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ImageOption"]], data)

        image_options = _parse_image_options(d.pop("ImageOptions", UNSET))

        type_options = cls(
            type_=type_,
            metadata_fetchers=metadata_fetchers,
            metadata_fetcher_order=metadata_fetcher_order,
            image_fetchers=image_fetchers,
            image_fetcher_order=image_fetcher_order,
            image_options=image_options,
        )

        return type_options
