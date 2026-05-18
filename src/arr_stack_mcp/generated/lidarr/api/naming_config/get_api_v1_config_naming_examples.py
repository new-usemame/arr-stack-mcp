from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rename_tracks: Union[Unset, bool] = UNSET,
    replace_illegal_characters: Union[Unset, bool] = UNSET,
    colon_replacement_format: Union[Unset, int] = UNSET,
    standard_track_format: Union[Unset, str] = UNSET,
    multi_disc_track_format: Union[Unset, str] = UNSET,
    artist_folder_format: Union[Unset, str] = UNSET,
    include_artist_name: Union[Unset, bool] = UNSET,
    include_album_title: Union[Unset, bool] = UNSET,
    include_quality: Union[Unset, bool] = UNSET,
    replace_spaces: Union[Unset, bool] = UNSET,
    separator: Union[Unset, str] = UNSET,
    number_style: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    resource_name: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["renameTracks"] = rename_tracks

    params["replaceIllegalCharacters"] = replace_illegal_characters

    params["colonReplacementFormat"] = colon_replacement_format

    params["standardTrackFormat"] = standard_track_format

    params["multiDiscTrackFormat"] = multi_disc_track_format

    params["artistFolderFormat"] = artist_folder_format

    params["includeArtistName"] = include_artist_name

    params["includeAlbumTitle"] = include_album_title

    params["includeQuality"] = include_quality

    params["replaceSpaces"] = replace_spaces

    params["separator"] = separator

    params["numberStyle"] = number_style

    params["id"] = id

    params["resourceName"] = resource_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/config/naming/examples",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    rename_tracks: Union[Unset, bool] = UNSET,
    replace_illegal_characters: Union[Unset, bool] = UNSET,
    colon_replacement_format: Union[Unset, int] = UNSET,
    standard_track_format: Union[Unset, str] = UNSET,
    multi_disc_track_format: Union[Unset, str] = UNSET,
    artist_folder_format: Union[Unset, str] = UNSET,
    include_artist_name: Union[Unset, bool] = UNSET,
    include_album_title: Union[Unset, bool] = UNSET,
    include_quality: Union[Unset, bool] = UNSET,
    replace_spaces: Union[Unset, bool] = UNSET,
    separator: Union[Unset, str] = UNSET,
    number_style: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    resource_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        rename_tracks (Union[Unset, bool]):
        replace_illegal_characters (Union[Unset, bool]):
        colon_replacement_format (Union[Unset, int]):
        standard_track_format (Union[Unset, str]):
        multi_disc_track_format (Union[Unset, str]):
        artist_folder_format (Union[Unset, str]):
        include_artist_name (Union[Unset, bool]):
        include_album_title (Union[Unset, bool]):
        include_quality (Union[Unset, bool]):
        replace_spaces (Union[Unset, bool]):
        separator (Union[Unset, str]):
        number_style (Union[Unset, str]):
        id (Union[Unset, int]):
        resource_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        rename_tracks=rename_tracks,
        replace_illegal_characters=replace_illegal_characters,
        colon_replacement_format=colon_replacement_format,
        standard_track_format=standard_track_format,
        multi_disc_track_format=multi_disc_track_format,
        artist_folder_format=artist_folder_format,
        include_artist_name=include_artist_name,
        include_album_title=include_album_title,
        include_quality=include_quality,
        replace_spaces=replace_spaces,
        separator=separator,
        number_style=number_style,
        id=id,
        resource_name=resource_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    rename_tracks: Union[Unset, bool] = UNSET,
    replace_illegal_characters: Union[Unset, bool] = UNSET,
    colon_replacement_format: Union[Unset, int] = UNSET,
    standard_track_format: Union[Unset, str] = UNSET,
    multi_disc_track_format: Union[Unset, str] = UNSET,
    artist_folder_format: Union[Unset, str] = UNSET,
    include_artist_name: Union[Unset, bool] = UNSET,
    include_album_title: Union[Unset, bool] = UNSET,
    include_quality: Union[Unset, bool] = UNSET,
    replace_spaces: Union[Unset, bool] = UNSET,
    separator: Union[Unset, str] = UNSET,
    number_style: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    resource_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        rename_tracks (Union[Unset, bool]):
        replace_illegal_characters (Union[Unset, bool]):
        colon_replacement_format (Union[Unset, int]):
        standard_track_format (Union[Unset, str]):
        multi_disc_track_format (Union[Unset, str]):
        artist_folder_format (Union[Unset, str]):
        include_artist_name (Union[Unset, bool]):
        include_album_title (Union[Unset, bool]):
        include_quality (Union[Unset, bool]):
        replace_spaces (Union[Unset, bool]):
        separator (Union[Unset, str]):
        number_style (Union[Unset, str]):
        id (Union[Unset, int]):
        resource_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        rename_tracks=rename_tracks,
        replace_illegal_characters=replace_illegal_characters,
        colon_replacement_format=colon_replacement_format,
        standard_track_format=standard_track_format,
        multi_disc_track_format=multi_disc_track_format,
        artist_folder_format=artist_folder_format,
        include_artist_name=include_artist_name,
        include_album_title=include_album_title,
        include_quality=include_quality,
        replace_spaces=replace_spaces,
        separator=separator,
        number_style=number_style,
        id=id,
        resource_name=resource_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
