"""Top-level CLI.

``arr-stack-mcp serve`` boots the MCP server. ``arr-stack-mcp init`` probes the
local environment and writes a starter config.
"""

from __future__ import annotations

import typer

from arr_stack_mcp import __version__

app = typer.Typer(
    help="Unified MCP server for the *arr media stack + Jellyfin.",
    no_args_is_help=True,
    add_completion=False,
)


@app.command()
def version() -> None:
    """Print the installed arr-stack-mcp version."""
    typer.echo(__version__)


@app.command()
def serve(
    config: str | None = typer.Option(
        None,
        "--config",
        "-c",
        help="Path to a YAML config file. Defaults to ./arr-stack-mcp.yaml, then ~/.config/arr-stack-mcp/config.yaml.",
    ),
    transport: str = typer.Option(
        "stdio",
        "--transport",
        "-t",
        help=("MCP transport. stdio is the default for Claude Desktop / Claude Code. streamable-http for n8n and remote consumers."),
    ),
    read_only: bool = typer.Option(
        False,
        "--read-only",
        help="Globally disable every tool tagged write or destructive.",
    ),
    disable_destructive: bool = typer.Option(
        False,
        "--disable-destructive",
        help="Globally disable every tool tagged destructive.",
    ),
) -> None:
    """Boot the MCP server. Loads config, registers enabled toolsets, starts the chosen transport."""
    from arr_stack_mcp.server import run

    run(
        config_path=config,
        transport=transport,
        read_only=read_only,
        disable_destructive=disable_destructive,
    )


@app.command()
def init(
    out: str = typer.Option(
        "arr-stack-mcp.yaml",
        "--out",
        "-o",
        help="Path to write the generated config file.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Overwrite an existing config without prompting.",
    ),
) -> None:
    """First-run discovery wizard.

    Probes localhost + common docker network names to auto-fill service URLs,
    then prompts for API keys.
    """
    from arr_stack_mcp.config import init_config

    init_config(out_path=out, force=force)


if __name__ == "__main__":
    app()
