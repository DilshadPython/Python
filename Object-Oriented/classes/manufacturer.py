"""Legacy Manufacturer Script (Refactored).

This module updates the original `manufacturer.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed car inventory, see `car_inventory.py`.
"""

from car_inventory import Car


if __name__ == "__main__":
    print("=== Legacy Manufacturer (Refactored) ===")
    audi = Car("Audi", 2017, "Black", "S3", 33000)
    print("Audi Details:", audi.get_details())
