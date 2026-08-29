"""
Comprehensive Unit Test Suite for Python With Statement & Context Manager Modules.
Tests custom class context managers (__enter__ and __exit__), exception handling
and suppression, file reading context managers, and custom MessageWriter wrappers.
"""

import os
import sys
import tempfile
import unittest

# Ensure module directory is in sys.path for direct imports
sys.path.insert(0, os.path.dirname(__file__))

from with_custom_context_manager import StudentContextManager, run_student_context
from with_context_manager_exception_handling import StudentExceptionContextManager, run_exception_context
from with_file_reading import read_lines_with_context, read_lines_legacy_close
from with_custom_file_writer import MessageWriter, write_message_with_writer
from build_with_files import temporary_file_builder, build_multiple_files, remove_file_safely


class TestWithCustomContextManager(unittest.TestCase):
    """Test custom class context manager __enter__ and __exit__ behavior."""

    def test_student_context_manager(self):
        with StudentContextManager() as obj:
            msg = obj.text_msg()
            self.assertIn("StudentContextManager", msg)
            self.assertIn("instance id:", msg)

    def test_run_student_context(self):
        result = run_student_context()
        self.assertTrue(result.startswith("Hi from StudentContextManager"))


class TestWithExceptionHandling(unittest.TestCase):
    """Test exception logging and exception suppression inside __exit__."""

    def test_clean_context_execution(self):
        clean, err = run_exception_context("Dilshad", trigger_error=False)
        self.assertTrue(clean)
        self.assertIsNone(err)

    def test_suppressed_exception_execution(self):
        clean, err_type = run_exception_context("Dilshad", trigger_error=True)
        self.assertFalse(clean)
        self.assertEqual(err_type, "ValueError")

    def test_unsuppressed_exception_propagation(self):
        manager = StudentExceptionContextManager(suppress_errors=False)
        with self.assertRaises(ZeroDivisionError):
            with manager:
                _ = 1 / 0


class TestWithFileOperations(unittest.TestCase):
    """Test file operations using context managers vs legacy manual closing."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_read_lines_with_context(self):
        sample_path = os.path.join(os.path.dirname(__file__), 'with_sample.txt')
        lines = read_lines_with_context(sample_path)
        self.assertTrue(len(lines) > 0)
        self.assertIn("# with EXPRESSION as TARGET: SUITE", lines[0])

    def test_read_lines_legacy_close(self):
        sample_path = os.path.join(os.path.dirname(__file__), 'with_sample.txt')
        lines = read_lines_legacy_close(sample_path)
        self.assertTrue(len(lines) > 0)
        self.assertEqual(lines[0], "# with EXPRESSION as TARGET: SUITE")

    def test_message_writer_class(self):
        tmp_file = os.path.join(self.temp_dir.name, 'test_writer.txt')
        success = write_message_with_writer(tmp_file, "Testing MessageWriter context manager\n")
        self.assertTrue(success)

        with open(tmp_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, "Testing MessageWriter context manager\n")


class TestWithGeneratorAndContextlib(unittest.TestCase):
    """Test contextlib generator context managers, ExitStack, and error suppression."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_temporary_file_builder(self):
        tmp_path = os.path.join(self.temp_dir.name, 'temp_gen_test.txt')
        with temporary_file_builder(tmp_path, "Generator context test") as path:
            self.assertTrue(os.path.exists(path))
            with open(path, 'r', encoding='utf-8') as f:
                self.assertEqual(f.read(), "Generator context test")

        # After exiting context, file should be cleaned up automatically
        self.assertFalse(os.path.exists(tmp_path))

    def test_build_multiple_files_exit_stack(self):
        files_map = {
            "a.txt": "Alpha content",
            "b.txt": "Beta content"
        }
        created = build_multiple_files(files_map, self.temp_dir.name)
        self.assertEqual(len(created), 2)
        for path in created:
            self.assertTrue(os.path.exists(path))

    def test_remove_file_safely(self):
        non_existent_file = os.path.join(self.temp_dir.name, 'does_not_exist.txt')
        result = remove_file_safely(non_existent_file)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

