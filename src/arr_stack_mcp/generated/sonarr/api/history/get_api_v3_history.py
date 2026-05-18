from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.history_resource_paging_resource import HistoryResourcePagingResource
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_series: Union[Unset, bool] = UNSET,
    include_episode: Union[Unset, bool] = UNSET,
    event_type: Union[Unset, list[int]] = UNSET,
    episode_id: Union[Unset, int] = UNSET,
    download_id: Union[Unset, str] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sortKey"] = sort_key

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    params["includeSeries"] = include_series

    params["includeEpisode"] = include_episode

    json_event_type: Union[Unset, list[int]] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type

    params["eventType"] = json_event_type

    params["episodeId"] = episode_id

    params["downloadId"] = download_id

    json_series_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(series_ids, Unset):
        json_series_ids = series_ids

    params["seriesIds"] = json_series_ids

    json_languages: Union[Unset, list[int]] = UNSET
    if not isinstance(languages, Unset):
        json_languages = languages

    params["languages"] = json_languages

    json_quality: Union[Unset, list[int]] = UNSET
    if not isinstance(quality, Unset):
        json_quality = quality

    params["quality"] = json_quality

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HistoryResourcePagingResource]:
    if response.status_code == 200:
        response_200 = HistoryResourcePagingResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HistoryResourcePagingResource]:
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
    include_series: Union[Unset, bool] = UNSET,
    include_episode: Union[Unset, bool] = UNSET,
    event_type: Union[Unset, list[int]] = UNSET,
    episode_id: Union[Unset, int] = UNSET,
    download_id: Union[Unset, str] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Response[HistoryResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):
        include_episode (Union[Unset, bool]):
        event_type (Union[Unset, list[int]]):
        episode_id (Union[Unset, int]):
        download_id (Union[Unset, str]):
        series_ids (Union[Unset, list[int]]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HistoryResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_series=include_series,
        include_episode=include_episode,
        event_type=event_type,
        episode_id=episode_id,
        download_id=download_id,
        series_ids=series_ids,
        languages=languages,
        quality=quality,
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
    include_series: Union[Unset, bool] = UNSET,
    include_episode: Union[Unset, bool] = UNSET,
    event_type: Union[Unset, list[int]] = UNSET,
    episode_id: Union[Unset, int] = UNSET,
    download_id: Union[Unset, str] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Optional[HistoryResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):
        include_episode (Union[Unset, bool]):
        event_type (Union[Unset, list[int]]):
        episode_id (Union[Unset, int]):
        download_id (Union[Unset, str]):
        series_ids (Union[Unset, list[int]]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HistoryResourcePagingResource
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_series=include_series,
        include_episode=include_episode,
        event_type=event_type,
        episode_id=episode_id,
        download_id=download_id,
        series_ids=series_ids,
        languages=languages,
        quality=quality,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_series: Union[Unset, bool] = UNSET,
    include_episode: Union[Unset, bool] = UNSET,
    event_type: Union[Unset, list[int]] = UNSET,
    episode_id: Union[Unset, int] = UNSET,
    download_id: Union[Unset, str] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Response[HistoryResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):
        include_episode (Union[Unset, bool]):
        event_type (Union[Unset, list[int]]):
        episode_id (Union[Unset, int]):
        download_id (Union[Unset, str]):
        series_ids (Union[Unset, list[int]]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HistoryResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_series=include_series,
        include_episode=include_episode,
        event_type=event_type,
        episode_id=episode_id,
        download_id=download_id,
        series_ids=series_ids,
        languages=languages,
        quality=quality,
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
    include_series: Union[Unset, bool] = UNSET,
    include_episode: Union[Unset, bool] = UNSET,
    event_type: Union[Unset, list[int]] = UNSET,
    episode_id: Union[Unset, int] = UNSET,
    download_id: Union[Unset, str] = UNSET,
    series_ids: Union[Unset, list[int]] = UNSET,
    languages: Union[Unset, list[int]] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Optional[HistoryResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):
        include_episode (Union[Unset, bool]):
        event_type (Union[Unset, list[int]]):
        episode_id (Union[Unset, int]):
        download_id (Union[Unset, str]):
        series_ids (Union[Unset, list[int]]):
        languages (Union[Unset, list[int]]):
        quality (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HistoryResourcePagingResource
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            sort_key=sort_key,
            sort_direction=sort_direction,
            include_series=include_series,
            include_episode=include_episode,
            event_type=event_type,
            episode_id=episode_id,
            download_id=download_id,
            series_ids=series_ids,
            languages=languages,
            quality=quality,
        )
    ).parsed
