"""Legacy Class Methods Script (Refactored).

This module updates the original `class_methods.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed car inventory, see `car_inventory.py`.
"""

from car_inventory import Car


if __name__ == "__main__":
    print("=== Legacy Class Methods (Refactored) ===")
    c = Car("Audi", 2017, "Black", "S3", 33000)
    print("Store Total:", Car.total_cars_in_store)
