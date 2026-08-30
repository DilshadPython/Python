"""Method Decorators Demonstration Module.

This module demonstrates the 3 distinct method decorators in Python:
- Instance Methods (bound to `self` instance)
- Class Methods (`@classmethod`, bound to `cls` class)
- Static Methods (`@staticmethod`, unbound utility functions inside class scope)
"""

from typing import Any


class InstanceCounter:
    """Class showcasing instance, class, and static method decorators."""

    total_count: int = 0

    def __init__(self, initial_value: Any) -> None:
        """Initialize InstanceCounter with static method integer filtering."""
        self.val: int = self.filter_int(initial_value)
        InstanceCounter.total_count += 1

    def get_val(self) -> int:
        """Instance method accessing instance state (self.val)."""
        return self.val

    def set_val(self, new_val: Any) -> None:
        """Instance method updating instance state."""
        self.val = self.filter_int(new_val)

    @classmethod
    def get_count(cls) -> int:
        """Class method accessing class state (cls.total_count)."""
        return cls.total_count

    @staticmethod
    def filter_int(value: Any) -> int:
        """Static method utility filtering integer inputs without needing self or cls."""
        return value if isinstance(value, int) else 0


if __name__ == "__main__":
    print("=== Method Decorators Demonstration ===")
    a = InstanceCounter(107)
    b = InstanceCounter(22)
    c = InstanceCounter("InvalidString")

    print("a Value:", a.get_val())
    print("b Value:", b.get_val())
    print("c Value (filtered invalid input):", c.get_val())
    print("Total Instance Count (via @classmethod):", InstanceCounter.get_count())
