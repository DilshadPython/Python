import numpy as np 

num_array = np.arange(20, 40)
print(num_array)
print('\n')

print('The index 6 in the array is: ', num_array[6])
print('The index 3 in the array is: ', num_array[3])
print('The index 17 in the array is: ', num_array[17])

print('\n')
print(num_array[2:9])
print(num_array[0:11])

print('\n')
print('Set all the value from 25 to 30 = 70: ')
num_array[6:11] = 70

print(num_array[6:11])
print(num_array)

print('\n')
print('Set all the value from 33 to 39 = "Dilshad": ')
num_array[0:5] = 1010
print(num_array[0:5])
print(num_array)
