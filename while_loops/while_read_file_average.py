"""
Demonstrates reading file line by line with a while loop and calculating metrics.
"""
import os
from typing import Tuple


def calculate_file_average(filepath: str) -> Tuple[float, int, float]:
    """Read numeric lines from a file using a while loop and compute total and average."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    count = 0
    total = 0.0

    with open(filepath, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            line_str = line.strip()
            if line_str:
                total += float(line_str)
                count += 1
            line = f.readline()

    average = total / count if count > 0 else 0.0
    return total, count, average


if __name__ == '__main__':
    q_path = os.path.join(os.path.dirname(__file__), 'quotes.txt')
    tot, cnt, avg = calculate_file_average(q_path)
    print(f"Total: {tot}, Count: {cnt}, Average: {avg:.2f}")
