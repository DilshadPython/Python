"""
Beginner Level Attributes & Methods Module (`beginner_attributes_methods.py`).

This module provides clear, well-commented examples of fundamental Python attributes,
instance methods, built-in data structure methods, and basic dunder hooks (`__init__`, `__str__`, `__len__`).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI execution exit status.
# - `from typing import Any, List`: PEP 484 type hint generics.
# =========================================================================
import sys
from typing import Any, List


class Book:
    """Beginner class demonstrating instance attributes and instance methods."""

    def __init__(self, title: str, author: str, pages: int) -> None:
        """Initialize instance attributes (`self.title`, `self.author`, `self.pages`).

        Args:
            title (str): Book title string.
            author (str): Author name string.
            pages (int): Total page count integer.
        """
        # Instance Attributes: bound to specific instance object
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self) -> str:
        """Instance Method: operates on self instance data."""
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def __str__(self) -> str:
        """Dunder Method (`__str__`): returns user-friendly string representation."""
        return f"Book: {self.title}"

    def __len__(self) -> int:
        """Dunder Method (`__len__`): defines custom len() behavior."""
        return self.pages


def demonstrate_builtin_type_methods() -> None:
    """Demonstrate built-in object attributes and methods for strings, lists, and dicts."""
    # 1. String Methods
    text = "  python programming  "
    cleaned = text.strip().title()  # .strip() and .title() string methods
    print(f"Cleaned String: '{cleaned}'")

    # 2. List Methods
    numbers = [10, 20, 30]
    numbers.append(40)  # .append() list method
    popped = numbers.pop()  # .pop() list method
    print(f"List After Append & Pop: {numbers} (Popped: {popped})")

    # 3. Dict Methods
    person = {"name": "Dilshad", "role": "Developer"}
    role = person.get("role", "Unknown")  # .get() dict method
    keys = list(person.keys())  # .keys() dict method
    print(f"Dict Key Lookup: role='{role}', keys={keys}")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for beginner attributes and methods demonstration."""
    print("=== Beginner Level Attributes & Methods Demonstration ===")

    book = Book("Python 101", "Dilshad Abdulla", 350)

    # Accessing instance attributes
    print(f"Book Title Attribute: {book.title}")
    print(f"Book Author Attribute: {book.author}")

    # Invoking instance methods
    print(f"Summary Method Output: {book.get_summary()}")

    # Invoking dunder methods via built-in functions str() and len()
    print(f"str(book): {str(book)}")
    print(f"len(book): {len(book)}")

    print("\n--- Built-in Type Methods ---")
    demonstrate_builtin_type_methods()

    return 0


if __name__ == "__main__":
    sys.exit(main())
