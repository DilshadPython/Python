"""
Demonstrates removing items via remove(), discard(), and pop().
"""

def demo_remove_methods():
    fruits = {'apples', 'oranges', 'cherry', 'bananas'}
    print('Initial set:', fruits)

    # remove() raises KeyError if element missing
    fruits.remove('oranges')
    print('After remove("oranges"):', fruits)

    # discard() silently succeeds if element missing
    fruits.discard('bananas')
    fruits.discard('non_existent_fruit')
    print('After discard("bananas"):', fruits)

    fruits.add('pineapple')
    
    # pop() removes and returns an arbitrary element from set
    popped_item = fruits.pop()
    print(f'Popped item: {popped_item}')
    print('Set after pop():', fruits)

    return fruits, popped_item

if __name__ == '__main__':
    demo_remove_methods()
