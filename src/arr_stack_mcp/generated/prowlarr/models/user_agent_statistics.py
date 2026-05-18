from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAgentStatistics")


@_attrs_define
class UserAgentStatistics:
    """
    Attributes:
        user_agent (Union[None, Unset, str]):
        number_of_queries (Union[Unset, int]):
        number_of_grabs (Union[Unset, int]):
    """

    user_agent: Union[None, Unset, str] = UNSET
    number_of_queries: Union[Unset, int] = UNSET
    number_of_grabs: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_agent: Union[None, Unset, str]
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        number_of_queries = self.number_of_queries

        number_of_grabs = self.number_of_grabs

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if number_of_queries is not UNSET:
            field_dict["numberOfQueries"] = number_of_queries
        if number_of_grabs is not UNSET:
            field_dict["numberOfGrabs"] = number_of_grabs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict):
        # ARRSTACK_FROM_DICT_NONE_OK
        if src_dict is None:
            return cls()
        d = dict(src_dict)

        def _parse_user_agent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_agent = _parse_user_agent(d.pop("userAgent", UNSET))

        number_of_queries = d.pop("numberOfQueries", UNSET)

        number_of_grabs = d.pop("numberOfGrabs", UNSET)

        user_agent_statistics = cls(
            user_agent=user_agent,
            number_of_queries=number_of_queries,
            number_of_grabs=number_of_grabs,
        )

        return user_agent_statistics
