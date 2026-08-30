"""Class Reflection and Introspection Demonstration Module.

This module demonstrates inspecting class and instance objects using built-in reflection tools:
`dir()`, `__dict__`, `__class__`, `__doc__`, and `__dir__()`.
"""

from typing import List, Dict, Any


class Person:
    """Class representing a person object for introspection demonstrations."""

    def __init__(self, name: str) -> None:
        """Initialize Person with name."""
        self.name: str = name

    def __str__(self) -> str:
        """Return person's name as string representation."""
        return self.name


def inspect_all_dunder_attributes(instance: Person) -> Dict[str, str]:
    """Inspect standard dunder attributes on an instance object.

    Args:
        instance: Person object instance.

    Returns:
        Dictionary mapping attribute name to string representation.
    """
    return {
        "__class__": str(instance.__class__),
        "__doc__": str(instance.__doc__),
        "__dict__": str(instance.__dict__),
        "__str__": str(instance.__str__()),
    }


if __name__ == "__main__":
    print("=== Class Reflection & Introspection Demonstration ===")
    person = Person("Tomas")

    print("--- 1. Class Introspection using dir(Person) ---")
    print([attr for attr in dir(Person) if not attr.startswith("__")])

    print("\n--- 2. Instance Introspection using dir(person) ---")
    print(dir(person))

    print("\n--- 3. Dunder Attributes Summary ---")
    for key, val in inspect_all_dunder_attributes(person).items():
        print(f"  {key}: {val}")
