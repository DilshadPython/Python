"""Legacy Finditer Regex Script (Refactored).

This module updates the original `finditer_re.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular searching and file scanning functions, see `regex_iterators.py`.
"""

from regex_iterators import find_phone_numbers, find_names_with_titles, find_words_negating_prefix


if __name__ == "__main__":
    print("=== Legacy Finditer Regex (Refactored) ===")
    sample_text = "532-658-0010 Mr Smith cat bat mat"
    print("Phones:", find_phone_numbers(sample_text))
    print("Names:", find_names_with_titles(sample_text))
    print("Words non-b:", find_words_negating_prefix(sample_text, "b"))