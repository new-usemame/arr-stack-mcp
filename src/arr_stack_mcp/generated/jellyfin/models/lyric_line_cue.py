from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LyricLineCue")


@_attrs_define
class LyricLineCue:
    """LyricLineCue model, holds information about the timing of words within a LyricLine.

    Attributes:
        position (Union[Unset, int]): Gets the start character index of the cue.
        end_position (Union[Unset, int]): Gets the end character index of the cue.
        start (Union[Unset, int]): Gets the timestamp the lyric is synced to in ticks.
        end (Union[None, Unset, int]): Gets the end timestamp the lyric is synced to in ticks.
    """

    position: Union[Unset, int] = UNSET
    end_position: Union[Unset, int] = UNSET
    start: Union[Unset, int] = UNSET
    end: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        end_position = self.end_position

        start = self.start

        end: Union[None, Unset, int]
        if isinstance(self.end, Unset):
            end = UNSET
        else:
            end = self.end

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if position is not UNSET:
            field_dict["Position"] = position
        if end_position is not UNSET:
            field_dict["EndPosition"] = end_position
        if start is not UNSET:
            field_dict["Start"] = start
        if end is not UNSET:
            field_dict["End"] = end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("Position", UNSET)

        end_position = d.pop("EndPosition", UNSET)

        start = d.pop("Start", UNSET)

        def _parse_end(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        end = _parse_end(d.pop("End", UNSET))

        lyric_line_cue = cls(
            position=position,
            end_position=end_position,
            start=start,
            end=end,
        )

        return lyric_line_cue
