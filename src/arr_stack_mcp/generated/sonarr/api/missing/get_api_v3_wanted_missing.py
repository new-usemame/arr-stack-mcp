from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.episode_resource_paging_resource import EpisodeResourcePagingResource
from ...models.sort_direction import SortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_images: Union[Unset, bool] = False,
    monitored: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["sortKey"] = sort_key

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    params["includeSeries"] = include_series

    params["includeImages"] = include_images

    params["monitored"] = monitored

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/wanted/missing",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EpisodeResourcePagingResource]:
    if response.status_code == 200:
        response_200 = EpisodeResourcePagingResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EpisodeResourcePagingResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_images: Union[Unset, bool] = False,
    monitored: Union[Unset, bool] = True,
) -> Response[EpisodeResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):  Default: False.
        include_images (Union[Unset, bool]):  Default: False.
        monitored (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EpisodeResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_series=include_series,
        include_images=include_images,
        monitored=monitored,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_images: Union[Unset, bool] = False,
    monitored: Union[Unset, bool] = True,
) -> Optional[EpisodeResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):  Default: False.
        include_images (Union[Unset, bool]):  Default: False.
        monitored (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EpisodeResourcePagingResource
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_series=include_series,
        include_images=include_images,
        monitored=monitored,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_images: Union[Unset, bool] = False,
    monitored: Union[Unset, bool] = True,
) -> Response[EpisodeResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):  Default: False.
        include_images (Union[Unset, bool]):  Default: False.
        monitored (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EpisodeResourcePagingResource]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        sort_key=sort_key,
        sort_direction=sort_direction,
        include_series=include_series,
        include_images=include_images,
        monitored=monitored,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
    sort_key: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, SortDirection] = UNSET,
    include_series: Union[Unset, bool] = False,
    include_images: Union[Unset, bool] = False,
    monitored: Union[Unset, bool] = True,
) -> Optional[EpisodeResourcePagingResource]:
    """
    Args:
        page (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 10.
        sort_key (Union[Unset, str]):
        sort_direction (Union[Unset, SortDirection]):
        include_series (Union[Unset, bool]):  Default: False.
        include_images (Union[Unset, bool]):  Default: False.
        monitored (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EpisodeResourcePagingResource
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            sort_key=sort_key,
            sort_direction=sort_direction,
            include_series=include_series,
            include_images=include_images,
            monitored=monitored,
        )
    ).parsed
