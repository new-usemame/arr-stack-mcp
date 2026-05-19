"""Prowlarr integration tests against the docker test stack.

Mirrors `test_sonarr_integration.py` shape. The Prowlarr v0.2 curated tool
layer is exercised end-to-end against a real Prowlarr container — empty
indexer config, empty health, empty stats are the right ground truth on a
fresh `scripts/test-stack-up.sh` boot.

See notes/DESIGN-v0.2.md §2.1.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from arr_stack_mcp.tools.prowlarr._client import make_prowlarr_client

if TYPE_CHECKING:
    from arr_stack_mcp.config import ServiceConfig

pytestmark = pytest.mark.integration


async def test_prowlarr_system_status_against_real_container(prowlarr_svc: ServiceConfig) -> None:
    """The simplest read tool. Proves wiring + auth + parsing all work for Prowlarr."""
    from arr_stack_mcp.generated.prowlarr.api.system import get_api_v1_system_status

    client = make_prowlarr_client(prowlarr_svc)
    result = await get_api_v1_system_status.asyncio(client=client)
    assert result is not None
    assert result.version, "Prowlarr should report its version"
    assert result.is_docker is True, "test container should report itself as docker"


async def test_prowlarr_health_endpoint_responds(prowlarr_svc: ServiceConfig) -> None:
    """Health endpoint returns the list of fired health checks. Empty list is the all-clear."""
    from arr_stack_mcp.generated.prowlarr.api.health import get_api_v1_health

    client = make_prowlarr_client(prowlarr_svc)
    items = await get_api_v1_health.asyncio(client=client)
    assert isinstance(items, list)


async def test_prowlarr_indexer_list_is_empty_on_fresh_stack(prowlarr_svc: ServiceConfig) -> None:
    """Fresh container has no configured indexers — list returns empty."""
    from arr_stack_mcp.generated.prowlarr.api.indexer import get_api_v1_indexer

    client = make_prowlarr_client(prowlarr_svc)
    indexers = await get_api_v1_indexer.asyncio(client=client)
    assert isinstance(indexers, list)
    assert len(indexers) == 0


async def test_prowlarr_indexer_stats_returns_payload(prowlarr_svc: ServiceConfig) -> None:
    """Stats endpoint returns a payload even with no indexers (empty `indexers` list inside)."""
    from arr_stack_mcp.generated.prowlarr.api.indexer_stats import get_api_v1_indexerstats

    client = make_prowlarr_client(prowlarr_svc)
    page = await get_api_v1_indexerstats.asyncio(client=client)
    assert page is not None


async def test_prowlarr_indexer_status_endpoint_responds(prowlarr_svc: ServiceConfig) -> None:
    """Status endpoint lists failing indexers. Fresh container = empty list."""
    from arr_stack_mcp.generated.prowlarr.api.indexer_status import get_api_v1_indexerstatus

    client = make_prowlarr_client(prowlarr_svc)
    rows = await get_api_v1_indexerstatus.asyncio(client=client)
    assert isinstance(rows, list)
