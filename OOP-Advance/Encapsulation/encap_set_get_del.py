"""Legacy Encap Set Get Del Script (Refactored).

This module updates the original `encap_set_get_del.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed property encapsulation, see `property_encapsulation.py`.
"""

from property_encapsulation import Monitor


if __name__ == "__main__":
    print("=== Legacy Encap Set Get Del (Refactored) ===")
    obj = Monitor(18)
    print("Initial Value:", obj.var)
    obj.var = 301
    print("Updated Value:", obj.var)
    del obj.var
    print("Value after del:", obj.var)
