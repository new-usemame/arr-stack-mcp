from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.write_audio_tags_type import WriteAudioTagsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataProviderConfigResource")


@_attrs_define
class MetadataProviderConfigResource:
    """
    Attributes:
        id (Union[Unset, int]):
        metadata_source (Union[None, Unset, str]):
        write_audio_tags (Union[Unset, WriteAudioTagsType]):
        scrub_audio_tags (Union[Unset, bool]):
        embed_cover_art (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    metadata_source: Union[None, Unset, str] = UNSET
    write_audio_tags: Union[Unset, WriteAudioTagsType] = UNSET
    scrub_audio_tags: Union[Unset, bool] = UNSET
    embed_cover_art: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        metadata_source: Union[None, Unset, str]
        if isinstance(self.metadata_source, Unset):
            metadata_source = UNSET
        else:
            metadata_source = self.metadata_source

        write_audio_tags: Union[Unset, str] = UNSET
        if not isinstance(self.write_audio_tags, Unset):
            write_audio_tags = self.write_audio_tags.value

        scrub_audio_tags = self.scrub_audio_tags

        embed_cover_art = self.embed_cover_art

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if metadata_source is not UNSET:
            field_dict["metadataSource"] = metadata_source
        if write_audio_tags is not UNSET:
            field_dict["writeAudioTags"] = write_audio_tags
        if scrub_audio_tags is not UNSET:
            field_dict["scrubAudioTags"] = scrub_audio_tags
        if embed_cover_art is not UNSET:
            field_dict["embedCoverArt"] = embed_cover_art

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_metadata_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        metadata_source = _parse_metadata_source(d.pop("metadataSource", UNSET))

        _write_audio_tags = d.pop("writeAudioTags", UNSET)
        write_audio_tags: Union[Unset, WriteAudioTagsType]
        if isinstance(_write_audio_tags, Unset):
            write_audio_tags = UNSET
        else:
            write_audio_tags = WriteAudioTagsType(_write_audio_tags)

        scrub_audio_tags = d.pop("scrubAudioTags", UNSET)

        embed_cover_art = d.pop("embedCoverArt", UNSET)

        metadata_provider_config_resource = cls(
            id=id,
            metadata_source=metadata_source,
            write_audio_tags=write_audio_tags,
            scrub_audio_tags=scrub_audio_tags,
            embed_cover_art=embed_cover_art,
        )

        return metadata_provider_config_resource
