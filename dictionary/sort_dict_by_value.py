"""
Demonstrates sorting dictionary entries by value using operator.itemgetter and lambda.
"""

import operator

def demo_sort_by_value():
    text = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}

    # Sorting using lambda
    sorted_lambda = sorted(text.items(), key=lambda x: x[1])

    # Sorting using operator.itemgetter (faster C implementation)
    sorted_itemgetter = sorted(text.items(), key=operator.itemgetter(1))

    print('Sorted via lambda:', sorted_lambda)
    print('Sorted via itemgetter:', sorted_itemgetter)

    return sorted_lambda, sorted_itemgetter

if __name__ == '__main__':
    demo_sort_by_value()
