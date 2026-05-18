from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    exclude_artist_ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_exclude_artist_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(exclude_artist_ids, Unset):
        json_exclude_artist_ids = []
        for exclude_artist_ids_item_data in exclude_artist_ids:
            exclude_artist_ids_item = str(exclude_artist_ids_item_data)
            json_exclude_artist_ids.append(exclude_artist_ids_item)

    params["excludeArtistIds"] = json_exclude_artist_ids

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Albums/{item_id}/Similar".format(
            item_id=item_id,
        ),
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
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Response[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        exclude_artist_ids=exclude_artist_ids,
        user_id=user_id,
        limit=limit,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    exclude_artist_ids: Union[Unset, list[UUID]] = UNSET,
    user_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fields: Union[Unset, list[ItemFields]] = UNSET,
) -> Optional[Union[Any, BaseItemDtoQueryResult]]:
    """Gets similar items.

    Args:
        item_id (UUID):
        exclude_artist_ids (Union[Unset, list[UUID]]):
        user_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
        fields (Union[Unset, list[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            exclude_artist_ids=exclude_artist_ids,
            user_id=user_id,
            limit=limit,
            fields=fields,
        )
    ).parsed
