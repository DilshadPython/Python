"""
Global Variable Modification Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.3 - 3.13 & Python 2.7: `global` statement declares that a function modifies a module-level variable.
"""

from __future__ import print_function

language = "Initial"
lang = "Initial"


def set_global_language(new_lang="Python"):
    """Modifies global variable language."""
    global language
    language = new_lang
    return language


def set_global_lang(new_lang="Java"):
    """Modifies global variable lang."""
    global lang
    lang = new_lang
    return lang


def run_demo():
    """Runs global scope modification demonstration."""
    set_global_language("Python")
    print("I love", language)

    set_global_lang("Java")
    print("I like this language", lang)

    return {
        "language": language,
        "lang": lang
    }


if __name__ == '__main__':
    run_demo()