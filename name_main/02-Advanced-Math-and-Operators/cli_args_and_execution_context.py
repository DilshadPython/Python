"""
Command Line Argument Parsing and Execution Context Module.

This module demonstrates:
- Parsing command-line arguments passed via `sys.argv`.
- Reading environment variables via `os.environ`.
- Passing structured options into main entry point functions.
"""

# Import os for environment variable inspection
import os

# Import sys for command line argument access
import sys


def parse_cli_arguments(args: list[str]) -> dict[str, object]:
    """Parse list of CLI command line arguments.

    Args:
        args (list[str]): Raw sys.argv list.

    Returns:
        dict[str, object]: Dictionary of parsed script flags and values.
    """
    script_name = args[0] if args else "unknown"
    custom_flags = args[1:] if len(args) > 1 else []
    return {
        "script_name": script_name,
        "argument_count": len(custom_flags),
        "arguments": custom_flags,
        "user_environment": os.environ.get("USER", "UnknownUser"),
    }


def main(argv: list[str] | None = None) -> int:
    """Entry point accepting explicit argument vector for testing and CLI usage.

    Args:
        argv (list[str] | None, optional): Argument list. Defaults to sys.argv if None.

    Returns:
        int: Return exit code (0 for success).
    """
    if argv is None:
        argv = sys.argv

    parsed = parse_cli_arguments(argv)
    print("--- CLI Execution Arguments ---")
    print(f"Script Invoked: {parsed['script_name']}")
    print(f"Arg Count:      {parsed['argument_count']}")
    print(f"User Env:       {parsed['user_environment']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
