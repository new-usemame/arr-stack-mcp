"""Shared HTTP error-translation helpers.

This module hosts the diagnostic-envelope translation we apply when generated-
client HTTP calls fail. It does NOT own httpx-client construction — each
per-service `_client.py` builds its own `Client(...)` via the openapi-python-
client constructor, which internally owns the bound `httpx.AsyncClient`. The
earlier `build_httpx_client` helper was unreferenced and has been removed; see
notes/DESIGN-v0.2.md §1.8.

Wiring `upstream_call` into the per-service tool functions (so raw httpx errors
surface as our diagnostic envelopes rather than bubbling up) is a real v0.2
quality improvement tracked separately from this cleanup. Today the helpers
exist as documented intent.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

import httpx

from arr_stack_mcp.errors import UpstreamAuthFailed, UpstreamBadRequest, UpstreamUnavailable

if TYPE_CHECKING:
    from collections.abc import AsyncIterator


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
