"""
Demonstrates inserting elements into specified list positions using insert().
"""

def demo_insert():
    numbers = [1, 2, 4, 5]
    print('Original:', numbers)

    # Insert number 3 at index 2
    numbers.insert(2, 3)
    print('After insert(2, 3):', numbers)

    # Insert at beginning
    numbers.insert(0, 0)
    print('After insert(0, 0):', numbers)

    return numbers

if __name__ == '__main__':
    demo_insert()
