"""
Demonstrates min(), max(), and sum() on numerical lists.
"""

def demo_number_stats():
    nums = [19, 11, 2, 6, 7, 13, 33]
    print('Numbers:', nums)

    min_val = min(nums)
    max_val = max(nums)
    total = sum(nums)

    print('Minimum number:', min_val)
    print('Maximum number:', max_val)
    print('Sum of numbers:', total)

    return min_val, max_val, total

if __name__ == '__main__':
    demo_number_stats()
