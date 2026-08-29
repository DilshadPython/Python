"""
Demonstrates string length measurement using built-in len() function.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def calculate_string_length(text: str) -> int:
    """Calculate and return character length of input string."""
    return len(text)


if __name__ == '__main__':
    sample_text: str = "Python Programming Language"
    print("Input Text:", sample_text)
    print("Character Count:", calculate_string_length(sample_text))
