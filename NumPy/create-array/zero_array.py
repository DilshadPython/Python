import numpy as np


alist = [22, 17, 9, 18, 33, 81, 50]
np_list = np.array(alist)

print('First: ', first_list)

new_list = [21, 19, 4, 30, 66, 6, 17]

print('Second: ', new_list)

all_lists = [alist, new_list]

print('All: ', all_list)

#  Now we create matrix or 3 d array
three_d_array = np.array(all_list)

print('\n')
print('Below is two dimienstion')
print(three_d_array)

print('\nShow a shape:')
print(three_d_array.shape)

print('\nShow data type')
print(three_d_array.dtype)

print(np.zeros(15))
zero_array = np.zeros(11)

print(zero_array)
print('The data type of zero array is: ', zero_array.dtype)
