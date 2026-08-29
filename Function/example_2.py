"""
Backwards-compatible wrapper alias for vowel_counter.py (descriptive filename).
"""
from Function.vowel_counter import vowels_count

__all__ = ["vowels_count"]

if __name__ == '__main__':
    print(f"Vowels in Dilshad: {vowels_count('Dilshad')}")
