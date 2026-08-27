"""
Demonstrates performance and syntax of computing mathematical series via comprehensions.
"""

def demo_math_series():
    # Square calculation using list comprehension
    squares = [x**2 for x in range(1, 21)]
    print('First 20 squares:', squares)

    # Conditional mathematical filter: squares of multiples of 5
    squares_mult_5 = [x**2 for x in range(1, 21) if x % 5 == 0]
    print('Squares of multiples of 5:', squares_mult_5)

    return squares, squares_mult_5

if __name__ == '__main__':
    demo_math_series()
