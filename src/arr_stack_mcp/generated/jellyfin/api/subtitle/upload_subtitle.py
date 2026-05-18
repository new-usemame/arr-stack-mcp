from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.upload_subtitle_dto import UploadSubtitleDto
from ...types import Response


def _get_kwargs(
    item_id: UUID,
    *,
    body: Union[
        UploadSubtitleDto,
        UploadSubtitleDto,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Videos/{item_id}/Subtitles".format(
            item_id=item_id,
        ),
    }

    if isinstance(body, UploadSubtitleDto):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, UploadSubtitleDto):
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
) -> Response[Union[Any, ProblemDetails]]:
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
    body: Union[
        UploadSubtitleDto,
        UploadSubtitleDto,
    ],
) -> Response[Union[Any, ProblemDetails]]:
    """Upload an external subtitle file.

    Args:
        item_id (UUID):
        body (UploadSubtitleDto): Upload subtitles dto.
        body (UploadSubtitleDto): Upload subtitles dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UploadSubtitleDto,
        UploadSubtitleDto,
    ],
) -> Optional[Union[Any, ProblemDetails]]:
    """Upload an external subtitle file.

    Args:
        item_id (UUID):
        body (UploadSubtitleDto): Upload subtitles dto.
        body (UploadSubtitleDto): Upload subtitles dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UploadSubtitleDto,
        UploadSubtitleDto,
    ],
) -> Response[Union[Any, ProblemDetails]]:
    """Upload an external subtitle file.

    Args:
        item_id (UUID):
        body (UploadSubtitleDto): Upload subtitles dto.
        body (UploadSubtitleDto): Upload subtitles dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        UploadSubtitleDto,
        UploadSubtitleDto,
    ],
) -> Optional[Union[Any, ProblemDetails]]:
    """Upload an external subtitle file.

    Args:
        item_id (UUID):
        body (UploadSubtitleDto): Upload subtitles dto.
        body (UploadSubtitleDto): Upload subtitles dto.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
