"""Class and Instance Attributes Demonstration Module.

This module demonstrates the distinction between Class Attributes (shared across all instances)
and Instance Attributes (unique to each object instance). It details attribute lookup resolution
order (Instance dict -> Class dict -> Superclasses) and how overriding class variables on an instance
creates instance-level attribute shadows.
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import Dict, Any


class EmployeeAccount:
    """Class demonstrating class attributes vs instance attributes."""

    # Class Attributes: shared across all instances
    total_employee_count: int = 0
    default_raise_rate: float = 1.05

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize an EmployeeAccount instance and increment total employee count.

        Args:
            first_name: First name.
            last_name: Last name.
            salary: Base annual salary amount.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = salary
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@company.com"

        # Increment shared class attribute counter
        EmployeeAccount.total_employee_count += 1

    def get_details(self) -> str:
        """Return formatted employee details."""
        return f"{self.first_name} {self.last_name}, Salary: ${self.salary:.2f}"

    def apply_pay_raise(self) -> None:
        """Apply salary increase based on raise rate (instance attribute if overridden, else class default)."""
        # Looks for self.raise_rate in instance dict; falls back to class attribute if not present
        raise_rate = getattr(self, "raise_rate", self.default_raise_rate)
        self.salary = float(int(self.salary * raise_rate))


if __name__ == "__main__":
    print("=== Class & Instance Attributes Demonstration ===")
    print("Initial Total Employees:", EmployeeAccount.total_employee_count)

    emp1 = EmployeeAccount("John", "Doe", 47000)
    emp2 = EmployeeAccount("Tom", "Smith", 55000)

    print("Total Employees after creating 2 instances:", EmployeeAccount.total_employee_count)

    print("\n--- Instance Dict vs Class Dict ---")
    print("emp1 __dict__ before raise:", emp1.__dict__)
    print("EmployeeAccount __dict__ keys:", list(EmployeeAccount.__dict__.keys()))

    print("\n--- Applying Default Pay Raise (1.05) ---")
    print("emp1 original salary:", emp1.salary)
    emp1.apply_pay_raise()
    print("emp1 salary after 1.05 raise:", emp1.salary)

    print("\n--- Overriding Raise Rate for emp1 (1.08) ---")
    # Setting an attribute on an instance creates an instance-level variable shadowing the class variable
    emp1.raise_rate = 1.08
    print("emp1 __dict__ after setting raise_rate:", emp1.__dict__)
    emp1.apply_pay_raise()
    print("emp1 salary after custom 1.08 raise:", emp1.salary)
    print("emp2 salary (unaffected default raise rate):", emp2.salary)
