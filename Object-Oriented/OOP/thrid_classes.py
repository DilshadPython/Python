"""Legacy Third Classes Script (Refactored).

This module updates the original `thrid_classes.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed vehicle hierarchy, see `vehicle_hierarchy.py`.
"""

from vehicle_hierarchy import Vehicle as Veichle, Car, Van


if __name__ == "__main__":
    print("=== Legacy Third Classes (Refactored) ===")
    mycar = Car("AM80 YTR", "Audi", 80)
    myvan = Van("RM69 GHT", "Ford Transit", 120, 6)
    print(mycar.description())
    print(myvan.description())
