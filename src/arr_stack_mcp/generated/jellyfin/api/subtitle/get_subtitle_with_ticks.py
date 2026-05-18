from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    item_id: Union[Unset, UUID] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    index: Union[Unset, int] = UNSET,
    start_position_ticks: Union[Unset, int] = UNSET,
    format_: Union[Unset, str] = UNSET,
    end_position_ticks: Union[Unset, int] = UNSET,
    copy_timestamps: Union[Unset, bool] = False,
    add_vtt_time_map: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_item_id: Union[Unset, str] = UNSET
    if not isinstance(item_id, Unset):
        json_item_id = str(item_id)
    params["itemId"] = json_item_id

    params["mediaSourceId"] = media_source_id

    params["index"] = index

    params["startPositionTicks"] = start_position_ticks

    params["format"] = format_

    params["endPositionTicks"] = end_position_ticks

    params["copyTimestamps"] = copy_timestamps

    params["addVttTimeMap"] = add_vtt_time_map

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Videos/{route_item_id}/{route_media_source_id}/Subtitles/{route_index}/{route_start_position_ticks}/Stream.{route_format}".format(
            route_item_id=route_item_id,
            route_media_source_id=route_media_source_id,
            route_index=route_index,
            route_start_position_ticks=route_start_position_ticks,
            route_format=route_format,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

        return response_200
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: Union[AuthenticatedClient, Client],
    item_id: Union[Unset, UUID] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    index: Union[Unset, int] = UNSET,
    start_position_ticks: Union[Unset, int] = UNSET,
    format_: Union[Unset, str] = UNSET,
    end_position_ticks: Union[Unset, int] = UNSET,
    copy_timestamps: Union[Unset, bool] = False,
    add_vtt_time_map: Union[Unset, bool] = False,
) -> Response[Union[Any, File]]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (Union[Unset, UUID]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        start_position_ticks (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: Union[AuthenticatedClient, Client],
    item_id: Union[Unset, UUID] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    index: Union[Unset, int] = UNSET,
    start_position_ticks: Union[Unset, int] = UNSET,
    format_: Union[Unset, str] = UNSET,
    end_position_ticks: Union[Unset, int] = UNSET,
    copy_timestamps: Union[Unset, bool] = False,
    add_vtt_time_map: Union[Unset, bool] = False,
) -> Optional[Union[Any, File]]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (Union[Unset, UUID]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        start_position_ticks (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        client=client,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    ).parsed


async def asyncio_detailed(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: Union[AuthenticatedClient, Client],
    item_id: Union[Unset, UUID] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    index: Union[Unset, int] = UNSET,
    start_position_ticks: Union[Unset, int] = UNSET,
    format_: Union[Unset, str] = UNSET,
    end_position_ticks: Union[Unset, int] = UNSET,
    copy_timestamps: Union[Unset, bool] = False,
    add_vtt_time_map: Union[Unset, bool] = False,
) -> Response[Union[Any, File]]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (Union[Unset, UUID]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        start_position_ticks (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_start_position_ticks=route_start_position_ticks,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        start_position_ticks=start_position_ticks,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_item_id: UUID,
    route_media_source_id: str,
    route_index: int,
    route_start_position_ticks: int,
    route_format: str,
    *,
    client: Union[AuthenticatedClient, Client],
    item_id: Union[Unset, UUID] = UNSET,
    media_source_id: Union[Unset, str] = UNSET,
    index: Union[Unset, int] = UNSET,
    start_position_ticks: Union[Unset, int] = UNSET,
    format_: Union[Unset, str] = UNSET,
    end_position_ticks: Union[Unset, int] = UNSET,
    copy_timestamps: Union[Unset, bool] = False,
    add_vtt_time_map: Union[Unset, bool] = False,
) -> Optional[Union[Any, File]]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (UUID):
        route_media_source_id (str):
        route_index (int):
        route_start_position_ticks (int):
        route_format (str):
        item_id (Union[Unset, UUID]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        start_position_ticks (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            route_item_id=route_item_id,
            route_media_source_id=route_media_source_id,
            route_index=route_index,
            route_start_position_ticks=route_start_position_ticks,
            route_format=route_format,
            client=client,
            item_id=item_id,
            media_source_id=media_source_id,
            index=index,
            start_position_ticks=start_position_ticks,
            format_=format_,
            end_position_ticks=end_position_ticks,
            copy_timestamps=copy_timestamps,
            add_vtt_time_map=add_vtt_time_map,
        )
    ).parsed
