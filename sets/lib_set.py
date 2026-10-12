"""
Demonstrates set.update() and introspection of set attributes.
"""

def demo_set_update_and_dir():
    fruits = {'apples', 'oranges', 'cherry', 'bananas'}
    new_fruits = {'mango', 'pineapple'}

    fruits.update(new_fruits)
    print('Updated fruits set:', fruits)

    public_methods = [m for m in dir(fruits) if not m.startswith('_')]
    print('Set public methods count:', len(public_methods))

    return fruits, public_methods

if __name__ == '__main__':
    demo_set_update_and_dir()
