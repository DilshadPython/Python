"""
Object-Oriented Programming Fundamentals: Single Inheritance & Method Overriding.

This module demonstrates single inheritance between base (parent) and derived (child) classes,
attribute delegation via `super()`, and instance type checking with `isinstance()`/`issubclass()`.
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Optional


class Person:
    """Base class representing a general person entity."""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """
        Initialize Person instance attributes.

        Args:
            first_name (str): Person's first name.
            last_name (str): Person's last name.
            age (int): Person's age in years.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age

    def full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"


class Developer(Person):
    """Derived class inheriting from Person representing a software developer."""

    def __init__(self, first_name: str, last_name: str, age: int, programming_language: str) -> None:
        """
        Initialize Developer instance delegating base attributes to Person via super().

        Args:
            first_name (str): Developer's first name.
            last_name (str): Developer's last name.
            age (int): Developer's age in years.
            programming_language (str): Primary coding language (e.g. Python, Rust).
        """
        # Call base class constructor using modern argumentless super()
        super().__init__(first_name, last_name, age)
        self.programming_language: str = programming_language

    def developer_summary(self) -> str:
        """Return formatted developer profile summary."""
        return f"{self.full_name()} ({self.age}) - Primary Tech: {self.programming_language}"
