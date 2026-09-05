"""
File Handling & I/O: File Searching & Filtering

This module demonstrates searching and filtering content in text files:
- Line-by-line pattern matching.
- Regular expression extraction (e.g. email pattern matching via `re.findall`).
- Counting keyword occurrences across text data.
"""
import re
from typing import List, Tuple


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
    email_regex = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    found_emails = set()

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

    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_text_path = os.path.join(base_dir, "search_sample.txt")

    # Create sample text with text and email entries
    sample_content = (
        "Welcome to Python File Processing.\n"
        "Contact support at support@example.com for help.\n"
        "Developer contact: alice.smith@domain.org or bob@company.io\n"
        "Python file processing supports text and binary modes.\n"
    )
    with open(sample_text_path, "w", encoding="utf-8") as f:
        f.write(sample_content)

    # 1. Search keyword
    term = "Python"
    kw_matches = search_keyword_in_file(sample_text_path, term)
    print(f"\n1. Keyword search for '{term}': {len(kw_matches)} matches found:")
    for line_no, text in kw_matches:
        print(f"   Line {line_no}: {text}")

    # 2. Extract emails via regex
    emails = extract_emails_from_file(sample_text_path)
    print(f"\n2. Extracted email addresses ({len(emails)} found):")
    for email in emails:
        print(f"   - {email}")

    # 3. Count total words
    w_count = count_words_in_file(sample_text_path)
    print(f"\n3. Total words in file: {w_count}")


if __name__ == "__main__":
    main()
