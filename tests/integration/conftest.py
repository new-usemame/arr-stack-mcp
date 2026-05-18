"""Fixtures for integration tests against the dockerised test stack.

The stack is brought up by ``scripts/test-stack-up.sh`` and uses the seeded
API keys defined there. Tests are gated by the ``integration`` marker so
``pytest -q`` (the default) skips them on machines without docker.
"""

from __future__ import annotations

import os

import httpx
import pytest
from pydantic import SecretStr

from arr_stack_mcp.config import ServiceConfig
from arr_stack_mcp.policy import Policy, PolicyConfig

TEST_KEYS = {
    "sonarr": "ar5tcmcptestsonarr00000000000001",
    "radarr": "ar5tcmcptestradarr00000000000002",
    "lidarr": "ar5tcmcptestlidarr00000000000003",
    "prowlarr": "ar5tcmcptestprowlarr0000000000004",
}

TEST_PORTS = {
    "sonarr": 18989,
    "radarr": 17878,
    "lidarr": 18686,
    "prowlarr": 19696,
    "jellyfin": 18096,
}


def _service(name: str, port: int, *, key: str | None) -> ServiceConfig:
    return ServiceConfig.model_validate(
        {
            "name": name,
            "enabled": True,
            "url": f"http://localhost:{port}",
            "api_key": SecretStr(key) if key else None,
            "verify_tls": False,
            "timeout_seconds": 15.0,
        }
    )


def _is_alive(url: str, *, headers: dict[str, str]) -> bool:
    try:
        with httpx.Client(timeout=2.0, verify=False) as c:
            r = c.get(f"{url}/ping", headers=headers)
        return r.status_code < 500
    except httpx.HTTPError:
        return False


def _skip_if_no_stack(svc: str, key: str | None) -> None:
    port = TEST_PORTS[svc]
    headers = {"X-Api-Key": key} if key else {}
    if os.environ.get("CI") and svc not in {"sonarr", "radarr"}:
        # On GitHub-hosted runners we slim the integration matrix; full stack on tag only.
        pytest.skip(f"{svc} skipped on slim-stack CI runner")
    if not _is_alive(f"http://localhost:{port}", headers=headers):
        pytest.skip(f"{svc} test container not running on port {port}")


@pytest.fixture
def sonarr_svc() -> ServiceConfig:
    _skip_if_no_stack("sonarr", TEST_KEYS["sonarr"])
    return _service("sonarr", TEST_PORTS["sonarr"], key=TEST_KEYS["sonarr"])


@pytest.fixture
def radarr_svc() -> ServiceConfig:
    _skip_if_no_stack("radarr", TEST_KEYS["radarr"])
    return _service("radarr", TEST_PORTS["radarr"], key=TEST_KEYS["radarr"])


@pytest.fixture
def lidarr_svc() -> ServiceConfig:
    _skip_if_no_stack("lidarr", TEST_KEYS["lidarr"])
    return _service("lidarr", TEST_PORTS["lidarr"], key=TEST_KEYS["lidarr"])


@pytest.fixture
def prowlarr_svc() -> ServiceConfig:
    _skip_if_no_stack("prowlarr", TEST_KEYS["prowlarr"])
    return _service("prowlarr", TEST_PORTS["prowlarr"], key=TEST_KEYS["prowlarr"])


@pytest.fixture
def integration_policy() -> Policy:
    return Policy.from_config(
        PolicyConfig(read_only=False, disable_destructive=False),
        read_only=False,
        disable_destructive=False,
    )
