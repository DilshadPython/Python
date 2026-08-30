# =========================================================================
# PYTHON REGULAR EXPRESSIONS (re) BASICS & ADVANCED PATTERNS
# Sourced & Standardized from DilshadPython/Python/RegularEx
# =========================================================================
"""
Production-grade Python Regular Expressions (re) Master Module.

Provides comprehensive implementations for:
- Email validation using character sets, TLD matching, and re.fullmatch()
- Name reformatting ("Last, First" -> "First Last") via split, groups, and re.sub
- Social handle extraction from URLs using str.removeprefix(), re.sub(), & re.search()
- Multi-line URL scanning and extraction via re.findall(), re.finditer(), & re.sub()
- Compiled pattern iterators, phone/title searching, and negative character sets
- Advanced regex: re.VERBOSE, named groups, lookaround assertions, & dir(re) introspection
"""

import sys
import re
from typing import Dict, List, Any, Optional, Tuple, Union


def validate_email_address(email: str) -> Dict[str, Any]:
    """
    Validates an email address using regex character sets, TLD matching, and flags.

    Args:
        email: The target email string to evaluate.

    Returns:
        Dict containing validation status, matched username, domain, and top-level domain.

    Raises:
        TypeError: If input 'email' is not a string object.
    """
    if not isinstance(email, str):
        raise TypeError("Input 'email' must be a valid string object")

    # PEP 8 / Clean Regex: Username + @ + Domain + . + TLD (2+ chars)
    email_pattern = re.compile(
        r"^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})$",
        re.IGNORECASE
    )

    is_valid = bool(email_pattern.fullmatch(email.strip()))
    
    # Detailed extraction via capturing groups
    match = re.search(r"^([^@]+)@([^@.]+)\.(.+)$", email.strip())
    username = match.group(1) if match else None
    domain = match.group(2) if match else None
    tld = match.group(3) if match else None

    return {
        "email": email,
        "is_valid": is_valid,
        "username": username,
        "domain": domain,
        "tld": tld,
        "pattern_used": email_pattern.pattern
    }


def format_person_name(name_str: str) -> Dict[str, Any]:
    """
    Reformats names from 'Last, First' to 'First Last' using re.search, group backreferences, and re.sub.

    Args:
        name_str: The raw input name string (e.g. 'Doe, John' or 'John Doe').

    Returns:
        Dict containing raw name, reformatted name, method used, and captured groups.

    Raises:
        TypeError: If input 'name_str' is not a string object.
    """
    if not isinstance(name_str, str):
        raise TypeError("Input 'name_str' must be a valid string object")

    raw_name = name_str.strip()

    # 1. Reformat 'Last, First' using re.sub with group backreference \2 \1
    reformatted_sub = re.sub(r"^([A-Za-z]+),\s*([A-Za-z]+)$", r"\2 \1", raw_name)

    # 2. Extract capturing groups using re.search and Walrus operator (Python 3.8+)
    if match := re.search(r"^([A-Za-z]+),\s*([A-Za-z]+)$", raw_name):
        last_name = match.group(1)
        first_name = match.group(2)
        formatted_walrus = f"{first_name} {last_name}"
    else:
        last_name = None
        first_name = None
        formatted_walrus = raw_name

    # 3. Fallback comparison using standard str.split()
    if "," in raw_name:
        parts = [p.strip() for p in raw_name.split(",")]
        split_formatted = f"{parts[1]} {parts[0]}" if len(parts) == 2 else raw_name
    else:
        split_formatted = raw_name

    return {
        "raw_name": raw_name,
        "reformatted_sub": reformatted_sub,
        "formatted_walrus": formatted_walrus,
        "first_name": first_name,
        "last_name": last_name,
        "split_fallback_match": reformatted_sub == split_formatted
    }


def extract_social_handle(url_or_text: str) -> Dict[str, Any]:
    """
    Parses profile URLs to extract handles using str.removeprefix(), re.sub(), and non-capturing groups.

    Args:
        url_or_text: Profile URL or handle string (e.g. 'https://twitter.com/alex_dev').

    Returns:
        Dict containing raw input, extracted username handle, platform, and extraction technique.

    Raises:
        TypeError: If input 'url_or_text' is not a string object.
    """
    if not isinstance(url_or_text, str):
        raise TypeError("Input 'url_or_text' must be a valid string object")

    raw_input = url_or_text.strip()

    # Python 3.9+ str.removeprefix / str.removesuffix demonstration
    cleaned_prefix = raw_input
    if sys.version_info >= (3, 9):
        cleaned_prefix = raw_input.removeprefix("https://").removeprefix("http://").removeprefix("www.")

    # Regex extraction with non-capturing groups (?:...) and platform matching
    pattern = re.compile(
        r"(?:https?://)?(?:www\.)?(?:(twitter|github|linkedin)\.com/)?@?([a-zA-Z0-9_]+)/?$",
        re.IGNORECASE
    )

    match = pattern.search(raw_input)
    platform = match.group(1) if (match and match.group(1)) else "unknown"
    handle = match.group(2) if match else raw_input

    # Clean domain substitution using re.sub
    sub_cleaned = re.sub(r"https?://(?:www\.)?(?:twitter|github|linkedin)\.com/", "", raw_input).strip("/")

    return {
        "raw_input": raw_input,
        "extracted_handle": handle,
        "detected_platform": platform,
        "sub_cleaned_handle": sub_cleaned,
        "has_prefix_removed": cleaned_prefix != raw_input
    }


def scan_and_extract_urls(text_content: str) -> Dict[str, Any]:
    """
    Scans multi-line text for web URLs via re.findall(), re.finditer(), and replaces URLs using re.sub().

    Args:
        text_content: Multi-line string containing embedded URLs.

    Returns:
        Dict containing total URLs found, URL list, match positions, and masked text.

    Raises:
        TypeError: If input 'text_content' is not a string object.
    """
    if not isinstance(text_content, str):
        raise TypeError("Input 'text_content' must be a valid string object")

    # Multi-line URL regex pattern
    url_pattern = re.compile(
        r"https?://(?:www\.)?[\w\.-]+\.[a-zA-Z]{2,}(?:/[\w\.-]*)?",
        re.IGNORECASE
    )

    # 1. Extract all matching URLs via re.findall()
    urls_findall = url_pattern.findall(text_content)

    # 2. Iterate matches with start/end character offsets via re.finditer()
    iter_matches = []
    for m in url_pattern.finditer(text_content):
        iter_matches.append({
            "url": m.group(0),
            "start": m.start(),
            "end": m.end(),
            "span": m.span()
        })

    # 3. Replace URLs with domain tags using re.sub()
    masked_text = url_pattern.sub("[LINK REMOVED]", text_content)

    return {
        "total_urls_found": len(urls_findall),
        "urls_list": urls_findall,
        "detailed_matches": iter_matches,
        "masked_text": masked_text
    }


def regex_iterators_and_patterns(sample_text: Optional[str] = None) -> Dict[str, Any]:
    """
    Demonstrates compiled regex patterns, phone/title searching, and negative character sets.

    Args:
        sample_text: Optional custom text to search. Defaults to sample technical dataset.

    Returns:
        Dict containing phone matches, title matches, negative set matches, and dataset stats.
    """
    if sample_text is None:
        sample_text = (
            "Contact Dr. John Doe at 555-123-4567 or Mr. Smith at 800.555.9999.\n"
            "Profiles: Mrs. Trump, Ms. Clara, Prof. Xavier.\n"
            "Keywords: cat, bat, hat, sat, mat, flat, vat."
        )

    # Pre-compiling regex objects for O(1) repeated matching
    phone_pattern = re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b")
    title_pattern = re.compile(r"\b(?:Mr|Mrs|Ms|Dr|Prof)\.\s+[A-Z][a-z]+\b")
    
    # Negative character set: match words ending in 'at' EXCEPT those starting with 'b' or 'm'
    neg_set_pattern = re.compile(r"\b[^bm]at\b", re.IGNORECASE)

    phone_numbers = phone_pattern.findall(sample_text)
    titles_found = title_pattern.findall(sample_text)
    neg_set_matches = neg_set_pattern.findall(sample_text)

    return {
        "phone_numbers": phone_numbers,
        "titles_found": titles_found,
        "negative_set_matches": neg_set_matches,
        "text_length": len(sample_text),
        "line_count": len(sample_text.splitlines())
    }


def advanced_regex_features() -> Dict[str, Any]:
    """
    Demonstrates advanced regex features: re.VERBOSE, named groups, lookarounds, and dir(re).

    Returns:
        Dict containing named group parsing, lookahead/lookbehind results, and re module attributes.
    """
    # 1. Verbose Mode (re.VERBOSE / re.X) with inline comments
    verbose_phone = re.compile(r"""
        \b                  # Word boundary
        (?P<area>\d{3})     # 3-digit Area code (named group 'area')
        [-.\s]?             # Optional separator
        (?P<prefix>\d{3})   # 3-digit Exchange prefix (named group 'prefix')
        [-.\s]?             # Optional separator
        (?P<line>\d{4})     # 4-digit Line number (named group 'line')
        \b                  # Word boundary
    """, re.VERBOSE)

    sample_phone = "Support Line: 415-555-2671"
    match_verbose = verbose_phone.search(sample_phone)
    named_groups = match_verbose.groupdict() if match_verbose else {}

    # 2. Lookahead & Lookbehind Assertions
    # Positive Lookahead (?=...): Verify string contains at least one digit and one uppercase letter
    password_sample = "CloudFlask2026!"
    has_digit = bool(re.search(r"(?=.*\d)", password_sample))
    has_upper = bool(re.search(r"(?=.*[A-Z])", password_sample))

    # Positive Lookbehind (?<=...): Extract currency amounts preceded by '$'
    price_text = "Item A costs $49.99 and Item B costs £19.50 and Item C costs $120.00"
    usd_prices = re.findall(r"(?<=\$)\d+\.\d{2}", price_text)

    # Negative Lookbehind (?<!...): Find numbers NOT preceded by '$'
    non_usd_numbers = re.findall(r"(?<!\$)\b\d+\.\d{2}\b", price_text)

    # 3. re.subn(): Substitution with count tracking
    subn_text, replacement_count = re.subn(r"\bItem\b", "Product", price_text)

    # 4. match.expand(): Template string expansion with backreferences
    expanded_template = match_verbose.expand(r"Area Code: (\g<area>), Line: \g<line>") if match_verbose else ""

    # 5. Pattern Slice Scanning (pos/endpos) & Group Index Inspection
    sliced_search = verbose_phone.search(sample_phone, pos=14, endpos=28)
    group_index_map = verbose_phone.groupindex

    # 6. Cache Maintenance via re.purge()
    re.purge()

    # 7. Object Introspection via dir(re)
    re_dir_attributes = [attr for attr in dir(re) if not attr.startswith("__")]

    return {
        "named_groups_extracted": named_groups,
        "password_has_digit": has_digit,
        "password_has_upper": has_upper,
        "usd_prices_lookbehind": usd_prices,
        "non_usd_numbers": non_usd_numbers,
        "subn_result": {"new_text": subn_text, "count": replacement_count},
        "expanded_template": expanded_template,
        "sliced_search_matched": bool(sliced_search),
        "group_index_map": dict(group_index_map),
        "re_dir_attr_count": len(re_dir_attributes),
        "sample_re_attributes": re_dir_attributes[:8]
    }
