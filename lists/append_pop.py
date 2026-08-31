"""
Demonstrates stack operations using list append() and pop() methods in Python.
"""

def demo_append_pop():
    # Initialize a empty or populated list acting as a LIFO stack
    items = ['apple', 'banana', 'cherry']
    print('Initial items:', items)

    # Append adds an item to the end of the list (O(1))
    items.append('orange')
    print('After append("orange"):', items)

    # Pop without arguments removes and returns the last item (O(1))
    last_item = items.pop()
    print(f'Popped last item: {last_item}')
    print('List after pop():', items)

    # Pop with index removes and returns item at specified index (O(N))
    first_item = items.pop(0)
    print(f'Popped index 0: {first_item}')
    print('List after pop(0):', items)

    return items

if __name__ == '__main__':
    demo_append_pop()
