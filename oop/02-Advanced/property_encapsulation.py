"""
Advanced Object-Oriented Programming: Pythonic Encapsulation & Property Accessors.

This module demonstrates managing internal state via `@property`, `@var.setter`, and `@var.deleter`
hooks for attribute validation, name mangling (`__private`), and protected (`_protected`) conventions.
"""
# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Any


class Monitor:
    """Class showcasing @property accessors for attribute encapsulation."""

    def __init__(self, value: int) -> None:
        """Initialize Monitor with internal protected value."""
        self._attribute_val: int = value
        self.__mangled_name: str = "Private Class Data"

    @property
    def value(self) -> int:
        """Getter property for 'value'."""
        return self._attribute_val

    @value.setter
    def value(self, new_val: int) -> None:
        """Setter property for 'value' with validation guard clause."""
        if not isinstance(new_val, int):
            raise TypeError("Monitor value must be an integer.")
        if new_val < 0:
            raise ValueError("Monitor value cannot be negative.")
        self._attribute_val = new_val

    @value.deleter
    def value(self) -> None:
        """Deleter property resetting 'value' to default baseline zero."""
        self._attribute_val = 0

    @property
    def private_data(self) -> str:
        """Getter exposing private mangled attribute securely."""
        return self.__mangled_name
