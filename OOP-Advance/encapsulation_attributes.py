"""Attribute Encapsulation, Privacy Modifiers, and Property Management Module.

This module demonstrates Python attribute access control conventions:
1. Public Attributes: Unrestricted access (`attribute_name`).
2. Protected Attributes: Non-public convention (`_attribute_name`).
3. Private Name Mangling: Double leading underscore (`__mangled_name`), mangled to `_ClassName__mangled_name`.
4. Managed Properties: Access controlled via `@property`, `@setter`, and `@deleter`.
"""

from typing import Optional, Any


class Monitor:
    """Class showcasing public, protected, private attributes and managed properties."""

    # Public class attribute
    instance_count: int = 0

    # Private mangled class attribute
    __mangled_name: str = "Private Class Data"

    def __init__(self, value: int) -> None:
        """Initialize Monitor with protected internal attribute.

        Args:
            value: Initial value.
        """
        self._attribute_val: int = value
        Monitor.instance_count += 1

    @property
    def value(self) -> int:
        """Getter property for managed attribute access."""
        print('Getting the "value" attribute')
        return self._attribute_val

    @value.setter
    def value(self, val: int) -> None:
        """Setter property for managed attribute modification."""
        print('Setting the "value" attribute')
        self._attribute_val = val

    @value.deleter
    def value(self) -> None:
        """Deleter property for managed attribute reset/deletion."""
        print('Deleting the "value" attribute')
        self._attribute_val = 0

    def get_private_mangled_name(self) -> str:
        """Internal method accessing private mangled class attribute."""
        return self.__mangled_name


if __name__ == "__main__":
    print("=== Attribute Encapsulation & Privacy Demonstration ===")
    obj = Monitor(18)

    print("\n--- 1. Protected Attribute Access (_single_underscore) ---")
    print("Protected attribute value:", obj._attribute_val)

    print("\n--- 2. Managed Property Access (@property) ---")
    print("Property Value:", obj.value)
    obj.value = 301
    print("Updated Property Value:", obj.value)
    del obj.value
    print("Value after del:", obj.value)

    print("\n--- 3. Private Name Mangling (__double_underscore) ---")
    print("Access via Class Method:", obj.get_private_mangled_name())
    print("Access via Mangled Name (_Monitor__mangled_name):", obj._Monitor__mangled_name)

    try:
        print("Direct access to __mangled_name (Fails):", obj.__mangled_name)  # Type: ignore
    except AttributeError as err:
        print("AttributeError Caught as expected:", err)
