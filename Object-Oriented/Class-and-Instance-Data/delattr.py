"""Legacy Delattr Script (Refactored).

This module updates the original `delattr.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed custom attribute deletion, see `custom_attribute_deleter.py`.
"""

from custom_attribute_deleter import TrackedProduct


if __name__ == "__main__":
    print("=== Legacy Delattr (Refactored) ===")
    prod = TrackedProduct("Computer")
    del prod.name