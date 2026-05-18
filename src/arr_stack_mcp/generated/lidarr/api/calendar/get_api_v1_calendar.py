import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_resource import AlbumResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    unmonitored: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    tags: Union[Unset, str] = "",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start: Union[Unset, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: Union[Unset, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    params["unmonitored"] = unmonitored

    params["includeArtist"] = include_artist

    params["tags"] = tags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/calendar",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["AlbumResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AlbumResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["AlbumResource"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    unmonitored: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    tags: Union[Unset, str] = "",
) -> Response[list["AlbumResource"]]:
    """
    Args:
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        unmonitored (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AlbumResource']]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        unmonitored=unmonitored,
        include_artist=include_artist,
        tags=tags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    unmonitored: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    tags: Union[Unset, str] = "",
) -> Optional[list["AlbumResource"]]:
    """
    Args:
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        unmonitored (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AlbumResource']
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        unmonitored=unmonitored,
        include_artist=include_artist,
        tags=tags,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    unmonitored: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    tags: Union[Unset, str] = "",
) -> Response[list["AlbumResource"]]:
    """
    Args:
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        unmonitored (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AlbumResource']]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        unmonitored=unmonitored,
        include_artist=include_artist,
        tags=tags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start: Union[Unset, datetime.datetime] = UNSET,
    end: Union[Unset, datetime.datetime] = UNSET,
    unmonitored: Union[Unset, bool] = False,
    include_artist: Union[Unset, bool] = False,
    tags: Union[Unset, str] = "",
) -> Optional[list["AlbumResource"]]:
    """
    Args:
        start (Union[Unset, datetime.datetime]):
        end (Union[Unset, datetime.datetime]):
        unmonitored (Union[Unset, bool]):  Default: False.
        include_artist (Union[Unset, bool]):  Default: False.
        tags (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AlbumResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            unmonitored=unmonitored,
            include_artist=include_artist,
            tags=tags,
        )
    ).parsed
