import sys


list_example = [1, 2, 5, 8, 12, 9, 24, 32.25, 17]

tuple_example = (1, 2, 5, 8, 12, 9, 24, 32.25, 17)

print('List size: ', sys.getsizeof(list_example))
print('Tuple size: ', sys.getsizeof(tuple_example))

import timeit


time_create_list = timeit.timeit(stmt="[2, 4, 5, 6, 7]", number=1000000)
time_create_tuple = timeit.timeit(stmt='(2, 4, 5, 6, 7)', number=1000000)

print('List time: ', time_create_list)
print('Tuple time: ', time_create_tuple)
