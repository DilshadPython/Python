"""
Example: String manipulation and print formatting in Python.
Demonstrates: strip(), capitalize(), title(), and Python 3.6+ f-strings.
"""


def format_name_demo(raw_name: str = "   john doe   ") -> str:
    print(f"Initial Input: '{raw_name}'\n")

    # -------------------------------------------------------------
    # 1. Basic Print (No formatting / Raw string)
    # -------------------------------------------------------------
    # [Old Version / Legacy Python]
    print('Hi, ', raw_name)
    # [New Version / Python 3.6+ f-string]
    print(f"Hi, {raw_name}")
    print()

    # -------------------------------------------------------------
    # 2. strip() - Remove leading and trailing whitespace
    # -------------------------------------------------------------
    # Notice: strip() removes all whitespace (spaces, tabs, newlines)
    # from the beginning and end of the string.
    name_stripped = raw_name.strip()

    # [Old Version / Legacy]
    # print('Hi, ' + name_stripped)
    # [New Version / Python 3.6+]
    print(f"After strip(): Hi, {name_stripped}")
    print()

    # -------------------------------------------------------------
    # 3. capitalize() - Capitalize only the first character
    # -------------------------------------------------------------
    # Notice: str.capitalize() capitalizes the very first character
    # of the entire string and converts all other characters to lowercase.
    name_capitalized = name_stripped.capitalize()

    # [Old Version / Legacy]
    # print('Hi, %s' % name_capitalized)
    # [New Version / Python 3.6+]
    print(f"After capitalize(): Hi, {name_capitalized}")
    print()

    # -------------------------------------------------------------
    # 4. title() - Capitalize the first character of each word
    # -------------------------------------------------------------
    # Notice: str.title() capitalizes the first letter of EVERY word in the string.
    name_titled = name_stripped.title()

    # [Old Version / Legacy str.format()]
    # print('Hi, {}'.format(name_titled))
    # [New Version / Python 3.6+]
    print(f"After title(): Hi, {name_titled}")
    print()

    # -------------------------------------------------------------
    # 5. Method Chaining (Clean Code Style)
    # -------------------------------------------------------------
    # Notice: You can chain methods cleanly in a single line.
    clean_name = raw_name.strip().title()
    print(f"Clean Chained Result: Hi, {clean_name}")

    return clean_name


# Default variable for backward compatibility with imports/tests
name = "john doe"

if __name__ == "__main__":
    user_input = input("Please enter your full name: ")
    if user_input.strip():
        name = user_input
    format_name_demo(name)
