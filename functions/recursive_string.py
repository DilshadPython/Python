"""
Demonstrates extracting and transforming string sequences using map().
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import List

def pick_first_letter(word: str) -> str:
    """Return the first character of a string."""
    return word[0] if word else ''

def extract_acronym(words: List[str]) -> str:
    """Extract acronym string from list of words."""
    return ''.join(map(pick_first_letter, words))

def extract_acronym_uppercase(words: List[str]) -> str:
    """Extract uppercase acronym string from list of words."""
    return extract_acronym(words).upper()

if __name__ == '__main__':
    words = ['Every', 'one', 'in', 'London', 'not', 'speak', 'english']
    print("First letters:", list(map(pick_first_letter, words)))
    print("Acronym:", extract_acronym(words))
    print("Uppercase Acronym:", extract_acronym_uppercase(words))
