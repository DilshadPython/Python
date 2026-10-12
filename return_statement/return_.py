"""Legacy Return Demonstration Script (Refactored).

This module updates the original `return_.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For advanced patterns and detailed educational guides, refer to `return_basics.py`,
`return_advanced.py`, and `return_patterns.py`.
"""

# import typing for float type hint annotations
from typing import Optional

# Re-export modern implementations from return_basics
from return_basics import calculate_triangle_volume as triangle_no_return
from return_basics import calculate_cube_volume as cube_volume


def triangle(x: float, y: float, z: float) -> Optional[float]:
    """Demonstrate a function without a return statement (returns None).

    Args:
        x: Dimension X.
        y: Dimension Y.
        z: Dimension Z.

    Returns:
        Implicitly returns None because no return statement is specified.
    """
    # Calculation performed without returning the value
    _val = x * y * z
    # Implicit return None occurs automatically


def cube(x: float, y: float, z: float) -> float:
    """Calculate and return the product of three dimensions.

    Args:
        x: Dimension X.
        y: Dimension Y.
        z: Dimension Z.

    Returns:
        The product as a float.
    """
    return x * y * z


if __name__ == "__main__":
    print("=== Legacy Return Demonstration (Refactored) ===")

    # Function without return statement prints None
    res_triangle = triangle(7.0, 8.0, 4.0)
    print(f"Triangle calculation without return: {res_triangle}")

    print("\n")

    # Function with return statement prints the calculated value
    res_cube = cube(7.0, 8.0, 4.0)
    print(f"Cube calculation with return: {res_cube}")
