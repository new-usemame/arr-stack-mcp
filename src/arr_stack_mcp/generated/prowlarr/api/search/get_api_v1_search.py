from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.release_resource import ReleaseResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    indexer_ids: Union[Unset, list[int]] = UNSET,
    categories: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["type"] = type_

    json_indexer_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(indexer_ids, Unset):
        json_indexer_ids = indexer_ids

    params["indexerIds"] = json_indexer_ids

    json_categories: Union[Unset, list[int]] = UNSET
    if not isinstance(categories, Unset):
        json_categories = categories

    params["categories"] = json_categories

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["ReleaseResource"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ReleaseResource.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ReleaseResource"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    indexer_ids: Union[Unset, list[int]] = UNSET,
    categories: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[list["ReleaseResource"]]:
    """
    Args:
        query (Union[Unset, str]):
        type_ (Union[Unset, str]):
        indexer_ids (Union[Unset, list[int]]):
        categories (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ReleaseResource']]
    """

    kwargs = _get_kwargs(
        query=query,
        type_=type_,
        indexer_ids=indexer_ids,
        categories=categories,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    indexer_ids: Union[Unset, list[int]] = UNSET,
    categories: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[list["ReleaseResource"]]:
    """
    Args:
        query (Union[Unset, str]):
        type_ (Union[Unset, str]):
        indexer_ids (Union[Unset, list[int]]):
        categories (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ReleaseResource']
    """

    return sync_detailed(
        client=client,
        query=query,
        type_=type_,
        indexer_ids=indexer_ids,
        categories=categories,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    indexer_ids: Union[Unset, list[int]] = UNSET,
    categories: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[list["ReleaseResource"]]:
    """
    Args:
        query (Union[Unset, str]):
        type_ (Union[Unset, str]):
        indexer_ids (Union[Unset, list[int]]):
        categories (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ReleaseResource']]
    """

    kwargs = _get_kwargs(
        query=query,
        type_=type_,
        indexer_ids=indexer_ids,
        categories=categories,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    indexer_ids: Union[Unset, list[int]] = UNSET,
    categories: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[list["ReleaseResource"]]:
    """
    Args:
        query (Union[Unset, str]):
        type_ (Union[Unset, str]):
        indexer_ids (Union[Unset, list[int]]):
        categories (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ReleaseResource']
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            type_=type_,
            indexer_ids=indexer_ids,
            categories=categories,
            limit=limit,
            offset=offset,
        )
    ).parsed
