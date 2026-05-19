"""Init wizard probe widening.

The current `_probe_services` tries every service against a small grid of
(host, scheme) combinations: localhost, 127.0.0.1, host.docker.internal, the
service's docker-compose hostname, and the `.lan` mDNS suffix of that
hostname. First successful response (200 or 401) wins.

See notes/DESIGN-v0.2.md §1.6. Real users running their arrs at
`host.docker.internal` (Docker Desktop on Mac/Win), docker-compose service
hostnames (`sonarr:8989`), or `teenyverse.lan`-style mDNS would all show as
"not found" under the v0.1 localhost-only probe.

Tests mock the httpx call to control which combinations "respond."
"""

from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

import httpx
import pytest

from arr_stack_mcp.config import (
    _PROBE_HOSTS_GENERIC,
    _PROBE_SCHEMES,
    _candidate_hosts_for,
    _probe_one,
    _probe_service,
    _probe_services,
)

# ---------- _candidate_hosts_for ----------


def test_candidate_hosts_includes_generic_loopbacks() -> None:
    hosts = _candidate_hosts_for("sonarr")
    for h in ("localhost", "127.0.0.1", "host.docker.internal"):
        assert h in hosts


def test_candidate_hosts_includes_service_name() -> None:
    """docker-compose deployments expose each service by its compose service name (`sonarr:8989`)."""
    hosts = _candidate_hosts_for("sonarr")
    assert "sonarr" in hosts


def test_candidate_hosts_includes_mdns_lan_suffix() -> None:
    """mDNS deployments expose hosts as `teenyverse.lan` / `sonarr.lan`."""
    hosts = _candidate_hosts_for("sonarr")
    assert "sonarr.lan" in hosts


def test_candidate_hosts_distinct_per_service() -> None:
    sonarr_hosts = _candidate_hosts_for("sonarr")
    radarr_hosts = _candidate_hosts_for("radarr")
    # Both share the generic loopback hosts; only the service-specific
    # entries differ.
    assert "sonarr" in sonarr_hosts
    assert "sonarr" not in radarr_hosts
    assert "radarr" in radarr_hosts
    assert "radarr" not in sonarr_hosts


def test_probe_scheme_pair() -> None:
    """Both schemes are always tried — local dev clusters routinely use self-signed HTTPS."""
    assert "http" in _PROBE_SCHEMES
    assert "https" in _PROBE_SCHEMES


def test_probe_generic_hosts_is_tuple() -> None:
    """Constant should be immutable; reassignment in tests would otherwise mask bugs."""
    assert isinstance(_PROBE_HOSTS_GENERIC, tuple)


# ---------- _probe_one ----------


@contextmanager
def _patch_get(monkeypatch: pytest.MonkeyPatch, status_codes_by_url: dict[str, int | type[Exception]]) -> Iterator[None]:
    """Patch httpx.AsyncClient.get to return synthetic responses per URL."""

    class _FakeResp:
        def __init__(self, status: int) -> None:
            self.status_code = status

    async def _fake_get(self: Any, url: str, **kwargs: Any) -> _FakeResp:
        result = status_codes_by_url.get(url)
        if isinstance(result, type) and issubclass(result, Exception):
            raise result(f"simulated for {url}")
        return _FakeResp(result if isinstance(result, int) else 500)

    monkeypatch.setattr("httpx.AsyncClient.get", _fake_get)
    yield


async def test_probe_one_accepts_200(monkeypatch: pytest.MonkeyPatch) -> None:
    with _patch_get(monkeypatch, {"http://localhost:8989/api/v3/system/status": 200}):
        assert await _probe_one("http", "localhost", 8989, "/api/v3/system/status") is True


async def test_probe_one_accepts_401(monkeypatch: pytest.MonkeyPatch) -> None:
    """401 means the service is up but the request lacks an API key — counts as present."""
    with _patch_get(monkeypatch, {"http://localhost:8989/api/v3/system/status": 401}):
        assert await _probe_one("http", "localhost", 8989, "/api/v3/system/status") is True


async def test_probe_one_rejects_404(monkeypatch: pytest.MonkeyPatch) -> None:
    with _patch_get(monkeypatch, {"http://localhost:8989/api/v3/system/status": 404}):
        assert await _probe_one("http", "localhost", 8989, "/api/v3/system/status") is False


async def test_probe_one_handles_connection_error(monkeypatch: pytest.MonkeyPatch) -> None:
    with _patch_get(monkeypatch, {"http://localhost:8989/api/v3/system/status": httpx.ConnectError}):
        assert await _probe_one("http", "localhost", 8989, "/api/v3/system/status") is False


async def test_probe_one_handles_timeout(monkeypatch: pytest.MonkeyPatch) -> None:
    with _patch_get(monkeypatch, {"http://localhost:8989/api/v3/system/status": httpx.TimeoutException}):
        assert await _probe_one("http", "localhost", 8989, "/api/v3/system/status") is False


# ---------- _probe_service ----------


async def test_probe_service_returns_first_hit(monkeypatch: pytest.MonkeyPatch) -> None:
    """A single working (host, scheme) wins. The probe doesn't depend on the others succeeding."""
    only_working = "http://host.docker.internal:8989/api/v3/system/status"
    # Default: everything else returns 500 (counts as miss). Just the one hit.
    with _patch_get(monkeypatch, {only_working: 200}):
        svc, url = await _probe_service("sonarr", 8989, "/api/v3/system/status")
    assert svc == "sonarr"
    assert url == "http://host.docker.internal:8989"


async def test_probe_service_returns_none_when_all_fail(monkeypatch: pytest.MonkeyPatch) -> None:
    with _patch_get(monkeypatch, {}):  # every URL gets default-500
        svc, url = await _probe_service("sonarr", 8989, "/api/v3/system/status")
    assert svc == "sonarr"
    assert url is None


async def test_probe_service_first_in_order_wins(monkeypatch: pytest.MonkeyPatch) -> None:
    """When multiple hosts respond, the result is deterministic — `localhost` precedes others in the host order."""
    with _patch_get(
        monkeypatch,
        {
            "http://localhost:8989/api/v3/system/status": 200,
            "http://127.0.0.1:8989/api/v3/system/status": 200,
            "http://host.docker.internal:8989/api/v3/system/status": 200,
        },
    ):
        _svc, url = await _probe_service("sonarr", 8989, "/api/v3/system/status")
    # `localhost` is first in _PROBE_HOSTS_GENERIC, so it wins.
    assert url is not None
    assert url.startswith("http://localhost:")


# ---------- _probe_services sync wrapper ----------


def test_sync_wrapper_runs_all_services(monkeypatch: pytest.MonkeyPatch) -> None:
    """The sync entry point aggregates results for every configured service in _SERVICE_DEFAULT_PORTS."""
    with _patch_get(monkeypatch, {}):  # everything misses
        out = _probe_services()
    # All five services present in the result, all None.
    expected = {"sonarr", "radarr", "lidarr", "prowlarr", "jellyfin"}
    assert set(out.keys()) == expected
    for svc in expected:
        assert out[svc] is None


def test_sync_wrapper_finds_docker_compose_hostname(monkeypatch: pytest.MonkeyPatch) -> None:
    """A docker-compose deployment where `sonarr:8989` resolves should be discovered."""
    targets = {"http://sonarr:8989/api/v3/system/status": 401}
    with _patch_get(monkeypatch, targets):
        out = _probe_services()
    assert out["sonarr"] == "http://sonarr:8989"


def test_sync_wrapper_finds_mdns_hostname(monkeypatch: pytest.MonkeyPatch) -> None:
    """An mDNS deployment where `radarr.lan` resolves should be discovered."""
    targets = {"https://radarr.lan:7878/api/v3/system/status": 200}
    with _patch_get(monkeypatch, targets):
        out = _probe_services()
    assert out["radarr"] == "https://radarr.lan:7878"
