from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_playlist_dto import CreatePlaylistDto
from ...models.media_type import MediaType
from ...models.playlist_creation_result import PlaylistCreationResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["name"] = name

    json_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(ids, Unset):
        json_ids = []
        for ids_item_data in ids:
            ids_item = str(ids_item_data)
            json_ids.append(ids_item)

    params["ids"] = json_ids

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    json_media_type: Union[Unset, str] = UNSET
    if not isinstance(media_type, Unset):
        json_media_type = media_type.value

    params["mediaType"] = json_media_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Playlists",
        "params": params,
    }

    if isinstance(body, CreatePlaylistDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePlaylistDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PlaylistCreationResult]]:
    if response.status_code == 200:
        response_200 = PlaylistCreationResult.from_dict(response.json())

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
) -> Response[Union[Any, PlaylistCreationResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Response[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaylistCreationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Optional[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaylistCreationResult]
    """

    return sync_detailed(
        client=client,
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Response[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PlaylistCreationResult]]
    """

    kwargs = _get_kwargs(
        body=body,
        name=name,
        ids=ids,
        user_id=user_id,
        media_type=media_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreatePlaylistDto,
        CreatePlaylistDto,
    ],
    name: Union[Unset, str] = UNSET,
    ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    media_type: Union[Unset, MediaType] = UNSET,
) -> Optional[Union[Any, PlaylistCreationResult]]:
    """Creates a new playlist.

     For backwards compatibility parameters can be sent via Query or Body, with Query having higher
    precedence.
    Query parameters are obsolete.

    Args:
        name (Union[Unset, str]):
        ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        media_type (Union[Unset, MediaType]): Media types.
        body (CreatePlaylistDto): Create new playlist dto.
        body (CreatePlaylistDto): Create new playlist dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PlaylistCreationResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
        )
    ).parsed
