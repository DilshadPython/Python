"""Legacy Add Func Script (Refactored).

This module updates the original `add_func.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed operator overloading demonstrations, see `vector_arithmetic_overloading.py`.
"""

from vector_arithmetic_overloading import SumList


if __name__ == "__main__":
    print("=== Legacy Add Func (Refactored) ===")
    ob1 = SumList([10, 11, 22, 33, 41])
    ob2 = SumList([80, 121, 20, 300, 50])
    print("Pairwise Sum:", ob1 + ob2)
    print("Pairwise Subtraction:", ob1 - ob2)