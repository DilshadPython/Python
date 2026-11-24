"""
Demonstrates recursive calculation of total string length across sequences.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Sequence

def count_letter(word: Sequence[str]) -> int:
    """Recursively calculate total character count of string/sequence elements."""
    if len(word) < 1:
        return 0
    else:
        return len(word[0]) + count_letter(word[1:])

if __name__ == '__main__':
    city = "London"
    print(f"Character length of '{city}' using recursion:", count_letter(city))
