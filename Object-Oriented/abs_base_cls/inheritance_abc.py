"""Legacy Abstract Inheritance Script (Refactored).

This module updates the original `inheritance_abc.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed abstract inheritance, see `abstract_inheritance.py`.
"""

from abstract_inheritance import GetSetInt, GetSetList


if __name__ == "__main__":
    print("=== Legacy Abstract Inheritance (Refactored) ===")
    obj = GetSetInt(9)
    obj.set_val(7)
    print("GetSetInt Val:", obj.get_val())

    gsl = GetSetList(6)
    gsl.set_val(99)
    gsl.set_val(3)
    gsl.set_val(49)
    print("GetSetList Recent Val:", gsl.get_val())
    print("GetSetList History:", gsl.get_vals())
