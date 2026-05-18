"""Shared pytest fixtures."""

from __future__ import annotations

import pytest

from arr_stack_mcp.policy import Policy, PolicyConfig


@pytest.fixture
def policy() -> Policy:
    """Default policy: nothing disabled, confirm required for destructive ops, 60s TTL."""
    cfg = PolicyConfig(
        read_only=False,
        disable_destructive=False,
        confirm_token_ttl_seconds=60,
        require_confirm_for_destructive=True,
    )
    return Policy.from_config(cfg, read_only=False, disable_destructive=False)
