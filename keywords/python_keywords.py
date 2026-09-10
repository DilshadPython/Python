"""
Python Reserved and Soft Keywords Inspection Module.

This module provides programmatic access to CPython reserved keywords (`keyword.kwlist`)
and soft keywords (`keyword.softkwlist`), supporting identifier validation and language evolution analysis.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import keyword`: Standard library module containing Python reserved keywords.
# - `import sys`: System utilities for CLI argument processing and exit status.
# - `from typing import List, Dict, Union`: PEP 484 type hint generics.
# =========================================================================
import keyword
import sys
from typing import Dict, List, Union


def get_all_python_keywords() -> List[str]:
    """Retrieve all hard reserved Python keywords in current CPython runtime.

    Returns:
        List[str]: List of reserved keyword strings.
    """
    return list(keyword.kwlist)


def get_soft_keywords() -> List[str]:
    """Retrieve soft keywords introduced in modern Python (e.g. match, case, type).

    Returns:
        List[str]: List of soft keyword strings (empty list if CPython < 3.10).
    """
    if hasattr(keyword, "softkwlist"):
        return list(keyword.softkwlist)
    return []


def is_reserved_keyword(word: str) -> bool:
    """Check whether a given string is a reserved Python keyword.

    Args:
        word (str): String identifier to inspect.

    Returns:
        bool: True if word is a hard keyword, False otherwise.
    """
    return keyword.iskeyword(word)


def is_soft_keyword(word: str) -> bool:
    """Check whether a given string is a soft Python keyword (CPython 3.10+).

    Args:
        word (str): String identifier to inspect.

    Returns:
        bool: True if word is a soft keyword, False otherwise.
    """
    if hasattr(keyword, "issoftkeyword"):
        return keyword.issoftkeyword(word)
    return False


def get_keyword_summary() -> Dict[str, Union[int, List[str]]]:
    """Generate summary dictionary of runtime keywords.

    Returns:
        Dict[str, Union[int, List[str]]]: Summary metadata.
    """
    keywords = get_all_python_keywords()
    soft_keywords = get_soft_keywords()

    return {
        "hard_keyword_count": len(keywords),
        "hard_keywords": keywords,
        "soft_keyword_count": len(soft_keywords),
        "soft_keywords": soft_keywords,
    }


def main(argv: list[str] | None = None) -> int:
    """CLI entry point demonstrating keyword inspection."""
    print("=== Python Reserved Keywords Inspection Module ===")

    summary = get_keyword_summary()
    print(f"Hard Reserved Keywords ({summary['hard_keyword_count']}):")
    print(summary["hard_keywords"])

    if summary["soft_keyword_count"] > 0:
        print(f"\nSoft Keywords ({summary['soft_keyword_count']}):")
        print(summary["soft_keywords"])

    return 0


if __name__ == "__main__":
    sys.exit(main())
