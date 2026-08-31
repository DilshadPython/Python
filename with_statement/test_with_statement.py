"""
Comprehensive Unit Test Suite for Python With Statement & Context Manager Modules.

Tests custom class context managers (__enter__ and __exit__), exception handling
and suppression, file reading context managers, custom MessageWriter wrappers,
generator-based context managers (@contextmanager), ExitStack, suppress,
range sequence properties, and dir() reflection matrix.
"""

# "import os" loads OS interface routines.
import os
# "import sys" loads system parameters for path configuration.
import sys
# "import tempfile" imports temporary file and directory creation tools.
import tempfile
# "import unittest" loads standard unit testing framework.
import unittest
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path

# Add parent directory to sys.path for direct module discovery
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Import module functions and classes for testing
# "from with_custom_context_manager import ..." imports StudentContextManager.
from with_custom_context_manager import StudentContextManager, run_student_context
# "from with_context_manager_exception_handling import ..." imports StudentExceptionContextManager.
from with_context_manager_exception_handling import (
    StudentExceptionContextManager,
    run_exception_context,
)
# "from with_file_reading import ..." imports file reading context managers.
from with_file_reading import read_lines_with_context, read_lines_legacy_close
# "from with_custom_file_writer import ..." imports MessageWriter class.
from with_custom_file_writer import MessageWriter, write_message_with_writer
# "from build_with_files import ..." imports generator context managers and ExitStack tools.
from build_with_files import (
    temporary_file_builder,
    build_multiple_files,
    remove_file_safely,
)


class TestWithCustomContextManager(unittest.TestCase):
    """Test custom class context manager __enter__ and __exit__ behavior."""

    def test_student_context_manager(self) -> None:
        """Verify StudentContextManager __enter__ returns self and text_msg formats properly."""
        with StudentContextManager() as obj:
            msg = obj.text_msg()
            self.assertIn("StudentContextManager", msg)
            self.assertIn("instance id:", msg)

    def test_run_student_context(self) -> None:
        """Verify run_student_context helper function execution."""
        result = run_student_context()
        self.assertTrue(result.startswith("Hi from StudentContextManager"))


class TestWithExceptionHandling(unittest.TestCase):
    """Test exception logging and exception suppression inside __exit__."""

    def test_clean_context_execution(self) -> None:
        """Verify clean execution returning zero caught errors."""
        clean, err = run_exception_context("Dilshad", trigger_error=False)
        self.assertTrue(clean)
        self.assertIsNone(err)

    def test_suppressed_exception_execution(self) -> None:
        """Verify exception is caught and suppressed by __exit__ returning True."""
        clean, err_type = run_exception_context("Dilshad", trigger_error=True)
        self.assertFalse(clean)
        self.assertEqual(err_type, "ValueError")

    def test_unsuppressed_exception_propagation(self) -> None:
        """Verify exception propagates when suppress_errors is False."""
        manager = StudentExceptionContextManager(suppress_errors=False)
        with self.assertRaises(ZeroDivisionError):
            with manager:
                _ = 1 / 0


class TestWithFileOperations(unittest.TestCase):
    """Test file operations using context managers vs legacy manual closing."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_read_lines_with_context(self) -> None:
        """Verify reading lines with context manager from with_sample.txt."""
        sample_path = BASE_DIR / "with_sample.txt"
        lines = read_lines_with_context(str(sample_path))
        self.assertTrue(len(lines) > 0)
        self.assertIn("# with EXPRESSION as TARGET: SUITE", lines[0])

    def test_read_lines_legacy_close(self) -> None:
        """Verify legacy manual file open and close within try-finally."""
        sample_path = BASE_DIR / "with_sample.txt"
        lines = read_lines_legacy_close(str(sample_path))
        self.assertTrue(len(lines) > 0)
        self.assertEqual(lines[0], "# with EXPRESSION as TARGET: SUITE")

    def test_message_writer_class(self) -> None:
        """Verify MessageWriter custom context manager creates and closes file."""
        tmp_file = Path(self.temp_dir.name) / "test_writer.txt"
        success = write_message_with_writer(
            str(tmp_file), "Testing MessageWriter context manager\n"
        )
        self.assertTrue(success)

        with open(tmp_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "Testing MessageWriter context manager\n")


class TestWithGeneratorAndContextlib(unittest.TestCase):
    """Test contextlib generator context managers, ExitStack, and error suppression."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_temporary_file_builder(self) -> None:
        """Verify generator context manager creates and cleans up temporary file."""
        tmp_path = Path(self.temp_dir.name) / "temp_gen_test.txt"
        with temporary_file_builder(str(tmp_path), "Generator context test") as path:
            self.assertTrue(Path(path).exists())
            with open(path, "r", encoding="utf-8") as f:
                self.assertEqual(f.read(), "Generator context test")

        # After exiting context, file should be cleaned up automatically
        self.assertFalse(tmp_path.exists())

    def test_build_multiple_files_exit_stack(self) -> None:
        """Verify ExitStack managing multiple file contexts simultaneously."""
        files_map = {"a.txt": "Alpha content", "b.txt": "Beta content"}
        created = build_multiple_files(files_map, self.temp_dir.name)
        self.assertEqual(len(created), 2)
        for path in created:
            self.assertTrue(Path(path).exists())

    def test_remove_file_safely(self) -> None:
        """Verify remove_file_safely handles non-existent files without raising error."""
        non_existent_file = Path(self.temp_dir.name) / "does_not_exist.txt"
        result = remove_file_safely(str(non_existent_file))
        self.assertFalse(result)


class TestRangeAndReflectionIntegration(unittest.TestCase):
    """Test range sequence behavior and dir() attribute reflection on context managers."""

    def test_range_properties_and_dir(self) -> None:
        """Verify range start, stop, step attributes, O(1) membership check, and dir(range)."""
        r = range(5, 50, 5)
        self.assertEqual(r.start, 5)
        self.assertEqual(r.stop, 50)
        self.assertEqual(r.step, 5)
        self.assertIn("start", dir(r))
        self.assertIn("stop", dir(r))
        self.assertIn("step", dir(r))
        self.assertTrue(25 in r)
        self.assertFalse(27 in r)

    def test_context_manager_reflection(self) -> None:
        """Verify dir() reflection on StudentContextManager returns __enter__ and __exit__."""
        manager = StudentContextManager()
        attributes = dir(manager)
        self.assertIn("__enter__", attributes)
        self.assertIn("__exit__", attributes)


if __name__ == "__main__":
    unittest.main()
