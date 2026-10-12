"""
Demonstrates sorted() function applied to immutable tuples and strings.
"""

def demo_sorted_immutable():
    numbers_tuple = (8, 5, 3, 1, 6, 7, 10, 2, 10, 4, 9)
    print('Original tuple:', numbers_tuple)

    # sorted() takes tuple iterable and returns a sorted list
    sorted_num_list = sorted(numbers_tuple)
    print('Sorted tuple returned as list:', sorted_num_list)
    print('Original tuple intact:', numbers_tuple)

    # Sorting a string sorts characters by ASCII/Unicode value (fixed typo: Manchester)
    sorted_char_list = sorted('Manchester United')
    print('\nSorted string characters:', sorted_char_list)

    return sorted_num_list, sorted_char_list

if __name__ == '__main__':
    demo_sorted_immutable()
