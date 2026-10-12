"""
Unit Test Suite for Argparse Fundamentals Module.

Tests positional argument validation, optional default flags, type conversions,
and message output generation.
"""

# Standard library test framework imports
import unittest
from typing import List

# Import target functions from basic_argparse module
from basic_argparse import create_basic_parser, display_messages, parse_and_process_args


class TestArgparseFundamentals(unittest.TestCase):
    """Test cases for basic CLI argument parsing and processing."""

    def test_positional_and_defaults(self) -> None:
        """Verify positional argument parsing and default values for optional args."""
        args_input: List[str] = ["data.csv"]
        filename, count, verbose = parse_and_process_args(args_input)

        self.assertEqual(filename, "data.csv")
        self.assertEqual(count, 1)
        self.assertFalse(verbose)

    def test_custom_count_and_verbose_flag(self) -> None:
        """Verify explicit optional parameters and boolean flag parsing."""
        args_input: List[str] = ["data.csv", "--count", "3", "--verbose"]
        filename, count, verbose = parse_and_process_args(args_input)

        self.assertEqual(filename, "data.csv")
        self.assertEqual(count, 3)
        self.assertTrue(verbose)

    def test_short_option_flags(self) -> None:
        """Verify short flag options (-c and -v)."""
        args_input: List[str] = ["report.txt", "-c", "2", "-v"]
        filename, count, verbose = parse_and_process_args(args_input)

        self.assertEqual(filename, "report.txt")
        self.assertEqual(count, 2)
        self.assertTrue(verbose)

    def test_display_messages_non_verbose(self) -> None:
        """Verify output message generation in non-verbose mode."""
        messages = display_messages("sample.txt", 2, verbose=False)
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0], "Processing 'sample.txt'")
        self.assertEqual(messages[1], "Processing 'sample.txt'")

    def test_display_messages_verbose(self) -> None:
        """Verify output message generation in verbose mode."""
        messages = display_messages("sample.txt", 1, verbose=True)
        self.assertEqual(len(messages), 1)
        self.assertIn("[VERBOSE] Cycle 1/1", messages[0])

    def test_missing_required_positional_arg(self) -> None:
        """Verify SystemExit exception is raised when required positional arg is missing."""
        parser = create_basic_parser()
        with self.assertRaises(SystemExit):
            # Divert stderr output during test execution to prevent clutter
            parser.parse_args([])


if __name__ == "__main__":
    unittest.main()
