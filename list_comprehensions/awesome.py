"""
Demonstrates basic list comprehensions with modulo conditional filtering.
"""

def demo_awesome_comp():
    # Syntax pattern: [expression for item in iterable if condition]
    # Filter numbers divisible by 3 (not x % 3 evaluates to True when x % 3 == 0)
    div_by_three = [x for x in range(30) if not (x % 3)]
    print('Numbers divisible by 3 (0-29):', div_by_three)
    return div_by_three

if __name__ == '__main__':
    demo_awesome_comp()
