"""Legacy Automobiles Script (Refactored).

This module updates the original `automobiles.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed car inventory, see `car_inventory.py`.
"""

from car_inventory import Car


if __name__ == "__main__":
    print("=== Legacy Automobiles (Refactored) ===")
    audi = Car("Audi", 2017, "Black", "S3", 33000)
    bmw = Car("BMW", 2016, "Gray", "Z3", 28500)
    print("Audi Details:", audi.get_details())
    print("Store Total:", Car.total_cars_in_store)
