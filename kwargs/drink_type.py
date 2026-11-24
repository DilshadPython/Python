"""Demonstrate explicit required parameters combined with variable keyword arguments (**kwargs).

This module shows how functions can require specific named attributes while
accepting arbitrary additional options via **kwargs.
"""

from typing import Any


def drinks_type(name: str, price: float, **details: Any) -> dict[str, Any]:
    """Record a drink item with its mandatory name and price, plus optional details.

    Args:
        name (str): The name of the drink.
        price (float): The price of the drink.
        **details: Extra optional key-value properties (e.g., brand, alcohol_free).

    Returns:
        dict[str, Any]: Summary dictionary of drink properties.
    """
    print(f"Drink: {name}")
    print(f"Price: £{price:.2f}")

    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"  -- {key}: {value}")

    return {
        "name": name,
        "price": price,
        "details": details
    }


if __name__ == "__main__":
    drinks_type("Whisky", 25.99, non_alcoholic=False, brand="Jack Daniels")
    print("-" * 30)
    drinks_type("Gin", 19.90, brand="Monkey Shoulder", style="London Dry")
