"""Shared HTTP client construction + error translation.

Wraps the generated thin clients so every per-service tool can rely on a
common error envelope. Generated httpx errors get mapped to our diagnostic
ToolError subclasses with hints the agent can act on.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, TypeVar

import httpx

from arr_stack_mcp.errors import UpstreamAuthFailed, UpstreamBadRequest, UpstreamUnavailable

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

    from arr_stack_mcp.config import ServiceConfig


_ARR_HEADER = "X-Api-Key"
_JELLYFIN_AUTH_TEMPLATE = 'MediaBrowser Client="arr-stack-mcp", Device="server", DeviceId="arr-stack-mcp", Version="0.1.0", Token="{token}"'

ClientT = TypeVar("ClientT")


def build_httpx_client(svc: ServiceConfig) -> httpx.AsyncClient:
    """Construct the httpx.AsyncClient the generated client will use.

    Sets timeout, TLS verification, and the right auth header for each service
    family. The generated openapi-python-client `Client` / `AuthenticatedClient`
    accepts an httpx-client factory through ``.set_async_httpx_client(...)``.
    """
    headers: dict[str, str] = {}
    if svc.api_key is not None:
        key = svc.api_key.get_secret_value()
        match svc.name:
            case "jellyfin":
                headers["Authorization"] = _JELLYFIN_AUTH_TEMPLATE.format(token=key)
                headers["X-Emby-Token"] = key
            case _:
                headers[_ARR_HEADER] = key
    return httpx.AsyncClient(
        base_url=str(svc.url).rstrip("/"),
        timeout=httpx.Timeout(svc.timeout_seconds),
        verify=svc.verify_tls,
        headers=headers,
        follow_redirects=False,
    )


@asynccontextmanager
async def upstream_call(*, service: str, url: str) -> AsyncIterator[None]:
    """Wrap an httpx call so transport/auth errors raise our diagnostic envelopes.

    Usage::

        async with upstream_call(service="sonarr", url=str(svc.url)):
            response = await client.series.get_api_v3_series()
    """
    try:
        yield
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        body = e.response.text
        if status in {401, 403}:
            raise UpstreamAuthFailed(service=service) from e
        raise UpstreamBadRequest(service=service, status=status, body=body) from e
    except httpx.ConnectError as e:
        raise UpstreamUnavailable(service=service, url=url, cause=str(e)) from e
    except httpx.TimeoutException as e:
        raise UpstreamUnavailable(service=service, url=url, cause=f"timeout: {e}") from e
    except httpx.HTTPError as e:
        # Catch-all for less-common transport errors (read disconnect, proxy errors, etc.).
        raise UpstreamUnavailable(service=service, url=url, cause=str(e)) from e


def raise_for_response_status(*, service: str, response: httpx.Response) -> None:
    """Translate a non-2xx response into our error envelope.

    The generated openapi-python-client returns Response[T] objects whose
    ``.status_code`` may be an error without raising; callers can opt-in to
    raise via this helper.
    """
    if response.is_success:
        return
    status = response.status_code
    if status in {401, 403}:
        raise UpstreamAuthFailed(service=service)
    raise UpstreamBadRequest(service=service, status=status, body=response.text)
