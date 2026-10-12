"""
Demonstrates counting vowels in a target text string.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Union


def vowels_count(var: str = "John") -> int:
    """Count and return the number of vowels in the provided text string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in var if char in vowels)


if __name__ == '__main__':
    user_input = input('Enter a name: ')
    if not user_input:
        user_input = "John"
    print(f"We found {vowels_count(user_input)} vowels in the name.")
