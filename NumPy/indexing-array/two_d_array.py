import numpy as np

num_2_array = np.array(
    [[120, 110, 100, 90], [80, 70, 60, 50], [40, 30, 20, 10]])
print(num_2_array)
print('\n')

print('First column: ', num_2_array[0],
      'Second column: ', num_2_array[1],
      'Third column', num_2_array[2])

print('num_2_array[1][1] ', num_2_array[1][1])
print('num_2_array[2][0] ', num_2_array[2][0])
print('num_2_array[0][1] ', num_2_array[0][1])

print('\n')
print('num_2_array[:1,2:] ', num_2_array[:1, 2:])
print('num_2_array[:2,1:] ', num_2_array[:2, 1:])
