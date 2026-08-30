"""Legacy Class/Instance Attribute Script (Refactored).

This module updates the original `cls_attrib_and_instance_attrib.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed attribute behavior, see `class_vs_instance_attributes.py`.
"""

from class_vs_instance_attributes import VehicleInventory


if __name__ == "__main__":
    print("=== Legacy Class/Instance Attribute (Refactored) ===")
    inv = VehicleInventory("Sedan")
    inv.configure_inventory(25000.0, 3)
    print("Instance stock count:", inv.stock_count)