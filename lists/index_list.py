"""
Demonstrates finding element positions using list.index() and error handling.
"""

def demo_index():
    items = ['apple', 'banana', 'cherry', 'banana', 'date']
    print('Items:', items)

    # Find index of first occurrence of 'banana'
    idx_banana = items.index('banana')
    print('Index of "banana":', idx_banana)

    # Find index within search range [start, end)
    idx_banana_2 = items.index('banana', 2)
    print('Index of "banana" starting from index 2:', idx_banana_2)

    # Handling missing item safely
    search_item = 'fig'
    if search_item in items:
        print('Index of fig:', items.index(search_item))
    else:
        print(f'"{search_item}" not found in list.')

    return idx_banana, idx_banana_2

if __name__ == '__main__':
    demo_index()
