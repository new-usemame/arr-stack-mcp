from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.history_resource import HistoryResource
from ...models.movie_history_event_type import MovieHistoryEventType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    movie_id: Union[Unset, int] = UNSET,
    event_type: Union[Unset, MovieHistoryEventType] = UNSET,
    include_movie: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["movieId"] = movie_id

    json_event_type: Union[Unset, str] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type.value

    params["eventType"] = json_event_type

    params["includeMovie"] = include_movie

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/history/movie",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["HistoryResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HistoryResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["HistoryResource"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, int] = UNSET,
    event_type: Union[Unset, MovieHistoryEventType] = UNSET,
    include_movie: Union[Unset, bool] = False,
) -> Response[list["HistoryResource"]]:
    """
    Args:
        movie_id (Union[Unset, int]):
        event_type (Union[Unset, MovieHistoryEventType]):
        include_movie (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['HistoryResource']]
    """

    kwargs = _get_kwargs(
        movie_id=movie_id,
        event_type=event_type,
        include_movie=include_movie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, int] = UNSET,
    event_type: Union[Unset, MovieHistoryEventType] = UNSET,
    include_movie: Union[Unset, bool] = False,
) -> Optional[list["HistoryResource"]]:
    """
    Args:
        movie_id (Union[Unset, int]):
        event_type (Union[Unset, MovieHistoryEventType]):
        include_movie (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['HistoryResource']
    """

    return sync_detailed(
        client=client,
        movie_id=movie_id,
        event_type=event_type,
        include_movie=include_movie,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, int] = UNSET,
    event_type: Union[Unset, MovieHistoryEventType] = UNSET,
    include_movie: Union[Unset, bool] = False,
) -> Response[list["HistoryResource"]]:
    """
    Args:
        movie_id (Union[Unset, int]):
        event_type (Union[Unset, MovieHistoryEventType]):
        include_movie (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['HistoryResource']]
    """

    kwargs = _get_kwargs(
        movie_id=movie_id,
        event_type=event_type,
        include_movie=include_movie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, int] = UNSET,
    event_type: Union[Unset, MovieHistoryEventType] = UNSET,
    include_movie: Union[Unset, bool] = False,
) -> Optional[list["HistoryResource"]]:
    """
    Args:
        movie_id (Union[Unset, int]):
        event_type (Union[Unset, MovieHistoryEventType]):
        include_movie (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['HistoryResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            movie_id=movie_id,
            event_type=event_type,
            include_movie=include_movie,
        )
    ).parsed
