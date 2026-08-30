"""Property Decorator Encapsulation Module.

This module demonstrates Pythonic property encapsulation using `@property`,
`@var.setter`, and `@var.deleter` decorators to manage attribute getter, setter, and deleter hooks.
"""

from typing import Any


class Monitor:
    """Class showcasing @property accessors for attribute encapsulation."""

    def __init__(self, value: int) -> None:
        """Initialize Monitor with internal attribute value.

        Args:
            value: Initial integer value.
        """
        self._attribute_val: int = value

    @property
    def var(self) -> int:
        """Getter property for 'var'."""
        print('Getting the "var" attribute')
        return self._attribute_val

    @var.setter
    def var(self, value: int) -> None:
        """Setter property for 'var'."""
        print('Setting the "var" attribute')
        self._attribute_val = value

    @var.deleter
    def var(self) -> None:
        """Deleter property for 'var'."""
        print('Deleting the "var" attribute')
        self._attribute_val = 0


if __name__ == "__main__":
    print("=== Property Encapsulation Demonstration ===")

    obj1 = Monitor(18)
    obj2 = Monitor(77)

    print("Initial Property Values:", obj1.var, obj2.var)

    obj1.var = 301
    obj2.var = 444

    print("Updated obj1.var:", obj1.var)
    print("Updated obj2.var:", obj2.var)

    print("\n--- Deleting obj1.var ---")
    del obj1.var
    print("obj1.var after deletion:", obj1.var)
    print("obj2.var (unaffected):", obj2.var)
