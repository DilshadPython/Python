"""
Demonstrates list append, remove, nested lists, and negative indexing in Python.
"""

def demo_append_remove():
    # Primary list of grocery items (fixed spelling: Vegetable)
    first_list = ['Milk', 'Bread', 'Cheese', 'Vegetable']
    second_list = ['Bow and Arrow', 'Lantern', 'Wumpus B Gone']

    print('First list:', first_list)
    print('Second list:', second_list)
    print()

    # Nested list containing references to first_list and second_list
    my_shopping_lists = [first_list, second_list]
    print('My Shopping list (nested):', my_shopping_lists)
    print()

    # Append item to second list (O(1) complexity)
    second_list.append('Rope')
    print('Added Rope to second list:', second_list)
    print()

    # Remove item from second list (O(N) search and remove)
    second_list.remove('Wumpus B Gone')
    print('Removed Wumpus B Gone from second list:', second_list)
    print()

    print('Nested list after modifications:', my_shopping_lists)
    print('Last element of second list (index -1):', second_list[-1])
    print('Second to last element (index -2):', second_list[-2])
    return first_list, second_list, my_shopping_lists

if __name__ == '__main__':
    demo_append_remove()
