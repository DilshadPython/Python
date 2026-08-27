"""
Demonstrates introspection of list methods using built-in dir() and method usage.
"""

def demo_list_methods():
    names = ['Dilshad', 'Azad']
    
    # Retrieve built-in attributes and methods for list
    list_attributes = dir(names)
    print('Total attributes/methods on list:', len(list_attributes))
    print('Public methods:', [m for m in list_attributes if not m.startswith('_')])

    # Note: list objects do NOT have a split() method; split() belongs to str.
    print('\nNote: split() is a string method, not a list method.')
    return list_attributes

if __name__ == '__main__':
    demo_list_methods()
