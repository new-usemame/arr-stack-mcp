"""Static bearer-token verifier for the streamable-HTTP transport.

FastMCP accepts a `TokenVerifier` protocol implementation via its
`token_verifier=` constructor argument. The protocol is a single async method:
``verify_token(token: str) -> AccessToken | None`` — non-None grants the
request access, None refuses it.

For the MCP-server use case here, full OAuth is overkill: a single static
bearer token configured at boot is enough. This module ships that minimum.
The token is read from an environment variable so it never lands in YAML or
on the command line where ps or shell history could log it. Comparison uses
`secrets.compare_digest` so a partial match does not leak via timing.

See notes/DESIGN-v0.2.md §1.5 for the design choice — `auth: AuthSettings`
(the OAuth metadata path) is not used; passing only `token_verifier=` to
FastMCP enforces bearer without the OAuth Protected Resource Metadata
endpoints, which we have no need to advertise.

Boot-time policy (enforced by `server.run` at startup):
  - stdio transport: auth is irrelevant; the verifier is not constructed
  - streamable-HTTP transport on a loopback bind (`127.0.0.1`, `::1`,
    `localhost`): bearer is OPTIONAL — operators on localhost can opt out
  - streamable-HTTP transport on any other bind: bearer is REQUIRED — start
    refuses with a clear error if the env var is not set
"""

from __future__ import annotations

import os
import secrets
from dataclasses import dataclass

from mcp.server.auth.provider import AccessToken, TokenVerifier

# Loopback host strings the boot-time check treats as "auth optional." Any
# other bind requires a bearer token.
LOOPBACK_HOSTS: frozenset[str] = frozenset({"127.0.0.1", "::1", "localhost"})

# Default env var name. The operator can override per call via the
# `--bearer-token-env` flag if they want a non-default name.
DEFAULT_BEARER_TOKEN_ENV: str = "ARR_STACK_MCP_BEARER_TOKEN"


@dataclass
class StaticBearerVerifier(TokenVerifier):
    """Constant-time-compare a single fixed bearer token against incoming requests.

    The expected token is captured at construction (typically by reading the
    env var named at server boot). `verify_token` returns a minimal
    `AccessToken` on match, `None` otherwise.

    The comparison uses `secrets.compare_digest`, which runs in time
    proportional to the longer of the two strings rather than to the index
    of the first divergence — a timing-side-channel-tolerant compare.
    """

    expected_token: str
    client_id: str = "arr-stack-mcp-bearer"

    async def verify_token(self, token: str) -> AccessToken | None:
        if not token or not self.expected_token:
            return None
        if not secrets.compare_digest(token, self.expected_token):
            return None
        return AccessToken(
            token=token,
            client_id=self.client_id,
            scopes=[],
            expires_at=None,
        )


def is_loopback_host(host: str) -> bool:
    """True if the given bind host is a loopback alias.

    Bare-bones — does not resolve DNS or inspect ip ranges, matches the
    literal strings we recognize as loopback. An operator who binds to a
    DNS name that resolves to 127.0.0.1 still gets "non-loopback" treatment
    here, which is the safer default (require bearer).
    """
    return host.lower() in LOOPBACK_HOSTS


def resolve_bearer_token(env_var: str) -> str | None:
    """Read the bearer token from the named env var. Empty string treated as unset."""
    val = os.environ.get(env_var, "")
    return val or None
