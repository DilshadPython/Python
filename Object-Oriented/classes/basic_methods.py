"""Legacy Basic Methods Script (Refactored).

This module updates the original `basic_methods.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed car inventory, see `car_inventory.py`.
"""

from car_inventory import Car


if __name__ == "__main__":
    print("=== Legacy Basic Methods (Refactored) ===")
    obj_audi = Car("Audi", 2017, "Black", "S3", 33000)
    print("Car Details:", obj_audi.get_details())
    print("Profit Price:", obj_audi.calculate_price_with_profit())
