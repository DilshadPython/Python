"""
Demonstrates clear() method and union operations on mathematical sets.
"""

def demo_set_clear_math():
    elements = set(['hello', 23, 'A', 2.36, 'Hello world'])
    elements.clear()
    print('Set after clear():', elements)

    odds = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21}
    evens = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22}

    combined_numbers = odds.union(evens)
    print('Combined odds and evens count:', len(combined_numbers))

    return elements, combined_numbers

if __name__ == '__main__':
    demo_set_clear_math()
