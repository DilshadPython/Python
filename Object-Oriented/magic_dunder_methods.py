"""Magic Dunder Methods Demonstration Module.

This module demonstrates special (dunder) methods in Python:
1. Object initialization: __init__
2. String representations: __repr__ (unambiguous developer representation) and __str__ (user-friendly string)
3. Arithmetic operator overloading: __add__ (plus operator +)
4. Length measurement: __len__ (built-in len())
5. Equality comparison: __eq__ (equals operator ==)
"""

# "from typing import ..." imports specific type hint symbols directly into local scope.
from typing import List, Any


class EmployeeRecord:
    """Class showcasing standard magic (dunder) method implementations."""

    def __init__(self, first_name: str, last_name: str, city: str, salary: float) -> None:
        """Initialize EmployeeRecord attributes."""
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.city: str = city
        self.salary: float = salary
        self.email: str = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def __repr__(self) -> str:
        """Return official, unambiguous string representation suitable for recreation."""
        return f"EmployeeRecord('{self.first_name}', '{self.last_name}', '{self.city}', {self.salary})"

    def __str__(self) -> str:
        """Return user-friendly string representation."""
        return f"{self.first_name} {self.last_name} ({self.city}) <{self.email}>"

    def __add__(self, other: Any) -> float:
        """Overload addition (+) operator to combine salaries of two EmployeeRecord instances."""
        if isinstance(other, EmployeeRecord):
            return self.salary + other.salary
        return NotImplemented

    def __len__(self) -> int:
        """Return character length of employee full name."""
        return len(f"{self.first_name} {self.last_name}")

    def __eq__(self, other: Any) -> bool:
        """Check equality (==) based on email address."""
        if isinstance(other, EmployeeRecord):
            return self.email == other.email
        return False


class ListNumber:
    """Class overloading addition (+) to perform element-wise sum of numeric lists."""

    def __init__(self, numbers: List[int]) -> None:
        """Initialize ListNumber with a list of integers."""
        self.numbers: List[int] = numbers

    def __add__(self, other: "ListNumber") -> "ListNumber":
        """Perform element-wise addition of two ListNumber instances using zip()."""
        combined = [x + y for x, y in zip(self.numbers, other.numbers)]
        return ListNumber(combined)

    def __repr__(self) -> str:
        """Return string representation of internal number list."""
        return str(self.numbers)


if __name__ == "__main__":
    print("=== Magic (Dunder) Methods Demonstration ===")

    emp1 = EmployeeRecord("John", "Doe", "Berlin", 45000)
    emp2 = EmployeeRecord("Tom", "Smith", "Paris", 54000)

    print("--- 1. __repr__ and __str__ ---")
    print("str(emp1): ", str(emp1))
    print("repr(emp1):", repr(emp1))

    print("\n--- 2. Operator Overloading (__add__) ---")
    combined_salary = emp1 + emp2
    print("emp1 + emp2 combined salary:", combined_salary)

    print("\n--- 3. Length Measurement (__len__) ---")
    print("len(emp1) (full name length):", len(emp1))

    print("\n--- 4. ListNumber Element-wise Addition ---")
    lst1 = ListNumber([1, 2, 3, 4, 5])
    lst2 = ListNumber([10, 20, 30, 40, 50])
    result_lst = lst1 + lst2
    print(f"lst1 ({lst1}) + lst2 ({lst2}) = {result_lst}")
