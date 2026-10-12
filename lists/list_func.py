"""
Demonstrates built-in aggregation functions: max(), min(), sum(), and len().
"""

def demo_list_aggregates():
    numbers = [15, 82, 3, 44, 99, 21, 6]
    print('Numbers list:', numbers)

    max_val = max(numbers)
    min_val = min(numbers)
    total_sum = sum(numbers)
    count = len(numbers)

    print(f'Max value: {max_val}')
    print(f'Min value: {min_val}')
    print(f'Sum of values: {total_sum}')
    print(f'Element count: {count}')

    # Convert string to character list using built-in list() constructor
    char_list = list('Dilshad')
    print('list("Dilshad"):', char_list)

    return max_val, min_val, total_sum, count, char_list

if __name__ == '__main__':
    demo_list_aggregates()
