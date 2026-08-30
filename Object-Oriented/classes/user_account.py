"""User Account Demonstration Module.

This module demonstrates user account initialization and full name formatting.
"""


class UserAccount:
    """Class representing a user account."""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Initialize UserAccount with first and last name.

        Args:
            first_name: User first name.
            last_name: User last name.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name

    def get_full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    print("=== User Account Demonstration ===")
    u1 = UserAccount("John", "Doe")
    u2 = UserAccount("Daniel", "Edward")

    print("User 1:", u1.get_full_name())
    print("User 2:", u2.get_full_name())
