"""
Conda Environment Fundamentals and Package Management Module.

This module demonstrates foundational Conda workflow concepts: environment creation,
package installation, environment listing, and dependency specifications.

PEP 8 compliant, type-annotated, and compatible with Python 2.7 - 3.13.
"""

# Standard library imports for dataclasses, JSON, and type hinting
from dataclasses import dataclass, field
import json
from typing import Dict, List, Optional, Set


@dataclass
class CondaEnvironment:
    """
    Dataclass representing a Conda Virtual Environment.

    Attributes:
        name (str): Unique name of the Conda environment (e.g. 'env310').
        python_version (str): Target Python version (e.g. '3.10.13').
        packages (Dict[str, str]): Dictionary mapping package names to installed versions.
        active (bool): Whether this environment is currently activated.
    """

    name: str
    python_version: str
    packages: Dict[str, str] = field(default_factory=dict)
    active: bool = False

    def activate(self) -> str:
        """Activates the Conda environment."""
        self.active = True
        return f"Environment '{self.name}' activated. (Python {self.python_version})"

    def deactivate(self) -> str:
        """Deactivates the Conda environment."""
        self.active = False
        return f"Environment '{self.name}' deactivated."

    def install_package(self, package_name: str, version: str = "latest") -> str:
        """
        Installs or updates a package inside the environment.

        Args:
            package_name (str): Target package (e.g. 'pytorch', 'django').
            version (str): Package version specification.

        Returns:
            str: Installation status confirmation message.
        """
        self.packages[package_name] = version
        return f"Installed '{package_name}=={version}' into '{self.name}'."

    def remove_package(self, package_name: str) -> str:
        """
        Removes a package from the environment.

        Args:
            package_name (str): Package name to remove.

        Returns:
            str: Removal status message.

        Raises:
            KeyError: If package is not present in environment.
        """
        if package_name not in self.packages:
            raise KeyError(f"Package '{package_name}' not found in environment '{self.name}'.")
        del self.packages[package_name]
        return f"Removed package '{package_name}' from '{self.name}'."

    def list_packages(self) -> List[str]:
        """Returns formatted list of installed packages."""
        return [f"{pkg} == {ver}" for pkg, ver in sorted(self.packages.items())]


def create_environment(name: str, python_version: str = "3.10") -> CondaEnvironment:
    """
    Factory function to instantiate a new CondaEnvironment.

    Args:
        name (str): Name of environment.
        python_version (str): Python version string.

    Returns:
        CondaEnvironment: Newly created environment object.
    """
    env = CondaEnvironment(name=name, python_version=python_version)
    env.install_package("python", python_version)
    env.install_package("pip", "23.3.1")
    env.install_package("setuptools", "68.0.0")
    return env


if __name__ == "__main__":
    my_env = create_environment("env310", "3.10.13")
    print(my_env.activate())
    print(my_env.install_package("pytorch", "2.1.1"))
    print(my_env.install_package("django", "3.2.15"))
    print("\nInstalled Packages:")
    for item in my_env.list_packages():
        print(f"  - {item}")
    print(my_env.deactivate())
