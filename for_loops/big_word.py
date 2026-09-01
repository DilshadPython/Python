"""File Reading and Word Frequency Analysis via Dictionary Accumulation.

Reads words from a file, calculates frequency counts using dictionary accumulator methods,
and identifies the most frequent word in the text.

Import Notes:
    - 'import os': Standard library OS module used for verifying file path existence.
    - 'from typing import Dict, Tuple, Optional': Standard library typing imports for structured hints.
"""

import os
from typing import Dict, Tuple, Optional


def calculate_word_frequencies(file_path: str) -> Dict[str, int]:
    """Read a text file and return a dictionary mapping words to their frequencies."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Target file not found at: {file_path}")

    word_counts: Dict[str, int] = {}
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file_handle:
        for line in file_handle:
            words = line.split()
            for word in words:
                # Clean punctuation from word boundaries for accurate counting
                cleaned_word = word.strip(".,;:!?\"'()[]{}#").lower()
                if cleaned_word:
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    return word_counts


def find_most_frequent_word(word_counts: Dict[str, int]) -> Tuple[Optional[str], int]:
    """Find the word with the highest frequency count in the dictionary."""
    biggest_word: Optional[str] = None
    biggest_count: int = 0

    for word, count in word_counts.items():
        if biggest_word is None or count > biggest_count:
            biggest_word = word
            biggest_count = count

    return biggest_word, biggest_count


def demo_big_word() -> None:
    """Run word frequency calculation demonstration on 'words.txt'."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_file = os.path.join(script_dir, "words.txt")

    if os.path.exists(target_file):
        counts = calculate_word_frequencies(target_file)
        top_word, top_count = find_most_frequent_word(counts)
        print(f"File: '{os.path.basename(target_file)}'")
        print(f"Total Unique Words: {len(counts)}")
        print(f"The biggest word is: '{top_word}' with a count of: {top_count}")
    else:
        print(f"File '{target_file}' does not exist.")


if __name__ == "__main__":
    demo_big_word()
