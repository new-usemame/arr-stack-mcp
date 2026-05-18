from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_statistics import HostStatistics
    from ..models.indexer_statistics import IndexerStatistics
    from ..models.user_agent_statistics import UserAgentStatistics


T = TypeVar("T", bound="IndexerStatsResource")


@_attrs_define
class IndexerStatsResource:
    """
    Attributes:
        id (Union[Unset, int]):
        indexers (Union[None, Unset, list['IndexerStatistics']]):
        user_agents (Union[None, Unset, list['UserAgentStatistics']]):
        hosts (Union[None, Unset, list['HostStatistics']]):
    """

    id: Union[Unset, int] = UNSET
    indexers: Union[None, Unset, list["IndexerStatistics"]] = UNSET
    user_agents: Union[None, Unset, list["UserAgentStatistics"]] = UNSET
    hosts: Union[None, Unset, list["HostStatistics"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        indexers: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.indexers, Unset):
            indexers = UNSET
        elif isinstance(self.indexers, list):
            indexers = []
            for indexers_type_0_item_data in self.indexers:
                indexers_type_0_item = indexers_type_0_item_data.to_dict()
                indexers.append(indexers_type_0_item)

        else:
            indexers = self.indexers

        user_agents: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.user_agents, Unset):
            user_agents = UNSET
        elif isinstance(self.user_agents, list):
            user_agents = []
            for user_agents_type_0_item_data in self.user_agents:
                user_agents_type_0_item = user_agents_type_0_item_data.to_dict()
                user_agents.append(user_agents_type_0_item)

        else:
            user_agents = self.user_agents

        hosts: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.hosts, Unset):
            hosts = UNSET
        elif isinstance(self.hosts, list):
            hosts = []
            for hosts_type_0_item_data in self.hosts:
                hosts_type_0_item = hosts_type_0_item_data.to_dict()
                hosts.append(hosts_type_0_item)

        else:
            hosts = self.hosts

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if indexers is not UNSET:
            field_dict["indexers"] = indexers
        if user_agents is not UNSET:
            field_dict["userAgents"] = user_agents
        if hosts is not UNSET:
            field_dict["hosts"] = hosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_statistics import HostStatistics
        from ..models.indexer_statistics import IndexerStatistics
        from ..models.user_agent_statistics import UserAgentStatistics

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_indexers(
            data: object,
        ) -> Union[None, Unset, list["IndexerStatistics"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indexers_type_0 = []
                _indexers_type_0 = data
                for indexers_type_0_item_data in _indexers_type_0:
                    indexers_type_0_item = IndexerStatistics.from_dict(
                        indexers_type_0_item_data
                    )

                    indexers_type_0.append(indexers_type_0_item)

                return indexers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IndexerStatistics"]], data)

        indexers = _parse_indexers(d.pop("indexers", UNSET))

        def _parse_user_agents(
            data: object,
        ) -> Union[None, Unset, list["UserAgentStatistics"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_agents_type_0 = []
                _user_agents_type_0 = data
                for user_agents_type_0_item_data in _user_agents_type_0:
                    user_agents_type_0_item = UserAgentStatistics.from_dict(
                        user_agents_type_0_item_data
                    )

                    user_agents_type_0.append(user_agents_type_0_item)

                return user_agents_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UserAgentStatistics"]], data)

        user_agents = _parse_user_agents(d.pop("userAgents", UNSET))

        def _parse_hosts(data: object) -> Union[None, Unset, list["HostStatistics"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hosts_type_0 = []
                _hosts_type_0 = data
                for hosts_type_0_item_data in _hosts_type_0:
                    hosts_type_0_item = HostStatistics.from_dict(hosts_type_0_item_data)

                    hosts_type_0.append(hosts_type_0_item)

                return hosts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["HostStatistics"]], data)

        hosts = _parse_hosts(d.pop("hosts", UNSET))

        indexer_stats_resource = cls(
            id=id,
            indexers=indexers,
            user_agents=user_agents,
            hosts=hosts,
        )

        return indexer_stats_resource
