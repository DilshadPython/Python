"""Unit Test Suite for Assignment Sub-directory Modules.

This module provides unittest coverage for `DoThis` dict subclassing and `ConfigDict` file persistence.
"""

import os
import unittest
from dict_subclass_setitem import DoThis
from config_dict_file_persistence import ConfigDict


class TestAssignment(unittest.TestCase):
    """Unit tests for Assignment sub-directory modules."""

    def setUp(self) -> None:
        """Set up temporary test config file paths."""
        self.test_filename = "test_temp_config.txt"
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def tearDown(self) -> None:
        """Clean up temporary test files."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_do_this_dict_subclass(self) -> None:
        """Verify DoThis dict subclassing setitem."""
        d = DoThis()
        d["a"] = "1"
        self.assertEqual(d["a"], "1")
        self.assertTrue(isinstance(d, dict))

    def test_config_dict_persistence(self) -> None:
        """Verify ConfigDict file persistence and reloading."""
        config = ConfigDict(self.test_filename)
        config["server"] = "nginx"
        config["threads"] = "4"

        self.assertTrue(os.path.exists(self.test_filename))

        # Reload from disk in a fresh object instance
        reloaded = ConfigDict(self.test_filename)
        self.assertEqual(reloaded["server"], "nginx")
        self.assertEqual(reloaded["threads"], "4")


if __name__ == "__main__":
    unittest.main()
