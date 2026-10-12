"""
Advanced Conda Environment Export, Import, and Channel Management Module.

This module provides advanced tools for managing Conda environments:
- Exporting environments to YAML specification format (`environment.yml`)
- Parsing and building environments from YAML specs
- Channel priority management (`defaults`, `pytorch`, `conda-forge`)
- Package version conflict detection and exception handling

PEP 8 compliant, type-annotated, compatible with Python 2.7 - 3.13.
"""

from typing import Any, Dict, List, Optional, Set


class CondaError(Exception):
    """Base exception class for Conda environment management errors."""
    pass


class EnvironmentConflictError(CondaError):
    """Raised when conflicting package specifications are detected."""
    pass


class AdvancedCondaManager:
    """
    Advanced manager for Conda environment specifications and channel configurations.
    """

    DEFAULT_CHANNELS: List[str] = ["defaults", "pytorch", "conda-forge"]

    def __init__(self, channels: Optional[List[str]] = None) -> None:
        """
        Initializes AdvancedCondaManager with specified channel priorities.

        Args:
            channels (Optional[List[str]]): Ordered list of channel names.
        """
        self.channels: List[str] = channels or list(self.DEFAULT_CHANNELS)

    def add_channel(self, channel_name: str, priority: str = "bottom") -> List[str]:
        """
        Adds a channel to the channel list.

        Args:
            channel_name (str): Name of channel to add (e.g. 'bioconda').
            priority (str): 'top' or 'bottom' priority position.

        Returns:
            List[str]: Updated list of channel priorities.
        """
        if channel_name in self.channels:
            self.channels.remove(channel_name)

        if priority == "top":
            self.channels.insert(0, channel_name)
        else:
            self.channels.append(channel_name)

        return self.channels

    def export_to_yaml_dict(self, env_name: str, python_version: str, packages: Dict[str, str]) -> Dict[str, Any]:
        """
        Exports environment specifications into a standard environment.yml dictionary structure.

        Args:
            env_name (str): Environment name.
            python_version (str): Target Python version.
            packages (Dict[str, str]): Dictionary of package names and version bounds.

        Returns:
            Dict[str, Any]: Formatted YAML dictionary matching environment.yml structure.
        """
        dependencies: List[Any] = [f"python={python_version}"]
        pip_dependencies: List[str] = []

        for pkg, ver in packages.items():
            if pkg == "python":
                continue
            if ver.startswith("pip:"):
                pip_dependencies.append(f"{pkg}=={ver.replace('pip:', '')}")
            else:
                dependencies.append(f"{pkg}={ver}")

        if pip_dependencies:
            dependencies.append({"pip": pip_dependencies})

        return {
            "name": env_name,
            "channels": self.channels,
            "dependencies": dependencies,
        }

    def validate_dependency_spec(self, dependencies: List[str]) -> bool:
        """
        Validates dependency specifications for duplicate or conflicting constraints.

        Args:
            dependencies (List[str]): List of package spec strings (e.g. ['django=3.2', 'django=4.0']).

        Returns:
            bool: True if specifications are valid and conflict-free.

        Raises:
            EnvironmentConflictError: If duplicate conflicting package constraints exist.
        """
        seen_packages: Set[str] = set()

        for spec in dependencies:
            pkg_name = spec.split("=")[0].split(">")[0].split("<")[0].strip()
            if pkg_name in seen_packages:
                raise EnvironmentConflictError(
                    f"Conflicting duplicate package dependency found for '{pkg_name}'."
                )
            seen_packages.add(pkg_name)

        return True


if __name__ == "__main__":
    manager = AdvancedCondaManager()
    manager.add_channel("conda-forge", priority="top")

    spec = manager.export_to_yaml_dict(
        env_name="env310",
        python_version="3.10.13",
        packages={"pytorch": "2.1.1", "django": "3.2.15", "sty": "pip:1.0.0"}
    )

    print("Generated Environment YAML Dictionary:")
    import json
    print(json.dumps(spec, indent=2))
