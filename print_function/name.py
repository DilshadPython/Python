"""
Name formatting demo: Demonstrating strip(), title(), end parameter, and f-strings.
"""

# Notices:
# 1. strip() removes leading and trailing empty spaces (whitespace).
# 2. title() capitalizes the first letter of each word (fname and lname).
# 3. The 'end' parameter in print() controls what is printed at the end (default is '\n').
# 4. Note: input() in Python 3 always returns a string (str), so wrapping with str() is optional.


def demonstrate_name_formatting(first: str = "john", last: str = "doe") -> None:
    # Notice: Demonstrating strip() on a string with whitespace
    remove_empty_space = '      world       '

    # -------------------------------------------------------------
    # String Stripping Comparison
    # -------------------------------------------------------------
    # [Old Version / Legacy Python]
    print('Hello, ', remove_empty_space.strip(), ' in Python')

    # [New Version / Python 3.6+ f-string]
    print(f"Hello, {remove_empty_space.strip()} in Python")

    # -------------------------------------------------------------
    # Combining First and Last Name Comparison
    # -------------------------------------------------------------
    # [Old Version / Legacy String Concatenation & str.format()]
    full_name_old = (first + ' ' + last).title()
    print('Hi, ', full_name_old)
    # print('Hi, {}'.format(full_name_old))

    # [New Version / Python 3.6+ f-string]
    full_name_new = f"{first} {last}".strip().title()
    print(f"Hi, {full_name_new}")

    # -------------------------------------------------------------
    # 'end' parameter demonstration
    # -------------------------------------------------------------
    # Notice: 'end' parameter prevents a new line
    print("Printing on the same line: ", end="")
    print(f"{first.title()} {last.title()}")


if __name__ == "__main__":
    fname = input("Enter first name: ").strip()
    lname = input("Enter last name: ").strip()
    demonstrate_name_formatting(fname, lname)
