"""Construct the generated Sonarr client wired with the operator's URL + API key."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from arr_stack_mcp.generated.sonarr.client import AuthenticatedClient, Client

if TYPE_CHECKING:
    from arr_stack_mcp.config import ServiceConfig


def make_sonarr_client(svc: ServiceConfig) -> Client | AuthenticatedClient:
    """Build a Sonarr generated-client wired with the operator's headers + TLS posture.

    Sonarr uses the ``X-Api-Key`` header. Self-signed certificates are allowed via
    ``svc.verify_tls=False`` (typical for the LinuxServer.io home-lab setup).
    """
    base_url = str(svc.url).rstrip("/")
    headers: dict[str, str] = {}
    if svc.api_key is not None:
        headers["X-Api-Key"] = svc.api_key.get_secret_value()
    return Client(
        base_url=base_url,
        headers=headers,
        timeout=httpx.Timeout(svc.timeout_seconds),
        verify_ssl=svc.verify_tls,
        follow_redirects=False,
        raise_on_unexpected_status=False,
    )
