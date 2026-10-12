"""Social Media Username Extractor Demonstration Module.

This module demonstrates techniques for extracting usernames from social media URLs.
It compares modern string methods (str.removeprefix introduced in Python 3.9) with
regular expression search (re.search, non-capturing groups, case-insensitivity) and
regex substitution (re.sub).
"""

# import standard re module for pattern-based extraction
import re
from typing import Optional, Match


def extract_username_removeprefix(url: str) -> str:
    """Extract username using Python 3.9+ str.removeprefix.

    Args:
        url: Social media profile URL.

    Returns:
        Extracted username or the original string if no prefix matched.
    """
    clean_url = url.strip()
    prefixes = [
        "https://www.twitter.com/",
        "http://www.twitter.com/",
        "https://twitter.com/",
        "http://twitter.com/",
    ]
    for prefix in prefixes:
        if clean_url.startswith(prefix):
            return clean_url.removeprefix(prefix)
    return clean_url


def extract_username_regex_sub(url: str) -> str:
    """Extract username by replacing protocol and domain with re.sub.

    Args:
        url: Social media profile URL.

    Returns:
        Extracted username string.
    """
    clean_url = url.strip()
    # Strip protocol (http/https), optional www., and domain name
    return re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", clean_url, flags=re.IGNORECASE)


def extract_username_regex_search(url: str) -> Optional[str]:
    """Extract username using re.search with non-capturing group (?:www\\.)?.

    Args:
        url: Social media profile URL.

    Returns:
        Username string if matched, or None if URL structure is invalid.
    """
    clean_url = url.strip()
    # Non-capturing group (?:www\.)? ignores www. for group numbering
    # Group 1 captures valid handle alphanumeric characters and underscores
    pattern = r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)/?$"
    if match := re.search(pattern, clean_url, re.IGNORECASE):
        return match.group(1)
    return None


if __name__ == "__main__":
    print("=== Social Media Username Extractor Demonstration ===")

    test_urls = [
        "http://twitter.com/dilshadabdulla",
        "https://www.twitter.com/dilshadabdulla",
        "https://twitter.com/john_doe123/",
        "http://www.twitter.com/user_name",
        "invalid_url_text",
    ]

    for test_url in test_urls:
        prefix_user = extract_username_removeprefix(test_url)
        sub_user = extract_username_regex_sub(test_url)
        search_user = extract_username_regex_search(test_url)
        print(f"URL: '{test_url}'")
        print(f"  removeprefix: '{prefix_user}' | re.sub: '{sub_user}' | re.search: '{search_user}'")
