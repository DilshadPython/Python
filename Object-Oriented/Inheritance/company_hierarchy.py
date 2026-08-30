"""Company Hierarchy Inheritance Module.

This module demonstrates complex class inheritance using `super()`, attribute overriding,
and employee management in `Company`, `Staff`, and `Manager` classes.
"""

from typing import List, Optional


class CompanyEmployee:
    """Base class for all company employees."""

    pay_raise_rate: float = 1.03

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """Initialize CompanyEmployee instance."""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.salary: float = float(salary)
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def get_full_name(self) -> str:
        """Return formatted full name."""
        return f"{self.first_name} {self.last_name}"

    def apply_pay_raise(self) -> None:
        """Apply pay raise using pay_raise_rate."""
        self.salary = float(int(self.salary * self.pay_raise_rate))


class Staff(CompanyEmployee):
    """Staff member subclass extending CompanyEmployee with skill attribute."""

    pay_raise_rate: float = 1.07

    def __init__(self, first_name: str, last_name: str, salary: float, primary_skill: str) -> None:
        """Initialize Staff with primary skill."""
        super().__init__(first_name, last_name, salary)
        self.primary_skill: str = primary_skill


class Manager(CompanyEmployee):
    """Manager subclass managing a team of employees."""

    def __init__(self, first_name: str, last_name: str, salary: float, team: Optional[List[CompanyEmployee]] = None) -> None:
        """Initialize Manager with optional team list."""
        super().__init__(first_name, last_name, salary)
        self.team: List[CompanyEmployee] = team if team is not None else []

    def add_employee(self, employee: CompanyEmployee) -> None:
        """Add employee to managed team."""
        if employee not in self.team:
            self.team.append(employee)

    def remove_employee(self, employee: CompanyEmployee) -> None:
        """Remove employee from managed team."""
        if employee in self.team:
            self.team.remove(employee)

    def get_team_names(self) -> List[str]:
        """Return list of managed employee full names."""
        return [emp.get_full_name() for emp in self.team]


if __name__ == "__main__":
    print("=== Company Hierarchy Demonstration ===")
    dev = Staff("Joe", "Philips", 7000.0, "Java")
    mgr = Manager("Georgina", "Holland", 12000.0)

    mgr.add_employee(dev)
    print("Manager Full Name:", mgr.get_full_name())
    print("Manager Team:", mgr.get_team_names())
