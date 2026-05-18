from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.album_resource import AlbumResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    foreign_album_id: Union[Unset, str] = UNSET,
    include_all_artist_albums: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["artistId"] = artist_id

    json_album_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(album_ids, Unset):
        json_album_ids = album_ids

    params["albumIds"] = json_album_ids

    params["foreignAlbumId"] = foreign_album_id

    params["includeAllArtistAlbums"] = include_all_artist_albums

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/album",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["AlbumResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
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
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    foreign_album_id: Union[Unset, str] = UNSET,
    include_all_artist_albums: Union[Unset, bool] = False,
) -> Response[list["AlbumResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        foreign_album_id (Union[Unset, str]):
        include_all_artist_albums (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AlbumResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        album_ids=album_ids,
        foreign_album_id=foreign_album_id,
        include_all_artist_albums=include_all_artist_albums,
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
    foreign_album_id: Union[Unset, str] = UNSET,
    include_all_artist_albums: Union[Unset, bool] = False,
) -> Optional[list["AlbumResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        foreign_album_id (Union[Unset, str]):
        include_all_artist_albums (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AlbumResource']
    """

    return sync_detailed(
        client=client,
        artist_id=artist_id,
        album_ids=album_ids,
        foreign_album_id=foreign_album_id,
        include_all_artist_albums=include_all_artist_albums,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    foreign_album_id: Union[Unset, str] = UNSET,
    include_all_artist_albums: Union[Unset, bool] = False,
) -> Response[list["AlbumResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        foreign_album_id (Union[Unset, str]):
        include_all_artist_albums (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['AlbumResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        album_ids=album_ids,
        foreign_album_id=foreign_album_id,
        include_all_artist_albums=include_all_artist_albums,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_ids: Union[Unset, list[int]] = UNSET,
    foreign_album_id: Union[Unset, str] = UNSET,
    include_all_artist_albums: Union[Unset, bool] = False,
) -> Optional[list["AlbumResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_ids (Union[Unset, list[int]]):
        foreign_album_id (Union[Unset, str]):
        include_all_artist_albums (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['AlbumResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            artist_id=artist_id,
            album_ids=album_ids,
            foreign_album_id=foreign_album_id,
            include_all_artist_albums=include_all_artist_albums,
        )
    ).parsed
