"""
Rounding numbers in Python using round() and Python 3.6+ format specifiers.
"""

# Notices:
# 1. round(number[, ndigits]): Rounds a number to 'ndigits' decimal places.
#    If ndigits is omitted or None, it returns the nearest integer.
# 2. Python 3 uses 'Banker's Rounding' (round half to even).
#    For example, round(2.5) == 2 and round(3.5) == 4.
# 3. Python 3.6+ f-strings support formatting specifiers:
#    - f"{z:,}" formats numbers with comma thousands separators.
#    - f"{val:.2f}" formats floating point numbers to 2 decimal places.


def demonstrate_rounding(x: float = 22.56, y: float = 15.09) -> None:
    print(f"Given numbers: x = {x}, y = {y}")
    addition = x + y

    # -------------------------------------------------------------
    # 1. Basic round() to nearest integer
    # -------------------------------------------------------------
    result = round(addition)

    # [Old Version / Legacy print]
    print('Result: ', result)

    # [New Version / Python 3.6+ f-string]
    print(f"Result (f-string): {result}")

    # -------------------------------------------------------------
    # 2. Formatting with comma thousands separator and decimals
    # -------------------------------------------------------------
    z = round(addition)
    # [Old Version]
    print('Z: ', f"{z:,}")

    # [New Version / Python 3.6+ advanced format specifiers]
    print(f"Z with comma separator: {z:,}")
    print(f"Formatted to 2 decimal places: {addition:.2f}")

    # -------------------------------------------------------------
    # 3. Rounding with ndigits parameter
    # -------------------------------------------------------------
    rounded_2dp = round(addition, 2)
    print(f"Rounded using round(x + y, 2): {rounded_2dp}")


if __name__ == "__main__":
    print("Enter float numbers:")
    try:
        user_x = float(input("Enter x (e.g. 22.56): "))
        user_y = float(input("Enter y (e.g. 15.09): "))
        demonstrate_rounding(user_x, user_y)

        print("\n--- Additional Calculation ---")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        total = round(a + b)
        print(f"Total: {total}")
    except ValueError:
        print("Invalid float entered, running demo with default values:")
        demonstrate_rounding()