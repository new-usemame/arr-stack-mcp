from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.import_list_exclusion_resource import ImportListExclusionResource
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ImportListExclusionResource,
        ImportListExclusionResource,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/importlistexclusion",
    }

    if isinstance(body, ImportListExclusionResource):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ImportListExclusionResource):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ImportListExclusionResource]:
    if response.status_code == 200:
        response_200 = ImportListExclusionResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ImportListExclusionResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ImportListExclusionResource,
        ImportListExclusionResource,
    ],
) -> Response[ImportListExclusionResource]:
    """
    Args:
        body (ImportListExclusionResource):
        body (ImportListExclusionResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportListExclusionResource]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ImportListExclusionResource,
        ImportListExclusionResource,
    ],
) -> Optional[ImportListExclusionResource]:
    """
    Args:
        body (ImportListExclusionResource):
        body (ImportListExclusionResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportListExclusionResource
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ImportListExclusionResource,
        ImportListExclusionResource,
    ],
) -> Response[ImportListExclusionResource]:
    """
    Args:
        body (ImportListExclusionResource):
        body (ImportListExclusionResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportListExclusionResource]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ImportListExclusionResource,
        ImportListExclusionResource,
    ],
) -> Optional[ImportListExclusionResource]:
    """
    Args:
        body (ImportListExclusionResource):
        body (ImportListExclusionResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportListExclusionResource
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
