from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_protocol import DownloadProtocol
from ...models.queue_resource_paging_resource import QueueResourcePagingResource
from ...models.queue_status import QueueStatus
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_unknown_series_items: Union[Unset, bool] = False,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[QueueStatus]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sortKey"] = sort_key

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    params["includeUnknownSeriesItems"] = include_unknown_series_items

    params["includeSeries"] = include_series

    params["includeEpisode"] = include_episode

    json_series_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(series_ids, Unset):
        json_series_ids = series_ids

    params["seriesIds"] = json_series_ids

    json_protocol: Union[Unset, str] = UNSET
    if not isinstance(protocol, Unset):
        json_protocol = protocol.value

    params["protocol"] = json_protocol

    json_languages: Union[Unset, list[int]] = UNSET
    if not isinstance(languages, Unset):
        json_languages = languages

    params["languages"] = json_languages

    json_quality: Union[Unset, list[int]] = UNSET
    if not isinstance(quality, Unset):
        json_quality = quality

    params["quality"] = json_quality

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/queue",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[QueueResourcePagingResource]:
    if response.status_code == 200:
        response_200 = QueueResourcePagingResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[QueueResourcePagingResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_unknown_series_items: Union[Unset, bool] = False,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[QueueStatus]] = UNSET,
) -> Response[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_series_items (Union[Unset, bool]):  Default: False.
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.
        series_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):
        status (Union[Unset, list[QueueStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueueResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_unknown_series_items=include_unknown_series_items,
        include_series=include_series,
        include_episode=include_episode,
        series_ids=series_ids,
        protocol=protocol,
        languages=languages,
        quality=quality,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_unknown_series_items: Union[Unset, bool] = False,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[QueueStatus]] = UNSET,
) -> Optional[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_series_items (Union[Unset, bool]):  Default: False.
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.
        series_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):
        status (Union[Unset, list[QueueStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueueResourcePagingResource
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_unknown_series_items=include_unknown_series_items,
        include_series=include_series,
        include_episode=include_episode,
        series_ids=series_ids,
        protocol=protocol,
        languages=languages,
        quality=quality,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_unknown_series_items: Union[Unset, bool] = False,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[QueueStatus]] = UNSET,
) -> Response[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_series_items (Union[Unset, bool]):  Default: False.
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.
        series_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):
        status (Union[Unset, list[QueueStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueueResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_unknown_series_items=include_unknown_series_items,
        include_series=include_series,
        include_episode=include_episode,
        series_ids=series_ids,
        protocol=protocol,
        languages=languages,
        quality=quality,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_unknown_series_items: Union[Unset, bool] = False,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
    series_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[QueueStatus]] = UNSET,
) -> Optional[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_series_items (Union[Unset, bool]):  Default: False.
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.
        series_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):
        status (Union[Unset, list[QueueStatus]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        QueueResourcePagingResource
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            sort_key=sort_key,
            sort_direction=sort_direction,
            include_unknown_series_items=include_unknown_series_items,
            include_series=include_series,
            include_episode=include_episode,
            series_ids=series_ids,
            protocol=protocol,
            languages=languages,
            quality=quality,
            status=status,
        )
    ).parsed
