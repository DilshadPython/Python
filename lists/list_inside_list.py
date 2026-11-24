"""
Demonstrates multi-dimensional (nested) lists and matrix index access.
"""

def demo_nested_lists():
    row_a = ['s', 'i', 'p']
    row_b = ['k', 'a', 'g']
    row_c = ['u', 'o', 'd']

    matrix = [row_a, row_b, row_c]

    print('Row A:', row_a)
    print('Row B:', row_b)
    print('Row C:', row_c)
    print('Matrix (List of lists):', matrix)
    print()

    # Access element at row 1, column 2 ('g')
    element = matrix[1][2]
    print(f'Element at matrix[1][2]: {element}')

    return matrix, element

if __name__ == '__main__':
    demo_nested_lists()
