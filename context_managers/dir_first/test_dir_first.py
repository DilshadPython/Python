"""
Unit Test Suite for Dir-First Context Manager Module.

Tests DirFirstResourceHandler class context manager, managed_dir_first_file generator context manager,
file reading helpers, range memory benchmarks, and dir() reflection matrix.
"""

# "import os" imports standard operating system interface routines.
import os
# "import sys" imports system parameters and path configuration tools.
import sys
# "import tempfile" imports temporary file and directory creation utilities.
import tempfile
# "import unittest" imports standard Python unit testing framework.
import unittest
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path

# Add parent directory to sys.path for direct module discovery
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# "from dir_first_context_manager import ..." imports context manager targets.
from dir_first_context_manager import (
    DirFirstResourceHandler,
    managed_dir_first_file,
    read_dir_first_lines,
)


class TestDirFirstContextManager(unittest.TestCase):
    """Test suite for class and generator context managers in dir-first subfolder."""

    def test_dir_first_resource_handler_reading(self) -> None:
        """Verify DirFirstResourceHandler reads test_a.txt and closes file stream on exit."""
        handler = DirFirstResourceHandler("test_a.txt", "r")
        with handler as stream:
            self.assertIsNotNone(stream)
            if stream:
                lines = [line.rstrip("\n") for line in stream]
                self.assertFalse(stream.closed)
                self.assertTrue(len(lines) > 0)

        # Stream should be closed after exiting context block
        self.assertTrue(handler.file_handle.closed)

    def test_dir_first_resource_handler_missing_file_handling(self) -> None:
        """Verify FileNotFoundError is handled gracefully inside __enter__ returning None."""
        handler = DirFirstResourceHandler("non_existent_file_xyz.txt", "r")
        with handler as stream:
            self.assertIsNone(stream)

    def test_managed_dir_first_file_generator(self) -> None:
        """Verify managed_dir_first_file generator context manager opens and closes stream."""
        with managed_dir_first_file("test.txt", "r") as stream:
            self.assertIsNotNone(stream)
            if stream:
                content = stream.read()
                self.assertIn("environment=development", content)
                self.assertFalse(stream.closed)

        self.assertTrue(stream.closed)

    def test_read_dir_first_lines(self) -> None:
        """Verify read_dir_first_lines helper function returns stripped lines list."""
        lines = read_dir_first_lines("test_a.txt")
        self.assertIsInstance(lines, list)
        self.assertTrue(any("Context Manager" in line for line in lines))


class TestDirFirstRangeAndReflection(unittest.TestCase):
    """Test suite for range sequence properties and dir(range) introspection within dir-first tests."""

    def test_range_properties_and_dir_reflection(self) -> None:
        """Verify range attributes, O(1) membership check, and dir(range) public members."""
        r = range(10, 100, 10)
        self.assertEqual(r.start, 10)
        self.assertEqual(r.stop, 100)
        self.assertEqual(r.step, 10)
        self.assertIn(50, r)
        self.assertNotIn(55, r)

        public_members = [m for m in dir(r) if not m.startswith("__")]
        self.assertIn("start", public_members)
        self.assertIn("stop", public_members)
        self.assertIn("step", public_members)
        self.assertIn("count", public_members)
        self.assertIn("index", public_members)

    def test_range_iterator_memory_footprint(self) -> None:
        """Verify range iterator size is O(1) constant memory footprint."""
        r_iter = iter(range(1_000_000))
        self.assertTrue(sys.getsizeof(r_iter) < 200)  # O(1) space footprint (~48 bytes)


if __name__ == "__main__":
    unittest.main()
