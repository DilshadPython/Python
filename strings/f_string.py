"""
F-String and String Formatting Demonstration (Python 3.3 to Python 3.13 Compatible)

Python Version Notes:
- Python 3.6 - 3.13: F-strings `f"Hello {name}"` allow embedded expressions and method calls inside `{}`.
- Python 3.13: PEP 701 standardizes quote nesting inside f-strings.
- Python 2.7 - 3.5 Comparison: `str.format()` was the primary formatting mechanism.
"""

from __future__ import print_function

try:
    get_input = raw_input  # Python 2.7
except NameError:
    get_input = input      # Python 3.3 - 3.13


def format_greeting(name='Azad', lang='Python', age=37):
    """Formats greeting string across version standards."""
    formatted_str = "Hello {0}, do you like to learn {1} programming language?".format(name, lang)
    upper_greeting = "Hello, {0}".format(name.upper())
    profile = "My name is {0} and I am {1} years old".format(name, age)
    return {
        "greeting": formatted_str,
        "upper_greeting": upper_greeting,
        "profile": profile
    }


def main():
    """Interactive execution for formatted greetings."""
    try:
        name = get_input('Enter a name: ') or 'Azad'
        lang = get_input('Enter a language: ') or 'Python'
        res = format_greeting(name, lang)
        print(res["greeting"])
        print(res["upper_greeting"])
        print(res["profile"])
    except (EOFError, KeyboardInterrupt):
        print("\nUsing defaults:")
        print(format_greeting()["greeting"])


if __name__ == '__main__':
    main()