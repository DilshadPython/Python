"""Regex Iterators and Pattern Searching Demonstration Module.

This module demonstrates compiling complex regular expressions, scanning text blocks using
re.finditer(), utilizing character class shortcuts (\\d, \\D, \\w, \\W, \\s, \\S), negative
character sets [^...], and reading external target files.
"""

# import standard re module and os/pathlib for safe file operations
import os
import re
from typing import List, Dict, Any, Optional


def find_phone_numbers(text: str) -> List[str]:
    """Find phone numbers formatted as XXX-XXX-XXXX or XXX.XXX.XXX(X).

    Args:
        text: Target text to search.

    Returns:
        List of matched phone number strings.
    """
    pattern = re.compile(r"\b\d{3}[.-]\d{3}[.-]\d{3,4}\b")
    return [match.group(0) for match in pattern.finditer(text)]


def find_names_with_titles(text: str) -> List[str]:
    """Find honorific titles and names (e.g. Mr Smith, Mrs Trump, Ms Claudia, Miss Georgina).

    Args:
        text: Target text to search.

    Returns:
        List of matched title and name strings.
    """
    # Match Mr, Mrs, Ms, or Miss followed by optional dot and capitalized name
    pattern = re.compile(r"\b(?:Mr|Mrs|Ms|Miss)\.?\s+[A-Z][a-z]+\b")
    return [match.group(0) for match in pattern.finditer(text)]


def find_words_negating_prefix(text: str, negated_char: str = "b") -> List[str]:
    """Find 3-letter words ending in 'at' except those starting with a specific letter (e.g. [^b]at).

    Args:
        text: Target text to search.
        negated_char: Character to exclude at the beginning of 'at' words.

    Returns:
        List of matched word strings.
    """
    pattern = re.compile(rf"\b[^{negated_char}]at\b", re.IGNORECASE)
    return [match.group(0) for match in pattern.finditer(text)]


def search_file_contents(file_path: str, pattern_str: str) -> List[Dict[str, Any]]:
    """Scan a target text file using a compiled regex pattern and return match locations.

    Args:
        file_path: Relative or absolute path to target file.
        pattern_str: Regular expression pattern string.

    Returns:
        List of dictionaries containing match string, line context, and span.
    """
    if not os.path.exists(file_path):
        return []

    results = []
    pattern = re.compile(pattern_str)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        for match in pattern.finditer(content):
            results.append({
                "match": match.group(0),
                "span": match.span(),
                "start": match.start(),
                "end": match.end(),
            })
    return results


if __name__ == "__main__":
    print("=== Regex Iterators & Pattern Searching Demonstration ===")

    sample_text = """
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    123 456 7890
    888.764.9890
    532-658-0010

    Mr Smith
    Mrs Trump
    Ms Claudia
    Miss Georgina

    cat bat mat pat sat jat wat
    """

    print("--- 1. Phone Numbers Found ---")
    phones = find_phone_numbers(sample_text)
    print(f"  Phone Numbers: {phones}")

    print("\n--- 2. Names with Titles Found ---")
    names = find_names_with_titles(sample_text)
    print(f"  Names: {names}")

    print("\n--- 3. 'at' Words Excluding 'bat' ---")
    at_words = find_words_negating_prefix(sample_text, negated_char="b")
    print(f"  Words: {at_words}")

    print("\n--- 4. Scanning External File data/REeX.txt ---")
    file_matches = search_file_contents("data/REeX.txt", r"\d{3}[.-]\d{3}[.-]\d{3,4}")
    print(f"  File Matches Count: {len(file_matches)}")
    for m in file_matches:
        print(f"    Match: {m['match']} at span {m['span']}")
