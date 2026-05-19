"""Policy: confirm tokens, tag-based gating (read / write / destructive), flag-driven risk-tolerance."""

from __future__ import annotations

import secrets
import time
from collections import deque
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Self

from pydantic import BaseModel, Field

from arr_stack_mcp.errors import ConfirmRequired, PolicyDenied

# Ring-buffer cap for the dry-run log surfaced by `stack.dryrun_log`. The buffer
# is per-process and lossy on the older end — the goal is "show me the last N
# would-have-fired mutations," not durable audit.
DRYRUN_LOG_CAPACITY: int = 200


class Tag(StrEnum):
    """Per-tool risk tag. Used to decide whether a flag-driven mode blocks the call and whether a confirm token is required."""

    READ = "read"
    WRITE = "write"
    DESTRUCTIVE = "destructive"


class PolicyConfig(BaseModel):
    """Config-driven policy knobs. Loaded from arr-stack-mcp.yaml under `policy:`."""

    read_only: bool = False
    disable_destructive: bool = False
    dry_run: bool = False
    confirm_token_ttl_seconds: int = Field(default=300, ge=10, le=3600)
    require_confirm_for_destructive: bool = True
    # Per-tool, per-hour call cap. Off by default — entries are opt-in. Catches
    # runaway-agent loops (a misbehaving consumer hitting one tool 1000x in
    # five minutes). Per-process; not per-user. The bot-side per-user-per-day
    # caps in ibis-bot live at the bot layer and stay there. Each entry maps a
    # tool name (e.g. "sonarr.series_add") to the maximum number of calls in
    # any rolling hour-window. See notes/DESIGN-v0.2.md §1.4.
    hourly_caps: dict[str, int] = Field(default_factory=dict)


@dataclass
class _PendingToken:
    token: str
    tool_name: str
    expires_at: float
    payload_fingerprint: str


@dataclass
class Policy:
    """Live policy enforcement. Owns the confirm-token cache + dry-run ring buffer + hourly cap counters."""

    read_only: bool
    disable_destructive: bool
    dry_run: bool
    require_confirm_for_destructive: bool
    confirm_token_ttl_seconds: int
    hourly_caps: dict[str, int] = field(default_factory=dict)
    _tokens: dict[str, _PendingToken] = field(default_factory=dict)
    # Bounded ring buffer of recorded would-have-fired mutations. Surfaced via
    # the `stack.dryrun_log` tool. Per-process; not persisted.
    _dryrun_log: deque[dict[str, object]] = field(default_factory=lambda: deque(maxlen=DRYRUN_LOG_CAPACITY))
    # (epoch_hour, tool_name) -> call count this hour. Per-process; not persisted.
    _hourly_counters: dict[tuple[int, str], int] = field(default_factory=dict)

    @classmethod
    def from_config(cls, cfg: PolicyConfig, *, read_only: bool, disable_destructive: bool, dry_run: bool = False) -> Self:
        return cls(
            read_only=read_only,
            disable_destructive=disable_destructive,
            dry_run=dry_run or cfg.dry_run,
            require_confirm_for_destructive=cfg.require_confirm_for_destructive,
            confirm_token_ttl_seconds=cfg.confirm_token_ttl_seconds,
            hourly_caps=dict(cfg.hourly_caps),
        )

    # --- dry-run ring buffer ------------------------------------------------

    def record_dryrun(self, tool_name: str, payload: dict[str, object]) -> None:
        """Append a would-have-fired mutation to the ring buffer.

        Called by ``tools.common.dryrun_short_circuit`` after the read-side
        prep (lookups, confirm-token validation) but BEFORE the upstream
        mutating call. ``payload`` should be a JSON-safe dict — usually the
        model_dump of the request body the upstream client would have sent.
        """
        self._dryrun_log.append(
            {
                "tool_name": tool_name,
                "recorded_at": time.time(),
                "payload": payload,
            }
        )

    def dryrun_log(self, *, limit: int | None = None) -> list[dict[str, object]]:
        """Return the recorded dry-run entries, newest-last.

        ``limit`` trims to the most recent ``limit`` entries when set.
        """
        entries = list(self._dryrun_log)
        if limit is not None and limit > 0:
            entries = entries[-limit:]
        return entries

    def clear_dryrun_log(self) -> None:
        """Reset the ring buffer. Test affordance; not exposed as a tool."""
        self._dryrun_log.clear()

    def check(self, tool_name: str, tag: Tag) -> None:
        """Raise PolicyDenied if any active gate blocks this tool. Called at the top of every tool implementation.

        Gate order (each raises PolicyDenied on miss):
          1. read-only mode (rejects WRITE + DESTRUCTIVE)
          2. disable-destructive mode (rejects DESTRUCTIVE)
          3. hourly cap (rejects any tool that has exhausted its rolling hour budget)

        Every call that passes all three gates is counted toward the hourly
        cap, so failed upstream calls still consume budget (intentional — a
        runaway agent retrying a failing call should hit the cap on the
        Nth attempt rather than burning the budget unaccounted).
        """
        if tag in {Tag.WRITE, Tag.DESTRUCTIVE} and self.read_only:
            raise PolicyDenied(
                tool=tool_name,
                reason="server started with --read-only; this tool would mutate state",
                hint="restart without --read-only or call a `*.search` / `*.status` tool instead",
            )
        if tag is Tag.DESTRUCTIVE and self.disable_destructive:
            raise PolicyDenied(
                tool=tool_name,
                reason="server started with --disable-destructive; this tool would delete data",
                hint="restart without --disable-destructive, or use the non-destructive equivalent",
            )
        self._check_and_count_hourly(tool_name)

    def _check_and_count_hourly(self, tool_name: str) -> None:
        """Enforce the per-tool hourly cap and increment the counter.

        Uncapped tools (no entry or entry <= 0 in ``hourly_caps``) are passed
        through without bookkeeping. For capped tools, the current epoch hour
        is the rollover boundary — a call at HH:59 and a call at HH+1:00 are
        in different buckets.

        Older buckets are swept opportunistically (drops counters from before
        the previous hour) to keep the dict bounded.
        """
        cap = self.hourly_caps.get(tool_name, 0)
        if cap <= 0:
            return
        hour = int(time.time() // 3600)
        self._sweep_hourly(hour)
        key = (hour, tool_name)
        count = self._hourly_counters.get(key, 0)
        if count >= cap:
            raise PolicyDenied(
                tool=tool_name,
                reason=f"hourly cap reached: {tool_name} has fired {count} times this hour (cap {cap})",
                hint=(
                    "wait for the hour boundary, raise the cap in `policy.hourly_caps`, "
                    "or remove the cap entry to disable it for this tool"
                ),
            )
        self._hourly_counters[key] = count + 1

    def _sweep_hourly(self, current_hour: int) -> None:
        """Drop hourly-counter buckets older than the previous hour. Cheap; bounded by tool count."""
        stale = [k for k in self._hourly_counters if k[0] < current_hour - 1]
        for k in stale:
            self._hourly_counters.pop(k, None)

    def issue_token(self, tool_name: str, payload_fingerprint: str) -> str:
        """Issue a single-use, time-limited confirm token.

        Returned to the caller; the caller is expected to invoke the tool a
        second time with ``confirm_token=<the returned value>``.
        """
        self._sweep()
        token = secrets.token_urlsafe(16)
        self._tokens[token] = _PendingToken(
            token=token,
            tool_name=tool_name,
            expires_at=time.monotonic() + self.confirm_token_ttl_seconds,
            payload_fingerprint=payload_fingerprint,
        )
        return token

    def consume_token(self, tool_name: str, payload_fingerprint: str, confirm_token: str | None) -> None:
        """Consume a confirm token. Raises ConfirmRequired if absent, mismatched, or expired."""
        self._sweep()
        if confirm_token is None:
            raise ConfirmRequired(tool=tool_name)
        pending = self._tokens.pop(confirm_token, None)
        if pending is None:
            raise ConfirmRequired(
                tool=tool_name,
                reason="confirm token unknown, already used, or expired",
            )
        if pending.tool_name != tool_name:
            raise ConfirmRequired(
                tool=tool_name,
                reason=f"confirm token belongs to a different tool ({pending.tool_name!r})",
            )
        if pending.payload_fingerprint != payload_fingerprint:
            raise ConfirmRequired(
                tool=tool_name,
                reason="confirm token does not match the current request; the agent must re-issue the plan",
            )

    def _sweep(self) -> None:
        """Drop tokens past their TTL. Called inside every issue/consume to keep the cache bounded."""
        now = time.monotonic()
        expired = [t for t, p in self._tokens.items() if p.expires_at < now]
        for t in expired:
            self._tokens.pop(t, None)


def fingerprint(payload: object) -> str:
    """Stable fingerprint of a request payload used to bind a confirm token to its plan.

    Deliberately not cryptographic — collisions are tolerated in exchange for shape stability.
    """
    import hashlib
    import json

    blob = json.dumps(payload, sort_keys=True, default=str).encode()
    return hashlib.sha256(blob).hexdigest()[:16]
