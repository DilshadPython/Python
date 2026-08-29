"""
Demonstrates string lowercase transformation using str.lower() method.
"""


def convert_to_lowercase(text: str) -> str:
    """Convert input string characters to lowercase."""
    return text.lower()


if __name__ == '__main__':
    sample_input: str = "PYTHON PROGRAMMING LESSONS"
    print("Original:", sample_input)
    print("Lowercase:", convert_to_lowercase(sample_input))
