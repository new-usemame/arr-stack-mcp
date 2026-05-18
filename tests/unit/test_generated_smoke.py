"""Smoke tests for the generated clients.

These run no HTTP traffic — they only verify the generated packages import,
their Client / AuthenticatedClient classes exist, and the expected api / models
sub-packages are present. Real-network exercise lives in tests/integration/.
"""

from __future__ import annotations

import importlib
import pkgutil

import pytest

GENERATED_SERVICES = ["sonarr", "radarr", "lidarr", "prowlarr", "jellyfin"]


@pytest.mark.parametrize("service", GENERATED_SERVICES)
def test_client_classes_exist(service: str) -> None:
    mod = importlib.import_module(f"arr_stack_mcp.generated.{service}.client")
    assert hasattr(mod, "Client"), f"{service}: no Client class"
    assert hasattr(mod, "AuthenticatedClient"), f"{service}: no AuthenticatedClient class"


@pytest.mark.parametrize("service", GENERATED_SERVICES)
def test_api_subpackage_has_modules(service: str) -> None:
    api_pkg = importlib.import_module(f"arr_stack_mcp.generated.{service}.api")
    submodules = [m.name for m in pkgutil.iter_modules(api_pkg.__path__)]
    assert len(submodules) > 0, f"{service}: api/ is empty"


@pytest.mark.parametrize("service", GENERATED_SERVICES)
def test_models_subpackage_has_models(service: str) -> None:
    models = importlib.import_module(f"arr_stack_mcp.generated.{service}.models")
    # Every generated client should export at least some pydantic model classes
    # at the top level of models/.
    public = [n for n in dir(models) if not n.startswith("_")]
    assert len(public) > 0, f"{service}: models exports nothing"


def test_sonarr_has_series_api() -> None:
    """Sonarr's primary tag is Series — assert that namespace is present."""
    api_series = importlib.import_module("arr_stack_mcp.generated.sonarr.api.series")
    # The generator emits one module per tag, with one submodule per operationId.
    submodules = [m.name for m in pkgutil.iter_modules(api_series.__path__)]
    assert any("series" in m.lower() for m in submodules), f"sonarr.api.series has no series-related submodules: {submodules}"


def test_jellyfin_has_library_api() -> None:
    """Jellyfin's primary tag for browsing is Library."""
    api_lib = importlib.import_module("arr_stack_mcp.generated.jellyfin.api.library")
    submodules = [m.name for m in pkgutil.iter_modules(api_lib.__path__)]
    assert len(submodules) > 0, "jellyfin.api.library has no submodules"
