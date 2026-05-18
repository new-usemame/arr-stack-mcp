from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.library_option_info_dto import LibraryOptionInfoDto
    from ..models.library_type_options_dto import LibraryTypeOptionsDto


T = TypeVar("T", bound="LibraryOptionsResultDto")


@_attrs_define
class LibraryOptionsResultDto:
    """Library options result dto.

    Attributes:
        metadata_savers (Union[Unset, list['LibraryOptionInfoDto']]): Gets or sets the metadata savers.
        metadata_readers (Union[Unset, list['LibraryOptionInfoDto']]): Gets or sets the metadata readers.
        subtitle_fetchers (Union[Unset, list['LibraryOptionInfoDto']]): Gets or sets the subtitle fetchers.
        lyric_fetchers (Union[Unset, list['LibraryOptionInfoDto']]): Gets or sets the list of lyric fetchers.
        media_segment_providers (Union[Unset, list['LibraryOptionInfoDto']]): Gets or sets the list of MediaSegment
            Providers.
        type_options (Union[Unset, list['LibraryTypeOptionsDto']]): Gets or sets the type options.
    """

    metadata_savers: Union[Unset, list["LibraryOptionInfoDto"]] = UNSET
    metadata_readers: Union[Unset, list["LibraryOptionInfoDto"]] = UNSET
    subtitle_fetchers: Union[Unset, list["LibraryOptionInfoDto"]] = UNSET
    lyric_fetchers: Union[Unset, list["LibraryOptionInfoDto"]] = UNSET
    media_segment_providers: Union[Unset, list["LibraryOptionInfoDto"]] = UNSET
    type_options: Union[Unset, list["LibraryTypeOptionsDto"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata_savers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_savers, Unset):
            metadata_savers = []
            for metadata_savers_item_data in self.metadata_savers:
                metadata_savers_item = metadata_savers_item_data.to_dict()
                metadata_savers.append(metadata_savers_item)

        metadata_readers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_readers, Unset):
            metadata_readers = []
            for metadata_readers_item_data in self.metadata_readers:
                metadata_readers_item = metadata_readers_item_data.to_dict()
                metadata_readers.append(metadata_readers_item)

        subtitle_fetchers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subtitle_fetchers, Unset):
            subtitle_fetchers = []
            for subtitle_fetchers_item_data in self.subtitle_fetchers:
                subtitle_fetchers_item = subtitle_fetchers_item_data.to_dict()
                subtitle_fetchers.append(subtitle_fetchers_item)

        lyric_fetchers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lyric_fetchers, Unset):
            lyric_fetchers = []
            for lyric_fetchers_item_data in self.lyric_fetchers:
                lyric_fetchers_item = lyric_fetchers_item_data.to_dict()
                lyric_fetchers.append(lyric_fetchers_item)

        media_segment_providers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.media_segment_providers, Unset):
            media_segment_providers = []
            for media_segment_providers_item_data in self.media_segment_providers:
                media_segment_providers_item = (
                    media_segment_providers_item_data.to_dict()
                )
                media_segment_providers.append(media_segment_providers_item)

        type_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.type_options, Unset):
            type_options = []
            for type_options_item_data in self.type_options:
                type_options_item = type_options_item_data.to_dict()
                type_options.append(type_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if metadata_savers is not UNSET:
            field_dict["MetadataSavers"] = metadata_savers
        if metadata_readers is not UNSET:
            field_dict["MetadataReaders"] = metadata_readers
        if subtitle_fetchers is not UNSET:
            field_dict["SubtitleFetchers"] = subtitle_fetchers
        if lyric_fetchers is not UNSET:
            field_dict["LyricFetchers"] = lyric_fetchers
        if media_segment_providers is not UNSET:
            field_dict["MediaSegmentProviders"] = media_segment_providers
        if type_options is not UNSET:
            field_dict["TypeOptions"] = type_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.library_option_info_dto import LibraryOptionInfoDto
        from ..models.library_type_options_dto import LibraryTypeOptionsDto

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        metadata_savers = []
        _metadata_savers = d.pop("MetadataSavers", UNSET)
        for metadata_savers_item_data in _metadata_savers or []:
            metadata_savers_item = LibraryOptionInfoDto.from_dict(
                metadata_savers_item_data
            )

            metadata_savers.append(metadata_savers_item)

        metadata_readers = []
        _metadata_readers = d.pop("MetadataReaders", UNSET)
        for metadata_readers_item_data in _metadata_readers or []:
            metadata_readers_item = LibraryOptionInfoDto.from_dict(
                metadata_readers_item_data
            )

            metadata_readers.append(metadata_readers_item)

        subtitle_fetchers = []
        _subtitle_fetchers = d.pop("SubtitleFetchers", UNSET)
        for subtitle_fetchers_item_data in _subtitle_fetchers or []:
            subtitle_fetchers_item = LibraryOptionInfoDto.from_dict(
                subtitle_fetchers_item_data
            )

            subtitle_fetchers.append(subtitle_fetchers_item)

        lyric_fetchers = []
        _lyric_fetchers = d.pop("LyricFetchers", UNSET)
        for lyric_fetchers_item_data in _lyric_fetchers or []:
            lyric_fetchers_item = LibraryOptionInfoDto.from_dict(
                lyric_fetchers_item_data
            )

            lyric_fetchers.append(lyric_fetchers_item)

        media_segment_providers = []
        _media_segment_providers = d.pop("MediaSegmentProviders", UNSET)
        for media_segment_providers_item_data in _media_segment_providers or []:
            media_segment_providers_item = LibraryOptionInfoDto.from_dict(
                media_segment_providers_item_data
            )

            media_segment_providers.append(media_segment_providers_item)

        type_options = []
        _type_options = d.pop("TypeOptions", UNSET)
        for type_options_item_data in _type_options or []:
            type_options_item = LibraryTypeOptionsDto.from_dict(type_options_item_data)

            type_options.append(type_options_item)

        library_options_result_dto = cls(
            metadata_savers=metadata_savers,
            metadata_readers=metadata_readers,
            subtitle_fetchers=subtitle_fetchers,
            lyric_fetchers=lyric_fetchers,
            media_segment_providers=media_segment_providers,
            type_options=type_options,
        )

        return library_options_result_dto
