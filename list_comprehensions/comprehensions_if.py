"""
Demonstrates list comprehension with even number calculations and squarings.
"""

def demo_even_squares():
    # Compute squares of even numbers in range 0-23
    even_squares = [num * num for num in range(24) if not (num % 2)]
    print('Squares of even numbers < 24:', even_squares)
    return even_squares

if __name__ == '__main__':
    demo_even_squares()
