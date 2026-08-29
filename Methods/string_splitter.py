"""
Demonstrates splitting strings using str.split() method.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List, Optional


def split_string(text: str, delimiter: Optional[str] = None) -> List[str]:
    """Split input string by specified delimiter (defaults to whitespace)."""
    return text.split(delimiter)


if __name__ == '__main__':
    sample_line: str = "apple,banana,cherry,date"
    print("Original:", sample_line)
    print("Split by comma:", split_string(sample_line, ','))
