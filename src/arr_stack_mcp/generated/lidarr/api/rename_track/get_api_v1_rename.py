from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rename_track_resource import RenameTrackResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    artist_id: Union[Unset, int] = UNSET,
    album_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["artistId"] = artist_id

    params["albumId"] = album_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/rename",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["RenameTrackResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
        for response_200_item_data in _response_200:
            response_200_item = RenameTrackResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["RenameTrackResource"]]:
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
    album_id: Union[Unset, int] = UNSET,
) -> Response[list["RenameTrackResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RenameTrackResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        album_id=album_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_id: Union[Unset, int] = UNSET,
) -> Optional[list["RenameTrackResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RenameTrackResource']
    """

    return sync_detailed(
        client=client,
        artist_id=artist_id,
        album_id=album_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_id: Union[Unset, int] = UNSET,
) -> Response[list["RenameTrackResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RenameTrackResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        album_id=album_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    album_id: Union[Unset, int] = UNSET,
) -> Optional[list["RenameTrackResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        album_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RenameTrackResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            artist_id=artist_id,
            album_id=album_id,
        )
    ).parsed
