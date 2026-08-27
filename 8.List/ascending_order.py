"""
Demonstrates ascending and descending order sorting for numeric lists.
"""

def demo_sorting():
    numbers = [42, 12, 88, 3, 27, 99, 1]
    print('Original list:', numbers)

    # Built-in sorted() returns a new sorted list (O(N log N))
    asc_sorted = sorted(numbers)
    print('Ascending sorted (sorted()):', asc_sorted)

    desc_sorted = sorted(numbers, reverse=True)
    print('Descending sorted (sorted()):', desc_sorted)

    # In-place sort using .sort() method
    numbers.sort()
    print('Original after numbers.sort():', numbers)

    return asc_sorted, desc_sorted

if __name__ == '__main__':
    demo_sorting()
