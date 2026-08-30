"""Custom Attribute Deleter Demonstration Module.

This module demonstrates overriding `__delattr__` to intercept attribute deletion attempts
on custom class instances.
"""


class TrackedProduct:
    """Class tracking attribute deletion via __delattr__ override."""

    default_category: str = "Electronics"

    def __init__(self, name: str) -> None:
        """Initialize TrackedProduct with product name."""
        self.name: str = name

    def __delattr__(self, item_name: str) -> None:
        """Intercept and log attribute deletion requests.

        Args:
            item_name: Attribute name requested for deletion.
        """
        print(f"Intercepted deletion request for attribute '{item_name}'")
        super().__delattr__(item_name)
        print(f"Attribute '{item_name}' successfully removed.")


if __name__ == "__main__":
    print("=== Custom Attribute Deleter Demonstration ===")
    prod = TrackedProduct("Computer")

    print("Product Name:", prod.name)
    del prod.name

    try:
        print(prod.name)
    except AttributeError as err:
        print("Expected AttributeError after deletion:", err)
