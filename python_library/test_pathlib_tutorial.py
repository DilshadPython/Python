"""
Unit Test Suite for Object-Oriented Path Manipulation across Developer Tiers (Beginner, Intermediate, Senior).

This module verifies:
1. Core `pathlib_tutorial.py` functions (decomposition, globbing, I/O).
2. Beginner level path operations (`beginner_pathlib.py`).
3. Intermediate level recursive globbing, extension transformation, and stat metadata (`intermediate_pathlib.py`).
4. Senior level path traversal sanitization, stream filtering, and async reading (`senior_pathlib.py`).
"""

import asyncio
from pathlib import Path
import sys
import tempfile
import unittest

# Support both package and local directory import paths
root = Path(__file__).parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from pathlib_tutorial import get_current_directory_info, decompose_path, list_directory_contents, write_and_read_text_file
from beginner_pathlib import create_and_join_path, check_path_status, read_and_write_file
from intermediate_pathlib import find_files_recursively, transform_file_extension, get_file_metadata
from senior_pathlib import sanitize_user_filepath, filter_path_stream, async_read_file_content


class TestPathlibTutorial(unittest.TestCase):
    """Test suite verifying pathlib operations across all modules and developer tiers."""

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

    def test_beginner_pathlib(self) -> None:
        """Verify beginner path creation, status check, and read/write."""
        joined = create_and_join_path("folder", "test.txt")
        self.assertEqual(joined, Path("folder/test.txt"))

        with tempfile.TemporaryDirectory() as temp_dir:
            f_path = Path(temp_dir) / "beginner.txt"
            content = read_and_write_file(f_path, "Beginner Content")
            self.assertEqual(content, "Beginner Content")

            status = check_path_status(f_path)
            self.assertTrue(status["exists"])
            self.assertTrue(status["is_file"])

    def test_intermediate_pathlib(self) -> None:
        """Verify intermediate rglob, extension transformation, and stat metadata."""
        sample_file = Path("doc.txt")
        transformed = transform_file_extension(sample_file, ".md")
        self.assertEqual(transformed, Path("doc.md"))

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            sub = temp_path / "nested"
            sub.mkdir()
            (sub / "test.py").write_text("code = 1", encoding="utf-8")

            found = find_files_recursively(temp_path, "*.py")
            self.assertEqual(len(found), 1)

            meta = get_file_metadata(sub / "test.py")
            self.assertGreater(meta["size_bytes"], 0)

    def test_senior_pathlib(self) -> None:
        """Verify senior path traversal sanitization, stream filtering, and async reading."""
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            (base / "valid.txt").write_text("secure data", encoding="utf-8")

            # Valid safe resolution
            safe = sanitize_user_filepath(base, "valid.txt")
            self.assertTrue(safe.exists())

            # Traversal attack attempt block
            with self.assertRaises(PermissionError):
                sanitize_user_filepath(base, "../../../etc/passwd")

            # Generator Stream Filter
            matches = list(filter_path_stream(base, min_size_bytes=1, extension=".txt"))
            self.assertEqual(len(matches), 1)

            # Async File Read
            content = asyncio.run(async_read_file_content(safe))
            self.assertEqual(content, "secure data")


if __name__ == "__main__":
    unittest.main()
