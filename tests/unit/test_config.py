"""Config loading + env-var expansion."""

from __future__ import annotations

from pathlib import Path

import pytest

from arr_stack_mcp.config import Config, ServiceConfig, load_config


def test_load_minimal_yaml(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SONARR_API_KEY", "test-sonarr-key")
    cfg_file = tmp_path / "arr-stack-mcp.yaml"
    cfg_file.write_text(
        """
services:
  sonarr:
    enabled: true
    url: http://localhost:8989
    api_key: ${SONARR_API_KEY}
"""
    )
    cfg = load_config(str(cfg_file))
    assert "sonarr" in cfg.services
    sonarr = cfg.services["sonarr"]
    assert sonarr.name == "sonarr"
    assert sonarr.enabled
    assert sonarr.api_key is not None
    assert sonarr.api_key.get_secret_value() == "test-sonarr-key"


def test_missing_env_var_yields_no_key(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("RADARR_API_KEY", raising=False)
    cfg_file = tmp_path / "arr-stack-mcp.yaml"
    cfg_file.write_text(
        """
services:
  radarr:
    url: http://localhost:7878
    api_key: ${RADARR_API_KEY}
"""
    )
    cfg = load_config(str(cfg_file))
    # Empty env-var expansion is treated as None by the validator.
    assert cfg.services["radarr"].api_key is None


def test_defaults_when_no_config_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    cfg = load_config(None)
    assert isinstance(cfg, Config)
    assert cfg.services == {}
    assert cfg.log_level == "info"


def test_service_config_validates_url() -> None:
    with pytest.raises(ValueError, match="url"):
        ServiceConfig.model_validate({"name": "sonarr", "url": "not-a-url"})


def test_config_rejects_non_mapping_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    cfg_file = tmp_path / "bad.yaml"
    cfg_file.write_text("- just\n- a\n- list\n")
    monkeypatch.chdir(tmp_path)
    with pytest.raises(TypeError, match="must be a mapping"):
        load_config(str(cfg_file))
