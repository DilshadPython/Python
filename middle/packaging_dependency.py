"""
Section 17: Packaging & Dependency Management

Description: Master modern Python packaging: pyproject.toml (PEP 621), virtual environments (venv), build backends, dev dependency groups, and Semantic Versioning.
Level: Middle
URL: http://127.0.0.1:5000/python/middle/packaging_dependency
"""

# --- Code Snippet 1 ---
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "cloud-app"
version = "1.0.0"
requires-python = ">=3.11"

dependencies = [
    "fastapi>=0.110.0,,
    "sqlalchemy[asyncio]>=2.0.28",
    "pydantic>=2.6.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "mypy>=1.8.0",
    "ruff>=0.3.0",
]

