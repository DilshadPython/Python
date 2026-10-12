"""cloud_app/tutorials/python_packaging_basics.py

Python Packaging, Distribution & Dependency Management Masterclass
===================================================================
Comprehensive tutorial module demonstrating:
1. Modern pyproject.toml Configuration & PEP 621 Standard Metadata
2. Package Directory Layout (src-layout vs flat-layout)
3. Semantic Versioning Parsing & Validation (MAJOR.MINOR.PATCH)
4. Dependency Specification & Version Constraint Resolution
5. Package Build & Distribution Artifact Generation (.whl & .tar.gz)
6. PyPI Publishing Pipeline & Local Editable Installation Workflow
"""

import os
import re
from typing import Any, Dict, List, Optional, Tuple


# ==============================================================================
# 1. SEMANTIC VERSIONING (SemVer 2.0.0) ENGINE
# ==============================================================================


class SemanticVersion:
    """Parses and validates Semantic Version strings (MAJOR.MINOR.PATCH[-PRERELEASE])."""

    SEMVER_REGEX = re.compile(
        r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
        r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
        r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?$"
    )

    def __init__(self, version_str: str) -> None:
        match = self.SEMVER_REGEX.match(version_str.strip())
        if not match:
            raise ValueError(
                f"Invalid Semantic Version format: '{version_str}'. Expected 'MAJOR.MINOR.PATCH'"
            )
        self.major = int(match.group("major"))
        self.minor = int(match.group("minor"))
        self.patch = int(match.group("patch"))
        self.prerelease = match.group("prerelease")
        self.version_str = version_str

    def bump_patch(self) -> str:
        """Bump patch version for backwards-compatible bug fixes."""
        return f"{self.major}.{self.minor}.{self.patch + 1}"

    def bump_minor(self) -> str:
        """Bump minor version for new backwards-compatible functionality."""
        return f"{self.major}.{self.minor + 1}.0"

    def bump_major(self) -> str:
        """Bump major version for incompatible API breaking changes."""
        return f"{self.major + 1}.0.0"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "version": self.version_str,
            "major": self.major,
            "minor": self.minor,
            "patch": self.patch,
            "prerelease": self.prerelease,
        }


# ==============================================================================
# 2. PYPROJECT.TOML CONFIGURATION GENERATOR (PEP 621)
# ==============================================================================


def generate_pyproject_toml(
    name: str = "teachcloud-sdk",
    version: str = "1.0.0",
    description: str = "TeachCloud Enterprise Python SDK",
    author_name: str = "TeachCloud Engineering",
    author_email: str = "dev@teachcloud.dev",
    dependencies: Optional[List[str]] = None,
    build_backend: str = "setuptools.build_meta",
) -> str:
    """Generate a standard PEP 621 compliant pyproject.toml specification."""
    if dependencies is None:
        dependencies = ["requests>=2.31.0,<3.0.0", "pydantic>=2.5.0"]

    deps_formatted = ",\n    ".join(f'"{d}"' for d in dependencies)

    toml_content = f"""[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "{build_backend}"

[project]
name = "{name}"
version = "{version}"
description = "{description}"
readme = "README.md"
requires-python = ">=3.10"
license = {{ text = "MIT" }}
authors = [
    {{ name = "{author_name}", email = "{author_email}" }}
]
keywords = ["packaging", "sdk", "teachcloud", "distribution"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
dependencies = [
    {deps_formatted}
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "mypy>=1.8.0",
    "ruff>=0.2.0",
]

[project.urls]
Homepage = "https://teachcloud.dev"
Documentation = "https://teachcloud.dev/docs"
Repository = "https://github.com/DilshadGit/cloud_flask"
"""
    return toml_content


# ==============================================================================
# 3. PACKAGE STRUCTURE & DEPENDENCY RESOLUTION SIMULATOR
# ==============================================================================


def analyze_package_structure(package_name: str = "my_library") -> Dict[str, Any]:
    """Simulate src-layout vs flat-layout package directory structure analysis."""
    src_layout_tree = [
        f"{package_name}/",
        "├── pyproject.toml",
        "├── README.md",
        "├── LICENSE",
        "├── src/",
        f"│   └── {package_name}/",
        "│       ├── __init__.py",
        "│       ├── core.py",
        "│       └── py.typed",
        "└── tests/",
        "    └── test_core.py",
    ]

    flat_layout_tree = [
        f"{package_name}/",
        "├── pyproject.toml",
        "├── README.md",
        f"├── {package_name}/",
        "│   ├── __init__.py",
        "│   └── core.py",
        "└── tests/",
        "    └── test_core.py",
    ]

    return {
        "package_name": package_name,
        "recommended_layout": "src-layout (PEP 621 Standard)",
        "src_layout_tree": "\n".join(src_layout_tree),
        "flat_layout_tree": "\n".join(flat_layout_tree),
        "src_layout_benefits": [
            "Prevents accidental import of un-installed local source files during testing",
            "Enforces clean installation testing using isolated virtual environments",
            "Explicit separation of source code, configuration, and test suites",
        ],
    }


def resolve_dependency_constraints(specs: List[str]) -> List[Dict[str, str]]:
    """Parse and resolve dependency version specifications."""
    resolved = []
    constraint_regex = re.compile(
        r"^(?P<package>[a-zA-Z0-9_\-]+)(?P<operator>>=|<=|==|~=|<|>|\^)?(?P<version>[\d\.]+)?$"
    )

    for spec in specs:
        match = constraint_regex.match(spec.strip())
        if match:
            pkg = match.group("package")
            op = match.group("operator") or "ANY"
            ver = match.group("version") or "*"
            resolved.append(
                {"package": pkg, "constraint": op, "version": ver, "spec_raw": spec}
            )

    return resolved


# ==============================================================================
# 4. PACKAGE BUILDING & PUBLISHING WORKFLOW SIMULATION
# ==============================================================================


def simulate_package_build(
    package_name: str = "teachcloud_sdk", version: str = "1.0.0"
) -> Dict[str, Any]:
    """Simulate generating build distribution artifacts (.whl and .tar.gz)."""
    norm_name = package_name.replace("-", "_")
    sdist_filename = f"{norm_name}-{version}.tar.gz"
    wheel_filename = f"{norm_name}-{version}-py3-none-any.whl"

    return {
        "package_name": package_name,
        "version": version,
        "build_command": "python -m build",
        "artifacts_generated": {
            "source_distribution": f"dist/{sdist_filename}",
            "wheel_distribution": f"dist/{wheel_filename}",
        },
        "build_steps": [
            "1. Validating pyproject.toml configuration and metadata...",
            f"2. Building source distribution: dist/{sdist_filename}",
            f"3. Building wheel distribution: dist/{wheel_filename}",
            "4. Successfully generated 2 distribution artifacts in ./dist/",
        ],
        "installation_commands": {
            "local_editable": f"pip install -e .",
            "wheel_install": f"pip install dist/{wheel_filename}",
            "pypi_publish": f"python -m twine upload dist/*",
        },
    }


# ==============================================================================
# MASTER DEMONSTRATION FUNCTION FOR INTERACTIVE STUDIO
# ==============================================================================


def demonstrate_packaging_masterclass() -> Dict[str, Any]:
    """Execute master packaging benchmark and workflow simulation."""
    semver = SemanticVersion("1.4.2")
    pyproject = generate_pyproject_toml(version=semver.version_str)
    layout = analyze_package_structure("teachcloud_sdk")
    deps = resolve_dependency_constraints(
        ["requests>=2.31.0", "pydantic~=2.5.0", "flask==3.0.2"]
    )
    build = simulate_package_build("teachcloud-sdk", semver.version_str)

    return {
        "semver_parsing": semver.to_dict(),
        "semver_next_minor": semver.bump_minor(),
        "pyproject_toml_sample": pyproject[:300] + "\n...",
        "package_layout": layout["recommended_layout"],
        "resolved_dependencies": deps,
        "build_artifacts": build["artifacts_generated"],
    }


if __name__ == "__main__":
    print("=== Python Packaging & Distribution Masterclass ===")
    demo = demonstrate_packaging_masterclass()
    print("SemVer:", demo["semver_parsing"])
    print("Package Layout:", demo["package_layout"])
    print("Build Artifacts:", demo["build_artifacts"])
