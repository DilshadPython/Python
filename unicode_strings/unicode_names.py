"""
Unicode Character Metadata & Inspection Module.

This module provides utility functions for retrieving official Unicode names,
categories, codepoints, and performing reverse lookups using CPython's standard
`unicodedata` library.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import sys`: System utilities for CLI argument processing and exit codes.
# - `import unicodedata`: Built-in database exposing Unicode character attributes
#   such as name, category, numeric value, and normalization form.
# - `from typing import Dict, List, Optional`: PEP 484 type annotations.
# =========================================================================
import sys
import unicodedata
from typing import Dict, List, Optional


def get_character_metadata(symbol: str) -> Dict[str, str]:
    """Retrieve Unicode character name, category, and hex codepoint.

    Args:
        symbol (str): A single Unicode character string.

    Returns:
        Dict[str, str]: Dictionary containing symbol, name, category, and codepoint.

    Raises:
        TypeError: If symbol is not a string.
        ValueError: If symbol length is not exactly 1 character.
    """
    if not isinstance(symbol, str):
        raise TypeError(f"Expected a string symbol, got {type(symbol).__name__}")
    if len(symbol) != 1:
        raise ValueError(f"Expected a single character string, got length {len(symbol)}")

    name = unicodedata.name(symbol, "UNKNOWN UNICODE NAME")
    category = unicodedata.category(symbol)
    codepoint = f"U+{ord(symbol):04X}"

    return {
        "symbol": symbol,
        "name": name,
        "category": category,
        "codepoint": codepoint,
    }


def lookup_character_by_name(name: str) -> str:
    """Perform reverse lookup to get character from official Unicode name.

    Args:
        name (str): Official Unicode character name (case-insensitive).

    Returns:
        str: Single character string.

    Raises:
        TypeError: If name is not a string.
        KeyError: If name is not found in Unicode database.
    """
    if not isinstance(name, str):
        raise TypeError(f"Expected string name, got {type(name).__name__}")

    try:
        return unicodedata.lookup(name)
    except KeyError:
        raise KeyError(f"Unicode character name '{name}' not found in database")


def inspect_symbol_suite(symbols: Optional[List[str]] = None) -> List[Dict[str, str]]:
    """Inspect a list of symbols and return their Unicode metadata dictionaries.

    Args:
        symbols (Optional[List[str]]): List of characters. Defaults to standard symbols.

    Returns:
        List[Dict[str, str]]: List of metadata dictionaries.
    """
    if symbols is None:
        symbols = ["&", "£", "$", "@", "~", "^", "|", "%", "€"]

    metadata_list: List[Dict[str, str]] = []
    for char in symbols:
        metadata_list.append(get_character_metadata(char))

    return metadata_list


def main(argv: list[str] | None = None) -> int:
    """CLI entry point for Unicode character inspector.

    Args:
        argv (list[str] | None): CLI arguments. Defaults to sys.argv[1:].

    Returns:
        int: Status exit code (0 for success).
    """
    print("=== Unicode Character Name & Metadata Inspector ===")
    results = inspect_symbol_suite()

    for item in results:
        print(f"Character '{item['symbol']}' ({item['codepoint']}) -> Name: {item['name']} [Category: {item['category']}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
