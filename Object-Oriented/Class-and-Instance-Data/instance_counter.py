"""Instance Counter Demonstration Module.

This module demonstrates tracking object creation counts across instances using class attributes.
"""

from typing import List


class TrackedCar:
    """Class maintaining a shared count of all instantiated instances."""

    total_instances: int = 0

    def __init__(self, serial_number: int) -> None:
        """Initialize TrackedCar with serial number and increment shared instance counter."""
        self.serial_number: int = serial_number
        TrackedCar.total_instances += 1

    def get_serial_number(self) -> int:
        """Return car serial number."""
        return self.serial_number

    @classmethod
    def get_instance_count(cls) -> int:
        """Return total instance count across all objects."""
        return cls.total_instances


if __name__ == "__main__":
    print("=== Instance Counter Demonstration ===")
    cars: List[TrackedCar] = [TrackedCar(num) for num in (4, 12, 27, 33, 9)]

    print(f"Created {len(cars)} car instances.")
    for car in cars:
        print(f"  Car Serial #{car.get_serial_number()} | Total Count: {car.get_instance_count()}")
