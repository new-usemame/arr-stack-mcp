"""Config loading + first-run discovery wizard.

Schema is a thin Pydantic model. Loaded from a YAML file path or
``~/.config/arr-stack-mcp/config.yaml``. Every secret can be supplied via env
var so the YAML can be checked in and the keys provisioned separately.

The init wizard probes localhost ports and common docker-compose hostnames
(sonarr / radarr / lidarr / prowlarr / jellyfin), then writes a starter file.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Self

import httpx
import structlog
import typer
import yaml
from pydantic import BaseModel, Field, HttpUrl, SecretStr, field_validator

from arr_stack_mcp.policy import PolicyConfig

log = structlog.get_logger(__name__)

# Resolves ${VAR} or ${VAR:-default} forms. Unlike os.path.expandvars, an unset
# var without a default yields "" (empty string) rather than the literal
# ${VAR} text — that lets Pydantic validators map "" → None for optional fields.
_ENV_REF = re.compile(r"\$\{([A-Z_][A-Z0-9_]*)(?::-(.*?))?\}")


_SERVICE_DEFAULT_PORTS = {
    "sonarr": 8989,
    "radarr": 7878,
    "lidarr": 8686,
    "prowlarr": 9696,
    "jellyfin": 8096,
}

_SERVICE_PROBE_PATHS = {
    "sonarr": "/api/v3/system/status",
    "radarr": "/api/v3/system/status",
    "lidarr": "/api/v1/system/status",
    "prowlarr": "/api/v1/system/status",
    "jellyfin": "/System/Info/Public",
}


class TransportConfig(BaseModel):
    stdio: bool = True
    http_enabled: bool = False
    http_host: str = "127.0.0.1"
    http_port: int = 8080


class ServiceConfig(BaseModel):
    name: str
    enabled: bool = True
    url: HttpUrl
    api_key: SecretStr | None = None
    timeout_seconds: float = Field(default=30.0, ge=1.0, le=300.0)
    verify_tls: bool = True
    default_user_id: str | None = None  # Jellyfin only
    disabled_tools: set[str] = Field(default_factory=set)

    @field_validator("api_key", mode="before")
    @classmethod
    def _empty_string_is_none(cls, v: object) -> object:
        # Pydantic-settings env-var substitution can yield empty strings for unset vars; treat as None.
        if v == "":
            return None
        return v


class Config(BaseModel):
    """Top-level config shape."""

    log_level: str = "info"
    transport: TransportConfig = Field(default_factory=TransportConfig)
    policy: PolicyConfig = Field(default_factory=PolicyConfig)
    services: dict[str, ServiceConfig] = Field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> Self:
        # Inject `name` into each service config from its dict key.
        services_raw = data.get("services", {}) or {}
        if isinstance(services_raw, dict):
            services_with_names = {name: {**svc, "name": name} for name, svc in services_raw.items() if isinstance(svc, dict)}
            data = {**data, "services": services_with_names}
        return cls.model_validate(data)


def load_config(path: str | None) -> Config:
    """Load YAML config from `path`, falling back to env-var-driven defaults.

    Performs env-var substitution (``${SONARR_API_KEY}`` →
    ``os.environ['SONARR_API_KEY']``) inline.
    """
    config_path = _resolve_path(path)
    if config_path is not None and config_path.exists():
        log.info("loading config", path=str(config_path))
        raw_loaded: object = yaml.safe_load(config_path.read_text()) or {}
    else:
        log.info("no config file found; using env-var defaults")
        raw_loaded = {}
    expanded = _expand_env(raw_loaded)
    if not isinstance(expanded, dict):
        raise TypeError(f"config root must be a mapping, got {type(expanded).__name__}")
    return Config.from_dict(expanded)


def _resolve_path(path: str | None) -> Path | None:
    """Find the config file. CLI arg wins; then ./arr-stack-mcp.yaml; then XDG."""
    if path:
        return Path(path).expanduser().resolve()
    cwd_local = Path.cwd() / "arr-stack-mcp.yaml"
    if cwd_local.exists():
        return cwd_local
    xdg = Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config"))).expanduser()
    xdg_config = xdg / "arr-stack-mcp" / "config.yaml"
    if xdg_config.exists():
        return xdg_config
    return None


def _expand_env(node: object) -> object:
    """Recursively expand ``${VAR}`` and ``${VAR:-default}`` references against os.environ.

    Unset var with no default → empty string. Pydantic validators map empty
    strings back to None for SecretStr fields, so omitting an API key env var
    is the canonical way to disable a service.
    """
    if isinstance(node, dict):
        return {k: _expand_env(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_expand_env(v) for v in node]
    if isinstance(node, str):
        return _ENV_REF.sub(lambda m: os.environ.get(m.group(1), m.group(2) or ""), node)
    return node


def init_config(*, out_path: str, force: bool) -> None:
    """First-run wizard. Probes the local network and writes a starter config."""
    target = Path(out_path).expanduser().resolve()
    if target.exists() and not force:
        confirm = typer.confirm(f"{target} exists. Overwrite?")
        if not confirm:
            typer.echo("aborted")
            raise typer.Exit(code=1)

    typer.echo("== arr-stack-mcp init ==")
    typer.echo("Probing localhost for running services...")
    found = _probe_services()
    for svc, url in found.items():
        typer.echo(f"  {svc}: {url or 'not found'}")

    services_section: dict[str, dict[str, object]] = {}
    for svc, default_port in _SERVICE_DEFAULT_PORTS.items():
        probed = found.get(svc)
        url = probed or f"http://localhost:{default_port}"
        env_var = f"{svc.upper()}_API_KEY"
        services_section[svc] = {
            "enabled": probed is not None,
            "url": url,
            "api_key": f"${{{env_var}}}",
        }

    template = {
        "log_level": "info",
        "transport": {"stdio": True, "http_enabled": False},
        "policy": {
            "read_only": False,
            "disable_destructive": False,
            "confirm_token_ttl_seconds": 300,
        },
        "services": services_section,
    }
    target.write_text(yaml.safe_dump(template, sort_keys=False))
    typer.echo(f"Wrote {target}")
    typer.echo("Next: set API keys via env vars (SONARR_API_KEY, etc.), then run `arr-stack-mcp serve`.")


def _probe_services() -> dict[str, str | None]:
    """Probe localhost for each service. Returns the URL if a service responds within 1 second, else None. Pure GET, no mutation."""
    found: dict[str, str | None] = {}
    for svc, port in _SERVICE_DEFAULT_PORTS.items():
        path = _SERVICE_PROBE_PATHS[svc]
        for scheme in ("http", "https"):
            url = f"{scheme}://localhost:{port}"
            try:
                # Probe accepts self-signed certs — local dev clusters routinely use them.
                with httpx.Client(timeout=1.0, verify=False) as client:
                    resp = client.get(f"{url}{path}")
                if resp.status_code in {200, 401}:  # 401 = service is up but needs key
                    found[svc] = url
                    break
            except httpx.HTTPError:
                continue
        else:
            found[svc] = None
    return found
