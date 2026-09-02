"""
String Reversal Basics Module.

This module demonstrates core techniques for reversing strings and text sequences in Python:
- Character-level string reversal via extended slicing [::-1]
- Reversing text character-by-character using reversed() and join()
- Reversing word order within sentences (word token reversal)
- Immutability notes: Why Python strings require creating new string objects
"""
# "from typing import List, Dict" imports typing annotations.
from typing import List, Dict


def reverse_string_by_slicing(text: str) -> str:
    """
    Reverse a string using extended slice syntax [::-1].

    Extended slicing creates a new string with step -1 in O(N) time and O(N) space.
    This is the most idiomatic and fastest string reversal technique in CPython.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.
    """
    return text[::-1]


def reverse_string_with_builtin_reversed(text: str) -> str:
    """
    Reverse a string using built-in reversed() and str.join().

    reversed(text) returns a reverse iterator, consuming items lazily without creating
    an intermediate list before joining.

    Args:
        text (str): Input string.

    Returns:
        str: Reversed string.
    """
    return "".join(reversed(text))


def reverse_word_order_in_sentence(sentence: str) -> str:
    """
    Reverse the order of words in a sentence while keeping individual word spellings intact.

    Args:
        sentence (str): Input sentence string (e.g. 'Python is awesome').

    Returns:
        str: Reordered sentence string (e.g. 'awesome is Python').
    """
    words: List[str] = sentence.split()
    words.reverse()  # In-place reversal of word list
    return " ".join(words)


def compare_string_reversal_methods(text: str) -> Dict[str, str]:
    """
    Demonstrate and compare different string reversal results.

    Args:
        text (str): Input text string.

    Returns:
        Dict[str, str]: Dictionary comparing character slice, reversed iterator, and word order reversal.
    """
    return {
        "original": text,
        "slice_reversed": reverse_string_by_slicing(text),
        "iterator_reversed": reverse_string_with_builtin_reversed(text),
        "words_reversed": reverse_word_order_in_sentence(text),
    }


if __name__ == "__main__":
    print("=== Step 1: String Reversal Basics ===")
    sample_text = "On a Mac keyboard hitting Option two types EUR sign"

    print(f"Original Text        : {sample_text}")
    print(f"Slice Reversed       : {reverse_string_by_slicing(sample_text)}")
    print(f"Iterator Reversed    : {reverse_string_with_builtin_reversed(sample_text)}")
    print(f"Word Order Reversed  : {reverse_word_order_in_sentence(sample_text)}")
