"""
Unit Test Suite for Advanced Conda Environment Management Module.

Tests YAML dictionary exports, channel priority configuration, dependency conflict validation,
and custom exception handling.
"""

import unittest
from conda_advanced import AdvancedCondaManager, EnvironmentConflictError


class TestAdvancedConda(unittest.TestCase):
    """Test cases for AdvancedCondaManager channel handling and YAML exporting."""

    def setUp(self) -> None:
        """Initialize AdvancedCondaManager instance before each test."""
        self.manager = AdvancedCondaManager()

    def test_channel_priority_top(self) -> None:
        """Verify inserting channel at top priority."""
        self.manager.add_channel("conda-forge", priority="top")
        self.assertEqual(self.manager.channels[0], "conda-forge")

    def test_channel_priority_bottom(self) -> None:
        """Verify adding channel at bottom priority."""
        self.manager.add_channel("bioconda", priority="bottom")
        self.assertEqual(self.manager.channels[-1], "bioconda")

    def test_export_to_yaml_dict(self) -> None:
        """Verify exporting environment specification to environment.yml dictionary."""
        spec = self.manager.export_to_yaml_dict(
            env_name="prod_env",
            python_version="3.10.13",
            packages={"pytorch": "2.1.1", "requests": "pip:2.31.0"}
        )

        self.assertEqual(spec["name"], "prod_env")
        self.assertIn("python=3.10.13", spec["dependencies"])
        self.assertIn("pytorch=2.1.1", spec["dependencies"])

        # Verify pip dependencies section
        pip_section = [item for item in spec["dependencies"] if isinstance(item, dict) and "pip" in item]
        self.assertEqual(len(pip_section), 1)
        self.assertIn("requests==2.31.0", pip_section[0]["pip"])

    def test_validate_dependency_spec_valid(self) -> None:
        """Verify validation passes for conflict-free package list."""
        valid_deps = ["python=3.10", "pytorch=2.1.1", "django=3.2"]
        self.assertTrue(self.manager.validate_dependency_spec(valid_deps))

    def test_validate_dependency_spec_conflict(self) -> None:
        """Verify EnvironmentConflictError is raised when duplicate specs exist."""
        conflict_deps = ["django=3.2", "django=4.0"]
        with self.assertRaises(EnvironmentConflictError):
            self.manager.validate_dependency_spec(conflict_deps)


if __name__ == "__main__":
    unittest.main()
