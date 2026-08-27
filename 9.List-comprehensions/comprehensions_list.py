"""
Demonstrates 2D matrix column extraction using list comprehensions.
"""

def demo_matrix_column_extraction():
    row_a = ['s', 'i', 'p']
    row_b = ['k', 'a', 'g']
    row_c = ['u', 'o', 'd']

    matrix = [row_a, row_b, row_c]

    # Extract first column (index 0) from each row
    first_column = [row[0] for row in matrix]
    print('First column [row[0]]:', first_column)

    # Extract third column (index 2) from each row
    third_column = [row[2] for row in matrix]
    print('Third column [row[2]]:', third_column)

    nested_list = [1, 3, [9, 6]]
    element = nested_list[2][1]
    print('Nested element access [2][1]:', element)

    return first_column, third_column, element

if __name__ == '__main__':
    demo_matrix_column_extraction()
