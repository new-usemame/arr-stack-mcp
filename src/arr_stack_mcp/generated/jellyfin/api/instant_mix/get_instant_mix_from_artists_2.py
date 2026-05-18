from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: UUID,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, list[ImageType]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_id = str(id)
    params["id"] = json_id

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["limit"] = limit

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["enableImages"] = enable_images

    params["enableUserData"] = enable_user_data

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Union[Unset, list[str]] = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Artists/InstantMix",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
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
) -> Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: UUID,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, list[ImageType]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Creates an instant playlist based on a given artist.

    Args:
        id (UUID):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, list[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        limit=limit,
        fields=fields,
        enable_images=enable_images,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: UUID,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, list[ImageType]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Creates an instant playlist based on a given artist.

    Args:
        id (UUID):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, list[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        id=id,
        user_id=user_id,
        limit=limit,
        fields=fields,
        enable_images=enable_images,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: UUID,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, list[ImageType]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Creates an instant playlist based on a given artist.

    Args:
        id (UUID):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, list[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        limit=limit,
        fields=fields,
        enable_images=enable_images,
        enable_user_data=enable_user_data,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: UUID,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
    enable_images: Union[Unset, bool] = UNSET,
    enable_user_data: Union[Unset, bool] = UNSET,
    image_type_limit: Union[Unset, int] = UNSET,
    enable_image_types: Union[Unset, list[ImageType]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]:
    """Creates an instant playlist based on a given artist.

    Args:
        id (UUID):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):
        enable_images (Union[Unset, bool]):
        enable_user_data (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, list[ImageType]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            user_id=user_id,
            limit=limit,
            fields=fields,
            enable_images=enable_images,
            enable_user_data=enable_user_data,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
        )
    ).parsed
