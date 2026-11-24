"""Demonstrate mandatory positional arguments alongside variable positional *args.

This module shows how standard positional parameters (name, age) can be
combined with optional trailing positional parameters (*extras).
"""

from typing import Any


def register_client(name: str, age: int, *extras: Any) -> dict[str, Any]:
    """Register a client with required basic info and optional extra details.

    Args:
        name (str): Client's full name.
        age (int): Client's age.
        *extras: Arbitrary additional positional attributes (location, email, etc.).

    Returns:
        dict[str, Any]: Structured dictionary of the registered client.
    """
    print(f"Client: {name}, Age: {age}")
    if extras:
        print("Additional info:")
        for arg in extras:
            print(f"  ---> {arg}")

    return {
        "name": name,
        "age": age,
        "extras": list(extras)
    }


if __name__ == "__main__":
    register_client("Alice", 25)
    register_client("Bob", 28)
    register_client("Charlie", 23, "London")
    register_client("David", 31, "david@live.com")
    register_client("Sam", 33, "Berlin", "sam@gmail.com")
    register_client("Eliot", 24, "Germany", "Musician", "07754 2144 2547")
