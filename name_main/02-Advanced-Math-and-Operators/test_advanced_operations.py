"""
Unit Test Suite for Advanced Module Import and CLI Operations.

Tests module import vs execution analysis, command line argument parsing,
environment variable inspection, and main(argv) invocation.
"""

from pathlib import Path
import sys
import unittest

# Ensure current folder is in Python search path BEFORE local imports
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from cli_args_and_execution_context import main as cli_main, parse_cli_arguments
from module_import_vs_execution import analyze_imported_module


class TestNameMainAdvancedOperations(unittest.TestCase):
    """Test cases for imported module behavior and CLI argument parsing."""

    def test_analyze_imported_module(self) -> None:
        """Verify module name identification in imported functions."""
        result = analyze_imported_module()
        self.assertEqual(result["current_file_module"], "module_import_vs_execution")
        self.assertIn("name_attribute_basics", result["imported_func_module"])

    def test_parse_cli_arguments(self) -> None:
        """Verify CLI argument parsing logic."""
        mock_argv = ["test_script.py", "--verbose", "--count", "10"]
        parsed = parse_cli_arguments(mock_argv)
        self.assertEqual(parsed["script_name"], "test_script.py")
        self.assertEqual(parsed["argument_count"], 3)
        self.assertListEqual(parsed["arguments"], ["--verbose", "--count", "10"])

    def test_cli_main_invocation(self) -> None:
        """Verify main entry point with custom argument vector."""
        code = cli_main(["test_script.py", "arg1"])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
