"""
Demonstrates combining function return values for user email welcome messages.
"""


def view_email(email: str) -> str:
    """Return email verification string."""
    return f"{email} is your email."


def welcome(name: str, email: str) -> str:
    """Return full welcome message with email."""
    return f"Hello {name.strip()} welcome to function!. {view_email(email)}"


if __name__ == '__main__':
    print(welcome("Tom", "tom@example.com"))
