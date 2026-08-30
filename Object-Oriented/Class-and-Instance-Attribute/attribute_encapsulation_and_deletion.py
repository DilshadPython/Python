"""Attribute Encapsulation and Deletion Demonstration Module.

This module demonstrates how assigning an attribute on an instance creates a local instance shadow,
and deleting that instance attribute (`del instance.attr`) restores access to the underlying class attribute.
"""


class LanguageEnvironment:
    """Class demonstrating instance attribute assignment and del attribute fallback."""

    language_name: str = "Python"


if __name__ == "__main__":
    print("=== Attribute Shadowing and Deletion Demonstration ===")
    env = LanguageEnvironment()

    print("1. Reading class attribute via instance:", env.language_name)

    # Shadowing class attribute by assigning to instance attribute
    env.language_name = "JavaScript"
    print("2. Instance attribute set to shadow class attribute:", env.language_name)
    print("   Class attribute remains:", LanguageEnvironment.language_name)

    # Deleting instance attribute restores class attribute lookup
    del env.language_name
    print("3. After 'del env.language_name', falls back to class attribute:", env.language_name)
