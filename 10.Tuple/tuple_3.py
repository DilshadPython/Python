"""
Demonstrates parenthesis-free tuple packing and single element syntax.
"""

def demo_parenthesis_free_tuples():
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    # Tuple created without parentheses via comma separation
    tup3 = 'a', 'b', 'c', 'd'

    single_val_tuple = ('solo',)

    print('tup3 type:', type(tup3))
    print('single_val_tuple:', single_val_tuple)

    return type(tup3), single_val_tuple

if __name__ == '__main__':
    demo_parenthesis_free_tuples()
