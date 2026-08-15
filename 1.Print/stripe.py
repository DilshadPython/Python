"""
Demonstration of string stripping, title casing, f-strings, and print end parameter.
"""

# Notices:
# 1. strip() removes all leading and trailing whitespace from the string.
# 2. Without the 'f' prefix, print('Hi, {name}') outputs '{name}' literally as text.
# 3. Python 3.6+ introduced f-strings (e.g. f"Hi, {name}") for formatted string evaluation.
# 4. The 'end' parameter in print() specifies what to print at the end instead of the default newline ('\n').


def demonstrate_strip_and_print(raw_name: str = "   john doe   ") -> None:
    # -------------------------------------------------------------
    # 1. Step-by-Step String Cleaning
    # -------------------------------------------------------------
    name = raw_name.strip()
    name = name.title()

    # Notice: Standard string literal vs Python 3.6+ f-string
    print('Literal without f-prefix: Hi, {name}')
    print(f"Evaluated with f-string:  Hi, {name}")

    print('=' * 35)

    # -------------------------------------------------------------
    # 2. Method Chaining (Clean Code Style)
    # -------------------------------------------------------------
    # Notice: Chaining strip() and title() in one step
    name = raw_name.strip().title()

    # [Old Version / str.format()]
    # print('Hi, {}'.format(name))

    # [New Version / Python 3.6+ f-string]
    print(f"Hi, {name}")

    # -------------------------------------------------------------
    # 3. Using the 'end' parameter
    # -------------------------------------------------------------
    # Notice: 'end' parameter suppresses the default newline
    print(f"Hi, {name}", end=' << ')
    print('Azad', ' ', end='')
    print('Tome')


if __name__ == "__main__":
    user_input = input("Please enter your full name: ")
    if user_input.strip():
        demonstrate_strip_and_print(user_input)
    else:
        demonstrate_strip_and_print()