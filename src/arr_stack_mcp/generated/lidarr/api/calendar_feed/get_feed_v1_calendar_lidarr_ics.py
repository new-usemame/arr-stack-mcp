from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    past_days: Union[Unset, int] = 7,
    future_days: Union[Unset, int] = 28,
    tags: Union[Unset, str] = "",
    unmonitored: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pastDays"] = past_days

    params["futureDays"] = future_days

    params["tags"] = tags

    params["unmonitored"] = unmonitored

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/feed/v1/calendar/lidarr.ics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    past_days: Union[Unset, int] = 7,
    future_days: Union[Unset, int] = 28,
    tags: Union[Unset, str] = "",
    unmonitored: Union[Unset, bool] = False,
) -> Response[Any]:
    """
    Args:
        past_days (Union[Unset, int]):  Default: 7.
        future_days (Union[Unset, int]):  Default: 28.
        tags (Union[Unset, str]):  Default: ''.
        unmonitored (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        past_days=past_days,
        future_days=future_days,
        tags=tags,
        unmonitored=unmonitored,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    past_days: Union[Unset, int] = 7,
    future_days: Union[Unset, int] = 28,
    tags: Union[Unset, str] = "",
    unmonitored: Union[Unset, bool] = False,
) -> Response[Any]:
    """
    Args:
        past_days (Union[Unset, int]):  Default: 7.
        future_days (Union[Unset, int]):  Default: 28.
        tags (Union[Unset, str]):  Default: ''.
        unmonitored (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        past_days=past_days,
        future_days=future_days,
        tags=tags,
        unmonitored=unmonitored,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
