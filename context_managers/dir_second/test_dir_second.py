"""
Unit Test Suite for Dir-Second Context Manager Module.

Tests DirSecondResourceHandler class context manager, managed_dir_second_file generator context manager,
multi-file ExitStack processing, range memory benchmarks, and dir() reflection matrix.
"""

# "import os" imports standard operating system interface routines.
import os
# "import sys" imports system parameters and path configuration tools.
import sys
# "import tempfile" imports temporary directory creation utilities.
import tempfile
# "import unittest" imports standard Python unit testing framework.
import unittest
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path

# Add parent directory to sys.path for direct module discovery
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# "from dir_second_context_manager import ..." imports context manager targets.
from dir_second_context_manager import (
    DirSecondResourceHandler,
    managed_dir_second_file,
    read_multiple_dir_second_files,
)


class TestDirSecondContextManager(unittest.TestCase):
    """Test suite for class and generator context managers in dir-second subfolder."""

    def test_dir_second_resource_handler_reading(self) -> None:
        """Verify DirSecondResourceHandler reads test_b.txt and closes file stream on exit."""
        handler = DirSecondResourceHandler("test_b.txt", "r")
        with handler as stream:
            self.assertIsNotNone(stream)
            if stream:
                lines = [line.rstrip("\n") for line in stream]
                self.assertFalse(stream.closed)
                self.assertTrue(len(lines) > 0)

        # Stream should be closed after exiting context block
        self.assertTrue(handler.file_handle.closed)

    def test_dir_second_resource_handler_missing_file(self) -> None:
        """Verify FileNotFoundError is handled gracefully returning None in __enter__."""
        handler = DirSecondResourceHandler("non_existent_file_abc.txt", "r")
        with handler as stream:
            self.assertIsNone(stream)

    def test_managed_dir_second_file_generator(self) -> None:
        """Verify managed_dir_second_file generator context manager opens and closes stream."""
        with managed_dir_second_file("test_c.txt", "r") as stream:
            self.assertIsNotNone(stream)
            if stream:
                content = stream.read()
                self.assertIn("Multi-file handling", content)
                self.assertFalse(stream.closed)

        self.assertTrue(stream.closed)

    def test_read_multiple_dir_second_files(self) -> None:
        """Verify ExitStack reads multiple files in dir-second subfolder simultaneously."""
        results = read_multiple_dir_second_files(["test_b.txt", "test_c.txt"])
        self.assertEqual(len(results), 2)
        self.assertTrue(any("[INFO]" in line for line in results[0]))
        self.assertTrue(any("ExitStack" in line for line in results[1]))


class TestDirSecondRangeAndReflection(unittest.TestCase):
    """Test suite for range sequence properties and dir(range) introspection within dir-second tests."""

    def test_range_properties_and_dir_reflection(self) -> None:
        """Verify range attributes, membership checks, and dir(range) reflection matrix."""
        r = range(5, 50, 5)
        self.assertEqual(r.start, 5)
        self.assertEqual(r.stop, 50)
        self.assertEqual(r.step, 5)
        self.assertIn(25, r)
        self.assertNotIn(26, r)

        public_members = [m for m in dir(r) if not m.startswith("__")]
        self.assertIn("start", public_members)
        self.assertIn("stop", public_members)
        self.assertIn("step", public_members)
        self.assertIn("count", public_members)
        self.assertIn("index", public_members)

    def test_range_iterator_memory_footprint(self) -> None:
        """Verify range iterator consumes O(1) constant memory footprint."""
        r_iter = iter(range(10_000_000))
        self.assertTrue(sys.getsizeof(r_iter) < 200)  # Constant memory footprint (~48 bytes)


if __name__ == "__main__":
    unittest.main()
