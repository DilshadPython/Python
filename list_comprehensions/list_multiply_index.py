"""
Demonstrates scalar multiplication and Cartesian product calculation via nested comprehensions.
"""

def demo_cartesian_product():
    vector = [2, 9, 4, -6, 1, 5.1, -7.9]

    # Multiply each element by 4
    scaled_vector = [4 * x for x in vector]
    print('Scaled vector (4 * x):', scaled_vector)

    list_a = [2, 4, 6]
    list_b = [1, 3, 5]

    # Cartesian Product: A x B = {(a, b) for a in A for b in B}
    cartesian_product = [(a, b) for a in list_a for b in list_b]
    print('Cartesian Product A x B:', cartesian_product)

    return scaled_vector, cartesian_product

if __name__ == '__main__':
    demo_cartesian_product()
