"""
Demonstrates string formatting, case transformation, and user detail composition.
"""


def username(fname: str = "John", lname: str = "Smith", age: int = 30) -> str:
    """Return formatted full name in uppercase with age details."""
    details = f"{fname.upper()} {lname.upper()}"
    return f"Your full name is {details} and your age is {age}"


if __name__ == '__main__':
    try:
        fn = input('Enter your first name: ')
        ln = input('Enter your last name: ')
        ag = int(input('Enter your age: '))
        print(username(fn, ln, ag))
    except ValueError:
        print("Invalid age input")
