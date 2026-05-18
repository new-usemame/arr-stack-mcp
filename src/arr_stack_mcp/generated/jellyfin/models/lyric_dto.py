from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lyric_line import LyricLine
    from ..models.lyric_metadata import LyricMetadata


T = TypeVar("T", bound="LyricDto")


@_attrs_define
class LyricDto:
    """LyricResponse model.

    Attributes:
        metadata (Union[Unset, LyricMetadata]): LyricMetadata model.
        lyrics (Union[Unset, list['LyricLine']]): Gets or sets a collection of individual lyric lines.
    """

    metadata: Union[Unset, "LyricMetadata"] = UNSET
    lyrics: Union[Unset, list["LyricLine"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        lyrics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lyrics, Unset):
            lyrics = []
            for lyrics_item_data in self.lyrics:
                lyrics_item = lyrics_item_data.to_dict()
                lyrics.append(lyrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["Metadata"] = metadata
        if lyrics is not UNSET:
            field_dict["Lyrics"] = lyrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lyric_line import LyricLine
        from ..models.lyric_metadata import LyricMetadata

        d = dict(src_dict)
        _metadata = d.pop("Metadata", UNSET)
        metadata: Union[Unset, LyricMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = LyricMetadata.from_dict(_metadata)

        lyrics = []
        _lyrics = d.pop("Lyrics", UNSET)
        for lyrics_item_data in _lyrics or []:
            lyrics_item = LyricLine.from_dict(lyrics_item_data)

            lyrics.append(lyrics_item)

        lyric_dto = cls(
            metadata=metadata,
            lyrics=lyrics,
        )

        return lyric_dto
