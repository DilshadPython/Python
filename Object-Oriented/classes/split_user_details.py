"""Split User Details and Age Calculation Module.

This module demonstrates parsing user names from full name strings and calculating age
from date of birth strings (YYYYMMDD).
"""

import datetime


class UserProfile:
    """Class storing user profile details and calculating current age."""

    def __init__(self, full_name: str, date_of_birth: str) -> None:
        """Initialize UserProfile, parsing first and last names.

        Args:
            full_name: Space-separated full name string (e.g., 'John Doe').
            date_of_birth: Date string in 'YYYYMMDD' format (e.g., '19750301').
        """
        self.full_name: str = full_name.strip()
        self.date_of_birth: str = date_of_birth.strip()

        # Parse first and last names
        parts = self.full_name.split()
        self.first_name: str = parts[0] if parts else ""
        self.last_name: str = parts[-1] if len(parts) > 1 else ""

    def calculate_age(self, reference_date: datetime.date = datetime.date(2018, 3, 28)) -> int:
        """Calculate age in years based on reference date.

        Args:
            reference_date: Current/reference date for age calculation.

        Returns:
            Age in full completed years.
        """
        year = int(self.date_of_birth[0:4])
        month = int(self.date_of_birth[4:6])
        day = int(self.date_of_birth[6:8])
        dob = datetime.date(year, month, day)

        age_in_days = (reference_date - dob).days
        return int(age_in_days / 365.25)


if __name__ == "__main__":
    print("=== Split User Details Demonstration ===")
    user = UserProfile("John Doe", "19750301")
    print("Full Name:", user.full_name)
    print("First Name:", user.first_name)
    print("Last Name:", user.last_name)
    print("Calculated Age:", user.calculate_age())
