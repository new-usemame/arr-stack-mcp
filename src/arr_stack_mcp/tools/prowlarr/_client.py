"""Construct the generated Prowlarr client wired with the operator's URL + API key.

Same shape as the Sonarr / Radarr / Lidarr clients — Prowlarr uses the
``X-Api-Key`` header. The key rotates on every container reset; the
``UpstreamAuthFailed`` envelope's hint nudges the operator to pull the live
value from `/config/config.xml`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from arr_stack_mcp.generated.prowlarr.client import AuthenticatedClient, Client

if TYPE_CHECKING:
    from arr_stack_mcp.config import ServiceConfig


def make_prowlarr_client(svc: ServiceConfig) -> Client | AuthenticatedClient:
    """Build a Prowlarr generated-client wired with the operator's headers + TLS posture."""
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
