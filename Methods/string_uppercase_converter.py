"""
Demonstrates string uppercase transformation using str.upper() method.
"""


def convert_to_uppercase(text: str) -> str:
    """Convert input string characters to uppercase."""
    return text.upper()


if __name__ == '__main__':
    sample_input: str = "python methods lesson"
    print("Original:", sample_input)
    print("Uppercase:", convert_to_uppercase(sample_input))
