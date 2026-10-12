"""
Demonstrates handling dynamic positional (*args) and keyword (**kwargs) arguments.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Any, Dict, Tuple


def view(*args: Any, **kwargs: Any) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
    """Return passed positional and keyword arguments as a tuple of (args, kwargs)."""
    return args, kwargs


if __name__ == "__main__":
    a, kw = view("Alpha", "Beta", key1="Val1", key2="Val2")
    print(f"Args: {a}")
    print(f"Kwargs: {kw}")
