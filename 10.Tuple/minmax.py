"""
Demonstrates calculating minimum and maximum values from tuples and lists.
"""

def minmax(numbers):
    return min(numbers), max(numbers)

def demo_minmax():
    num_tuple = (11, 25, 1, 67, -9, 99, 654, 35, 7, 8, 56)
    lower, upper = minmax(num_tuple)

    print('Tuple numbers:', num_tuple)
    print('Lowest number:', lower)
    print('Highest number:', upper)

    num_list = [11, 25, 1, 67, -9, 99, 654, -7, 35, 7, 8, 56, 715]
    lst_lower, lst_upper = minmax(num_list)
    print('\nList lowest:', lst_lower, 'List highest:', lst_upper)

    return lower, upper, lst_lower, lst_upper

if __name__ == '__main__':
    demo_minmax()
