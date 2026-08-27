"""
Demonstrates passing tuple elements to functions using single asterisk * unpacking.
"""

def multiply_add(a, b, c):
    return a + b * c

def demo_function_unpacking():
    items = (4, 3, 7)
    res = multiply_add(*items)
    print('Result of multiply_add(*items):', res)
    return res

if __name__ == '__main__':
    demo_function_unpacking()
