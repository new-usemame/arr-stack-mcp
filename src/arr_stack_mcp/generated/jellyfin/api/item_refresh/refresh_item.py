from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metadata_refresh_mode import MetadataRefreshMode
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: UUID,
    *,
    metadata_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, bool] = False,
    replace_all_images: Union[Unset, bool] = False,
    regenerate_trickplay: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_metadata_refresh_mode: Union[Unset, str] = UNSET
    if not isinstance(metadata_refresh_mode, Unset):
        json_metadata_refresh_mode = metadata_refresh_mode.value

    params["metadataRefreshMode"] = json_metadata_refresh_mode

    json_image_refresh_mode: Union[Unset, str] = UNSET
    if not isinstance(image_refresh_mode, Unset):
        json_image_refresh_mode = image_refresh_mode.value

    params["imageRefreshMode"] = json_image_refresh_mode

    params["replaceAllMetadata"] = replace_all_metadata

    params["replaceAllImages"] = replace_all_images

    params["regenerateTrickplay"] = regenerate_trickplay

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Items/{item_id}/Refresh".format(
            item_id=item_id,
        ),
        "params": params,
    }

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
    metadata_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, bool] = False,
    replace_all_images: Union[Unset, bool] = False,
    regenerate_trickplay: Union[Unset, bool] = False,
) -> Response[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (UUID):
        metadata_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, bool]):  Default: False.
        replace_all_images (Union[Unset, bool]):  Default: False.
        regenerate_trickplay (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        metadata_refresh_mode=metadata_refresh_mode,
        image_refresh_mode=image_refresh_mode,
        replace_all_metadata=replace_all_metadata,
        replace_all_images=replace_all_images,
        regenerate_trickplay=regenerate_trickplay,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    metadata_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, bool] = False,
    replace_all_images: Union[Unset, bool] = False,
    regenerate_trickplay: Union[Unset, bool] = False,
) -> Optional[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (UUID):
        metadata_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, bool]):  Default: False.
        replace_all_images (Union[Unset, bool]):  Default: False.
        regenerate_trickplay (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        metadata_refresh_mode=metadata_refresh_mode,
        image_refresh_mode=image_refresh_mode,
        replace_all_metadata=replace_all_metadata,
        replace_all_images=replace_all_images,
        regenerate_trickplay=regenerate_trickplay,
    ).parsed


async def asyncio_detailed(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    metadata_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, bool] = False,
    replace_all_images: Union[Unset, bool] = False,
    regenerate_trickplay: Union[Unset, bool] = False,
) -> Response[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (UUID):
        metadata_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, bool]):  Default: False.
        replace_all_images (Union[Unset, bool]):  Default: False.
        regenerate_trickplay (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        metadata_refresh_mode=metadata_refresh_mode,
        image_refresh_mode=image_refresh_mode,
        replace_all_metadata=replace_all_metadata,
        replace_all_images=replace_all_images,
        regenerate_trickplay=regenerate_trickplay,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: UUID,
    *,
    client: AuthenticatedClient,
    metadata_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    image_refresh_mode: Union[Unset, MetadataRefreshMode] = MetadataRefreshMode.NONE,
    replace_all_metadata: Union[Unset, bool] = False,
    replace_all_images: Union[Unset, bool] = False,
    regenerate_trickplay: Union[Unset, bool] = False,
) -> Optional[Union[Any, ProblemDetails]]:
    """Refreshes metadata for an item.

    Args:
        item_id (UUID):
        metadata_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        image_refresh_mode (Union[Unset, MetadataRefreshMode]):  Default:
            MetadataRefreshMode.NONE.
        replace_all_metadata (Union[Unset, bool]):  Default: False.
        replace_all_images (Union[Unset, bool]):  Default: False.
        regenerate_trickplay (Union[Unset, bool]):  Default: False.

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
            metadata_refresh_mode=metadata_refresh_mode,
            image_refresh_mode=image_refresh_mode,
            replace_all_metadata=replace_all_metadata,
            replace_all_images=replace_all_images,
            regenerate_trickplay=regenerate_trickplay,
        )
    ).parsed
