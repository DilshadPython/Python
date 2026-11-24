"""
Demonstrates calculation of list sum and length using built-in functions.
"""

def demo_sum_len():
    numbers = [12, 34, 56, 67, 60]
    total = sum(numbers)
    count = len(numbers)
    avg = total / count if count > 0 else 0

    print(f'Numbers: {numbers}')
    print(f'Sum: {total}')
    print(f'Count: {count}')
    print(f'Average: {avg:.2f}')

    return total, count, avg

if __name__ == '__main__':
    demo_sum_len()
