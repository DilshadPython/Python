"""Regular Instance Method Demonstration Module.

This module demonstrates standard instance methods bound to individual object instances
via `self`. It details state encapsulation, instance mutation, and class attribute interaction.
"""


class Staff:
    """Class representing staff members with regular instance methods."""

    number_of_staff: int = 0
    default_pay_raise: float = 1.06

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize Staff instance.

        Args:
            first_name: First name.
            last_name: Last name.
            salary: Base salary.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = salary
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@mail.com"

        Staff.number_of_staff += 1

    def full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    def show_email(self) -> str:
        """Return staff email address."""
        return self.email

    def increase_salary(self) -> None:
        """Apply pay raise multiplier to base salary."""
        self.salary = float(int(self.salary * self.default_pay_raise))


if __name__ == "__main__":
    print("=== Regular Instance Method Demonstration ===")

    staff1 = Staff("John", "Doe", 4100.0)
    print("Staff 1 Name:", staff1.full_name())
    print("Staff 1 Email:", staff1.show_email())
    print("Staff 1 Salary Before Raise:", staff1.salary)
    staff1.increase_salary()
    print("Staff 1 Salary After Raise:", staff1.salary)
    print()

    staff2 = Staff("Jack", "Wall", 3900.0)
    print("Staff 2 Name:", staff2.full_name())
    print("Staff 2 Email:", staff2.show_email())
    print("Staff 2 Salary Before Raise:", staff2.salary)
    staff2.increase_salary()
    print("Staff 2 Salary After Raise:", staff2.salary)
