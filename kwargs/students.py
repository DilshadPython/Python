"""Student registration demonstrating standard positional and keyword invocation.

This module shows clean parameter naming, type annotations, and calling
conventions with default parameters.
"""

from typing import Optional


def register_student(std_name: str, language: str, level: Optional[str] = "Beginner") -> dict[str, str]:
    """Register a student with their chosen study language and proficiency level.

    Args:
        std_name (str): Full name of the student.
        language (str): Target study language (e.g., 'French', 'English').
        level (str, optional): Proficiency level. Defaults to 'Beginner'.

    Returns:
        dict[str, str]: Student profile record.
    """
    profile = {
        "student_name": std_name,
        "language": language,
        "level": level or "Beginner"
    }
    print(f"Registered Student: {profile['student_name']} -> {profile['language']} ({profile['level']})")
    return profile


if __name__ == "__main__":
    register_student("Alice", "French")
    register_student("Bob", "English", level="Advanced")
    register_student("Charlie", language="Spanish", level="Intermediate")
