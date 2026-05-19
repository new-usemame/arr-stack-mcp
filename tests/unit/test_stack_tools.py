"""`stack.*` cross-service tools — dryrun_log + report_issue + health.

See notes/DESIGN-v0.2.md §2.2.

Each tool is exercised at the registered-on-FastMCP level: a fresh FastMCP
instance gets stack tools registered, and the handler is called by name.
Pure-function helpers (`_compose_issue_body`) are tested directly. The
aggregating tools (`stack.queue_status_all`, `stack.find_anywhere`) land in
a follow-up commit.
"""

from __future__ import annotations

import json
import urllib.parse
from typing import Any

from arr_stack_mcp.config import Config
from arr_stack_mcp.policy import Policy, PolicyConfig
from arr_stack_mcp.tools.stack._models import (
    DryRunLogInput,
    ReportIssueInput,
    StackHealthInput,
)
from arr_stack_mcp.tools.stack.tools import _compose_issue_body, _gather_health


def _policy(*, dry_run: bool = False) -> Policy:
    return Policy.from_config(PolicyConfig(dry_run=dry_run), read_only=False, disable_destructive=False, dry_run=dry_run)


# We exercise the tool handlers via the same FastMCP instance the runtime uses.
# That ensures the @mcp.tool registration path actually wires up correctly.
class _StubMCP:
    """Captures `@mcp.tool` decorated handlers so tests can call them directly."""

    def __init__(self) -> None:
        self.handlers: dict[str, object] = {}

    def tool(self, *, name: str, description: str) -> Any:
        # `description` is unused here — we mirror FastMCP's tool() signature
        # for fidelity, but only capture the handler so tests can call it.
        del description

        def _decorator(fn: Any) -> Any:
            self.handlers[name] = fn
            return fn

        return _decorator


def _register_stack(policy: Policy, cfg: Config | None = None) -> _StubMCP:
    from arr_stack_mcp.tools.stack.tools import register_all

    stub = _StubMCP()
    register_all(stub, cfg or Config(), policy)  # type: ignore[arg-type]
    return stub


# ---------- stack.dryrun_log ----------


async def test_dryrun_log_returns_empty_when_buffer_empty() -> None:
    p = _policy(dry_run=True)
    mcp = _register_stack(p)
    handler = mcp.handlers["stack.dryrun_log"]
    result = await handler(DryRunLogInput())  # type: ignore[operator]
    assert result.count == 0
    assert result.entries == []


async def test_dryrun_log_returns_recorded_entries() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("sonarr.series_add", {"tvdb_id": 42})
    p.record_dryrun("radarr.movie_delete", {"radarr_id": 7, "delete_files": True})
    mcp = _register_stack(p)
    handler = mcp.handlers["stack.dryrun_log"]
    result = await handler(DryRunLogInput())  # type: ignore[operator]
    assert result.count == 2
    assert [e.tool_name for e in result.entries] == ["sonarr.series_add", "radarr.movie_delete"]
    assert result.entries[0].payload == {"tvdb_id": 42}
    assert result.entries[1].payload == {"radarr_id": 7, "delete_files": True}


async def test_dryrun_log_respects_limit() -> None:
    p = _policy(dry_run=True)
    for i in range(10):
        p.record_dryrun(f"tool{i}", {"i": i})
    mcp = _register_stack(p)
    handler = mcp.handlers["stack.dryrun_log"]
    result = await handler(DryRunLogInput(limit=3))  # type: ignore[operator]
    assert result.count == 3
    # Newest three.
    assert [e.tool_name for e in result.entries] == ["tool7", "tool8", "tool9"]


# ---------- stack.report_issue ----------


async def test_report_issue_returns_well_formed_url() -> None:
    p = _policy()
    mcp = _register_stack(p)
    handler = mcp.handlers["stack.report_issue"]
    result = await handler(  # type: ignore[operator]
        ReportIssueInput(summary="series_add returned None", detail="Got an empty body after POST.")
    )
    assert result.repo == "new-usemame/arr-stack-mcp"
    assert result.url.startswith("https://github.com/new-usemame/arr-stack-mcp/issues/new?")
    # The URL must carry the title and body as query params.
    parsed = urllib.parse.urlparse(result.url)
    params = urllib.parse.parse_qs(parsed.query)
    assert params["title"] == ["series_add returned None"]
    assert "Got an empty body after POST." in params["body"][0]


async def test_report_issue_omits_dryrun_log_by_default() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("sonarr.series_add", {"tvdb_id": 42})
    mcp = _register_stack(p)
    handler = mcp.handlers["stack.report_issue"]
    result = await handler(ReportIssueInput(summary="x"))  # type: ignore[operator]
    parsed = urllib.parse.urlparse(result.url)
    params = urllib.parse.parse_qs(parsed.query)
    assert "dry-run log" not in params["body"][0].lower()


async def test_report_issue_includes_dryrun_log_when_flag_set() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("sonarr.series_add", {"tvdb_id": 42})
    mcp = _register_stack(p)
    handler = mcp.handlers["stack.report_issue"]
    result = await handler(  # type: ignore[operator]
        ReportIssueInput(summary="bug", include_dryrun_log=True)
    )
    parsed = urllib.parse.urlparse(result.url)
    body = urllib.parse.parse_qs(parsed.query)["body"][0]
    assert "dry-run log" in body.lower()
    assert "sonarr.series_add" in body


def test_compose_issue_body_minimal() -> None:
    """Body always includes the filed-via line, even without detail or log."""
    p = _policy()
    body = _compose_issue_body(ReportIssueInput(summary="x"), p)
    assert "Filed via `stack.report_issue`" in body
    assert "Detail:" not in body


def test_compose_issue_body_with_detail() -> None:
    p = _policy()
    body = _compose_issue_body(ReportIssueInput(summary="x", detail="The series add returned empty."), p)
    assert "Detail:" in body
    assert "The series add returned empty." in body


def test_compose_issue_body_with_dryrun_log_is_json_block() -> None:
    p = _policy(dry_run=True)
    p.record_dryrun("sonarr.series_add", {"tvdb_id": 42})
    body = _compose_issue_body(ReportIssueInput(summary="x", include_dryrun_log=True), p)
    assert "```json" in body
    # The embedded log must be valid JSON for downstream consumers.
    start = body.index("```json\n") + len("```json\n")
    end = body.index("\n```", start)
    payload = body[start:end]
    parsed = json.loads(payload)
    assert isinstance(parsed, list)
    assert parsed[0]["tool_name"] == "sonarr.series_add"


# ---------- stack.health ----------


async def test_health_no_services_returns_overall_ok_true() -> None:
    """With zero services configured, `overall_ok` is vacuously True (no enabled services to fail)."""
    rows = await _gather_health(Config())
    assert rows == []


async def test_health_handler_returns_ok_envelope_when_no_services() -> None:
    p = _policy()
    mcp = _register_stack(p, Config())
    handler = mcp.handlers["stack.health"]
    result = await handler(StackHealthInput())  # type: ignore[operator]
    assert result.ok is True
    assert result.overall_ok is True
    assert result.services == []


async def test_health_handler_marks_disabled_service() -> None:
    """A disabled service appears with `enabled=False, reachable=False, version=None`."""
    from pydantic import HttpUrl

    from arr_stack_mcp.config import ServiceConfig

    cfg = Config(
        services={"sonarr": ServiceConfig(name="sonarr", enabled=False, url=HttpUrl("http://localhost:8989"))},
        policy=PolicyConfig(),
    )
    p = _policy()
    mcp = _register_stack(p, cfg)
    handler = mcp.handlers["stack.health"]
    result = await handler(StackHealthInput())  # type: ignore[operator]
    assert len(result.services) == 1
    row = result.services[0]
    assert row.name == "sonarr"
    assert row.enabled is False
    assert row.reachable is False
    assert row.version is None
    # Vacuous overall_ok — no enabled services to fail.
    assert result.overall_ok is True


# ---------- stack.find_anywhere ----------


async def test_find_anywhere_no_services_returns_empty() -> None:
    from arr_stack_mcp.tools.stack._models import FindAnywhereInput

    p = _policy()
    mcp = _register_stack(p, Config())
    handler = mcp.handlers["stack.find_anywhere"]
    result = await handler(FindAnywhereInput(query="dune"))  # type: ignore[operator]
    assert result.ok is True
    assert result.query == "dune"
    assert result.total_count == 0
    assert result.sources == []


async def test_find_anywhere_skips_disabled_services() -> None:
    """A disabled arr is omitted from the source list entirely."""
    from pydantic import HttpUrl

    from arr_stack_mcp.config import ServiceConfig
    from arr_stack_mcp.tools.stack._models import FindAnywhereInput

    cfg = Config(
        services={"sonarr": ServiceConfig(name="sonarr", enabled=False, url=HttpUrl("http://localhost:8989"))},
        policy=PolicyConfig(),
    )
    p = _policy()
    mcp = _register_stack(p, cfg)
    handler = mcp.handlers["stack.find_anywhere"]
    result = await handler(FindAnywhereInput(query="dune"))  # type: ignore[operator]
    assert result.sources == []


# ---------- stack.queue_status_all ----------


async def test_queue_status_all_no_services_returns_empty() -> None:
    from arr_stack_mcp.tools.stack._models import QueueStatusAllInput

    p = _policy()
    mcp = _register_stack(p, Config())
    handler = mcp.handlers["stack.queue_status_all"]
    result = await handler(QueueStatusAllInput())  # type: ignore[operator]
    assert result.ok is True
    assert result.total_count == 0
    assert result.sources == []


def test_project_arr_queue_handles_empty_page() -> None:
    """`page is None` and missing-records both project to empty source rows without crashing."""
    from arr_stack_mcp.tools.stack.tools import _project_arr_queue

    out = _project_arr_queue("sonarr", None, entity_attr="series_id")
    assert out.source == "sonarr"
    assert out.count == 0
    assert out.total == 0
    assert out.items == []


def test_project_arr_queue_records_normalized() -> None:
    """Real upstream queue rows project into StackQueueItem with progress + entity_id."""
    from types import SimpleNamespace

    from arr_stack_mcp.tools.stack.tools import _project_arr_queue

    page = SimpleNamespace(
        total_records=2,
        records=[
            SimpleNamespace(
                id=10,
                series_id=42,
                title="dune.s01e01",
                status="downloading",
                size=1000,
                sizeleft=250,
                estimated_completion_time=None,
                download_client="qbit",
                protocol="torrent",
            ),
            SimpleNamespace(
                id=11,
                series_id=99,
                title="dune.s01e02",
                status="completed",
                size=1000,
                sizeleft=0,
                estimated_completion_time=None,
                download_client="qbit",
                protocol="torrent",
            ),
        ],
    )
    out = _project_arr_queue("sonarr", page, entity_attr="series_id")
    assert out.source == "sonarr"
    assert out.count == 2
    assert out.total == 2
    assert out.items[0].queue_id == 10
    assert out.items[0].entity_id == 42
    # 750 of 1000 bytes complete = 75.0% progress
    assert out.items[0].progress_pct == 75.0
    # second row: 100% complete
    assert out.items[1].progress_pct == 100.0


def test_project_arr_queue_handles_zero_size() -> None:
    """A queue row with size=0 doesn't divide-by-zero on progress; reports 0.0%."""
    from types import SimpleNamespace

    from arr_stack_mcp.tools.stack.tools import _project_arr_queue

    page = SimpleNamespace(
        total_records=1,
        records=[
            SimpleNamespace(
                id=5,
                series_id=1,
                title="x",
                status="grabbing",
                size=0,
                sizeleft=0,
                estimated_completion_time=None,
                download_client=None,
                protocol=None,
            ),
        ],
    )
    out = _project_arr_queue("sonarr", page, entity_attr="series_id")
    assert out.items[0].progress_pct == 0.0
    assert out.items[0].download_client is None
