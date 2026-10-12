import unittest
from cloud_app.tutorials.regex_basics import (
    validate_email_address,
    format_person_name,
    extract_social_handle,
    scan_and_extract_urls,
    regex_iterators_and_patterns,
    advanced_regex_features
)


class TestRegexTutorial(unittest.TestCase):
    """Unit test suite verifying Regular Expressions tutorial functions."""

    def test_validate_email_address(self):
        # Valid email test
        res_valid = validate_email_address("alex.dev@cloudflask.co.uk")
        self.assertTrue(res_valid["is_valid"])
        self.assertEqual(res_valid["username"], "alex.dev")
        self.assertEqual(res_valid["domain"], "cloudflask")
        self.assertEqual(res_valid["tld"], "co.uk")

        # Invalid email test
        res_invalid = validate_email_address("invalid-email-address")
        self.assertFalse(res_invalid["is_valid"])
        self.assertIsNone(res_invalid["username"])

        # Type checking
        with self.assertRaises(TypeError):
            validate_email_address(12345)  # type: ignore

    def test_format_person_name(self):
        res = format_person_name("Doe, John")
        self.assertEqual(res["reformatted_sub"], "John Doe")
        self.assertEqual(res["formatted_walrus"], "John Doe")
        self.assertEqual(res["first_name"], "John")
        self.assertEqual(res["last_name"], "Doe")
        self.assertTrue(res["split_fallback_match"])

        # Already formatted name
        res_plain = format_person_name("John Doe")
        self.assertEqual(res_plain["reformatted_sub"], "John Doe")

        with self.assertRaises(TypeError):
            format_person_name(None)  # type: ignore

    def test_extract_social_handle(self):
        res_tw = extract_social_handle("https://twitter.com/alex_python")
        self.assertEqual(res_tw["extracted_handle"], "alex_python")
        self.assertEqual(res_tw["detected_platform"], "twitter")

        res_gh = extract_social_handle("https://github.com/monika")
        self.assertEqual(res_gh["extracted_handle"], "monika")
        self.assertEqual(res_gh["detected_platform"], "github")

        with self.assertRaises(TypeError):
            extract_social_handle([])  # type: ignore

    def test_scan_and_extract_urls(self):
        sample_text = (
            "Check https://cloudflask.com/docs and http://github.com/DilshadPython for details."
        )
        res = scan_and_extract_urls(sample_text)
        self.assertEqual(res["total_urls_found"], 2)
        self.assertEqual(len(res["detailed_matches"]), 2)
        self.assertIn("[LINK REMOVED]", res["masked_text"])

        with self.assertRaises(TypeError):
            scan_and_extract_urls(100)  # type: ignore

    def test_regex_iterators_and_patterns(self):
        res = regex_iterators_and_patterns()
        self.assertGreater(len(res["phone_numbers"]), 0)
        self.assertGreater(len(res["titles_found"]), 0)
        self.assertIn("cat", res["negative_set_matches"])
        self.assertNotIn("bat", res["negative_set_matches"])

    def test_advanced_regex_features(self):
        res = advanced_regex_features()
        self.assertEqual(res["named_groups_extracted"]["area"], "415")
        self.assertEqual(res["named_groups_extracted"]["prefix"], "555")
        self.assertEqual(res["named_groups_extracted"]["line"], "2671")
        self.assertTrue(res["password_has_digit"])
        self.assertTrue(res["password_has_upper"])
        self.assertIn("49.99", res["usd_prices_lookbehind"])
        self.assertIn("19.50", res["non_usd_numbers"])
        self.assertEqual(res["subn_result"]["count"], 3)
        self.assertEqual(res["expanded_template"], "Area Code: (415), Line: 2671")
        self.assertTrue(res["sliced_search_matched"])
        self.assertEqual(res["group_index_map"]["area"], 1)
        self.assertGreater(res["re_dir_attr_count"], 10)


if __name__ == "__main__":
    unittest.main()
