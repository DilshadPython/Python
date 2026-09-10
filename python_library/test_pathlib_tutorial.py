"""
Unit Test Suite for `pathlib_tutorial.py`.

This module verifies:
1. Current working directory and home path inspection.
2. Path decomposition (stem, suffix, name, parent, type checks).
3. Directory listing and glob pattern matching.
4. File reading and writing via `Path.write_text()` and `Path.read_text()`.
"""

from pathlib import Path
import tempfile
import unittest

# Support both package and local directory import paths
try:
    from python_library.pathlib_tutorial import (
        get_current_directory_info,
        decompose_path,
        list_directory_contents,
        write_and_read_text_file,
    )
except ImportError:
    from pathlib_tutorial import (
        get_current_directory_info,
        decompose_path,
        list_directory_contents,
        write_and_read_text_file,
    )


class TestPathlibTutorial(unittest.TestCase):
    """Test suite verifying pathlib operations and helper functions."""

    def test_get_current_directory_info(self) -> None:
        """Verify CWD and Home directory retrieval."""
        info = get_current_directory_info()
        self.assertIn("current_working_directory", info)
        self.assertIn("user_home_directory", info)
        self.assertTrue(Path(info["current_working_directory"]).exists())

    def test_decompose_path(self) -> None:
        """Verify path decomposition fields for a sample file path."""
        target = "data/report.config.json"
        details = decompose_path(target)

        self.assertEqual(details["name"], "report.config.json")
        self.assertEqual(details["stem"], "report.config")
        self.assertEqual(details["suffix"], ".json")
        self.assertEqual(details["parent"], "data")

    def test_list_directory_contents(self) -> None:
        """Verify directory iteration using temporary test directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            (temp_path / "file1.py").write_text("print('hello')", encoding="utf-8")
            (temp_path / "file2.txt").write_text("sample text", encoding="utf-8")

            items = list_directory_contents(temp_dir)
            self.assertEqual(len(items), 2)

            py_items = list_directory_contents(temp_dir, pattern="*.py")
            self.assertEqual(len(py_items), 1)
            self.assertEqual(py_items[0]["name"], "file1.py")

    def test_list_directory_contents_errors(self) -> None:
        """Verify error handling for invalid or missing directories."""
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "not_a_dir.txt"
            file_path.write_text("data", encoding="utf-8")

            with self.assertRaises(NotADirectoryError):
                list_directory_contents(file_path)

        with self.assertRaises(FileNotFoundError):
            list_directory_contents("/non_existent_directory_12345")

    def test_write_and_read_text_file(self) -> None:
        """Verify atomic file writing and reading using Path.write_text and Path.read_text."""
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "sub_folder" / "test_file.txt"
            content = "Hello, Python Pathlib!"

            res = write_and_read_text_file(file_path, content)
            self.assertEqual(res["read_content"], content)
            self.assertTrue(Path(file_path).exists())


if __name__ == "__main__":
    unittest.main()
