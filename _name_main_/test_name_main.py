"""Unit tests for the `_name_main_` tutorial module.

Verifies that functions return expected messages and respect `__name__` execution
contexts when run directly vs imported.
"""

import unittest

from _name_main_._main_ import callme
from _name_main_._name_ import hello
from _name_main_.main import get_environment_summary
from _name_main_.myfile import hello_py
from _name_main_.yourfile import main as yourfile_main


class TestNameMainTutorial(unittest.TestCase):
    """Test suite covering `__name__` behaviors across scripts."""

    def test_hello_and_callme_output(self):
        """Verify that hello() and callme() return valid module name descriptions."""
        msg1 = hello()
        self.assertIn("The module __name__ in Python is:", msg1)
        self.assertIn("_name_main_._name_", msg1)

        msg2 = callme()
        self.assertIn("The module __name__ in Python is:", msg2)
        self.assertIn("_name_main_._main_", msg2)

    def test_myfile_imported_context(self):
        """Verify that when myfile is imported, its __name__ matches the module name."""
        msg = hello_py()
        self.assertIn("This file is 'myfile'", msg)
        self.assertIn("_name_main_.myfile", msg)

    def test_yourfile_imported_comparison(self):
        """Verify yourfile correctly identifies itself vs the imported myfile."""
        results = yourfile_main()
        self.assertIn("yourfile", results["current_name"])
        self.assertIn("myfile", results["imported_name"])

    def test_main_environment_summary(self):
        """Verify safe environment summary retrieval."""
        summary = get_environment_summary("PATH")
        self.assertEqual(summary["author"], "DILSHAD")
        self.assertEqual(summary["variable_inspected"], "PATH")
        self.assertIsNotNone(summary["value"])


if __name__ == "__main__":
    unittest.main()
