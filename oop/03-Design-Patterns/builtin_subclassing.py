"""
Advanced Object-Oriented Programming: Built-in Subclassing & Container Operator Overloading.

This module demonstrates extending native Python data types (`dict`, `list`) by subclassing built-in classes,
implementing 1-based indexing sequence containers, and overloading `__getitem__` / `__setitem__`.
"""
# "from typing import ..." imports specific type annotations directly into local scope.
from typing import Any, List


class LoggingDict(dict):
    """Dictionary subclass logging key assignment operations."""

    def __setitem__(self, key: Any, value: Any) -> None:
        """Override __setitem__ to log key assignment."""
        print(f"LoggingDict: Assigning key '{key}' -> value '{value}'")
        super().__setitem__(key, value)


class OneBasedList(list):
    """List subclass supporting 1-based indexing for educational containers."""

    def __getitem__(self, index: int) -> Any:
        """Override __getitem__ converting 1-based index to 0-based list offset."""
        if isinstance(index, int):
            if index > 0:
                return super().__getitem__(index - 1)
            elif index < 0:
                return super().__getitem__(index)
            raise IndexError("1-based index cannot be zero.")
        return super().__getitem__(index)

    def __setitem__(self, index: int, value: Any) -> None:
        """Override __setitem__ converting 1-based index to 0-based list offset."""
        if isinstance(index, int) and index > 0:
            super().__setitem__(index - 1, value)
        else:
            super().__setitem__(index, value)
