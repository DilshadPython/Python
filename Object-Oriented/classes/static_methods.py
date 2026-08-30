"""Legacy Static Methods Script (Refactored).

This module updates the original `static_methods.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed car inventory, see `car_inventory.py`.
"""

import datetime
from car_inventory import Car


def is_workday(day: datetime.date) -> bool:
    """Check if date is a workday (Monday through Friday)."""
    return day.weekday() < 5


if __name__ == "__main__":
    print("=== Legacy Static Methods (Refactored) ===")
    car = Car("Audi", 2017, "Black", "S3", 33000)
    today = datetime.date(2017, 3, 28)
    print("Is Workday?:", is_workday(today))
