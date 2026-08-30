"""Legacy Ice Cream Machine Script (Refactored).

This module updates the original `IceCreamMachine.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed domain modeling, see `ice_cream_machine.py`.
"""

from ice_cream_machine import IceCreamMachine


if __name__ == "__main__":
    print("=== Legacy Ice Cream Machine (Refactored) ===")
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print("Generated Scoops:", machine.generate_scoops())