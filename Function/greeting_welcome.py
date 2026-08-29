"""
Demonstrates multi-argument greeting function with custom messages.
"""


def welcome_user(msg: str, name: str = "User") -> str:
    """Return formatted message string combining greeting message and name."""
    return f"{msg}, {name}"


if __name__ == '__main__':
    print(welcome_user("Hello", "Dilshad"))
