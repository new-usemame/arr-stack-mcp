"""Construct the generated Jellyfin client.

Jellyfin's API uses the ``X-Emby-Token`` header (or the longer
``Authorization: MediaBrowser ... Token="..."`` form). The generated
AuthenticatedClient is parameterized to write to ``X-Emby-Token`` directly,
which keeps every endpoint that requires authentication working without
extra glue.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from arr_stack_mcp.generated.jellyfin.client import AuthenticatedClient, Client

if TYPE_CHECKING:
    from arr_stack_mcp.config import ServiceConfig


def make_jellyfin_client(svc: ServiceConfig) -> Client | AuthenticatedClient:
    """Build a Jellyfin generated-client. Returns an AuthenticatedClient when an
    API key is configured; otherwise a plain Client (suitable for unauthenticated
    public endpoints like ``get_public_system_info``).
    """
    base_url = str(svc.url).rstrip("/")
    if svc.api_key is None:
        return Client(
            base_url=base_url,
            timeout=httpx.Timeout(svc.timeout_seconds),
            verify_ssl=svc.verify_tls,
            follow_redirects=False,
            raise_on_unexpected_status=False,
        )
    return AuthenticatedClient(
        base_url=base_url,
        token=svc.api_key.get_secret_value(),
        prefix="",
        auth_header_name="X-Emby-Token",
        timeout=httpx.Timeout(svc.timeout_seconds),
        verify_ssl=svc.verify_tls,
        follow_redirects=False,
        raise_on_unexpected_status=False,
    )
