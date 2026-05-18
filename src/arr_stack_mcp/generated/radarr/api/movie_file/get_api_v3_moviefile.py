from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.movie_file_resource import MovieFileResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    movie_id: Union[Unset, list[int]] = UNSET,
    movie_file_ids: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_movie_id: Union[Unset, list[int]] = UNSET
    if not isinstance(movie_id, Unset):
        json_movie_id = movie_id

    params["movieId"] = json_movie_id

    json_movie_file_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(movie_file_ids, Unset):
        json_movie_file_ids = movie_file_ids

    params["movieFileIds"] = json_movie_file_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/moviefile",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["MovieFileResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MovieFileResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["MovieFileResource"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, list[int]] = UNSET,
    movie_file_ids: Union[Unset, list[int]] = UNSET,
) -> Response[list["MovieFileResource"]]:
    """
    Args:
        movie_id (Union[Unset, list[int]]):
        movie_file_ids (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['MovieFileResource']]
    """

    kwargs = _get_kwargs(
        movie_id=movie_id,
        movie_file_ids=movie_file_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, list[int]] = UNSET,
    movie_file_ids: Union[Unset, list[int]] = UNSET,
) -> Optional[list["MovieFileResource"]]:
    """
    Args:
        movie_id (Union[Unset, list[int]]):
        movie_file_ids (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['MovieFileResource']
    """

    return sync_detailed(
        client=client,
        movie_id=movie_id,
        movie_file_ids=movie_file_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, list[int]] = UNSET,
    movie_file_ids: Union[Unset, list[int]] = UNSET,
) -> Response[list["MovieFileResource"]]:
    """
    Args:
        movie_id (Union[Unset, list[int]]):
        movie_file_ids (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['MovieFileResource']]
    """

    kwargs = _get_kwargs(
        movie_id=movie_id,
        movie_file_ids=movie_file_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    movie_id: Union[Unset, list[int]] = UNSET,
    movie_file_ids: Union[Unset, list[int]] = UNSET,
) -> Optional[list["MovieFileResource"]]:
    """
    Args:
        movie_id (Union[Unset, list[int]]):
        movie_file_ids (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['MovieFileResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            movie_id=movie_id,
            movie_file_ids=movie_file_ids,
        )
    ).parsed
