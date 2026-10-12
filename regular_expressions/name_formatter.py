"""Name Formatter Demonstration Module.

This module demonstrates methods for reformatting name strings from "Last, First"
to "First Last". It compares basic string manipulation (str.split) against regular
expression pattern matching (re.search, capturing groups, walrus assignment :=, re.sub).
"""

# import standard re module for regex searching and substitution
import re
from typing import Optional, Match


def format_name_split(name: str) -> str:
    """Format a name string using basic str.split().

    Args:
        name: Name string, potentially formatted as "Last, First".

    Returns:
        Reformatted name string as "First Last".
    """
    clean_name = name.strip()
    if "," in clean_name:
        parts = clean_name.split(",", 1)
        lname = parts[0].strip()
        fname = parts[1].strip()
        return f"{fname} {lname}"
    return clean_name


def format_name_regex_groups(name: str) -> str:
    """Format a name string using re.search capturing groups.

    Args:
        name: Input name string.

    Returns:
        Reformatted name string as "First Last".
    """
    clean_name = name.strip()
    # Match pattern: ^(.+),\s*(.+)$
    # Group 1: Last Name, Group 2: First Name
    match: Optional[Match] = re.search(r"^(.+),\s*(.+)$", clean_name)
    if match:
        lname = match.group(1).strip()
        fname = match.group(2).strip()
        return f"{fname} {lname}"
    return clean_name


def format_name_regex_walrus(name: str) -> str:
    """Format a name string using Python 3.8+ walrus operator (:=) in conditional.

    Args:
        name: Input name string.

    Returns:
        Reformatted name string as "First Last".
    """
    clean_name = name.strip()
    if match := re.search(r"^(.+),\s*(.+)$", clean_name):
        return f"{match.group(2).strip()} {match.group(1).strip()}"
    return clean_name


def format_name_regex_sub(name: str) -> str:
    """Format a name string using re.sub with backreferences (\\2 \\1).

    Args:
        name: Input name string.

    Returns:
        Reformatted name string as "First Last".
    """
    clean_name = name.strip()
    # Replace "Last, First" with "First Last" using backreferences \2 and \1
    return re.sub(r"^(.+),\s*(.+)$", r"\2 \1", clean_name)


if __name__ == "__main__":
    print("=== Name Formatter Demonstration ===")

    test_names = [
        "Trump, Mrs Donald",
        "Smith, Mr John",
        "Claudia, Ms",
        "SingleName",
        "  Curie,  Marie  ",
    ]

    for name in test_names:
        split_res = format_name_split(name)
        group_res = format_name_regex_groups(name)
        walrus_res = format_name_regex_walrus(name)
        sub_res = format_name_regex_sub(name)
        print(f"Original: '{name}'")
        print(f"  Split:  '{split_res}' | Regex Groups: '{group_res}' | Walrus: '{walrus_res}' | Sub: '{sub_res}'")
