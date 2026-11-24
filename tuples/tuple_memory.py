"""
Demonstrates memory size efficiency and creation speed benchmarks of tuples vs lists.
"""

import sys
import timeit

def compare_tuple_vs_list():
    list_example = [1, 2, 5, 8, 12, 9, 24, 32.25, 17]
    tuple_example = (1, 2, 5, 8, 12, 9, 24, 32.25, 17)

    list_size = sys.getsizeof(list_example)
    tuple_size = sys.getsizeof(tuple_example)

    print(f'List memory size: {list_size} bytes')
    print(f'Tuple memory size: {tuple_size} bytes')

    time_list = timeit.timeit(stmt="[2, 4, 5, 6, 7]", number=100000)
    time_tuple = timeit.timeit(stmt="(2, 4, 5, 6, 7)", number=100000)

    print(f'Creation time (100k ops) - List: {time_list:.5f}s, Tuple: {time_tuple:.5f}s')

    return list_size, tuple_size, time_list, time_tuple

if __name__ == '__main__':
    compare_tuple_vs_list()
