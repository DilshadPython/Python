"""Book Instance Demonstration Module.

This module demonstrates basic class blueprint instantiation and attribute encapsulation in Python.
"""


class Book:
    """Class representing a book with title, cost, and owner attributes."""

    def __init__(self, title: str, cost: float, owner: str) -> None:
        """Initialize Book instance.

        Args:
            title: Book title.
            cost: Purchase cost.
            owner: Book owner name.
        """
        self.title: str = title
        self.cost: float = cost
        self.owner: str = owner

    def get_summary(self) -> str:
        """Return formatted summary string."""
        return f"'{self.title}' - ${self.cost:.2f} (Owner: {self.owner})"


if __name__ == "__main__":
    print("=== Book Instance Demonstration ===")
    b1 = Book("Data Science", 20.0, "Martin Schulter")
    b2 = Book("Computer Science", 39.0, "Tomas Adam")

    print(b1.get_summary())
    print(b2.get_summary())
