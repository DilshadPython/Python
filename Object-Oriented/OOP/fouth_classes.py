"""Legacy Fourth Classes Script (Refactored).

This module updates the original `fouth_classes.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed point geometry, see `point_geometry.py`.
"""

from point_geometry import Point


if __name__ == "__main__":
    print("=== Legacy Fourth Classes (Refactored) ===")
    p1 = Point(4, 5)
    p3 = Point(1, 4)
    print("p1 + p3:", p1 + p3)
