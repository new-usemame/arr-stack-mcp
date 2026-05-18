from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.queue_resource import QueueResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    series_id: Union[Unset, int] = UNSET,
    episode_ids: Union[Unset, list[int]] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["seriesId"] = series_id

    json_episode_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(episode_ids, Unset):
        json_episode_ids = episode_ids

    params["episodeIds"] = json_episode_ids

    params["includeSeries"] = include_series

    params["includeEpisode"] = include_episode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/queue/details",
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
    series_id: Union[Unset, int] = UNSET,
    episode_ids: Union[Unset, list[int]] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
) -> Response[list["QueueResource"]]:
    """
    Args:
        series_id (Union[Unset, int]):
        episode_ids (Union[Unset, list[int]]):
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QueueResource']]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        episode_ids=episode_ids,
        include_series=include_series,
        include_episode=include_episode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    series_id: Union[Unset, int] = UNSET,
    episode_ids: Union[Unset, list[int]] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
) -> Optional[list["QueueResource"]]:
    """
    Args:
        series_id (Union[Unset, int]):
        episode_ids (Union[Unset, list[int]]):
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QueueResource']
    """

    return sync_detailed(
        client=client,
        series_id=series_id,
        episode_ids=episode_ids,
        include_series=include_series,
        include_episode=include_episode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    series_id: Union[Unset, int] = UNSET,
    episode_ids: Union[Unset, list[int]] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
) -> Response[list["QueueResource"]]:
    """
    Args:
        series_id (Union[Unset, int]):
        episode_ids (Union[Unset, list[int]]):
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['QueueResource']]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        episode_ids=episode_ids,
        include_series=include_series,
        include_episode=include_episode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    series_id: Union[Unset, int] = UNSET,
    episode_ids: Union[Unset, list[int]] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_episode: Union[Unset, bool] = False,
) -> Optional[list["QueueResource"]]:
    """
    Args:
        series_id (Union[Unset, int]):
        episode_ids (Union[Unset, list[int]]):
        include_series (Union[Unset, bool]):  Default: False.
        include_episode (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['QueueResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            series_id=series_id,
            episode_ids=episode_ids,
            include_series=include_series,
            include_episode=include_episode,
        )
    ).parsed
