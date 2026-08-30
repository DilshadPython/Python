"""Legacy Encapsulation Class/Instance Variable Script (Refactored).

This module updates the original `encapsulate_classvar_instancevar.py` script into a PEP 8-compliant,
type-annotated, modular implementation while maintaining backward compatibility.
For detailed attribute deletion and fallback, see `attribute_encapsulation_and_deletion.py`.
"""

from attribute_encapsulation_and_deletion import LanguageEnvironment


if __name__ == "__main__":
    print("=== Legacy Encapsulation Class/Instance Variable (Refactored) ===")
    env = LanguageEnvironment()
    env.language_name = "JavaScript"
    print("Instance Name:", env.language_name)
    del env.language_name
    print("Restored Class Name:", env.language_name)
