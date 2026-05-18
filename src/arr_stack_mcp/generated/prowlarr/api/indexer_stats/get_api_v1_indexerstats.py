import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.indexer_stats_resource import IndexerStatsResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    indexers: Union[Unset, str] = UNSET,
    protocols: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["indexers"] = indexers

    params["protocols"] = protocols

    params["tags"] = tags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/indexerstats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IndexerStatsResource]:
    if response.status_code == 200:
        response_200 = IndexerStatsResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IndexerStatsResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    indexers: Union[Unset, str] = UNSET,
    protocols: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
) -> Response[IndexerStatsResource]:
    """
    Args:
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        indexers (Union[Unset, str]):
        protocols (Union[Unset, str]):
        tags (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IndexerStatsResource]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        indexers=indexers,
        protocols=protocols,
        tags=tags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    indexers: Union[Unset, str] = UNSET,
    protocols: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
) -> Optional[IndexerStatsResource]:
    """
    Args:
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        indexers (Union[Unset, str]):
        protocols (Union[Unset, str]):
        tags (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IndexerStatsResource
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        indexers=indexers,
        protocols=protocols,
        tags=tags,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    indexers: Union[Unset, str] = UNSET,
    protocols: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
) -> Response[IndexerStatsResource]:
    """
    Args:
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        indexers (Union[Unset, str]):
        protocols (Union[Unset, str]):
        tags (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IndexerStatsResource]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        indexers=indexers,
        protocols=protocols,
        tags=tags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    start_date: Union[Unset, datetime.datetime] = UNSET,
    end_date: Union[Unset, datetime.datetime] = UNSET,
    indexers: Union[Unset, str] = UNSET,
    protocols: Union[Unset, str] = UNSET,
    tags: Union[Unset, str] = UNSET,
) -> Optional[IndexerStatsResource]:
    """
    Args:
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        indexers (Union[Unset, str]):
        protocols (Union[Unset, str]):
        tags (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IndexerStatsResource
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            indexers=indexers,
            protocols=protocols,
            tags=tags,
        )
    ).parsed
