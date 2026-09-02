"""
Range Iteration inside Entry Points Module.

This module demonstrates:
- Executing range() sequence processing inside main() entry point functions.
- Comparing sequence generation in local vs global module scopes.
"""

# Import sys for system inspection
import sys


def process_range_in_local_scope(count: int = 100_000) -> int:
    """Process range sequence summation inside local function scope.

    Args:
        count (int, optional): Element count. Defaults to 100000.

    Returns:
        int: Total sum of range sequence.
    """
    total = 0
    for i in range(count):
        total += i
    return total


def main() -> None:
    """Main entry point processing range iterations."""
    res = process_range_in_local_scope(10_000)
    print(f"Range Processing Result (count=10,000): {res}")


if __name__ == "__main__":
    main()
