from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.track_file_resource import TrackFileResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    artist_id: Union[Unset, int] = UNSET,
    track_file_ids: Union[Unset, list[int]] = UNSET,
    album_id: Union[Unset, list[int]] = UNSET,
    unmapped: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["artistId"] = artist_id

    json_track_file_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(track_file_ids, Unset):
        json_track_file_ids = track_file_ids

    params["trackFileIds"] = json_track_file_ids

    json_album_id: Union[Unset, list[int]] = UNSET
    if not isinstance(album_id, Unset):
        json_album_id = album_id

    params["albumId"] = json_album_id

    params["unmapped"] = unmapped

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/trackfile",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["TrackFileResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.text
        for response_200_item_data in _response_200:
            response_200_item = TrackFileResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["TrackFileResource"]]:
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
    track_file_ids: Union[Unset, list[int]] = UNSET,
    album_id: Union[Unset, list[int]] = UNSET,
    unmapped: Union[Unset, bool] = UNSET,
) -> Response[list["TrackFileResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        track_file_ids (Union[Unset, list[int]]):
        album_id (Union[Unset, list[int]]):
        unmapped (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['TrackFileResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        track_file_ids=track_file_ids,
        album_id=album_id,
        unmapped=unmapped,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    track_file_ids: Union[Unset, list[int]] = UNSET,
    album_id: Union[Unset, list[int]] = UNSET,
    unmapped: Union[Unset, bool] = UNSET,
) -> Optional[list["TrackFileResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        track_file_ids (Union[Unset, list[int]]):
        album_id (Union[Unset, list[int]]):
        unmapped (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['TrackFileResource']
    """

    return sync_detailed(
        client=client,
        artist_id=artist_id,
        track_file_ids=track_file_ids,
        album_id=album_id,
        unmapped=unmapped,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    track_file_ids: Union[Unset, list[int]] = UNSET,
    album_id: Union[Unset, list[int]] = UNSET,
    unmapped: Union[Unset, bool] = UNSET,
) -> Response[list["TrackFileResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        track_file_ids (Union[Unset, list[int]]):
        album_id (Union[Unset, list[int]]):
        unmapped (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['TrackFileResource']]
    """

    kwargs = _get_kwargs(
        artist_id=artist_id,
        track_file_ids=track_file_ids,
        album_id=album_id,
        unmapped=unmapped,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    artist_id: Union[Unset, int] = UNSET,
    track_file_ids: Union[Unset, list[int]] = UNSET,
    album_id: Union[Unset, list[int]] = UNSET,
    unmapped: Union[Unset, bool] = UNSET,
) -> Optional[list["TrackFileResource"]]:
    """
    Args:
        artist_id (Union[Unset, int]):
        track_file_ids (Union[Unset, list[int]]):
        album_id (Union[Unset, list[int]]):
        unmapped (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['TrackFileResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            artist_id=artist_id,
            track_file_ids=track_file_ids,
            album_id=album_id,
            unmapped=unmapped,
        )
    ).parsed
