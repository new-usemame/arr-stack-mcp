"""Config loading + first-run discovery wizard.

Schema is a thin Pydantic model. Loaded from a YAML file path or
``~/.config/arr-stack-mcp/config.yaml``. Every secret can be supplied via env
var so the YAML can be checked in and the keys provisioned separately.

The init wizard probes a small grid of (host, scheme) combinations per
service — localhost + 127.0.0.1 + host.docker.internal + the docker-compose
service hostname + the same hostname with `.lan` suffix for mDNS — then
writes a starter file. See notes/DESIGN-v0.2.md §1.6.
"""

from __future__ import annotations

import asyncio
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
    typer.echo("Probing localhost, docker-compose hostnames, host.docker.internal, and *.lan mDNS for running services...")
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
    typer.echo(
        "If any service runs behind a reverse proxy (https://sonarr.mydomain.com), the wizard cannot auto-probe it. "
        f"Edit the `url:` for that service in {target} by hand.",
    )


# Hosts the wizard tries for every service, in order of preference. The first
# successful (host, scheme) wins. Operators on reverse-proxied deployments
# (https://sonarr.mydomain.com) cannot be auto-probed — the wizard surfaces a
# reminder to set those URLs manually after writing the starter config.
_PROBE_HOSTS_GENERIC: tuple[str, ...] = ("localhost", "127.0.0.1", "host.docker.internal")
_PROBE_SCHEMES: tuple[str, ...] = ("http", "https")
# Per-probe timeout. Set short so DNS misses (`*.lan` on a network without
# mDNS) and unreachable hosts fail fast.
_PROBE_TIMEOUT_SECONDS: float = 1.5


def _candidate_hosts_for(service: str) -> list[str]:
    """Hosts to probe for one service. Generic loopbacks + the docker-compose service hostname + mDNS."""
    return [*_PROBE_HOSTS_GENERIC, service, f"{service}.lan"]


async def _probe_one(scheme: str, host: str, port: int, path: str) -> bool:
    """Single probe: GET ``{scheme}://{host}:{port}{path}`` and report whether the response looks healthy.

    200 (open) and 401 (up but needs API key) both count as "service present."
    """
    url = f"{scheme}://{host}:{port}{path}"
    try:
        async with httpx.AsyncClient(timeout=_PROBE_TIMEOUT_SECONDS, verify=False) as client:
            resp = await client.get(url)
    except httpx.HTTPError:
        return False
    return resp.status_code in {200, 401}


async def _probe_service(service: str, port: int, path: str) -> tuple[str, str | None]:
    """Probe every (host, scheme) combination for one service. First success wins.

    Probes run concurrently; the first hit determines the result and the
    remaining requests still complete in the background (their results are
    discarded but the connections close cleanly via the asyncgen lifecycle).
    """
    hosts = _candidate_hosts_for(service)
    targets = [(scheme, host) for host in hosts for scheme in _PROBE_SCHEMES]
    results = await asyncio.gather(
        *(_probe_one(scheme, host, port, path) for scheme, host in targets),
        return_exceptions=False,
    )
    for (scheme, host), ok in zip(targets, results, strict=True):
        if ok:
            return service, f"{scheme}://{host}:{port}"
    return service, None


async def _probe_services_async() -> dict[str, str | None]:
    """Probe every configured service concurrently. ~1.5s worst-case wall time."""
    results = await asyncio.gather(
        *(_probe_service(svc, port, _SERVICE_PROBE_PATHS[svc]) for svc, port in _SERVICE_DEFAULT_PORTS.items()),
    )
    return dict(results)


def _probe_services() -> dict[str, str | None]:
    """Sync wrapper for the async probe — keeps ``init_config``'s call-site unchanged.

    Each service is probed against five hosts crossed with two schemes in
    parallel. First successful response (200 or 401) wins.
    """
    return asyncio.run(_probe_services_async())
