"""
Demonstrates tuple iteration and non-destructive concatenation.
"""

def demo_tuple_iteration():
    a = ('England', 'USA', 'France', 'Germany', 'Spain', 24, -10)
    print('Original tuple:', a)

    # Iteration
    elements = [item for item in a]

    # Non-destructive concatenation
    expanded = a + (0, 221.364, 246e5)
    print('Expanded tuple:', expanded)

    # Original remains unmodified due to immutability
    print('Original tuple after expansion intact:', a)

    return elements, expanded

if __name__ == '__main__':
    demo_tuple_iteration()
