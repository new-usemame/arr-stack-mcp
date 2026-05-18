from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_format import ImageFormat
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Union[Unset, UUID] = UNSET,
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_user_id: Union[Unset, str] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = str(user_id)
    params["userId"] = json_user_id

    params["tag"] = tag

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/UserImage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
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
    client: Union[AuthenticatedClient, Client],
    user_id: Union[Unset, UUID] = UNSET,
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Get user profile image.

    Args:
        user_id (Union[Unset, UUID]):
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        tag=tag,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    user_id: Union[Unset, UUID] = UNSET,
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Get user profile image.

    Args:
        user_id (Union[Unset, UUID]):
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        tag=tag,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    user_id: Union[Unset, UUID] = UNSET,
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Get user profile image.

    Args:
        user_id (Union[Unset, UUID]):
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        tag=tag,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    user_id: Union[Unset, UUID] = UNSET,
    tag: Union[Unset, str] = UNSET,
    format_: Union[Unset, ImageFormat] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Get user profile image.

    Args:
        user_id (Union[Unset, UUID]):
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            tag=tag,
            format_=format_,
        )
    ).parsed
