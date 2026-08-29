"""
Backwards-compatible wrapper alias for student_directory.py (descriptive filename).
"""
from Function.student_directory import STUDENT_DIRECTORY, get_student_name

__all__ = ["STUDENT_DIRECTORY", "get_student_name"]

if __name__ == '__main__':
    print(get_student_name(814747))
