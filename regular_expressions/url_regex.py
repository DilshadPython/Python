"""Legacy URL Regex Script (Refactored).

This module updates the original `url_regex.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For modular URL extraction and reformatting functions, see `url_extractor.py`.
"""

from url_extractor import reformat_urls_to_domains, find_all_url_tuples


if __name__ == "__main__":
    print("=== Legacy URL Regex (Refactored) ===")
    sample_text = "http://twitter.com/username\nhttps://google.com"
    print("Captured Tuples:")
    print(find_all_url_tuples(sample_text))
    print("\nReformatted Domains:")
    print(reformat_urls_to_domains(sample_text))
