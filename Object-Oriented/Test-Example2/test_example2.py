"""Unit Test Suite for Test-Example2 Module.

This module provides unittest coverage for CSV/Log formatters and abstract file writers.
"""

import os
import unittest
from file_formatters import CSVFormatter, LogFormatter, FileWriter
from abstract_file_writers import DelimFile, LogFile


class TestExample2(unittest.TestCase):
    """Unit tests for formatting and file writing components."""

    def test_csv_formatter(self) -> None:
        """Verify CSVFormatter quotes items containing commas."""
        formatter = CSVFormatter(",")
        formatted = formatter.format(["a", "b,2", "c"])
        self.assertEqual(formatted, 'a,"b,2",c')

    def test_file_writer(self) -> None:
        """Verify FileWriter creates file and formats output."""
        test_file = "test_output.csv"
        writer = FileWriter(test_file, CSVFormatter)
        writer.write(["x", "y,z", "w"])
        writer.close()

        self.assertTrue(os.path.exists(test_file))
        with open(test_file, "r", encoding="utf-8") as fh:
            content = fh.read().strip()
        self.assertEqual(content, 'x,"y,z",w')

        if os.path.exists(test_file):
            os.remove(test_file)

    def test_abstract_delim_file(self) -> None:
        """Verify DelimFile appending behavior."""
        test_file = "test_delim.txt"
        delim = DelimFile(test_file, "|")
        delim.write(["1", "2", "3"])

        self.assertTrue(os.path.exists(test_file))
        with open(test_file, "r", encoding="utf-8") as fh:
            content = fh.read().strip()
        self.assertEqual(content, "1|2|3")

        if os.path.exists(test_file):
            os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
