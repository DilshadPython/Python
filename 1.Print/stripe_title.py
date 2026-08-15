"""
Demonstration of strip(), title(), count(), and Python 3.6+ f-strings.
"""

# Notices:
# 1. strip() removes leading and trailing whitespace from a string.
# 2. title() capitalizes the first character of each word.
# 3. str.count(sub) returns the number of non-overlapping occurrences of substring 'sub'.
# 4. Clean Code Tip: Avoid reassigning variables to different data types (e.g., from str to int).


def demonstrate_stripe_title(input_name: str = "john doe") -> None:
    # -------------------------------------------------------------
    # 1. Method Chaining: strip() and title()
    # -------------------------------------------------------------
    name = input_name.strip().title()

    # [Old Version / str.format()]
    # print('Hi, {}'.format(name))

    # [New Version / Python 3.6+ f-string]
    print(f"Hi, {name}")
    print()

    # Demonstrating repeated clean operation
    name = name.strip().title()
    print(f"Hello, {name}")
    print()

    # -------------------------------------------------------------
    # 2. str.count() Demonstration
    # -------------------------------------------------------------
    # Notice: Counting how many times 'name' occurs inside itself returns 1 (integer)
    # [Old Version Style]
    # count_val = name.count(name)
    # print('Count: %d' % count_val)

    # [New Version / Python 3.6+ f-string]
    occurrences = name.count(name)
    print(f"Occurrences of '{name}' inside itself: {occurrences}")

    # Preserving original variable re-assignment for demonstration:
    counted_name = name.count(name)
    print(f"Hi, {counted_name}")


if __name__ == "__main__":
    user_input = input("Please enter your full name: ")
    if user_input.strip():
        demonstrate_stripe_title(user_input)
    else:
        demonstrate_stripe_title()
