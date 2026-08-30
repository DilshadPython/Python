"""Legacy Set and Get Script (Refactored).

This module updates the original `set_and_get.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed house price property encapsulation, see `house_price_encapsulation.py`.
"""

from house_price_encapsulation import House


if __name__ == "__main__":
    print("=== Legacy Set and Get (Refactored) ===")
    obj1 = House(745662)
    obj2 = House(850434)
    print("First House Cost:", obj1.price)
    print("Second House Cost:", obj2.price)