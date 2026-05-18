from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    channel_ids: Union[Unset, list[UUID]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_filters: Union[Unset, list[str]] = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    json_channel_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(channel_ids, Unset):
        json_channel_ids = []
        for channel_ids_item_data in channel_ids:
            channel_ids_item = str(channel_ids_item_data)
            json_channel_ids.append(channel_ids_item)

    params["channelIds"] = json_channel_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Channels/Items/Latest",
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
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    channel_ids: Union[Unset, list[UUID]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        filters (Union[Unset, list[ItemFilter]]):
        fields (Union[Unset, list[ItemFields]]):
        channel_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    channel_ids: Union[Unset, list[UUID]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        filters (Union[Unset, list[ItemFilter]]):
        fields (Union[Unset, list[ItemFields]]):
        channel_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    channel_ids: Union[Unset, list[UUID]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        filters (Union[Unset, list[ItemFilter]]):
        fields (Union[Unset, list[ItemFields]]):
        channel_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        filters=filters,
        fields=fields,
        channel_ids=channel_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    start_index: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    filters: Union[Unset, list[ItemFilter]] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    channel_ids: Union[Unset, list[UUID]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets latest channel items.

    Args:
        user_id (Union[Unset, UUID]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        filters (Union[Unset, list[ItemFilter]]):
        fields (Union[Unset, list[ItemFields]]):
        channel_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            filters=filters,
            fields=fields,
            channel_ids=channel_ids,
        )
    ).parsed
