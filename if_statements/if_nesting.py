"""Nested 'if' Statements versus Flat Compound Conditions.

Demonstrates nested conditional blocks for multi-level decision trees,
along with Pythonic flattening techniques using boolean 'and' operators.

Import Notes:
    - 'from typing import Tuple': Imports type hint construct from typing standard library.
"""

from typing import Tuple


def evaluate_housing_option(housing_type: str, building_category: str) -> str:
    """Evaluate housing suitability using nested conditional statements."""
    if housing_type.lower() == "apartment":
        if building_category.lower() == "house":
            return "You can buy it and enjoy a spacious private garden."
        else:
            return "You can rent it as a modern flat without a garden."
    else:
        return "Unknown housing category."


def evaluate_housing_flat(housing_type: str, building_category: str) -> str:
    """Pythonic alternative: Flattening nested conditionals using 'and'."""
    if housing_type.lower() == "apartment" and building_category.lower() == "house":
        return "You can buy it and enjoy a spacious private garden."
    elif housing_type.lower() == "apartment":
        return "You can rent it as a modern flat without a garden."
    else:
        return "Unknown housing category."


def demo_if_nesting() -> None:
    """Run nested conditional demonstration."""
    result_nested = evaluate_housing_option("apartment", "house")
    result_flat = evaluate_housing_flat("apartment", "house")
    print(f"Nested Result: {result_nested}")
    print(f"Flat Result  : {result_flat}")


if __name__ == "__main__":
    demo_if_nesting()
