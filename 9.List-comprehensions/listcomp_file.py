"""
Demonstrates cleaning text lines extracted via readlines() using list comprehensions.
"""

import os

def clean_file_lines():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    grades_file = os.path.join(dir_path, 'grades.txt')

    with open(grades_file, 'r') as f:
        lines = f.readlines()

    cleaned_lines = [line.rstrip() for line in lines]
    print('Cleaned file lines:', cleaned_lines)
    return cleaned_lines

if __name__ == '__main__':
    clean_file_lines()
