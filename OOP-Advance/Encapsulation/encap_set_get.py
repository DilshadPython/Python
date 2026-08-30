"""Legacy Encap Set Get Script (Refactored).

This module updates the original `encap_set_get.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed getter/setter method demonstrations, see `getter_setter_methods.py`.
"""

from getter_setter_methods import Monitor


if __name__ == "__main__":
    print("=== Legacy Encap Set Get (Refactored) ===")
    obj1 = Monitor()
    obj1.set_val(22)
    print("Object 1 Value:", obj1.get_val())
