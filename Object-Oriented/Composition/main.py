"""Legacy Composition Main Script (Refactored).

This module updates the original `main.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed composition patterns, see `object_composition.py`.
"""

import io
from object_composition import TextComposer


if __name__ == "__main__":
    print("=== Legacy Composition Main (Refactored) ===")
    string_stream = io.StringIO()
    composer = TextComposer(string_stream)
    composer.write_message("This is the message we write.")
    print("StringIO Output:", string_stream.getvalue())
