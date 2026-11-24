"""Demonstrate combined *args and **kwargs parameter registration.

This module shows how functions can accept both flexible positional arguments
and arbitrary keyword arguments to handle dynamic customer data.
"""

from typing import Any


def register_customer(*args: Any, **kwargs: Any) -> dict[str, Any]:
    """Register a customer using flexible positional and keyword metadata.

    Args:
        *args: Variable positional arguments (e.g., name, age, country).
        **kwargs: Variable key-value pairs (e.g., email, mobile, job).

    Returns:
        dict[str, Any]: Structured record of the customer.
    """
    print(f"Positional args: {args}")
    print(f"Keyword args:    {kwargs}")
    for key, value in kwargs.items():
        print(f"  ---> {key}: {value}")

    return {
        "args": list(args),
        "kwargs": kwargs
    }


if __name__ == "__main__":
    register_customer("Alice", 25)
    register_customer("Bob", 28)
    register_customer("Charlie", 23, city="London")
    register_customer("David", 31, email="david@live.com")
    register_customer("Sam", 33, city="Berlin", email="sam@gmail.com", country="Germany")
    register_customer("Eliot", 24, "UK", job="Musician", mobile="07754 2144 2547")
