"""Unit Test Suite for the Regular Expressions Tutorial Module.

This module provides comprehensive unittest coverage for all regular expression
functions, email validation, name formatting, username extraction, URL parsing,
iterator searching, lookaround assertions, named capturing groups, and dir() introspection.
"""

# import standard unittest module for test runner and assertions
import unittest

# import functions from target modules
from email_validator import validate_email, extract_email_parts
from name_formatter import (
    format_name_split,
    format_name_regex_groups,
    format_name_regex_walrus,
    format_name_regex_sub,
)
from social_username_extractor import (
    extract_username_removeprefix,
    extract_username_regex_sub,
    extract_username_regex_search,
)
from url_extractor import (
    find_all_url_tuples,
    find_iter_url_matches,
    reformat_urls_to_domains,
)
from regex_iterators import (
    find_phone_numbers,
    find_names_with_titles,
    find_words_negating_prefix,
    search_file_contents,
)
from regex_advanced import (
    parse_log_line_named_groups,
    extract_prices_lookahead,
    extract_hashtags_lookbehind,
    inspect_regex_objects,
)


class TestEmailValidator(unittest.TestCase):
    """Unit tests for email validation and component extraction."""

    def test_validate_email(self) -> None:
        """Verify valid vs invalid email address formats."""
        self.assertTrue(validate_email("user@example.com"))
        self.assertTrue(validate_email("john.doe@teach-cloud.net"))
        self.assertFalse(validate_email("invalid-email@"))
        self.assertFalse(validate_email("user@domain"))

    def test_extract_email_parts(self) -> None:
        """Verify extracting username and domain from email."""
        parts = extract_email_parts("alice@domain.co.uk")
        self.assertIsNotNone(parts)
        self.assertEqual(parts, ("alice", "domain.co.uk"))
        self.assertIsNone(extract_email_parts("invalid_email"))


class TestNameFormatter(unittest.TestCase):
    """Unit tests for name formatting implementations."""

    def test_format_name_methods(self) -> None:
        """Verify name formatting across split, regex groups, walrus, and sub methods."""
        raw_name = "Smith, John"
        expected = "John Smith"

        self.assertEqual(format_name_split(raw_name), expected)
        self.assertEqual(format_name_regex_groups(raw_name), expected)
        self.assertEqual(format_name_regex_walrus(raw_name), expected)
        self.assertEqual(format_name_regex_sub(raw_name), expected)


class TestSocialUsernameExtractor(unittest.TestCase):
    """Unit tests for username extraction from social media URLs."""

    def test_username_extraction(self) -> None:
        """Verify username extraction using removeprefix, re.sub, and re.search."""
        url = "https://www.twitter.com/dilshadabdulla"
        expected = "dilshadabdulla"

        self.assertEqual(extract_username_removeprefix(url), expected)
        self.assertEqual(extract_username_regex_sub(url), expected)
        self.assertEqual(extract_username_regex_search(url), expected)


class TestURLExtractor(unittest.TestCase):
    """Unit tests for URL matching and reformatting."""

    def test_url_extraction_and_reformat(self) -> None:
        """Verify findall, finditer, and reformat functions."""
        text = "Check http://google.com and https://www.gov.uk"
        tuples = find_all_url_tuples(text)
        self.assertEqual(len(tuples), 2)

        matches = find_iter_url_matches(text)
        self.assertEqual(len(matches), 2)

        reformatted = reformat_urls_to_domains(text)
        self.assertIn("google.com", reformatted)
        self.assertIn("gov.uk", reformatted)


class TestRegexIterators(unittest.TestCase):
    """Unit tests for pattern searching, negation sets, and file scanning."""

    def test_pattern_matchers(self) -> None:
        """Verify phone numbers, title names, and negative character set matching."""
        sample = "Contact 888.764.9890 or 532-658-0010. Mr Smith and Mrs Trump met bat cat mat."
        phones = find_phone_numbers(sample)
        self.assertEqual(len(phones), 2)

        names = find_names_with_titles(sample)
        self.assertEqual(len(names), 2)
        self.assertIn("Mr Smith", names)

        words = find_words_negating_prefix(sample, "b")
        self.assertIn("cat", words)
        self.assertIn("mat", words)
        self.assertNotIn("bat", words)

    def test_file_scanning(self) -> None:
        """Verify scanning external file contents."""
        file_matches = search_file_contents("data/REeX.txt", r"\d{3}[.-]\d{3}[.-]\d{3,4}")
        self.assertGreaterEqual(len(file_matches), 1)


class TestRegexAdvanced(unittest.TestCase):
    """Unit tests for named capturing groups, lookaround assertions, and dir() introspection."""

    def test_named_groups_log_parser(self) -> None:
        """Verify log parsing using named capturing groups."""
        log = "[2026-08-30 14:00:00] ERROR : Database offline"
        parsed = parse_log_line_named_groups(log)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed["level"], "ERROR")
        self.assertEqual(parsed["message"], "Database offline")

    def test_lookaround_assertions(self) -> None:
        """Verify lookahead and lookbehind assertion matching."""
        price_text = "Cost 50 USD, 100 EUR, 25.50 $"
        prices = extract_prices_lookahead(price_text)
        self.assertEqual(prices, ["50", "25.50"])

        tweet = "Posts with #Python and #Regex"
        tags = extract_hashtags_lookbehind(tweet)
        self.assertEqual(tags, ["Python", "Regex"])

    def test_dir_introspection(self) -> None:
        """Verify Pattern and Match object dir() attribute lists."""
        intro = inspect_regex_objects(r"\w+", "Sample Text")
        self.assertIn("pattern", intro["pattern_attributes"])
        self.assertIn("group", intro["match_attributes"])


if __name__ == "__main__":
    unittest.main()
