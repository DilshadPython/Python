"""Age Bracket Categorization with 'if-elif-else'.

Demonstrates categorizing a person's age into life stage brackets:
- Minor (< 18)
- Adult (18 - 64)
- Senior (65+)

Import Notes:
    - 'from typing import List': Standard library typing module import to type-annotate
      lists of sample integer ages.
"""

from typing import List


def categorize_age_stage(age: int) -> str:
    """Categorize age into life stages: Minor, Adult, or Senior."""
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


def demo_if_elif() -> None:
    """Demonstrate age categorization."""
    test_ages: List[int] = [10, 25, 70]
    for age in test_ages:
        stage = categorize_age_stage(age)
        print(f"Age {age:2d} -> Category: {stage}")


if __name__ == "__main__":
    demo_if_elif()
