"""Legacy Regular Methods Script (Refactored).

This module updates the original `regular_methods.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed car inventory, see `car_inventory.py`.
"""

from car_inventory import Car


if __name__ == "__main__":
    print("=== Legacy Regular Methods (Refactored) ===")
    obj_one = "Ford-2010-Black-S3-33100"
    name, model, color, types, price = obj_one.split("-")
    car = Car(name, int(model), color, types, float(price))
    print(car.get_details())
