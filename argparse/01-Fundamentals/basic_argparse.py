"""
Basic Argument Parsing Fundamentals Module.

This module demonstrates foundational CLI argument parsing using Python's standard
library `argparse` module, supporting positional arguments, optional flags,
type conversion, default values, and program execution.

PEP 8 compliant, type-annotated, and compatible with Python 2.7 - 3.13 standards.
"""

# Standard library imports explaining argument parsing and command line execution
import argparse  # Provides command-line option and argument parsing
from typing import List, Optional, Tuple


def create_basic_parser() -> argparse.ArgumentParser:
    """
    Constructs and configures a fundamental ArgumentParser instance.

    Returns:
        argparse.ArgumentParser: Configured parser with positional and optional arguments.
    """
    parser = argparse.ArgumentParser(
        prog="basic_cli",
        description="Demonstrates basic positional and optional CLI argument parsing.",
        epilog="Use -h or --help for argument details.",
    )

    # Positional argument (required)
    parser.add_argument(
        "filename",
        type=str,
        help="Target file name to process (positional argument)",
    )

    # Optional argument with value and type conversion
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="Number of iterations to execute (default: 1)",
    )

    # Optional boolean flag (on/off)
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output logging",
    )

    return parser


def parse_and_process_args(args_list: Optional[List[str]] = None) -> Tuple[str, int, bool]:
    """
    Parses command-line arguments and returns structured tuple data.

    Args:
        args_list (Optional[List[str]]): List of string arguments to parse.
            If None, parses arguments from sys.argv.

    Returns:
        Tuple[str, int, bool]: Processed filename, iteration count, and verbose flag.
    """
    parser = create_basic_parser()
    parsed_args = parser.parse_args(args_list)

    filename: str = parsed_args.filename
    count: int = parsed_args.count
    verbose: bool = parsed_args.verbose

    return filename, count, verbose


def display_messages(filename: str, count: int, verbose: bool) -> List[str]:
    """
    Generates output messages based on parsed CLI parameters.

    Args:
        filename (str): Target filename.
        count (int): Number of repetition cycles.
        verbose (bool): Verbosity flag state.

    Returns:
        List[str]: Formatted list of generated log messages.
    """
    logs: List[str] = []

    for i in range(count):
        if verbose:
            msg = f"[VERBOSE] Cycle {i + 1}/{count}: Processing file '{filename}'"
        else:
            msg = f"Processing '{filename}'"
        logs.append(msg)

    return logs


if __name__ == "__main__":
    # Execute default argument parser via command line interface
    parsed_file, parsed_count, parsed_verbose = parse_and_process_args()
    output_messages = display_messages(parsed_file, parsed_count, parsed_verbose)
    for line in output_messages:
        print(line)
