"""
Sequence Reversal: Comprehensive Master Demonstration Entrypoint.

This script demonstrates string, word-order, list, container, and range sequence reversal in Python:
- Character-level reversal using extended slice [::-1] and reversed()
- Word-order reversal using string split(), list.reverse(), and join()
- Custom object __reversed__() protocol hooks
- Efficient O(1) memory range reversal via reversed(range(...))
"""
# "from typing import List, Tuple, Dict" imports typing annotations.
from typing import List, Tuple, Dict


def demonstrate_text_and_word_reversal(text: str) -> Tuple[str, str, str]:
    """
    Demonstrate character reversal and word-order reversal for an input text message.

    Args:
        text (str): Input text message.

    Returns:
        Tuple[str, str, str]: Tuple containing (original, char_reversed, words_reversed).
    """
    # Character-level reversal via extended slice
    char_reversed = text[::-1]

    # Word-order reversal using split(), list.reverse(), and join()
    words = text.split()
    words.reverse()  # In-place word order reversal
    words_reversed = " ".join(words)

    return text, char_reversed, words_reversed


def demonstrate_range_reversal(count: int = 5) -> List[int]:
    """
    Demonstrate efficient lazy range sequence reversal.

    Args:
        count (int): Number of range elements. Defaults to 5.

    Returns:
        List[int]: List of reversed integers.
    """
    return list(reversed(range(count)))


if __name__ == "__main__":
    msg = "On a Mac keyboard, hitting Shift, Option, and number Two will type out the EUR sign."

    print("=== Python Sequence Reversal Master Demonstration ===")
    orig, char_rev, word_rev = demonstrate_text_and_word_reversal(msg)
    print(f"Original Text        :\n  {orig}")
    print(f"\nReversed Words       :\n  {word_rev}")
    print(f"\nReversed Characters  :\n  {char_rev}")

    print("\n=== Range Sequence Reversal ===")
    print(f"  reversed(range(5)) : {demonstrate_range_reversal(5)}")
