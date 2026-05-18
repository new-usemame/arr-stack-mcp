from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    t: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    cat: Union[Unset, str] = UNSET,
    imdbid: Union[Unset, str] = UNSET,
    tmdbid: Union[Unset, int] = UNSET,
    extended: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    minage: Union[Unset, int] = UNSET,
    maxage: Union[Unset, int] = UNSET,
    minsize: Union[Unset, int] = UNSET,
    maxsize: Union[Unset, int] = UNSET,
    rid: Union[Unset, int] = UNSET,
    tvmazeid: Union[Unset, int] = UNSET,
    traktid: Union[Unset, int] = UNSET,
    tvdbid: Union[Unset, int] = UNSET,
    doubanid: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    ep: Union[Unset, str] = UNSET,
    album: Union[Unset, str] = UNSET,
    artist: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    track: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
    genre: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    publisher: Union[Unset, str] = UNSET,
    configured: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    host: Union[Unset, str] = UNSET,
    server: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["t"] = t

    params["q"] = q

    params["cat"] = cat

    params["imdbid"] = imdbid

    params["tmdbid"] = tmdbid

    params["extended"] = extended

    params["limit"] = limit

    params["offset"] = offset

    params["minage"] = minage

    params["maxage"] = maxage

    params["minsize"] = minsize

    params["maxsize"] = maxsize

    params["rid"] = rid

    params["tvmazeid"] = tvmazeid

    params["traktid"] = traktid

    params["tvdbid"] = tvdbid

    params["doubanid"] = doubanid

    params["season"] = season

    params["ep"] = ep

    params["album"] = album

    params["artist"] = artist

    params["label"] = label

    params["track"] = track

    params["year"] = year

    params["genre"] = genre

    params["author"] = author

    params["title"] = title

    params["publisher"] = publisher

    params["configured"] = configured

    params["source"] = source

    params["host"] = host

    params["server"] = server

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/indexer/{id}/newznab".format(
            id=id,
        ),
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
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    t: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    cat: Union[Unset, str] = UNSET,
    imdbid: Union[Unset, str] = UNSET,
    tmdbid: Union[Unset, int] = UNSET,
    extended: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    minage: Union[Unset, int] = UNSET,
    maxage: Union[Unset, int] = UNSET,
    minsize: Union[Unset, int] = UNSET,
    maxsize: Union[Unset, int] = UNSET,
    rid: Union[Unset, int] = UNSET,
    tvmazeid: Union[Unset, int] = UNSET,
    traktid: Union[Unset, int] = UNSET,
    tvdbid: Union[Unset, int] = UNSET,
    doubanid: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    ep: Union[Unset, str] = UNSET,
    album: Union[Unset, str] = UNSET,
    artist: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    track: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
    genre: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    publisher: Union[Unset, str] = UNSET,
    configured: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    host: Union[Unset, str] = UNSET,
    server: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (int):
        t (Union[Unset, str]):
        q (Union[Unset, str]):
        cat (Union[Unset, str]):
        imdbid (Union[Unset, str]):
        tmdbid (Union[Unset, int]):
        extended (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        minage (Union[Unset, int]):
        maxage (Union[Unset, int]):
        minsize (Union[Unset, int]):
        maxsize (Union[Unset, int]):
        rid (Union[Unset, int]):
        tvmazeid (Union[Unset, int]):
        traktid (Union[Unset, int]):
        tvdbid (Union[Unset, int]):
        doubanid (Union[Unset, int]):
        season (Union[Unset, int]):
        ep (Union[Unset, str]):
        album (Union[Unset, str]):
        artist (Union[Unset, str]):
        label (Union[Unset, str]):
        track (Union[Unset, str]):
        year (Union[Unset, int]):
        genre (Union[Unset, str]):
        author (Union[Unset, str]):
        title (Union[Unset, str]):
        publisher (Union[Unset, str]):
        configured (Union[Unset, str]):
        source (Union[Unset, str]):
        host (Union[Unset, str]):
        server (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        t=t,
        q=q,
        cat=cat,
        imdbid=imdbid,
        tmdbid=tmdbid,
        extended=extended,
        limit=limit,
        offset=offset,
        minage=minage,
        maxage=maxage,
        minsize=minsize,
        maxsize=maxsize,
        rid=rid,
        tvmazeid=tvmazeid,
        traktid=traktid,
        tvdbid=tvdbid,
        doubanid=doubanid,
        season=season,
        ep=ep,
        album=album,
        artist=artist,
        label=label,
        track=track,
        year=year,
        genre=genre,
        author=author,
        title=title,
        publisher=publisher,
        configured=configured,
        source=source,
        host=host,
        server=server,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    t: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    cat: Union[Unset, str] = UNSET,
    imdbid: Union[Unset, str] = UNSET,
    tmdbid: Union[Unset, int] = UNSET,
    extended: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    minage: Union[Unset, int] = UNSET,
    maxage: Union[Unset, int] = UNSET,
    minsize: Union[Unset, int] = UNSET,
    maxsize: Union[Unset, int] = UNSET,
    rid: Union[Unset, int] = UNSET,
    tvmazeid: Union[Unset, int] = UNSET,
    traktid: Union[Unset, int] = UNSET,
    tvdbid: Union[Unset, int] = UNSET,
    doubanid: Union[Unset, int] = UNSET,
    season: Union[Unset, int] = UNSET,
    ep: Union[Unset, str] = UNSET,
    album: Union[Unset, str] = UNSET,
    artist: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    track: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
    genre: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    publisher: Union[Unset, str] = UNSET,
    configured: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    host: Union[Unset, str] = UNSET,
    server: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (int):
        t (Union[Unset, str]):
        q (Union[Unset, str]):
        cat (Union[Unset, str]):
        imdbid (Union[Unset, str]):
        tmdbid (Union[Unset, int]):
        extended (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        minage (Union[Unset, int]):
        maxage (Union[Unset, int]):
        minsize (Union[Unset, int]):
        maxsize (Union[Unset, int]):
        rid (Union[Unset, int]):
        tvmazeid (Union[Unset, int]):
        traktid (Union[Unset, int]):
        tvdbid (Union[Unset, int]):
        doubanid (Union[Unset, int]):
        season (Union[Unset, int]):
        ep (Union[Unset, str]):
        album (Union[Unset, str]):
        artist (Union[Unset, str]):
        label (Union[Unset, str]):
        track (Union[Unset, str]):
        year (Union[Unset, int]):
        genre (Union[Unset, str]):
        author (Union[Unset, str]):
        title (Union[Unset, str]):
        publisher (Union[Unset, str]):
        configured (Union[Unset, str]):
        source (Union[Unset, str]):
        host (Union[Unset, str]):
        server (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        t=t,
        q=q,
        cat=cat,
        imdbid=imdbid,
        tmdbid=tmdbid,
        extended=extended,
        limit=limit,
        offset=offset,
        minage=minage,
        maxage=maxage,
        minsize=minsize,
        maxsize=maxsize,
        rid=rid,
        tvmazeid=tvmazeid,
        traktid=traktid,
        tvdbid=tvdbid,
        doubanid=doubanid,
        season=season,
        ep=ep,
        album=album,
        artist=artist,
        label=label,
        track=track,
        year=year,
        genre=genre,
        author=author,
        title=title,
        publisher=publisher,
        configured=configured,
        source=source,
        host=host,
        server=server,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
