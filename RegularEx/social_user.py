"""Legacy Social User Script (Refactored).

This module updates the original `social_user.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular username extraction functions, see `social_username_extractor.py`.
"""

from social_username_extractor import extract_username_regex_search


def get_twitter_handle(url: str) -> str:
    """Extract Twitter handle from URL.

    Args:
        url: Social media profile URL.

    Returns:
        Extracted handle or 'Invalid URL'.
    """
    handle = extract_username_regex_search(url)
    return handle if handle else "Invalid URL"


if __name__ == "__main__":
    print("=== Legacy Social User (Refactored) ===")
    sample_url = "https://www.twitter.com/dilshadabdulla"
    handle = get_twitter_handle(sample_url)
    print(f"URL: '{sample_url}' -> Handle: '{handle}'")
