from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    rename_episodes: Union[Unset, bool] = UNSET,
    replace_illegal_characters: Union[Unset, bool] = UNSET,
    colon_replacement_format: Union[Unset, int] = UNSET,
    custom_colon_replacement_format: Union[Unset, str] = UNSET,
    multi_episode_style: Union[Unset, int] = UNSET,
    standard_episode_format: Union[Unset, str] = UNSET,
    daily_episode_format: Union[Unset, str] = UNSET,
    anime_episode_format: Union[Unset, str] = UNSET,
    series_folder_format: Union[Unset, str] = UNSET,
    season_folder_format: Union[Unset, str] = UNSET,
    specials_folder_format: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    resource_name: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["renameEpisodes"] = rename_episodes

    params["replaceIllegalCharacters"] = replace_illegal_characters

    params["colonReplacementFormat"] = colon_replacement_format

    params["customColonReplacementFormat"] = custom_colon_replacement_format

    params["multiEpisodeStyle"] = multi_episode_style

    params["standardEpisodeFormat"] = standard_episode_format

    params["dailyEpisodeFormat"] = daily_episode_format

    params["animeEpisodeFormat"] = anime_episode_format

    params["seriesFolderFormat"] = series_folder_format

    params["seasonFolderFormat"] = season_folder_format

    params["specialsFolderFormat"] = specials_folder_format

    params["id"] = id

    params["resourceName"] = resource_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/config/naming/examples",
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
    rename_episodes: Union[Unset, bool] = UNSET,
    replace_illegal_characters: Union[Unset, bool] = UNSET,
    colon_replacement_format: Union[Unset, int] = UNSET,
    custom_colon_replacement_format: Union[Unset, str] = UNSET,
    multi_episode_style: Union[Unset, int] = UNSET,
    standard_episode_format: Union[Unset, str] = UNSET,
    daily_episode_format: Union[Unset, str] = UNSET,
    anime_episode_format: Union[Unset, str] = UNSET,
    series_folder_format: Union[Unset, str] = UNSET,
    season_folder_format: Union[Unset, str] = UNSET,
    specials_folder_format: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    resource_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        rename_episodes (Union[Unset, bool]):
        replace_illegal_characters (Union[Unset, bool]):
        colon_replacement_format (Union[Unset, int]):
        custom_colon_replacement_format (Union[Unset, str]):
        multi_episode_style (Union[Unset, int]):
        standard_episode_format (Union[Unset, str]):
        daily_episode_format (Union[Unset, str]):
        anime_episode_format (Union[Unset, str]):
        series_folder_format (Union[Unset, str]):
        season_folder_format (Union[Unset, str]):
        specials_folder_format (Union[Unset, str]):
        id (Union[Unset, int]):
        resource_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        rename_episodes=rename_episodes,
        replace_illegal_characters=replace_illegal_characters,
        colon_replacement_format=colon_replacement_format,
        custom_colon_replacement_format=custom_colon_replacement_format,
        multi_episode_style=multi_episode_style,
        standard_episode_format=standard_episode_format,
        daily_episode_format=daily_episode_format,
        anime_episode_format=anime_episode_format,
        series_folder_format=series_folder_format,
        season_folder_format=season_folder_format,
        specials_folder_format=specials_folder_format,
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
    rename_episodes: Union[Unset, bool] = UNSET,
    replace_illegal_characters: Union[Unset, bool] = UNSET,
    colon_replacement_format: Union[Unset, int] = UNSET,
    custom_colon_replacement_format: Union[Unset, str] = UNSET,
    multi_episode_style: Union[Unset, int] = UNSET,
    standard_episode_format: Union[Unset, str] = UNSET,
    daily_episode_format: Union[Unset, str] = UNSET,
    anime_episode_format: Union[Unset, str] = UNSET,
    series_folder_format: Union[Unset, str] = UNSET,
    season_folder_format: Union[Unset, str] = UNSET,
    specials_folder_format: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    resource_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        rename_episodes (Union[Unset, bool]):
        replace_illegal_characters (Union[Unset, bool]):
        colon_replacement_format (Union[Unset, int]):
        custom_colon_replacement_format (Union[Unset, str]):
        multi_episode_style (Union[Unset, int]):
        standard_episode_format (Union[Unset, str]):
        daily_episode_format (Union[Unset, str]):
        anime_episode_format (Union[Unset, str]):
        series_folder_format (Union[Unset, str]):
        season_folder_format (Union[Unset, str]):
        specials_folder_format (Union[Unset, str]):
        id (Union[Unset, int]):
        resource_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        rename_episodes=rename_episodes,
        replace_illegal_characters=replace_illegal_characters,
        colon_replacement_format=colon_replacement_format,
        custom_colon_replacement_format=custom_colon_replacement_format,
        multi_episode_style=multi_episode_style,
        standard_episode_format=standard_episode_format,
        daily_episode_format=daily_episode_format,
        anime_episode_format=anime_episode_format,
        series_folder_format=series_folder_format,
        season_folder_format=season_folder_format,
        specials_folder_format=specials_folder_format,
        id=id,
        resource_name=resource_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
