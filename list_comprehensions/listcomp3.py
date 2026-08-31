"""
Demonstrates opening and parsing files directly in a one-line list comprehension.
"""

import os

def read_numbers_one_liner():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    numbers_file = os.path.join(dir_path, 'numbers.txt')

    with open(numbers_file, 'r') as f:
        numbers = [line.rstrip() for line in f]

    print('File contents cleaned via rstrip():', numbers)
    return numbers

if __name__ == '__main__':
    read_numbers_one_liner()
