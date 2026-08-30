"""Legacy Style Class Script (Refactored).

This module updates the original `style_class.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed class model evolution analysis, see `classic_vs_new_style_class.py`.
"""

from classic_vs_new_style_class import ClassicStyle as OldName, ExplicitNewStyle as NewClass


if __name__ == "__main__":
    print("=== Legacy Style Class (Refactored) ===")
    oc = OldName()
    nc = NewClass()
    print("OldName type:", type(oc))
    print("NewClass type:", type(nc))