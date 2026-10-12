"""
URL Slicing and String Manipulation Module
-------------------------------------------
This module demonstrates string slicing techniques on URL strings,
comparing basic string slicing [start:stop:step] with standard library
URL parsing via `urllib.parse.urlparse`.
"""

# =========================================================================
# IMPORT EXPLANATION:
# - `from urllib.parse import urlparse`: Standard library utility to parse
#   URLs into structured components (scheme, netloc, path, params, query, fragment).
# =========================================================================
from urllib.parse import urlparse


def demonstrate_url_slicing(url: str = "http://www.python.org/") -> dict[str, str]:
    """Demonstrate various string slicing operations on a URL string.

    Args:
        url (str): Target URL string. Defaults to "http://www.python.org/".

    Returns:
        dict[str, str]: Dictionary mapping operation names to sliced strings.
    """
    # 1. Reverse the entire string: [start:stop:step] with step = -1
    reversed_url = url[::-1]

    # 2. Extract top-level domain extension (last 5 characters)
    tld_extension = url[-5:]

    # 3. Slice string from index -15 backwards with a step of -2
    sliced_step_backwards = url[-15::-2]

    # 4. Standard library parsing using urllib.parse.urlparse
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc.removeprefix("www.")

    return {
        "original_url": url,
        "reversed_url": reversed_url,
        "tld_extension": tld_extension,
        "sliced_step_backwards": sliced_step_backwards,
        "domain_name": domain_name,
    }


def main() -> int:
    """Entry point when script is run directly."""
    target_url = "http://www.python.org/"
    print(f"--- URL Slicing & Parsing Demonstration ---")
    results = demonstrate_url_slicing(target_url)
    
    print(f"Original URL:          {results['original_url']}")
    print(f"Reversed URL:          {results['reversed_url']}")
    print(f"TLD Extension:         {results['tld_extension']}")
    print(f"Step -2 Backwards:     {results['sliced_step_backwards']}")
    print(f"Parsed Domain Name:    {results['domain_name']}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
