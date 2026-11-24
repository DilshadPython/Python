"""
Python Easter Egg: `import this` (The Zen of Python)

Importing `this` displays Tim Peters' 19 guiding principles for Python's design.
This module also exposes internal attributes used to encode/decode the text:
- `this.s`: The ROT13-encoded text of the Zen of Python.
- `this.d`: The cipher lookup dictionary mapping characters for ROT13 translation.

Example:
    >>> import import_this_zen_of_python
    >>> import_this_zen_of_python.get_encoded_text()[:21]
    'Gur Mra bs Clguba, ol'
"""
import io
import contextlib
import this


def get_zen_text() -> str:
    """
    Captures and returns the decrypted Zen of Python text emitted by `import this`.

    Returns:
        str: Plain text of the 19 Zen of Python aphorisms.
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        # Re-decodes the ROT13 string using the module's cipher dictionary
        decoded = "".join(this.d.get(c, c) for c in this.s)
    return decoded.strip()


def get_encoded_text() -> str:
    """
    Accesses the internal ROT13-encoded string stored in `this.s`.

    Returns:
        str: The raw ROT13 obfuscated text string.
    """
    return this.s


def get_cipher_map() -> dict[str, str]:
    """
    Accesses the character translation dictionary stored in `this.d`.

    Returns:
        dict[str, str]: The ROT13 mapping dictionary.
    """
    return this.d


def main() -> None:
    """Executes the Zen of Python demonstration."""
    print("=" * 60)
    print("🐍 Python Easter Egg: The Zen of Python (`import this`)")
    print("=" * 60)

    # 1. Decrypted output
    print("\n--- Decrypted Text ---")
    print(get_zen_text())

    # 2. Attribute introspection
    print("\n--- Module Attributes Introspection ---")
    print(f"`this.s` (Encoded length): {len(get_encoded_text())} characters")
    print(f"`this.d` (Cipher entries): {len(get_cipher_map())} mappings")
    print(f"Sample mapping ('a' -> '{this.d.get('a')}'): ROT13 transformation")


if __name__ == "__main__":
    main()
