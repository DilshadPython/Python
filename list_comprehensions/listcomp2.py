"""
Demonstrates reading files line-by-line using context managers and list comprehensions.
"""

import os

def read_files_with_comp():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    grades_file = os.path.join(dir_path, 'grades.txt')
    numbers_file = os.path.join(dir_path, 'numbers.txt')

    with open(grades_file, 'r') as f:
        raw_grades = [line.rstrip() for line in f]

    with open(numbers_file, 'r') as f:
        numbers = [int(line.strip()) for line in f if line.strip()]

    print('Raw grades from file:', raw_grades)
    print('Parsed integer numbers:', numbers)

    return raw_grades, numbers

if __name__ == '__main__':
    read_files_with_comp()
