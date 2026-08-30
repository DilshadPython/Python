"""Built-in Dictionary Subclassing Demonstration Module.

This module demonstrates inheriting directly from the built-in `dict` class,
overriding `__setitem__` to insert custom logging while retaining core dictionary functionality.
"""

from typing import Any


class People(dict):
    """Subclass of dict logging key-value assignments."""

    def __setitem__(self, key: Any, value: Any) -> None:
        """Set key-value pair and print notification message.

        Args:
            key: Key identifier.
            value: Value payload.
        """
        print(f"Setting key: '{key}' -> value: '{value}'")
        dict.__setitem__(self, key, value)


if __name__ == "__main__":
    print("=== Dictionary Subclassing Demonstration ===")

    obj = People()
    obj["f"] = "Female"
    obj["m"] = "Male"
    obj["g"] = "Girl"
    obj["b"] = "Boy"

    print("\n--- Iterating over custom People dictionary ---")
    for key, value in obj.items():
        print(f"{key} : {value}")
