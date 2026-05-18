from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lyric_line_cue import LyricLineCue


T = TypeVar("T", bound="LyricLine")


@_attrs_define
class LyricLine:
    """Lyric model.

    Attributes:
        text (Union[Unset, str]): Gets the text of this lyric line.
        start (Union[None, Unset, int]): Gets the start time in ticks.
        cues (Union[None, Unset, list['LyricLineCue']]): Gets the time-aligned cues for the song's lyrics.
    """

    text: Union[Unset, str] = UNSET
    start: Union[None, Unset, int] = UNSET
    cues: Union[None, Unset, list["LyricLineCue"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        start: Union[None, Unset, int]
        if isinstance(self.start, Unset):
            start = UNSET
        else:
            start = self.start

        cues: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.cues, Unset):
            cues = UNSET
        elif isinstance(self.cues, list):
            cues = []
            for cues_type_0_item_data in self.cues:
                cues_type_0_item = cues_type_0_item_data.to_dict()
                cues.append(cues_type_0_item)

        else:
            cues = self.cues

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if text is not UNSET:
            field_dict["Text"] = text
        if start is not UNSET:
            field_dict["Start"] = start
        if cues is not UNSET:
            field_dict["Cues"] = cues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lyric_line_cue import LyricLineCue

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        text = d.pop("Text", UNSET)

        def _parse_start(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        start = _parse_start(d.pop("Start", UNSET))

        def _parse_cues(data: object) -> Union[None, Unset, list["LyricLineCue"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cues_type_0 = []
                _cues_type_0 = data
                for cues_type_0_item_data in _cues_type_0:
                    cues_type_0_item = LyricLineCue.from_dict(cues_type_0_item_data)

                    cues_type_0.append(cues_type_0_item)

                return cues_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["LyricLineCue"]], data)

        cues = _parse_cues(d.pop("Cues", UNSET))

        lyric_line = cls(
            text=text,
            start=start,
            cues=cues,
        )

        return lyric_line
