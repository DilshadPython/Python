"""
Demonstrates reverse slicing [::-1] and statistical functions on lists.
"""

def demo_numeric_operations():
    numbers = [6, 9, 12, 15, 18, 21, 24, 28, 31, 34, 38]
    print('Original numbers:', numbers)

    reversed_slice = numbers[::-1]
    print('Reversed slice:', reversed_slice)

    min_val = min(numbers)
    max_val = max(numbers)
    total_sum = sum(numbers)

    print(f'Min: {min_val}, Max: {max_val}, Sum: {total_sum}')
    return reversed_slice, min_val, max_val, total_sum

if __name__ == '__main__':
    demo_numeric_operations()
