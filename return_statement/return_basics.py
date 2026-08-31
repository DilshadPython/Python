"""Return Basics Demonstration Module.

This module provides clear, PEP 8-compliant implementations demonstrating the core
mechanics of the `return` statement in Python. It covers implicit `None` returns,
explicit return values, calculations, multiple return values via tuple packing,
and early return conditional structures.
"""

# import typing for explicit type annotations
from typing import Tuple, Optional


def calculate_triangle_volume(base_area: float, height: float) -> Optional[float]:
    """Demonstrate a function without a return statement.

    In Python, if a function executes without encountering an explicit `return`
    statement, it implicitly returns `None`.

    Args:
        base_area: Base area of the triangle pyramid.
        height: Height of the triangle pyramid.

    Returns:
        Implicitly returns None because no return statement is specified.
    """
    # Calculation is performed but the result is not returned
    _volume = (1 / 3) * base_area * height
    # Implicit return None occurs at the end of function execution


def calculate_cube_volume(length: float, width: float, height: float) -> float:
    """Calculate and return the volume of a rectangular prism (cube/box).

    Demonstrates using an explicit `return` statement to send a calculated
    value back to the caller.

    Args:
        length: Length of the prism.
        width: Width of the prism.
        height: Height of the prism.

    Returns:
        The calculated volume as a float.
    """
    return length * width * height


def explicit_none_return(condition: bool) -> Optional[str]:
    """Demonstrate explicit `return` and `return None` statements.

    Args:
        condition: Boolean flag determining execution path.

    Returns:
        A string message if condition is True, or explicit None if False.
    """
    if condition:
        return "Condition satisfied"
    # Explicit return None for clarity when returning optional values
    return None


def get_coordinate_3d(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """Demonstrate returning multiple values from a function.

    In Python, comma-separated values in a `return` statement are automatically
    packed into a tuple object.

    Args:
        x: X-coordinate.
        y: Y-coordinate.
        z: Z-coordinate.

    Returns:
        A tuple containing (x, y, z).
    """
    return x, y, z


def check_even_odd(number: int) -> str:
    """Demonstrate early return pattern based on conditional branches.

    Args:
        number: Integer value to check.

    Returns:
        'Even' if number is divisible by 2, otherwise 'Odd'.
    """
    if number % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    print("=== Python Return Basics Demonstration ===")
    
    # 1. Implicit None return demonstration
    tri_result = calculate_triangle_volume(7.0, 8.0)
    print(f"Function without return statement output: {tri_result} (Type: {type(tri_result).__name__})")

    # 2. Explicit value return demonstration
    cube_result = calculate_cube_volume(7.0, 8.0, 4.0)
    print(f"Cube volume (7 * 8 * 4): {cube_result}")

    # 3. Explicit None return demonstration
    print(f"Explicit return with True: '{explicit_none_return(True)}'")
    print(f"Explicit return with False: {explicit_none_return(False)}")

    # 4. Multiple values return (Tuple packing & unpacking)
    coords = get_coordinate_3d(7.0, 8.0, 4.0)
    print(f"Returned tuple: {coords} (Type: {type(coords).__name__})")
    pos_x, pos_y, pos_z = coords
    print(f"Unpacked coordinates: x={pos_x}, y={pos_y}, z={pos_z}")

    # 5. Conditional early return
    print(f"Is 42 even or odd? {check_even_odd(42)}")
    print(f"Is 7 even or odd? {check_even_odd(7)}")
