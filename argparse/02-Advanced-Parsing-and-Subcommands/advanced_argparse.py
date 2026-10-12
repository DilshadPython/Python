"""
Advanced Argument Parsing and Subcommands Module.

This module demonstrates advanced CLI techniques using `argparse`, including:
- Subparsers for multi-command CLI applications (similar to git/docker)
- Mutually exclusive argument groups (e.g., choosing JSON vs XML formatting)
- Choices validation (`choices=['development', 'staging', 'production']`)
- Custom argument actions (`action='append'`, `action='count'`)
- Custom type validation functions

PEP 8 compliant, type-annotated, and compatible with Python 2.7 - 3.13.
"""

# Standard library imports for advanced command-line parsing
import argparse
from typing import Any, Dict, List, Optional


def validate_positive_int(value: str) -> int:
    """
    Custom type validator function for argparse ensuring input is a positive integer.

    Args:
        value (str): Raw string argument from CLI.

    Returns:
        int: Converted positive integer.

    Raises:
        argparse.ArgumentTypeError: If value cannot be converted or is <= 0.
    """
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid integer value: '{value}'")

    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"Value must be a positive integer (> 0), got {ivalue}")

    return ivalue


def create_advanced_parser() -> argparse.ArgumentParser:
    """
    Constructs an advanced ArgumentParser featuring subparsers, mutually exclusive groups,
    choices, and custom actions.

    Returns:
        argparse.ArgumentParser: Fully configured multi-command CLI parser.
    """
    parser = argparse.ArgumentParser(
        prog="advanced_cli",
        description="Advanced CLI utility demonstrating subparsers and mutually exclusive options.",
    )

    # Subparsers for commands (e.g. 'run', 'config')
    subparsers = parser.add_subparsers(
        dest="command",
        title="Available Subcommands",
        description="Valid subcommand operations",
        help="Subcommand help menu",
    )
    subparsers.required = True

    # ------------------ Subcommand: run ------------------
    run_parser = subparsers.add_parser(
        "run",
        help="Execute task runner with specified environment and formatting",
    )

    # Choices argument
    run_parser.add_argument(
        "--env",
        choices=["dev", "staging", "prod"],
        default="dev",
        help="Target environment (choices: dev, staging, prod)",
    )

    # Custom type validator
    run_parser.add_argument(
        "--workers",
        type=validate_positive_int,
        default=2,
        help="Number of worker processes (must be positive integer > 0)",
    )

    # Action='append' allows multiple --tag arguments
    run_parser.add_argument(
        "--tag",
        action="append",
        dest="tags",
        help="Tag labels to apply (can be specified multiple times)",
    )

    # Action='count' counts instances of flag (-v, -vv, -vvv)
    run_parser.add_argument(
        "-v",
        "--verbosity",
        action="count",
        default=0,
        help="Verbosity level (-v: low, -vv: medium, -vvv: high)",
    )

    # Mutually Exclusive Group (Format output as JSON OR XML, not both)
    format_group = run_parser.add_mutually_exclusive_group()
    format_group.add_argument(
        "--json",
        action="store_true",
        help="Format output response as JSON",
    )
    format_group.add_argument(
        "--xml",
        action="store_true",
        help="Format output response as XML",
    )

    # ------------------ Subcommand: config ------------------
    config_parser = subparsers.add_parser(
        "config",
        help="Manage application configuration settings",
    )
    config_parser.add_argument(
        "key",
        type=str,
        help="Configuration key name",
    )
    config_parser.add_argument(
        "value",
        type=str,
        help="Configuration setting value",
    )

    return parser


def parse_advanced_args(args_list: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Parses CLI arguments using the advanced parser and returns dictionary representation.

    Args:
        args_list (Optional[List[str]]): CLI argument list to parse.

    Returns:
        Dict[str, Any]: Parsed arguments converted to a dictionary.
    """
    parser = create_advanced_parser()
    parsed_namespace = parser.parse_args(args_list)
    return vars(parsed_namespace)


if __name__ == "__main__":
    # Execute sample subcommand CLI
    sample_args = ["run", "--env", "prod", "--workers", "4", "--tag", "v1.0", "--tag", "release", "-vv", "--json"]
    result = parse_advanced_args(sample_args)
    print("Parsed Advanced CLI Arguments:")
    for k, v in result.items():
        print(f"  {k}: {v}")
