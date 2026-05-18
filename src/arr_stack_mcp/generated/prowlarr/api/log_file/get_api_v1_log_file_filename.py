from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.i_action_result import IActionResult
from ...types import Response


def _get_kwargs(
    filename: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/log/file/{filename}".format(
            filename=filename,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IActionResult]:
    if response.status_code == 200:
        response_200 = IActionResult.from_dict(response.text)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IActionResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[IActionResult]:
    """
    Args:
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IActionResult]
    """

    kwargs = _get_kwargs(
        filename=filename,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[IActionResult]:
    """
    Args:
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IActionResult
    """

    return sync_detailed(
        filename=filename,
        client=client,
    ).parsed


async def asyncio_detailed(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[IActionResult]:
    """
    Args:
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IActionResult]
    """

    kwargs = _get_kwargs(
        filename=filename,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    filename: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[IActionResult]:
    """
    Args:
        filename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IActionResult
    """

    return (
        await asyncio_detailed(
            filename=filename,
            client=client,
        )
    ).parsed
