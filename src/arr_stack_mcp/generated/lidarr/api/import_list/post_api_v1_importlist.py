from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.import_list_resource import ImportListResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ImportListResource,
    force_save: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["forceSave"] = force_save

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/importlist",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ImportListResource]:
    if response.status_code == 200:
        response_200 = ImportListResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ImportListResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ImportListResource,
    force_save: Union[Unset, bool] = False,
) -> Response[ImportListResource]:
    """
    Args:
        force_save (Union[Unset, bool]):  Default: False.
        body (ImportListResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportListResource]
    """

    kwargs = _get_kwargs(
        body=body,
        force_save=force_save,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ImportListResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[ImportListResource]:
    """
    Args:
        force_save (Union[Unset, bool]):  Default: False.
        body (ImportListResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportListResource
    """

    return sync_detailed(
        client=client,
        body=body,
        force_save=force_save,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ImportListResource,
    force_save: Union[Unset, bool] = False,
) -> Response[ImportListResource]:
    """
    Args:
        force_save (Union[Unset, bool]):  Default: False.
        body (ImportListResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportListResource]
    """

    kwargs = _get_kwargs(
        body=body,
        force_save=force_save,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ImportListResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[ImportListResource]:
    """
    Args:
        force_save (Union[Unset, bool]):  Default: False.
        body (ImportListResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportListResource
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            force_save=force_save,
        )
    ).parsed
