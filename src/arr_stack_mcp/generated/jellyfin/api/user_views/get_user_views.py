from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.collection_type import CollectionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, UUID] = UNSET,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, list[CollectionType]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["includeExternalContent"] = include_external_content

    json_preset_views: Union[Unset, list[str]] = UNSET
    if not isinstance(preset_views, Unset):
        json_preset_views = []
        for preset_views_item_data in preset_views:
            preset_views_item = preset_views_item_data.value
            json_preset_views.append(preset_views_item)

    params["presetViews"] = json_preset_views

    params["includeHidden"] = include_hidden

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/UserViews",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    if response.status_code == 200:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

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
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, list[CollectionType]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (Union[Unset, UUID]):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, list[CollectionType]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_external_content=include_external_content,
        preset_views=preset_views,
        include_hidden=include_hidden,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, list[CollectionType]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (Union[Unset, UUID]):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, list[CollectionType]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        include_external_content=include_external_content,
        preset_views=preset_views,
        include_hidden=include_hidden,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, list[CollectionType]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (Union[Unset, UUID]):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, list[CollectionType]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_external_content=include_external_content,
        preset_views=preset_views,
        include_hidden=include_hidden,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Union[Unset, UUID] = UNSET,
    include_external_content: Union[Unset, bool] = UNSET,
    preset_views: Union[Unset, list[CollectionType]] = UNSET,
    include_hidden: Union[Unset, bool] = False,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Get user views.

    Args:
        user_id (Union[Unset, UUID]):
        include_external_content (Union[Unset, bool]):
        preset_views (Union[Unset, list[CollectionType]]):
        include_hidden (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            include_external_content=include_external_content,
            preset_views=preset_views,
            include_hidden=include_hidden,
        )
    ).parsed
