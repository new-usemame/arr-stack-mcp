"""Static bearer auth for streamable-HTTP transport.

Covers the `StaticBearerVerifier`, the loopback predicate, the env-var
resolution helper, and the `_resolve_token_verifier` boot policy in
`server.py` that decides whether the server is allowed to start.

See notes/DESIGN-v0.2.md §1.5. The policy:
  - stdio transport => no auth (verifier is None)
  - streamable-HTTP + loopback bind => auth optional (None when no token)
  - streamable-HTTP + non-loopback bind => bearer REQUIRED; refuse boot

Full uvicorn-driven integration of the streamable-HTTP transport is out of
unit-test scope (it would spin a real server). These tests validate the
verifier behavior and the boot policy directly.
"""

from __future__ import annotations

import pytest

from arr_stack_mcp.auth import (
    DEFAULT_BEARER_TOKEN_ENV,
    LOOPBACK_HOSTS,
    StaticBearerVerifier,
    is_loopback_host,
    resolve_bearer_token,
)
from arr_stack_mcp.config import Config, TransportConfig
from arr_stack_mcp.policy import PolicyConfig
from arr_stack_mcp.server import BearerRequired, _resolve_token_verifier

# ---------- StaticBearerVerifier ----------


async def test_verifier_accepts_matching_token() -> None:
    v = StaticBearerVerifier(expected_token="abc123")
    result = await v.verify_token("abc123")
    assert result is not None
    assert result.token == "abc123"
    assert result.client_id == "arr-stack-mcp-bearer"
    assert result.scopes == []


async def test_verifier_rejects_wrong_token() -> None:
    v = StaticBearerVerifier(expected_token="abc123")
    assert await v.verify_token("wrong") is None


async def test_verifier_rejects_empty_token() -> None:
    v = StaticBearerVerifier(expected_token="abc123")
    assert await v.verify_token("") is None


async def test_verifier_rejects_when_expected_empty() -> None:
    """A misconfigured verifier (empty expected token) must refuse every request."""
    v = StaticBearerVerifier(expected_token="")
    assert await v.verify_token("abc123") is None
    assert await v.verify_token("") is None


async def test_verifier_handles_substring_match_safely() -> None:
    """`compare_digest` does not fall back to substring matching; partial matches must fail."""
    v = StaticBearerVerifier(expected_token="abc123def456")
    assert await v.verify_token("abc123") is None
    assert await v.verify_token("abc123def456") is not None
    assert await v.verify_token("abc123def456extra") is None


# ---------- loopback predicate ----------


@pytest.mark.parametrize("host", ["127.0.0.1", "::1", "localhost", "LOCALHOST"])
def test_loopback_detected(host: str) -> None:
    assert is_loopback_host(host) is True


@pytest.mark.parametrize("host", ["0.0.0.0", "192.168.1.10", "10.0.0.5", "::", "example.com", "host.docker.internal"])
def test_non_loopback_detected(host: str) -> None:
    assert is_loopback_host(host) is False


def test_loopback_constant_is_frozen_set() -> None:
    """`LOOPBACK_HOSTS` must be a frozenset so it cannot drift accidentally."""
    assert isinstance(LOOPBACK_HOSTS, frozenset)


# ---------- env-var resolver ----------


def test_resolve_bearer_token_present(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("X_TOK", "secret123")
    assert resolve_bearer_token("X_TOK") == "secret123"


def test_resolve_bearer_token_absent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("X_TOK", raising=False)
    assert resolve_bearer_token("X_TOK") is None


def test_resolve_bearer_token_empty_treated_as_absent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("X_TOK", "")
    assert resolve_bearer_token("X_TOK") is None


def test_default_env_var_name_is_stable() -> None:
    """The default env var name is part of the user-facing contract; pin it."""
    assert DEFAULT_BEARER_TOKEN_ENV == "ARR_STACK_MCP_BEARER_TOKEN"


# ---------- _resolve_token_verifier boot policy ----------


def _cfg(*, http_host: str = "127.0.0.1", http_port: int = 8080) -> Config:
    return Config(
        services={},
        policy=PolicyConfig(),
        transport=TransportConfig(http_host=http_host, http_port=http_port),
    )


def test_stdio_transport_never_constructs_verifier(monkeypatch: pytest.MonkeyPatch) -> None:
    """Stdio is process-local; bearer auth is irrelevant. Even with a token in env, return None."""
    monkeypatch.setenv("ARR_STACK_MCP_BEARER_TOKEN", "abc")
    cfg = _cfg(http_host="0.0.0.0")  # would normally refuse with streamable-http
    assert _resolve_token_verifier(cfg, "stdio", "ARR_STACK_MCP_BEARER_TOKEN") is None


def test_http_loopback_no_token_returns_none(monkeypatch: pytest.MonkeyPatch) -> None:
    """Localhost is trusted by default; bearer is optional. No token -> no verifier (auth disabled)."""
    monkeypatch.delenv("ARR_STACK_MCP_BEARER_TOKEN", raising=False)
    cfg = _cfg(http_host="127.0.0.1")
    assert _resolve_token_verifier(cfg, "streamable-http", "ARR_STACK_MCP_BEARER_TOKEN") is None


def test_http_loopback_with_token_returns_verifier(monkeypatch: pytest.MonkeyPatch) -> None:
    """If the operator sets a token on a loopback bind, use it."""
    monkeypatch.setenv("ARR_STACK_MCP_BEARER_TOKEN", "abc123")
    cfg = _cfg(http_host="127.0.0.1")
    v = _resolve_token_verifier(cfg, "streamable-http", "ARR_STACK_MCP_BEARER_TOKEN")
    assert isinstance(v, StaticBearerVerifier)
    assert v.expected_token == "abc123"


def test_http_non_loopback_no_token_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    """The whole point of 1.5: non-loopback without a bearer is a misconfiguration."""
    monkeypatch.delenv("ARR_STACK_MCP_BEARER_TOKEN", raising=False)
    cfg = _cfg(http_host="0.0.0.0")
    with pytest.raises(BearerRequired) as exc:
        _resolve_token_verifier(cfg, "streamable-http", "ARR_STACK_MCP_BEARER_TOKEN")
    # Error names the env var and the bind so the operator can fix it.
    assert "ARR_STACK_MCP_BEARER_TOKEN" in str(exc.value)
    assert "0.0.0.0" in str(exc.value)


def test_http_non_loopback_with_token_returns_verifier(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ARR_STACK_MCP_BEARER_TOKEN", "secret")
    cfg = _cfg(http_host="192.168.1.10")
    v = _resolve_token_verifier(cfg, "streamable-http", "ARR_STACK_MCP_BEARER_TOKEN")
    assert isinstance(v, StaticBearerVerifier)
    assert v.expected_token == "secret"


def test_custom_env_var_name_honored(monkeypatch: pytest.MonkeyPatch) -> None:
    """`--bearer-token-env` lets operators pick a non-default env var name."""
    monkeypatch.delenv("ARR_STACK_MCP_BEARER_TOKEN", raising=False)
    monkeypatch.setenv("MY_CUSTOM_TOKEN", "from-custom-var")
    cfg = _cfg(http_host="192.168.1.10")
    v = _resolve_token_verifier(cfg, "streamable-http", "MY_CUSTOM_TOKEN")
    assert isinstance(v, StaticBearerVerifier)
    assert v.expected_token == "from-custom-var"
