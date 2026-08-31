"""
Demonstrates string formatting within functions and variable argument lists (*args, **kwargs).
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Dict, Tuple


def welcome_msg(greeting: str, name: str = 'John') -> str:
    """Return formatted greeting string."""
    return f"{greeting}{name}"


def user_details(*args: Any, **kwargs: Any) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
    """Return tuple of positional and keyword arguments passed."""
    return args, kwargs


if __name__ == '__main__':
    print(welcome_msg('Hello, '))
    args, kwargs = user_details('John', 'john@example.com', age=41, sex='Male')
    print("Args:", args)
    print("Kwargs:", kwargs)
