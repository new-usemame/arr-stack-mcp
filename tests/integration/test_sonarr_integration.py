"""Sonarr integration tests against the docker test stack.

These exercise the curated tool layer end-to-end against a real Sonarr
container. The container has no library content (just the seeded API key),
so most tools return empty lists — which is the right ground truth for
testing the wire shapes.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from arr_stack_mcp.tools.sonarr._client import make_sonarr_client

if TYPE_CHECKING:
    from arr_stack_mcp.config import ServiceConfig

pytestmark = pytest.mark.integration


async def test_sonarr_system_status_against_real_container(sonarr_svc: ServiceConfig) -> None:
    """The simplest read tool. Proves wiring + auth + parsing all work."""
    from arr_stack_mcp.generated.sonarr.api.system import get_api_v3_system_status

    client = make_sonarr_client(sonarr_svc)
    result = await get_api_v3_system_status.asyncio(client=client)
    assert result is not None
    assert result.version, "Sonarr should report its version"
    assert result.is_docker is True, "test container should report itself as docker"


async def test_sonarr_series_list_is_empty_on_fresh_stack(sonarr_svc: ServiceConfig) -> None:
    """Fresh container has no series — the list endpoint should return empty."""
    from arr_stack_mcp.generated.sonarr.api.series import get_api_v3_series

    client = make_sonarr_client(sonarr_svc)
    series = await get_api_v3_series.asyncio(client=client)
    assert series is not None
    assert isinstance(series, list)
    assert len(series) == 0


async def test_sonarr_queue_is_empty(sonarr_svc: ServiceConfig) -> None:
    from arr_stack_mcp.generated.sonarr.api.queue import get_api_v3_queue

    client = make_sonarr_client(sonarr_svc)
    page = await get_api_v3_queue.asyncio(client=client, page=1, page_size=10)
    assert page is not None
    assert getattr(page, "total_records", 0) == 0


async def test_sonarr_health_endpoint_responds(sonarr_svc: ServiceConfig) -> None:
    """Sonarr's health endpoint returns the list of fired health checks. Empty on a
    fresh container is the success case."""
    from arr_stack_mcp.generated.sonarr.api.health import get_api_v3_health

    client = make_sonarr_client(sonarr_svc)
    items = await get_api_v3_health.asyncio(client=client)
    assert isinstance(items, list)
