"""
Senior Level Python Unpacking Demonstration Module.

This module provides enterprise unpacking patterns designed for senior software engineers
(structural pattern matching unpacking `match/case`, TypedDict `Unpack` PEP 692 parameter hints, and CPython AST unpacking inspection).
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import ast`: CPython Abstract Syntax Tree parser module.
# - `import sys`: System utilities for CLI execution exit status.
# - `from typing import Any, Dict, List, TypedDict`: PEP 484 & 589 type hinting.
# =========================================================================
import ast
import sys
from typing import Any, Dict, List, TypedDict

try:
    from typing import Unpack  # Python 3.12+
except ImportError:
    try:
        from typing_extensions import Unpack  # Python 3.11 fallback
    except ImportError:
        Unpack = Any  # Type hint fallback for older CPython environments


class DimensionKwargs(TypedDict):
    """TypedDict defining strict type layout for dimension keyword arguments (PEP 692)."""

    length: float
    width: float
    height: float


def demonstrate_pattern_matching_unpacking(data: Any) -> str:
    """Demonstrate structural pattern matching sequence unpacking (PEP 634, Python 3.10+).

    Args:
        data (Any): Input data structure to unpack.

    Returns:
        str: Description of unpacked pattern matching structure.
    """
    match data:
        case [first, *middle, last]:
            return f"Matched List Pattern: First={first}, Middle={middle}, Last={last}"
        case {"length": l, "width": w, "height": h}:
            return f"Matched Mapping Pattern: Length={l}, Width={w}, Height={h}"
        case (x, y):
            return f"Matched 2-Tuple Point: x={x}, y={y}"
        case _:
            return "Unmatched Pattern"


def calculate_volume_typed_unpack(**kwargs: Any) -> float:
    """Calculate volume using PEP 692 dictionary unpacking structure.

    Args:
        **kwargs: Dimension keyword arguments ('length', 'width', 'height').

    Returns:
        float: Calculated volume in cubic inches.
    """
    length = float(kwargs["length"])
    width = float(kwargs["width"])
    height = float(kwargs["height"])
    return round((length * width * height) * 0.0610237, 4)


def inspect_unpacking_ast(code_snippet: str) -> List[str]:
    """Parse Python source code snippet and extract unpacking targets from AST nodes.

    Args:
        code_snippet (str): Python source statement (e.g., "a, *b, c = seq").

    Returns:
        List[str]: Extracted AST target identifier names.
    """
    tree = ast.parse(code_snippet)
    target_names: List[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, (ast.Tuple, ast.List)):
                    for elt in target.elts:
                        if isinstance(elt, ast.Name):
                            target_names.append(elt.id)
                        elif isinstance(elt, ast.Starred) and isinstance(elt.value, ast.Name):
                            target_names.append(f"*{elt.value.id}")

    return target_names


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for senior unpacking demonstration."""
    print("=== Senior Level Python Unpacking Demonstration ===")

    pm_res1 = demonstrate_pattern_matching_unpacking([10, 20, 30, 40])
    print(f"Pattern Matching Unpacking: {pm_res1}")

    pm_res2 = demonstrate_pattern_matching_unpacking({"length": 15, "width": 10, "height": 8})
    print(f"Pattern Matching Dict Unpacking: {pm_res2}")

    vol = calculate_volume_typed_unpack(length=15.0, width=10.0, height=8.0)
    print(f"TypedDict Unpack (PEP 692): {vol} Cubic Inches")

    ast_targets = inspect_unpacking_ast("first, *middle, last = items")
    print(f"AST Parsed Unpacking Targets: {ast_targets}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
