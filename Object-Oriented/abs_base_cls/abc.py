"""Legacy Abstract Base Class Script (Refactored).

This module updates the original `abc.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For comprehensive abstract base class definitions, see `abstract_base_class.py`.
"""

from abstract_base_class import GetterSetter, ValueContainer


if __name__ == "__main__":
    print("=== Legacy Abstract Base Class (Refactored) ===")
    obj = ValueContainer(100)
    print("Value Container Value:", obj.get_val())
