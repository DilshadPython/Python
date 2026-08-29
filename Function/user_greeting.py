"""
Demonstrates user greeting function with default values.
"""


def greet_user(first_name: str = "Guest") -> str:
    """Return greeting string for given user first name."""
    return f"Your name is {first_name}"


if __name__ == '__main__':
    print(greet_user("Dilshad"))
