import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.download_protocol import DownloadProtocol
from ..models.indexer_privacy import IndexerPrivacy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field
    from ..models.indexer_capability_resource import IndexerCapabilityResource
    from ..models.indexer_status_resource import IndexerStatusResource
    from ..models.provider_message import ProviderMessage


T = TypeVar("T", bound="IndexerResource")


@_attrs_define
class IndexerResource:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[None, Unset, str]):
        fields (Union[None, Unset, list['Field']]):
        implementation_name (Union[None, Unset, str]):
        implementation (Union[None, Unset, str]):
        config_contract (Union[None, Unset, str]):
        info_link (Union[None, Unset, str]):
        message (Union[Unset, ProviderMessage]):
        tags (Union[None, Unset, list[int]]):
        presets (Union[None, Unset, list['IndexerResource']]):
        indexer_urls (Union[None, Unset, list[str]]):
        legacy_urls (Union[None, Unset, list[str]]):
        definition_name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        language (Union[None, Unset, str]):
        encoding (Union[None, Unset, str]):
        enable (Union[Unset, bool]):
        redirect (Union[Unset, bool]):
        supports_rss (Union[Unset, bool]):
        supports_search (Union[Unset, bool]):
        supports_redirect (Union[Unset, bool]):
        supports_pagination (Union[Unset, bool]):
        app_profile_id (Union[Unset, int]):
        protocol (Union[Unset, DownloadProtocol]):
        privacy (Union[Unset, IndexerPrivacy]):
        capabilities (Union[Unset, IndexerCapabilityResource]):
        priority (Union[Unset, int]):
        download_client_id (Union[Unset, int]):
        added (Union[Unset, datetime.datetime]):
        status (Union[Unset, IndexerStatusResource]):
        sort_name (Union[None, Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    fields: Union[None, Unset, list["Field"]] = UNSET
    implementation_name: Union[None, Unset, str] = UNSET
    implementation: Union[None, Unset, str] = UNSET
    config_contract: Union[None, Unset, str] = UNSET
    info_link: Union[None, Unset, str] = UNSET
    message: Union[Unset, "ProviderMessage"] = UNSET
    tags: Union[None, Unset, list[int]] = UNSET
    presets: Union[None, Unset, list["IndexerResource"]] = UNSET
    indexer_urls: Union[None, Unset, list[str]] = UNSET
    legacy_urls: Union[None, Unset, list[str]] = UNSET
    definition_name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    language: Union[None, Unset, str] = UNSET
    encoding: Union[None, Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    redirect: Union[Unset, bool] = UNSET
    supports_rss: Union[Unset, bool] = UNSET
    supports_search: Union[Unset, bool] = UNSET
    supports_redirect: Union[Unset, bool] = UNSET
    supports_pagination: Union[Unset, bool] = UNSET
    app_profile_id: Union[Unset, int] = UNSET
    protocol: Union[Unset, DownloadProtocol] = UNSET
    privacy: Union[Unset, IndexerPrivacy] = UNSET
    capabilities: Union[Unset, "IndexerCapabilityResource"] = UNSET
    priority: Union[Unset, int] = UNSET
    download_client_id: Union[Unset, int] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, "IndexerStatusResource"] = UNSET
    sort_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        implementation_name: Union[None, Unset, str]
        if isinstance(self.implementation_name, Unset):
            implementation_name = UNSET
        else:
            implementation_name = self.implementation_name

        implementation: Union[None, Unset, str]
        if isinstance(self.implementation, Unset):
            implementation = UNSET
        else:
            implementation = self.implementation

        config_contract: Union[None, Unset, str]
        if isinstance(self.config_contract, Unset):
            config_contract = UNSET
        else:
            config_contract = self.config_contract

        info_link: Union[None, Unset, str]
        if isinstance(self.info_link, Unset):
            info_link = UNSET
        else:
            info_link = self.info_link

        message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        tags: Union[None, Unset, list[int]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

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

        indexer_urls: Union[None, Unset, list[str]]
        if isinstance(self.indexer_urls, Unset):
            indexer_urls = UNSET
        elif isinstance(self.indexer_urls, list):
            indexer_urls = self.indexer_urls

        else:
            indexer_urls = self.indexer_urls

        legacy_urls: Union[None, Unset, list[str]]
        if isinstance(self.legacy_urls, Unset):
            legacy_urls = UNSET
        elif isinstance(self.legacy_urls, list):
            legacy_urls = self.legacy_urls

        else:
            legacy_urls = self.legacy_urls

        definition_name: Union[None, Unset, str]
        if isinstance(self.definition_name, Unset):
            definition_name = UNSET
        else:
            definition_name = self.definition_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        encoding: Union[None, Unset, str]
        if isinstance(self.encoding, Unset):
            encoding = UNSET
        else:
            encoding = self.encoding

        enable = self.enable

        redirect = self.redirect

        supports_rss = self.supports_rss

        supports_search = self.supports_search

        supports_redirect = self.supports_redirect

        supports_pagination = self.supports_pagination

        app_profile_id = self.app_profile_id

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        privacy: Union[Unset, str] = UNSET
        if not isinstance(self.privacy, Unset):
            privacy = self.privacy.value

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        priority = self.priority

        download_client_id = self.download_client_id

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        sort_name: Union[None, Unset, str]
        if isinstance(self.sort_name, Unset):
            sort_name = UNSET
        else:
            sort_name = self.sort_name

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if fields is not UNSET:
            field_dict["fields"] = fields
        if implementation_name is not UNSET:
            field_dict["implementationName"] = implementation_name
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if config_contract is not UNSET:
            field_dict["configContract"] = config_contract
        if info_link is not UNSET:
            field_dict["infoLink"] = info_link
        if message is not UNSET:
            field_dict["message"] = message
        if tags is not UNSET:
            field_dict["tags"] = tags
        if presets is not UNSET:
            field_dict["presets"] = presets
        if indexer_urls is not UNSET:
            field_dict["indexerUrls"] = indexer_urls
        if legacy_urls is not UNSET:
            field_dict["legacyUrls"] = legacy_urls
        if definition_name is not UNSET:
            field_dict["definitionName"] = definition_name
        if description is not UNSET:
            field_dict["description"] = description
        if language is not UNSET:
            field_dict["language"] = language
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if enable is not UNSET:
            field_dict["enable"] = enable
        if redirect is not UNSET:
            field_dict["redirect"] = redirect
        if supports_rss is not UNSET:
            field_dict["supportsRss"] = supports_rss
        if supports_search is not UNSET:
            field_dict["supportsSearch"] = supports_search
        if supports_redirect is not UNSET:
            field_dict["supportsRedirect"] = supports_redirect
        if supports_pagination is not UNSET:
            field_dict["supportsPagination"] = supports_pagination
        if app_profile_id is not UNSET:
            field_dict["appProfileId"] = app_profile_id
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if privacy is not UNSET:
            field_dict["privacy"] = privacy
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if priority is not UNSET:
            field_dict["priority"] = priority
        if download_client_id is not UNSET:
            field_dict["downloadClientId"] = download_client_id
        if added is not UNSET:
            field_dict["added"] = added
        if status is not UNSET:
            field_dict["status"] = status
        if sort_name is not UNSET:
            field_dict["sortName"] = sort_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field import Field
        from ..models.indexer_capability_resource import IndexerCapabilityResource
        from ..models.indexer_status_resource import IndexerStatusResource
        from ..models.provider_message import ProviderMessage

        # ARRSTACK_FROM_DICT_NONE_OK — upstream may return null for a
        # nullable nested object; treat it as 'no fields supplied'.
        if src_dict is None:
            return cls()
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_implementation_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation_name = _parse_implementation_name(
            d.pop("implementationName", UNSET)
        )

        def _parse_implementation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        implementation = _parse_implementation(d.pop("implementation", UNSET))

        def _parse_config_contract(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        config_contract = _parse_config_contract(d.pop("configContract", UNSET))

        def _parse_info_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_link = _parse_info_link(d.pop("infoLink", UNSET))

        _message = d.pop("message", UNSET)
        message: Union[Unset, ProviderMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = ProviderMessage.from_dict(_message)

        def _parse_tags(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_presets(data: object) -> Union[None, Unset, list["IndexerResource"]]:
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
                    presets_type_0_item = IndexerResource.from_dict(
                        presets_type_0_item_data
                    )

                    presets_type_0.append(presets_type_0_item)

                return presets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["IndexerResource"]], data)

        presets = _parse_presets(d.pop("presets", UNSET))

        def _parse_indexer_urls(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indexer_urls_type_0 = cast(list[str], data)

                return indexer_urls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        indexer_urls = _parse_indexer_urls(d.pop("indexerUrls", UNSET))

        def _parse_legacy_urls(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                legacy_urls_type_0 = cast(list[str], data)

                return legacy_urls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        legacy_urls = _parse_legacy_urls(d.pop("legacyUrls", UNSET))

        def _parse_definition_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        definition_name = _parse_definition_name(d.pop("definitionName", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_language(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_encoding(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        encoding = _parse_encoding(d.pop("encoding", UNSET))

        enable = d.pop("enable", UNSET)

        redirect = d.pop("redirect", UNSET)

        supports_rss = d.pop("supportsRss", UNSET)

        supports_search = d.pop("supportsSearch", UNSET)

        supports_redirect = d.pop("supportsRedirect", UNSET)

        supports_pagination = d.pop("supportsPagination", UNSET)

        app_profile_id = d.pop("appProfileId", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, DownloadProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = DownloadProtocol(_protocol)

        _privacy = d.pop("privacy", UNSET)
        privacy: Union[Unset, IndexerPrivacy]
        if isinstance(_privacy, Unset):
            privacy = UNSET
        else:
            privacy = IndexerPrivacy(_privacy)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, IndexerCapabilityResource]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = IndexerCapabilityResource.from_dict(_capabilities)

        priority = d.pop("priority", UNSET)

        download_client_id = d.pop("downloadClientId", UNSET)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IndexerStatusResource]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IndexerStatusResource.from_dict(_status)

        def _parse_sort_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sort_name = _parse_sort_name(d.pop("sortName", UNSET))

        indexer_resource = cls(
            id=id,
            name=name,
            fields=fields,
            implementation_name=implementation_name,
            implementation=implementation,
            config_contract=config_contract,
            info_link=info_link,
            message=message,
            tags=tags,
            presets=presets,
            indexer_urls=indexer_urls,
            legacy_urls=legacy_urls,
            definition_name=definition_name,
            description=description,
            language=language,
            encoding=encoding,
            enable=enable,
            redirect=redirect,
            supports_rss=supports_rss,
            supports_search=supports_search,
            supports_redirect=supports_redirect,
            supports_pagination=supports_pagination,
            app_profile_id=app_profile_id,
            protocol=protocol,
            privacy=privacy,
            capabilities=capabilities,
            priority=priority,
            download_client_id=download_client_id,
            added=added,
            status=status,
            sort_name=sort_name,
        )

        return indexer_resource
