"""
Demonstrates nested tuple unpacking syntax.
"""

def demo_nested_unpacking():
    nested_tuple = (12, 11, 10, 9, (8, 7, 6, 5, (4, 3, 2, 1)))

    (a, b, c, d, (e, f, g, h, (i, j, k, l))) = nested_tuple

    print('Unpacked a:', a)
    print('Unpacked e:', e)
    print('Unpacked i:', i)
    print('Unpacked l:', l)

    return a, e, i, l

if __name__ == '__main__':
    demo_nested_unpacking()
