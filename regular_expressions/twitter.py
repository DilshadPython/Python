"""Legacy Twitter Prefix Strip Script (Refactored).

This module updates the original `twitter.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular username extraction functions, see `social_username_extractor.py`.
"""

from social_username_extractor import extract_username_removeprefix


def strip_twitter_prefix(url: str) -> str:
    """Extract Twitter handle using str.removeprefix (Python 3.9+).

    Args:
        url: Social media profile URL.

    Returns:
        Extracted handle.
    """
    return extract_username_removeprefix(url)


if __name__ == "__main__":
    print("=== Legacy Twitter Prefix Strip (Refactored) ===")
    sample_url = "http://twitter.com/dilshadabdulla"
    handle = strip_twitter_prefix(sample_url)
    print(f"URL: '{sample_url}' -> Handle: '{handle}'")
