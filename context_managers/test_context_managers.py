"""
Comprehensive Unit Test Suite for context_managers Module.

Tests class-based context managers (OpenTextFile), directory switching context managers
(change_directory), and generator-based context managers (open_text_file).
"""

# "import os" imports standard operating system interface routines.
import os
# "import sys" imports system parameters and path configuration tools.
import sys
# "import tempfile" imports temporary file and directory creation tools.
import tempfile
# "import unittest" imports Python standard unit testing framework.
import unittest
# "from pathlib import Path" imports object-oriented filesystem paths.
from pathlib import Path

# Ensure local module discovery by adding parent directory to sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# "from class_context_manager import OpenTextFile" imports class context manager.
from class_context_manager import OpenTextFile
# "from context_manager_directory_change import change_directory" imports directory context manager.
from context_manager_directory_change import change_directory
# "from generator_context_manager import open_text_file" imports generator context manager.
from generator_context_manager import open_text_file


class TestClassContextManager(unittest.TestCase):
    """Test suite for class-based OpenTextFile context manager."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_open_text_file_write_and_read(self) -> None:
        """Verify OpenTextFile context manager writes content and closes file descriptor on exit."""
        file_path = Path(self.temp_dir.name) / "test_class_cm.txt"
        with OpenTextFile(str(file_path), "w") as stream:
            stream.write("Class context manager output\n")
            self.assertFalse(stream.closed)

        # Verify file is closed after exiting with block
        self.assertTrue(stream.closed)

        # Verify file content
        with open(file_path, "r", encoding="utf-8") as stream:
            content = stream.read()
        self.assertEqual(content, "Class context manager output\n")


class TestDirectoryChangeContextManager(unittest.TestCase):
    """Test suite for change_directory context manager."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_change_directory_restoration(self) -> None:
        """Verify working directory changes inside context and restores original directory on exit."""
        original_cwd = os.getcwd()
        target_dir = Path(self.temp_dir.name) / "sub_folder"

        with change_directory(target_dir):
            self.assertEqual(Path(os.getcwd()).resolve(), target_dir.resolve())

        # Verify working directory is restored
        self.assertEqual(os.getcwd(), original_cwd)


class TestGeneratorContextManager(unittest.TestCase):
    """Test suite for generator-based open_text_file context manager."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_generator_open_text_file(self) -> None:
        """Verify open_text_file generator context manager opens, writes, and closes file."""
        file_path = Path(self.temp_dir.name) / "test_gen_cm.txt"
        with open_text_file(str(file_path), "w") as stream:
            stream.write("Generator context manager output\n")
            self.assertFalse(stream.closed)

        # Verify stream is closed after exit
        self.assertTrue(stream.closed)

        # Verify content
        with open(file_path, "r", encoding="utf-8") as stream:
            content = stream.read()
        self.assertEqual(content, "Generator context manager output\n")


if __name__ == "__main__":
    unittest.main()
