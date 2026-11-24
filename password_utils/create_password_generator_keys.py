#!/usr/bin/env python3
"""
password_utils/test_create_password_generator_keys.py
Automated Unit Tests verifying create_password_generator_keys.py post definitions.

Target repository:
  https://github.com/DilshadPython/Python/tree/main/password_utils
"""

import pytest
from password_utils.create_password_generator_keys import (
    TITLE,
    SLUG,
    EXCERPT,
    CONTENT,
    CATEGORY,
    TAGS,
)
from password_utils.generate_pass import (
    generate_password,
    generate_secret_key,
)

def test_post_title_and_slug():
    assert "16 to 256" in TITLE
    assert SLUG == "python-cryptographic-password-and-secret-key-generator"
    assert CATEGORY == "Python"

def test_post_bounds_consistency():
    assert "16 to 24 characters" in CONTENT
    assert "64 up to 256 characters" in CONTENT
    assert "Enter password length (16-24)" in CONTENT
    assert "Enter key length (64-256)" in CONTENT

def test_generate_password_functional_smoke():
    pwd = generate_password(16)
    assert len(pwd) == 16
    with pytest.raises(ValueError):
        generate_password(8)

def test_generate_secret_key_functional_smoke():
    key = generate_secret_key(64)
    assert len(key) == 64
    assert len(set(key)) == 64
    with pytest.raises(ValueError):
        generate_secret_key(32)

