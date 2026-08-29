"""
Demonstrates difference between append() and extend() on Python lists.
"""

def demo_extend():
    list_a = [1, 2, 3]
    list_b = [4, 5]

    # append adds the argument as a SINGLE nested element
    appended = list_a.copy()
    appended.append(list_b)
    print('Result of append([4, 5]):', appended)

    # extend unpacks elements from the iterable argument
    extended = list_a.copy()
    extended.extend(list_b)
    print('Result of extend([4, 5]):', extended)

    return appended, extended

if __name__ == '__main__':
    demo_extend()
