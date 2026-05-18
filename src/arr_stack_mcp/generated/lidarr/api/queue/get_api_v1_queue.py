from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_protocol import DownloadProtocol
from ...models.queue_resource_paging_resource import QueueResourcePagingResource
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_unknown_artist_items: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = False,
    artist_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
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

    params["includeUnknownArtistItems"] = include_unknown_artist_items

    params["includeArtist"] = include_artist

    params["includeAlbum"] = include_album

    json_artist_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(artist_ids, Unset):
        json_artist_ids = artist_ids

    params["artistIds"] = json_artist_ids

    json_protocol: Union[Unset, str] = UNSET
    if not isinstance(protocol, Unset):
        json_protocol = protocol.value

    params["protocol"] = json_protocol

    json_quality: Union[Unset, list[int]] = UNSET
    if not isinstance(quality, Unset):
        json_quality = quality

    params["quality"] = json_quality

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/queue",
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
    include_unknown_artist_items: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = False,
    artist_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Response[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_artist_items (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: False.
        artist_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        quality (Union[Unset, list[int]]):

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
        include_unknown_artist_items=include_unknown_artist_items,
        include_artist=include_artist,
        include_album=include_album,
        artist_ids=artist_ids,
        protocol=protocol,
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
    include_unknown_artist_items: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = False,
    artist_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Optional[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_artist_items (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: False.
        artist_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        quality (Union[Unset, list[int]]):

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
        include_unknown_artist_items=include_unknown_artist_items,
        include_artist=include_artist,
        include_album=include_album,
        artist_ids=artist_ids,
        protocol=protocol,
        quality=quality,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_unknown_artist_items: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = False,
    artist_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Response[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_artist_items (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: False.
        artist_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        quality (Union[Unset, list[int]]):

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
        include_unknown_artist_items=include_unknown_artist_items,
        include_artist=include_artist,
        include_album=include_album,
        artist_ids=artist_ids,
        protocol=protocol,
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
    include_unknown_artist_items: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = False,
    artist_ids: Union[Unset, list[int]] = UNSET,
    protocol: Union[Unset, DownloadProtocol] = UNSET,
    quality: Union[Unset, list[int]] = UNSET,
) -> Optional[QueueResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_unknown_artist_items (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: False.
        artist_ids (Union[Unset, list[int]]):
        protocol (Union[Unset, DownloadProtocol]):
        quality (Union[Unset, list[int]]):

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
            include_unknown_artist_items=include_unknown_artist_items,
            include_artist=include_artist,
            include_album=include_album,
            artist_ids=artist_ids,
            protocol=protocol,
            quality=quality,
        )
    ).parsed
