"""
Demonstrates removing leading and trailing whitespace using str.strip().
"""


def strip_whitespace(text: str) -> str:
    """Remove leading and trailing whitespace from string."""
    return text.strip()


if __name__ == '__main__':
    sample_text: str = "   Hello Python Developers!   "
    print("Original:", repr(sample_text))
    print("Stripped:", repr(strip_whitespace(sample_text)))
