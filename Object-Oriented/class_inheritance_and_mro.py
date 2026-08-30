"""Class Inheritance and Method Resolution Order (MRO) Demonstration Module.

This module demonstrates single and multiple inheritance, super() initialization,
subclass attribute overriding, polymorphism, runtime type checks (isinstance, issubclass),
and Method Resolution Order (MRO).
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Optional, Tuple


class Employee:
    """Base class for organization employees."""

    default_raise_rate: float = 1.05

    def __init__(self, first_name: str, last_name: str, city: str, salary: float) -> None:
        """Initialize base Employee instance.

        Args:
            first_name: First name.
            last_name: Last name.
            city: City location.
            salary: Base annual salary amount.
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.city: str = city
        self.salary: float = salary
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def get_details(self) -> str:
        """Return formatted employee summary."""
        return f"{self.first_name} {self.last_name} ({self.city}) - Salary: ${self.salary:.2f}"

    def apply_pay_raise(self) -> None:
        """Apply base salary raise."""
        self.salary = float(int(self.salary * self.default_raise_rate))


class Developer(Employee):
    """Subclass representing software developers, overriding raise rate."""

    default_raise_rate: float = 1.07

    def __init__(self, first_name: str, last_name: str, city: str, salary: float, programming_language: str) -> None:
        """Initialize Developer instance using super().__init__().

        Args:
            first_name: First name.
            last_name: Last name.
            city: City location.
            salary: Base salary.
            programming_language: Primary programming language.
        """
        super().__init__(first_name, last_name, city, salary)
        self.programming_language: str = programming_language


class Manager(Employee):
    """Subclass representing team managers who supervise a list of employees."""

    def __init__(self, first_name: str, last_name: str, city: str, salary: float, employees: Optional[List[Employee]] = None) -> None:
        """Initialize Manager instance with optional supervised employees list.

        Args:
            first_name: First name.
            last_name: Last name.
            city: City location.
            salary: Base salary.
            employees: List of supervised Employee instances.
        """
        super().__init__(first_name, last_name, city, salary)
        self.employees: List[Employee] = employees if employees is not None else []

    def add_employee(self, emp: Employee) -> None:
        """Add an employee to the manager's supervised team.

        Args:
            emp: Employee instance to add.
        """
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp: Employee) -> None:
        """Remove an employee from the manager's supervised team.

        Args:
            emp: Employee instance to remove.
        """
        if emp in self.employees:
            self.employees.remove(emp)

    def list_team_members(self) -> List[str]:
        """Get summary list of team member details.

        Returns:
            List of formatted employee details.
        """
        return [emp.get_details() for emp in self.employees]


if __name__ == "__main__":
    print("=== Inheritance & Method Resolution Order (MRO) Demonstration ===")

    dev1 = Developer("John", "Doe", "Berlin", 45000, "Python")
    dev2 = Developer("Tom", "Smith", "Paris", 54000, "Java")
    mgr = Manager("Elmot", "David", "Cologne", 85300, [dev1])

    print("Developer Details:", dev1.get_details())
    print("Programming Language:", dev1.programming_language)
    print("Initial Manager Team:", mgr.list_team_members())

    print("\n--- Adding Team Member ---")
    mgr.add_employee(dev2)
    print("Updated Manager Team:", mgr.list_team_members())

    print("\n--- Type Inspection & Subclass Verification ---")
    print("isinstance(mgr, Employee):", isinstance(mgr, Employee))
    print("isinstance(mgr, Developer):", isinstance(mgr, Developer))
    print("issubclass(Developer, Employee):", issubclass(Developer, Employee))
    print("issubclass(Manager, Developer):", issubclass(Manager, Developer))

    print("\n--- Developer Method Resolution Order (MRO) ---")
    for cls in Developer.__mro__:
        print("  -", cls)
