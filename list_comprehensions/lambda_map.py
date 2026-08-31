"""
Demonstrates functional map() + lambda vs Pythonic list comprehensions.
"""

def demo_map_vs_comprehension():
    numbers = [1, 3, 5, 7, 9, 11]

    # Functional approach using map() and lambda
    doubled_map = list(map(lambda x: x * 2, numbers))
    squared_map = list(map(lambda x: x * x, numbers))

    # Pythonic list comprehension alternative
    doubled_comp = [x * 2 for x in numbers]
    squared_comp = [x * x for x in numbers]

    # Filter even numbers using list comprehension
    evens_comp = [x for x in range(30) if x % 2 == 0]

    print('Doubled (map):', doubled_map)
    print('Doubled (comp):', doubled_comp)
    print('Evens (comp):', evens_comp[:5])

    return doubled_comp, squared_comp, evens_comp

if __name__ == '__main__':
    demo_map_vs_comprehension()
