from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.notification_resource import NotificationResource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: NotificationResource,
    force_save: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["forceSave"] = force_save

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/notification/{id}".format(
            id=id,
        ),
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[NotificationResource]:
    if response.status_code == 200:
        response_200 = NotificationResource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[NotificationResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotificationResource,
    force_save: Union[Unset, bool] = False,
) -> Response[NotificationResource]:
    """
    Args:
        id (str):
        force_save (Union[Unset, bool]):  Default: False.
        body (NotificationResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationResource]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        force_save=force_save,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotificationResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[NotificationResource]:
    """
    Args:
        id (str):
        force_save (Union[Unset, bool]):  Default: False.
        body (NotificationResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationResource
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        force_save=force_save,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotificationResource,
    force_save: Union[Unset, bool] = False,
) -> Response[NotificationResource]:
    """
    Args:
        id (str):
        force_save (Union[Unset, bool]):  Default: False.
        body (NotificationResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NotificationResource]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        force_save=force_save,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NotificationResource,
    force_save: Union[Unset, bool] = False,
) -> Optional[NotificationResource]:
    """
    Args:
        id (str):
        force_save (Union[Unset, bool]):  Default: False.
        body (NotificationResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NotificationResource
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            force_save=force_save,
        )
    ).parsed
