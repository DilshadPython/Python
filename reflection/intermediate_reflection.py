"""
Intermediate Level Object Introspection & Attribute Reflection Module (`intermediate_reflection.py`).

This module provides functional reflection patterns designed for intermediate developers
(dynamic attribute inspection `getattr`, `setattr`, `hasattr`, `dir()`, function signature introspection `inspect.signature`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import inspect`: Standard library module for signature and docstring introspection.
# - `import sys`: System execution utilities.
# - `from typing import Any, Dict, List`: PEP 484 type hint generics.
# =========================================================================
import inspect
import sys
from typing import Any, Dict, List


class StudentProfile:
    """Sample class representing a student profile for introspection testing."""

    def __init__(self, name: str, age: int, skills: List[str]) -> None:
        self.name = name
        self.age = age
        self.skills = skills

    def add_skill(self, skill: str) -> None:
        """Add a new skill string to student profile."""
        self.skills.append(skill)

    def get_summary(self) -> str:
        """Return formatted profile summary string."""
        return f"Student {self.name} (Age: {self.age}) - Skills: {', '.join(self.skills)}"


def introspect_object_details(obj: Any) -> Dict[str, Any]:
    """Inspect object attributes, types, and method signatures at runtime.

    Args:
        obj (Any): Target object instance.

    Returns:
        Dict[str, Any]: Metadata map containing attribute names, values, and signatures.
    """
    metadata: Dict[str, Any] = {"class_name": type(obj).__name__, "attributes": {}, "methods": {}}

    for attr in dir(obj):
        if not attr.startswith("__"):
            val = getattr(obj, attr)
            if callable(val):
                sig = str(inspect.signature(val))
                metadata["methods"][attr] = sig
            else:
                metadata["attributes"][attr] = val

    return metadata


def dynamically_update_attribute(obj: Any, attr_name: str, new_value: Any) -> bool:
    """Safely check and dynamically update attribute using `hasattr` and `setattr`.

    Args:
        obj (Any): Target object instance.
        attr_name (str): Attribute name string.
        new_value (Any): New value to assign.

    Returns:
        bool: True if attribute existed and was updated, False if newly created.
    """
    existed = hasattr(obj, attr_name)
    setattr(obj, attr_name, new_value)
    return existed


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for intermediate reflection demonstration."""
    print("=== Intermediate Level Object Introspection ===")

    student = StudentProfile("Dilshad", 25, ["Python", "Django"])
    details = introspect_object_details(student)

    print(f"Inspected Class: {details['class_name']}")
    print(f"Attributes: {details['attributes']}")
    print(f"Methods & Signatures: {details['methods']}")

    updated = dynamically_update_attribute(student, "age", 26)
    print(f"Updated 'age' (Existed previously? {updated}) -> New Age: {student.age}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
