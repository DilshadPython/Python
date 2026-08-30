"""Legacy Procedural vs Object Paradigm Script (Refactored).

This module updates the original `procedural_obj_paradigm.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed procedural vs OOP comparison, see `procedural_vs_oop.py`.
"""

from procedural_vs_oop import CustomerCounter, run_procedural_example


if __name__ == "__main__":
    print("=== Legacy Procedural vs Object Paradigm (Refactored) ===")
    print("Procedural Result:", run_procedural_example())
    counter = CustomerCounter(2)
    counter.increment(3)
    print("OOP Counter Result:", counter.count)