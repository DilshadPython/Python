"""
Unit Test Suite for Conda Fundamentals Module.

Tests environment instantiation, activation, package installation, package removal,
and package listing functionality.
"""

import unittest
from conda_basics import CondaEnvironment, create_environment


class TestCondaFundamentals(unittest.TestCase):
    """Test cases for CondaEnvironment creation, activation, and package handling."""

    def setUp(self) -> None:
        """Initialize test environment before each test case."""
        self.env = create_environment("test_env", "3.10.0")

    def test_environment_initialization(self) -> None:
        """Verify environment creation defaults and base packages."""
        self.assertEqual(self.env.name, "test_env")
        self.assertEqual(self.env.python_version, "3.10.0")
        self.assertFalse(self.env.active)
        self.assertIn("python", self.env.packages)
        self.assertIn("pip", self.env.packages)

    def test_activation_state(self) -> None:
        """Verify activation and deactivation toggle state correctly."""
        act_msg = self.env.activate()
        self.assertTrue(self.env.active)
        self.assertIn("activated", act_msg)

        deact_msg = self.env.deactivate()
        self.assertFalse(self.env.active)
        self.assertIn("deactivated", deact_msg)

    def test_install_and_remove_package(self) -> None:
        """Verify package installation and deletion."""
        self.env.install_package("numpy", "1.24.3")
        self.assertEqual(self.env.packages.get("numpy"), "1.24.3")

        rem_msg = self.env.remove_package("numpy")
        self.assertNotIn("numpy", self.env.packages)
        self.assertIn("Removed package", rem_msg)

    def test_remove_nonexistent_package(self) -> None:
        """Verify KeyError is raised when removing non-installed package."""
        with self.assertRaises(KeyError):
            self.env.remove_package("nonexistent_package")

    def test_list_packages(self) -> None:
        """Verify formatted list of packages."""
        pkgs = self.env.list_packages()
        self.assertTrue(any("python == 3.10.0" in item for item in pkgs))
        self.assertTrue(any("pip == 23.3.1" in item for item in pkgs))


if __name__ == "__main__":
    unittest.main()
