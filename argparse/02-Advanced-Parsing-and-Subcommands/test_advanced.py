"""
Unit Test Suite for Advanced Argparse and Subcommands Module.

Tests subparsers, choices validation, custom type validators, count and append actions,
and mutually exclusive argument groups.
"""

# Standard library test framework imports
import argparse
import unittest
from typing import List

# Import target functions from advanced_argparse module
from advanced_argparse import create_advanced_parser, parse_advanced_args, validate_positive_int


class TestAdvancedArgparse(unittest.TestCase):
    """Test cases for advanced CLI subcommand features and error handling."""

    def test_run_subcommand_defaults(self) -> None:
        """Verify 'run' subcommand parsing with default options."""
        args_input: List[str] = ["run"]
        result = parse_advanced_args(args_input)

        self.assertEqual(result["command"], "run")
        self.assertEqual(result["env"], "dev")
        self.assertEqual(result["workers"], 2)
        self.assertIsNone(result["tags"])
        self.assertEqual(result["verbosity"], 0)
        self.assertFalse(result["json"])
        self.assertFalse(result["xml"])

    def test_run_subcommand_with_custom_values(self) -> None:
        """Verify 'run' subcommand with choices, custom tags, and verbosity flags."""
        args_input: List[str] = [
            "run",
            "--env", "staging",
            "--workers", "8",
            "--tag", "alpha",
            "--tag", "beta",
            "-vvv",
            "--json",
        ]
        result = parse_advanced_args(args_input)

        self.assertEqual(result["env"], "staging")
        self.assertEqual(result["workers"], 8)
        self.assertEqual(result["tags"], ["alpha", "beta"])
        self.assertEqual(result["verbosity"], 3)
        self.assertTrue(result["json"])
        self.assertFalse(result["xml"])

    def test_config_subcommand(self) -> None:
        """Verify 'config' subcommand key-value parsing."""
        args_input: List[str] = ["config", "database_host", "localhost"]
        result = parse_advanced_args(args_input)

        self.assertEqual(result["command"], "config")
        self.assertEqual(result["key"], "database_host")
        self.assertEqual(result["value"], "localhost")

    def test_invalid_choices(self) -> None:
        """Verify SystemExit is raised when an invalid choice is provided for --env."""
        parser = create_advanced_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["run", "--env", "invalid_env"])

    def test_mutually_exclusive_group_conflict(self) -> None:
        """Verify SystemExit is raised when mutually exclusive flags (--json and --xml) are passed together."""
        parser = create_advanced_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["run", "--json", "--xml"])

    def test_validate_positive_int_valid(self) -> None:
        """Verify custom positive integer validator accepts valid numbers > 0."""
        self.assertEqual(validate_positive_int("5"), 5)
        self.assertEqual(validate_positive_int("100"), 100)

    def test_validate_positive_int_invalid(self) -> None:
        """Verify ArgumentTypeError is raised for invalid or non-positive integers."""
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_positive_int("0")

        with self.assertRaises(argparse.ArgumentTypeError):
            validate_positive_int("-5")

        with self.assertRaises(argparse.ArgumentTypeError):
            validate_positive_int("not_a_number")


if __name__ == "__main__":
    unittest.main()
