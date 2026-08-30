"""URL Extractor and Parser Demonstration Module.

This module demonstrates scanning multi-line texts for web URLs, extracting domain components
with regex capturing groups, comparing re.findall() vs re.finditer(), and performing
url reformatting using re.sub().
"""

# import standard re module for pattern matching and iterators
import re
from typing import List, Tuple, Dict, Any, Match


# Regex pattern to match HTTP/HTTPS URLs and capture:
# Group 1: optional 'www.'
# Group 2: domain name (e.g. 'google', 'cambridge')
# Group 3: top-level domain extension (e.g. '.com', '.edu', '.gov.uk')
URL_PATTERN: re.Pattern = re.compile(
    r"https?://(www\.)?([a-zA-Z0-9-]+)(\.[a-zA-Z0-9\.-]+)",
    re.IGNORECASE,
)


def find_all_url_tuples(text: str) -> List[Tuple[str, str, str]]:
    """Find all matching URLs in text returning tuples of captured groups using re.findall().

    Args:
        text: Multi-line raw text containing URLs.

    Returns:
        List of tuples matching (www_prefix, domain_name, tld_extension).
    """
    return URL_PATTERN.findall(text)


def find_iter_url_matches(text: str) -> List[Dict[str, Any]]:
    """Scan text using re.finditer() to retrieve detailed Match objects and metadata.

    Args:
        text: Multi-line raw text containing URLs.

    Returns:
        List of dictionaries containing matched string, start/end spans, and groups.
    """
    results = []
    for match in URL_PATTERN.finditer(text):
        results.append({
            "full_match": match.group(0),
            "span": match.span(),
            "domain": match.group(2),
            "extension": match.group(3),
        })
    return results


def reformat_urls_to_domains(text: str) -> str:
    """Reformat URLs to display clean 'domain.extension' using re.sub backreferences.

    Args:
        text: Multi-line raw text containing URLs.

    Returns:
        Reformatted text string where full URLs are replaced with domain.extension.
    """
    # Replace full URL with Group 2 + Group 3 (\2\3)
    return URL_PATTERN.sub(r"\2\3", text)


if __name__ == "__main__":
    print("=== URL Extractor & Parser Demonstration ===")

    sample_urls_text = """
    http://twitter.com/username
    https://google.com
    http://youtube.com
    https://www.gov.uk
    http://cambridge.edu
    """

    print("--- 1. re.findall() Captured Groups ---")
    all_tuples = find_all_url_tuples(sample_urls_text)
    for item in all_tuples:
        print(f"  Tuple: {item}")

    print("\n--- 2. re.finditer() Match Inspection ---")
    match_details = find_iter_url_matches(sample_urls_text)
    for detail in match_details:
        print(f"  Found '{detail['full_match']}' at {detail['span']} -> Domain: {detail['domain']}{detail['extension']}")

    print("\n--- 3. re.sub() Reformatted Output ---")
    reformatted = reformat_urls_to_domains(sample_urls_text)
    print(reformatted.strip())
