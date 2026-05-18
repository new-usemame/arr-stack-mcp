from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.session_info_dto import SessionInfoDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    controllable_by_user_id: Union[Unset, UUID] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    active_within_seconds: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_controllable_by_user_id: Union[Unset, str] = UNSET
    if not isinstance(controllable_by_user_id, Unset):
        json_controllable_by_user_id = str(controllable_by_user_id)
    params["controllableByUserId"] = json_controllable_by_user_id

    params["deviceId"] = device_id

    params["activeWithinSeconds"] = active_within_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["SessionInfoDto"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SessionInfoDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["SessionInfoDto"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Union[Unset, UUID] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    active_within_seconds: Union[Unset, int] = UNSET,
) -> Response[Union[Any, list["SessionInfoDto"]]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, UUID]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['SessionInfoDto']]]
    """

    kwargs = _get_kwargs(
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Union[Unset, UUID] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    active_within_seconds: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, list["SessionInfoDto"]]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, UUID]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['SessionInfoDto']]
    """

    return sync_detailed(
        client=client,
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Union[Unset, UUID] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    active_within_seconds: Union[Unset, int] = UNSET,
) -> Response[Union[Any, list["SessionInfoDto"]]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, UUID]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['SessionInfoDto']]]
    """

    kwargs = _get_kwargs(
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Union[Unset, UUID] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    active_within_seconds: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, list["SessionInfoDto"]]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, UUID]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['SessionInfoDto']]
    """

    return (
        await asyncio_detailed(
            client=client,
            controllable_by_user_id=controllable_by_user_id,
            device_id=device_id,
            active_within_seconds=active_within_seconds,
        )
    ).parsed
