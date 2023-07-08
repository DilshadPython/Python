import numpy as np

num_2d_array = np.zeros((14, 14))
print(num_2d_array)
print('\n')

num_2d_array_length = num_2d_array.shape[1]

# display the shap
print(num_2d_array_length, ' << shape')

for x in range(num_2d_array_length):
    num_2d_array[x] = x

print('\n')
print(num_2d_array[[3, 6, 9, 12]])

print('\n')
print(num_2d_array[[8, 6, 4, 0]])
