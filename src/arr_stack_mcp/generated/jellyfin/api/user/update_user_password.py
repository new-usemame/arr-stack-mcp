from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.update_user_password import UpdateUserPassword
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        UpdateUserPassword,
        UpdateUserPassword,
    ],
    user_id: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Users/Password",
        "params": params,
    }

    if isinstance(body, UpdateUserPassword):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateUserPassword):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUserPassword,
        UpdateUserPassword,
    ],
    user_id: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Updates a user's password.

    Args:
        user_id (Union[Unset, UUID]):
        body (UpdateUserPassword): The update user password request body.
        body (UpdateUserPassword): The update user password request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        body=body,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUserPassword,
        UpdateUserPassword,
    ],
    user_id: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Updates a user's password.

    Args:
        user_id (Union[Unset, UUID]):
        body (UpdateUserPassword): The update user password request body.
        body (UpdateUserPassword): The update user password request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        body=body,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUserPassword,
        UpdateUserPassword,
    ],
    user_id: Union[Unset, UUID] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Updates a user's password.

    Args:
        user_id (Union[Unset, UUID]):
        body (UpdateUserPassword): The update user password request body.
        body (UpdateUserPassword): The update user password request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        body=body,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateUserPassword,
        UpdateUserPassword,
    ],
    user_id: Union[Unset, UUID] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Updates a user's password.

    Args:
        user_id (Union[Unset, UUID]):
        body (UpdateUserPassword): The update user password request body.
        body (UpdateUserPassword): The update user password request body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            user_id=user_id,
        )
    ).parsed
