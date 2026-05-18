from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.queue_resource import QueueResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["artistId"] = artist_id

    json_album_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(album_ids, Unset):
        json_album_ids = album_ids

    params["albumIds"] = json_album_ids

    params["includeArtist"] = include_artist

    params["includeAlbum"] = include_album

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/queue/details",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["QueueResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = QueueResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["QueueResource"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = True,
) -> Response[list["QueueResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QueueResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        album_ids=album_ids,
        include_artist=include_artist,
        include_album=include_album,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = True,
) -> Optional[list["QueueResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QueueResource']
    """

    return sync_detailed(
        client=client,
        artist_id=artist_id,
        album_ids=album_ids,
        include_artist=include_artist,
        include_album=include_album,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = True,
) -> Response[list["QueueResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QueueResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        album_ids=album_ids,
        include_artist=include_artist,
        include_album=include_album,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    include_artist: Union[Unset, bool] = False,
    include_album: Union[Unset, bool] = True,
) -> Optional[list["QueueResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        include_artist (Union[Unset, bool]):  Default: False.
        include_album (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QueueResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            artist_id=artist_id,
            album_ids=album_ids,
            include_artist=include_artist,
            include_album=include_album,
        )
    ).parsed
