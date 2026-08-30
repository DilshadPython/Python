"""Legacy Example Script (Refactored).

This module updates the original `example.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed instance counting, see `instance_counter.py`.
"""

from instance_counter import TrackedCar


if __name__ == "__main__":
    print("=== Legacy Instance Counter Example (Refactored) ===")
    car1 = TrackedCar(4)
    car2 = TrackedCar(12)
    print("Total Instance Count:", TrackedCar.get_instance_count())
