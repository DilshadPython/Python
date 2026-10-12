"""
Demonstrates dictionary key-value lookup for student ID mapping.
"""
# "from module import name" imports specific type hint symbols directly into local scope.
from typing import Dict

STUDENT_DIRECTORY: Dict[int, str] = {
    814747: 'John Smith',
    814748: 'John Doe',
    814749: 'Jane Smith'
}


def get_student_name(student_id: int) -> str:
    """Return student full name corresponding to student ID, or unknown warning."""
    return STUDENT_DIRECTORY.get(student_id, f"Unknown user ID: {student_id}")


if __name__ == '__main__':
    print("Student 814747:", get_student_name(814747))
