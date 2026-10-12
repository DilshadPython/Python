"""
Demonstrates lambda functions for string concatenation and title capitalization.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Callable

# Lambda function appending a surname to a given first name
append_surname: Callable[[str], str] = lambda name: f"{name.strip()} Smith"

# Lambda function capitalizing title and appending surname
format_full_name_string: Callable[[str], str] = lambda name: f"{name.strip().title()} Smith"


def build_full_name(first_name: str = "john") -> str:
    """Return formatted full name string using lambda function."""
    return format_full_name_string(first_name)


if __name__ == '__main__':
    input_name = "john"
    print("Full name:", format_full_name_string(input_name))
