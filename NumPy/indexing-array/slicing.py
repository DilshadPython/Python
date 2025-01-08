import numpy as np

num_array = np.arange(10, 30)
print(num_array)
print('\n')

slice_in_array = num_array[0:8]
print(slice_in_array)

slice_in_array[:] = 55
print(slice_in_array)
print(num_array)

print('\n')
num_array_copy = num_array.copy()
print(num_array_copy)
