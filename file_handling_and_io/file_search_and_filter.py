"""
File Handling & I/O: File Searching & Filtering

This module demonstrates searching and filtering content in text files:
- Line-by-line pattern matching.
- Regular expression extraction (e.g. email pattern matching via `re.findall`).
- Processing real email datasets (`emailList.txt` and `email_from.txt`).
- Counting keyword occurrences across text data.
"""
import os
import re
from typing import List, Tuple, Set


def search_keyword_in_file(filepath: str, keyword: str) -> List[Tuple[int, str]]:
    """
    Searches for lines containing a specific keyword and returns line numbers and content.

    Args:
        filepath (str): Path to file.
        keyword (str): Search term.

    Returns:
        List[Tuple[int, str]]: List of (1-based line_number, matching_line_text) tuples.
    """
    matches: List[Tuple[int, str]] = []
    if not os.path.exists(filepath):
        return matches

    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                matches.append((line_num, line.strip()))
    return matches


def extract_emails_from_file(filepath: str) -> List[str]:
    """
    Extracts all email addresses from a text file using regular expressions.

    Args:
        filepath (str): Target text file path.

    Returns:
        List[str]: List of unique email addresses found.
    """
    if not os.path.exists(filepath):
        return []

    email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    found_emails: Set[str] = set()

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            matches = email_regex.findall(line)
            found_emails.update(matches)

    return sorted(list(found_emails))


def count_words_in_file(filepath: str) -> int:
    """
    Counts total word occurrences in a text file.

    Args:
        filepath (str): Target text file path.

    Returns:
        int: Word count.
    """
    if not os.path.exists(filepath):
        return 0

    total_words = 0
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words = line.strip().split()
            total_words += len(words)
    return total_words


def main() -> None:
    """Demonstrates file searching and regex extraction."""
    print("=" * 60)
    print("4. File Searching & Pattern Filtering (`re.findall`, line search)")
    print("=" * 60)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    email_file_1 = os.path.join(base_dir, "emailList.txt")
    email_file_2 = os.path.join(base_dir, "email_from.txt")
    cities_file = os.path.join(base_dir, "cities.txt")

    # 1. Search keyword in cities.txt
    term = "London"
    kw_matches = search_keyword_in_file(cities_file, term)
    print(f"\n1. Searching for '{term}' in {cities_file}: {len(kw_matches)} matches found:")
    for line_no, text in kw_matches:
        print(f"   Line {line_no}: {text}")

    # 2. Extract emails from emailList.txt
    emails1 = extract_emails_from_file(email_file_1)
    print(f"\n2. Extracted email addresses from `emailList.txt` ({len(emails1)} found):")
    for email in emails1:
        print(f"   - {email}")

    # 3. Extract emails from email_from.txt
    emails2 = extract_emails_from_file(email_file_2)
    print(f"\n3. Extracted email addresses from `email_from.txt` ({len(emails2)} found):")
    for email in emails2:
        print(f"   - {email}")


if __name__ == "__main__":
    main()
