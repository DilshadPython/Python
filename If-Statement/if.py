"""Basic List Element Inspection using Conditional Statements.

Demonstrates accessing list elements by index and evaluating conditional statements
to inspect weekday categories.

Import Notes:
    - 'from typing import List': Imports the 'List' generic type from the standard library
      'typing' module to specify list element types in type hints.
"""

from typing import List


def classify_day_type(day_name: str) -> str:
    """Classify a weekday name as Weekend or Workday."""
    # Checks if day_name exists in the set of weekend days
    if day_name in ["Saturday", "Sunday"]:
        return f"{day_name} is a Weekend"
    else:
        return f"{day_name} is a Workday"


def demo_if() -> None:
    """Demonstrate list element evaluation."""
    workdays: List[str] = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    print(classify_day_type(workdays[5]))  # Saturday
    print(classify_day_type(workdays[3]))  # Thursday


if __name__ == "__main__":
    demo_if()
