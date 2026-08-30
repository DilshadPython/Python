"""Advanced Regular Expressions Demonstration Module.

This module demonstrates advanced features of Python's `re` module, including:
1. Compilation flags: re.IGNORECASE, re.MULTILINE, re.DOTALL, re.VERBOSE.
2. Named capturing groups (?P<name>...) and match.groupdict() extraction.
3. Lookahead and Lookbehind assertions (?=...), (?!...), (?<=...), (?<!...).
4. Object introspection of re.Pattern and re.Match objects using dir().
"""

# import standard re module for pattern matching and introspection
import re
from typing import Dict, Any, List, Optional, Match, Pattern


def parse_log_line_named_groups(log_line: str) -> Optional[Dict[str, str]]:
    """Parse log line using verbose mode (re.VERBOSE) and named capturing groups (?P<name>...).

    Args:
        log_line: Raw log line string.

    Returns:
        Dictionary mapping group names to values if matched, or None.
    """
    # re.VERBOSE allows whitespace and comments inside the regex string for readability
    pattern: Pattern = re.compile(
        r"""
        ^\[(?P<timestamp>[^\]]+)\]  # Match timestamp inside brackets [2026-08-30 14:00:00]
        \s+                          # Whitespace separator
        (?P<level>INFO|WARNING|ERROR|DEBUG) # Match log level
        \s+:\s+                      # Separator ' : '
        (?P<message>.+)$             # Remaining log message
        """,
        re.VERBOSE,
    )
    match: Optional[Match] = pattern.match(log_line.strip())
    if match:
        return match.groupdict()
    return None


def extract_prices_lookahead(text: str) -> List[str]:
    """Demonstrate positive lookahead (?=\\s*USD|\\$) to extract numbers followed by currency markers.

    Args:
        text: Target text containing currency values.

    Returns:
        List of matched numeric price strings.
    """
    # Match digits only if followed by USD or dollar sign
    pattern: Pattern = re.compile(r"\d+(?:\.\d{2})?(?=\s*(?:USD|\$))")
    return pattern.findall(text)


def extract_hashtags_lookbehind(text: str) -> List[str]:
    """Demonstrate positive lookbehind (?<=#) to extract tags following a hash symbol.

    Args:
        text: Target text containing hashtags.

    Returns:
        List of hashtag word strings without the '#' symbol.
    """
    # Match word characters only if preceded by '#'
    pattern: Pattern = re.compile(r"(?<=#)\w+")
    return pattern.findall(text)


def inspect_regex_objects(pattern_str: str, text_sample: str) -> Dict[str, List[str]]:
    """Demonstrate dir() introspection on re.Pattern and re.Match objects.

    Args:
        pattern_str: Regex string to compile.
        text_sample: Text string to execute match against.

    Returns:
        Dictionary containing public attribute lists for 'pattern' and 'match' objects.
    """
    pattern: Pattern = re.compile(pattern_str)
    match: Optional[Match] = pattern.search(text_sample)

    pattern_attrs = [a for a in dir(pattern) if not a.startswith("__")]
    match_attrs = [a for a in dir(match) if not a.startswith("__")] if match else []

    return {
        "pattern_attributes": pattern_attrs,
        "match_attributes": match_attrs,
    }


if __name__ == "__main__":
    print("=== Advanced Regular Expressions Demonstration ===")

    # 1. Named Groups and Verbose Regex
    sample_log = "[2026-08-30 14:00:00] ERROR : Database connection refused"
    log_dict = parse_log_line_named_groups(sample_log)
    print(f"Log parsing: {log_dict}")

    # 2. Lookahead assertion
    price_text = "Item A costs 45 USD, Item B costs 120 EUR, Item C costs 99.99 $"
    prices = extract_prices_lookahead(price_text)
    print(f"Prices matching USD/$ lookahead: {prices}")

    # 3. Lookbehind assertion
    tweet = "Learning #Python and #Regex with #Antigravity!"
    tags = extract_hashtags_lookbehind(tweet)
    print(f"Hashtags matching lookbehind: {tags}")

    # 4. Introspection with dir()
    intro = inspect_regex_objects(r"\w+", "Hello World")
    print("\n--- Pattern Object Attributes (first 5) ---")
    print(intro["pattern_attributes"][:5])
    print("--- Match Object Attributes (first 5) ---")
    print(intro["match_attributes"][:5])
