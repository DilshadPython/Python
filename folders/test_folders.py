"""Unit Test Suite for Directory Management Operations.

Validates creation, scanning, metadata management, removal, and temporary directory operations.
"""

import shutil
import tempfile
import unittest
from pathlib import Path

from create_directory_ops import (
    create_directory_with_pathlib,
    create_nested_directories,
    create_single_directory,
)
from manage_directory_ops import (
    get_directory_size,
    move_directory,
    rename_directory,
)
from remove_directory_ops import (
    remove_directory_tree,
    remove_empty_directory,
)
from scan_directory_ops import (
    glob_directory_files,
    list_directory_contents,
    scan_directory_entries,
    walk_directory_tree,
)
from temp_directory_ops import (
    create_temp_directory_context,
    create_temp_directory_explicit,
)


class TestFoldersModule(unittest.TestCase):
    """Test suite covering all directory operations."""

    def setUp(self) -> None:
        """Create an isolated temporary environment for each test."""
        self.test_dir = Path(tempfile.mkdtemp(prefix="unittest_folders_"))

    def tearDown(self) -> None:
        """Clean up test environment after test execution."""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_create_single_directory(self) -> None:
        """Test creating a single directory."""
        target = self.test_dir / "single_dir"
        result = create_single_directory(str(target))
        self.assertTrue(result.exists())
        self.assertTrue(result.is_dir())

    def test_create_nested_directories(self) -> None:
        """Test creating nested multi-level directories."""
        target = self.test_dir / "parent" / "child" / "grandchild"
        result = create_nested_directories(str(target))
        self.assertTrue(result.exists())
        self.assertTrue(result.is_dir())

    def test_create_directory_with_pathlib(self) -> None:
        """Test directory creation using pathlib."""
        target = self.test_dir / "pathlib_dir" / "sub"
        result = create_directory_with_pathlib(target)
        self.assertTrue(result.exists())
        self.assertTrue(result.is_dir())

    def test_list_and_scan_directory(self) -> None:
        """Test listing and scanning directory entries."""
        sub_folder = self.test_dir / "scan_target"
        sub_folder.mkdir()
        (sub_folder / "file1.txt").write_text("Hello")
        (sub_folder / "file2.py").write_text("print('test')")

        # Test list_directory_contents
        contents = list_directory_contents(sub_folder)
        self.assertIn("file1.txt", contents)
        self.assertIn("file2.py", contents)

        # Test scan_directory_entries
        entries = scan_directory_entries(sub_folder)
        names = [entry["name"] for entry in entries]
        self.assertIn("file1.txt", names)
        self.assertIn("file2.py", names)

    def test_walk_and_glob_directory(self) -> None:
        """Test walking directory trees and pattern globbing."""
        sub_folder = self.test_dir / "glob_target"
        sub_folder.mkdir()
        (sub_folder / "script.py").write_text("# py file")
        (sub_folder / "doc.txt").write_text("text doc")

        # Test walk
        tree = walk_directory_tree(sub_folder)
        self.assertGreaterEqual(len(tree), 1)

        # Test glob
        py_matches = glob_directory_files(sub_folder, pattern="*.py")
        self.assertEqual(len(py_matches), 1)
        self.assertEqual(py_matches[0].name, "script.py")

    def test_manage_directory(self) -> None:
        """Test renaming, moving, and calculating folder size."""
        source = self.test_dir / "manage_src"
        source.mkdir()
        (source / "data.bin").write_bytes(b"1234567890")

        # Size check
        size = get_directory_size(source)
        self.assertEqual(size, 10)

        # Rename
        dest_rename = self.test_dir / "manage_renamed"
        renamed = rename_directory(source, dest_rename)
        self.assertTrue(renamed.exists())
        self.assertFalse(source.exists())

        # Move
        dest_parent = self.test_dir / "target_container"
        dest_parent.mkdir()
        moved = move_directory(renamed, dest_parent)
        self.assertTrue(moved.exists())

    def test_remove_directory(self) -> None:
        """Test empty and recursive directory deletion."""
        # Empty dir
        empty = self.test_dir / "empty_dir"
        empty.mkdir()
        self.assertTrue(remove_empty_directory(empty))
        self.assertFalse(empty.exists())

        # Tree dir
        tree = self.test_dir / "tree_dir"
        (tree / "sub").mkdir(parents=True)
        (tree / "sub" / "file.txt").write_text("data")
        self.assertTrue(remove_directory_tree(tree))
        self.assertFalse(tree.exists())

    def test_temp_directory(self) -> None:
        """Test temporary directory context manager and explicit creation."""
        create_temp_directory_context(prefix="test_ctx_")

        explicit_path = create_temp_directory_explicit(prefix="test_exp_")
        self.assertTrue(explicit_path.exists())
        remove_directory_tree(explicit_path)
        self.assertFalse(explicit_path.exists())


if __name__ == "__main__":
    unittest.main()
