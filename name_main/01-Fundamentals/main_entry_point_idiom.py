"""
Python Main Entry Point Idiom (if __name__ == '__main__') Module.

This module demonstrates:
- Structuring Python scripts using the standard `def main() -> int` entry point pattern.
- Preventing unintended side-effects when importing functions into other modules.
- Return codes (0 for success, non-zero for errors) for shell invocation.
"""

# Import sys for system exit codes and CLI argument handling
import sys


def calculate_square_sequence(limit: int) -> list[int]:
    """Generate a list of square numbers up to the specified limit.

    Args:
        limit (int): Total count of squares to generate.

    Returns:
        list[int]: List of squared integers.
    """
    return [x**2 for x in range(limit)]


def main() -> int:
    """Primary application entry point invoked when script is run directly.

    Returns:
        int: Status code (0 indicates successful execution).
    """
    print("--- Executing Main Entry Point ---")
    squares = calculate_square_sequence(5)
    print(f"Generated Squares (0..4): {squares}")
    print(f"Executing module name: '{__name__}'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
