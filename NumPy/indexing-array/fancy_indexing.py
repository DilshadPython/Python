import numpy as np 

# Initialize different types of array
num_2d_array = np.zeros((7, 7))
print(num_2d_array)
print('\n')


num_2d_array_length = num_2d_array.shape[1]
print(num_2d_array_length)

print('\n')

for x in range(num_2d_array_length):
	num_2d_array[x] = 33

print(num_2d_array)

print('\n')
for x in range(num_2d_array_length):
	num_2d_array[x] = x

print(num_2d_array)