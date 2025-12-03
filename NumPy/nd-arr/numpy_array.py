import numpy as np

np.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)

# Object: any object exposing the array interface method returns an array, or any (netsted) sequence.

num_obj = np.array([1, 2, 3])
print(num_obj)

print('###' * 14)

str_obj = np.array(['a', 'b', 'c'])
print(str_obj)
print('***' * 14)

# list inside list
example_objects = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10]
    ]
)
print('Print two num in one list')
print(example_objects)

print('====' * 14)

example_obj = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Print three num in one list')
print(example_obj)

print('#####' * 14)

example_obj = np.array([[1, 2, 1], [3, 3, 5], [4, 5, 6], [7, 8, 9], ['a', 'b', 'f'], ['c', 'd', 'e']])
print('Print three and more num in one list')
print(example_obj)

mult_obj = np.array(
    [
        [
            [1, 2],
            [3, 4],
            [5, 6],
        ],
        [
            [7, 8],
            [9, 10],
            [11, 12],
        ],
        [
            [14, 12],
            [13, 41],
            [15, 66],
        ],
        [
            [17, 18],
            [19, 0],
            [21, 13],
        ]
    ]
)

print(mult_obj)