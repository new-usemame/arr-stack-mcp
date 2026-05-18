"""Diagnostic error envelopes.

Surfaced to the MCP client as structured tool errors with self-suggesting next steps.
"""

from __future__ import annotations

from pydantic import BaseModel


class ToolError(Exception):
    """Base class for every error arr-stack-mcp tools raise.

    Carries a structured payload that gets serialized into the MCP error response
    so an LLM consumer can decide what to do next.
    """

    code: str = "tool_error"

    def __init__(self, *, message: str, hint: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.hint = hint

    def to_envelope(self) -> ErrorEnvelope:
        return ErrorEnvelope(code=self.code, message=self.message, hint=self.hint)


class PolicyDenied(ToolError):
    """The active server flags (read-only / disable-destructive) blocked this tool.

    Tells the agent the call shape was valid; the *server posture* is the problem.
    """

    code = "policy_denied"

    def __init__(self, *, tool: str, reason: str, hint: str | None = None) -> None:
        super().__init__(message=f"{tool}: {reason}", hint=hint)


class ConfirmRequired(ToolError):
    """The tool would mutate destructive state and no valid confirm token was supplied.

    The caller should re-invoke the tool first with no token to receive a plan + token,
    then invoke again with the token to execute.
    """

    code = "confirm_required"

    def __init__(self, *, tool: str, reason: str | None = None) -> None:
        msg = reason or (
            f"{tool} is destructive — call once with no confirm_token to receive a plan, then again with the returned token to execute"
        )
        super().__init__(
            message=msg,
            hint="set needs_confirm=true in the plan reply; the user must explicitly authorize the second call",
        )


class UpstreamUnavailable(ToolError):
    """The underlying arr / Jellyfin service did not respond.

    Different from a 4xx because the action wasn't even attempted — retry may help.
    """

    code = "upstream_unavailable"

    def __init__(self, *, service: str, url: str, cause: str) -> None:
        super().__init__(
            message=f"{service} at {url} did not respond ({cause})",
            hint=(f"check the service is running and that the URL is reachable; try `{service}.system_status` to verify connectivity"),
        )


class UpstreamAuthFailed(ToolError):
    """The arr / Jellyfin service returned 401/403.

    The action wasn't attempted server-side; the API key is wrong or rotated.
    """

    code = "upstream_auth_failed"

    def __init__(self, *, service: str) -> None:
        super().__init__(
            message=f"{service} rejected our API key (401/403)",
            hint=(
                f"the {service} key may have rotated. For Prowlarr this happens on every container reset. "
                f"Pull the live key from /config/config.xml and re-run `arr-stack-mcp init` or set the env var."
            ),
        )


class UpstreamBadRequest(ToolError):
    """The arr / Jellyfin service returned a non-auth 4xx.

    Usually a shape mismatch — likely the generated client lags upstream.
    """

    code = "upstream_bad_request"

    def __init__(self, *, service: str, status: int, body: str) -> None:
        super().__init__(
            message=f"{service} rejected the request with HTTP {status}",
            hint=(
                "this usually means the generated client is out of sync with the running version. "
                "Run `scripts/regen-clients.sh --check` to compare. The raw response body is in this error for diagnosis."
            ),
        )
        self.body = body


class Ambiguous(ToolError):
    """A free-text lookup matched multiple library rows.

    Returned with `candidates` so the agent can disambiguate by id.
    """

    code = "ambiguous"

    def __init__(self, *, tool: str, query: str, candidates: list[dict[str, object]]) -> None:
        super().__init__(
            message=f"{tool}: query {query!r} matched {len(candidates)} rows",
            hint="retry with the stable id from candidates[]",
        )
        self.candidates = candidates


class ErrorEnvelope(BaseModel):
    """Wire shape every ToolError gets serialized into."""

    code: str
    message: str
    hint: str | None = None
