"""Dictionary Subclassing and Custom Item Assignment Demonstration Module.

This module demonstrates subclassing Python's built-in `dict` class and overriding `__setitem__`.
It highlights the importance of invoking `dict.__setitem__(self, key, val)` or `super().__setitem__(key, val)`
to avoid infinite recursive method calls (`self[key] = val`).
"""

from typing import Any


class DoThis(dict):
    """Subclass of dict overriding __setitem__ safely."""

    def __setitem__(self, key: Any, val: Any) -> None:
        """Override __setitem__ without recursive infinite loop.

        Args:
            key: Dictionary key.
            val: Dictionary value.
        """
        # Invoking dict.__setitem__ directly avoids infinite recursion loop (self[key] = val)
        dict.__setitem__(self, key, val)


if __name__ == "__main__":
    print("=== Dictionary Subclassing Demonstration ===")
    obj = DoThis()
    obj["key"] = "val"
    print("Dict Object Contents:", obj)
    print("Is instance of dict?:", isinstance(obj, dict))
