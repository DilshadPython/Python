"""
Demonstrates adding elements via add() and extending sets via update().
"""

def demo_add_to_set():
    a = {81, 41, 11, 77}
    print('Initial set:', a)

    # add() inserts a single element (O(1) average complexity)
    a.add(55)
    print('After add(55):', a)

    a.add(105)
    print('After add(105):', a)

    # Adding duplicate element has no effect (sets contain unique elements)
    a.add(55)
    print('After re-adding 55:', a)

    # update() adds multiple elements from any iterable
    a.update([9, 0, -5, 4444])
    print('After update([9, 0, -5, 4444]):', a)

    return a

if __name__ == '__main__':
    demo_add_to_set()
