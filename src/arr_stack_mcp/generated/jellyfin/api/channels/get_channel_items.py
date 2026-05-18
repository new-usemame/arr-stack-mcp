from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...models.item_sort_by import ItemSortBy
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: UUID,
    *,
    folder_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, list[SortOrder]] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    sort_by: Union[Unset, list[ItemSortBy]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_folder_id: Union[Unset, str] = UNSET
    if not isinstance(folder_id, Unset):
        json_folder_id = str(folder_id)
    params["folderId"] = json_folder_id

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_sort_order: Union[Unset, list[str]] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    json_filters: Union[Unset, list[str]] = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    json_sort_by: Union[Unset, list[str]] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = []
        for sort_by_item_data in sort_by:
            sort_by_item = sort_by_item_data.value
            json_sort_by.append(sort_by_item)

    params["sortBy"] = json_sort_by

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Channels/{channel_id}/Items".format(
            channel_id=channel_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == 200:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, list[SortOrder]] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    sort_by: Union[Unset, list[ItemSortBy]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, list[SortOrder]]):
        filters (Union[Unset, list[ItemFilter]]):
        sort_by (Union[Unset, list[ItemSortBy]]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, list[SortOrder]] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    sort_by: Union[Unset, list[ItemSortBy]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, list[SortOrder]]):
        filters (Union[Unset, list[ItemFilter]]):
        sort_by (Union[Unset, list[ItemSortBy]]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, list[SortOrder]] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    sort_by: Union[Unset, list[ItemSortBy]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, list[SortOrder]]):
        filters (Union[Unset, list[ItemFilter]]):
        sort_by (Union[Unset, list[ItemSortBy]]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: UUID,
    *,
    client: AuthenticatedClient,
    folder_id: Union[Unset, UUID] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort_order: Union[Unset, list[SortOrder]] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    sort_by: Union[Unset, list[ItemSortBy]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get channel items.

    Args:
        channel_id (UUID):
        folder_id (Union[Unset, UUID]):
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, list[SortOrder]]):
        filters (Union[Unset, list[ItemFilter]]):
        sort_by (Union[Unset, list[ItemSortBy]]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            folder_id=folder_id,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            sort_order=sort_order,
            filters=filters,
            sort_by=sort_by,
            fields=fields,
        )
    ).parsed
