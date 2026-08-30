"""Legacy Class Library Script (Refactored).

This module updates the original `class_lib.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For comprehensive class definition basics, see `class_definition_basics.py`.
"""

from class_definition_basics import Car, inspect_object_attributes


if __name__ == "__main__":
    print("=== Legacy Class Library (Refactored) ===")
    print("Car Class Attributes:", inspect_object_attributes(Car))
    my_car = Car()
    print("Car Instance Attributes:", inspect_object_attributes(my_car))