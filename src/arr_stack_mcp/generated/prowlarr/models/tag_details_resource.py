from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagDetailsResource")


@_attrs_define
class TagDetailsResource:
    """
    Attributes:
        id (Union[Unset, int]):
        label (Union[None, Unset, str]):
        notification_ids (Union[None, Unset, list[int]]):
        indexer_ids (Union[None, Unset, list[int]]):
        indexer_proxy_ids (Union[None, Unset, list[int]]):
        application_ids (Union[None, Unset, list[int]]):
    """

    id: Union[Unset, int] = UNSET
    label: Union[None, Unset, str] = UNSET
    notification_ids: Union[None, Unset, list[int]] = UNSET
    indexer_ids: Union[None, Unset, list[int]] = UNSET
    indexer_proxy_ids: Union[None, Unset, list[int]] = UNSET
    application_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        notification_ids: Union[None, Unset, list[int]]
        if isinstance(self.notification_ids, Unset):
            notification_ids = UNSET
        elif isinstance(self.notification_ids, list):
            notification_ids = self.notification_ids

        else:
            notification_ids = self.notification_ids

        indexer_ids: Union[None, Unset, list[int]]
        if isinstance(self.indexer_ids, Unset):
            indexer_ids = UNSET
        elif isinstance(self.indexer_ids, list):
            indexer_ids = self.indexer_ids

        else:
            indexer_ids = self.indexer_ids

        indexer_proxy_ids: Union[None, Unset, list[int]]
        if isinstance(self.indexer_proxy_ids, Unset):
            indexer_proxy_ids = UNSET
        elif isinstance(self.indexer_proxy_ids, list):
            indexer_proxy_ids = self.indexer_proxy_ids

        else:
            indexer_proxy_ids = self.indexer_proxy_ids

        application_ids: Union[None, Unset, list[int]]
        if isinstance(self.application_ids, Unset):
            application_ids = UNSET
        elif isinstance(self.application_ids, list):
            application_ids = self.application_ids

        else:
            application_ids = self.application_ids

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if notification_ids is not UNSET:
            field_dict["notificationIds"] = notification_ids
        if indexer_ids is not UNSET:
            field_dict["indexerIds"] = indexer_ids
        if indexer_proxy_ids is not UNSET:
            field_dict["indexerProxyIds"] = indexer_proxy_ids
        if application_ids is not UNSET:
            field_dict["applicationIds"] = application_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_notification_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_ids_type_0 = cast(list[int], data)

                return notification_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        notification_ids = _parse_notification_ids(d.pop("notificationIds", UNSET))

        def _parse_indexer_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indexer_ids_type_0 = cast(list[int], data)

                return indexer_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        indexer_ids = _parse_indexer_ids(d.pop("indexerIds", UNSET))

        def _parse_indexer_proxy_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                indexer_proxy_ids_type_0 = cast(list[int], data)

                return indexer_proxy_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        indexer_proxy_ids = _parse_indexer_proxy_ids(d.pop("indexerProxyIds", UNSET))

        def _parse_application_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                application_ids_type_0 = cast(list[int], data)

                return application_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        application_ids = _parse_application_ids(d.pop("applicationIds", UNSET))

        tag_details_resource = cls(
            id=id,
            label=label,
            notification_ids=notification_ids,
            indexer_ids=indexer_ids,
            indexer_proxy_ids=indexer_proxy_ids,
            application_ids=application_ids,
        )

        return tag_details_resource
