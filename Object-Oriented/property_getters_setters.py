"""Property Getters, Setters, and Deleters Demonstration Module.

This module demonstrates property encapsulation in Python using the @property decorator,
getter methods, setter methods (@property_name.setter), and deleter methods (@property_name.deleter).
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Optional


class EmployeeProfile:
    """Class showcasing Pythonic attribute access control using properties."""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Initialize EmployeeProfile with first and last names.

        Args:
            first_name: First name.
            last_name: Last name.
        """
        self.first_name: Optional[str] = first_name
        self.last_name: Optional[str] = last_name

    @property
    def email(self) -> str:
        """Property getter for dynamic email computation.

        Returns:
            Calculated email address string or empty string if name deleted.
        """
        if self.first_name and self.last_name:
            return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"
        return ""

    @property
    def full_name(self) -> str:
        """Property getter for dynamic full name.

        Returns:
            Combined first name and last name.
        """
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return "Name Deleted"

    @full_name.setter
    def full_name(self, name_str: str) -> None:
        """Property setter allowing full name string assignment ('First Last').

        Args:
            name_str: Space-separated full name string.
        """
        parts = name_str.strip().split(" ", 1)
        self.first_name = parts[0]
        self.last_name = parts[1] if len(parts) > 1 else ""

    @full_name.deleter
    def full_name(self) -> None:
        """Property deleter invoked when deleting the property (del instance.full_name)."""
        print("Executing full_name deleter: resetting first_name and last_name to None")
        self.first_name = None
        self.last_name = None


if __name__ == "__main__":
    print("=== Property Getters, Setters, and Deleters Demonstration ===")
    emp = EmployeeProfile("John", "Doe")

    print("--- 1. Initial State ---")
    print("First Name:", emp.first_name)
    print("Full Name (Property):", emp.full_name)
    print("Email (Property):", emp.email)

    print("\n--- 2. Setting Full Name via Setter ---")
    emp.full_name = "George Alan"
    print("Updated First Name:", emp.first_name)
    print("Updated Last Name:", emp.last_name)
    print("Updated Full Name:", emp.full_name)
    print("Updated Email:", emp.email)

    print("\n--- 3. Deleting Full Name via Deleter ---")
    del emp.full_name
    print("Full Name after del:", emp.full_name)
    print("Email after del:", emp.email)
