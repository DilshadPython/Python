"""Demonstration of combining positional *args and keyword **kwargs.

This module shows how variable positional arguments (*names) and variable
keyword arguments (**details) can be accepted together in a single function.
"""

from typing import Any


def drinks_type(*names: Any, **details: Any) -> dict[str, Any]:
    """Display and return a catalogue of drink names and extra detail attributes.

    Args:
        *names: Variable number of drink names or positional details.
        **details: Arbitrary keyword attributes (e.g., type, wine, origin).

    Returns:
        dict[str, Any]: A dictionary containing recorded names and details.
    """
    print("List of drinks:")
    for name in names:
        print(f" -- {name}")

    if details:
        print("Details:")
        for key, value in details.items():
            print(f" -- {key}: {value}")

    return {"names": list(names), "details": details}


if __name__ == "__main__":
    # Example 1: Whisky with extra details
    drinks_type("Whisky", 25.99, category="Spirits", brand="Jack Daniels")

    print("-" * 30)

    # Example 2: Gin with price and wine details
    drinks_type("Gin", 19.90, brand="Monkey Shoulder", wine="Red Wine")
