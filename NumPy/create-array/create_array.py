import numpy as np

list_num = [22, 17, 9, 18, 33, 81, 50]

first_list = np.array(list_num)

print('First: ', first_list)

second_list = [21, 19, 4, 30, 66, 6, 17]

print('Second: ', second_list)

all_list = [first_list, second_list]

print('All: ', all_list)

#  Now we create matrix or 3 d array
three_d_array = np.array(all_list)

print('\n')
print('Below is two dimienstion')
print(three_d_array)

print('\nNow we try to display the shape what is look like')
print(three_d_array.shape)

print('\nNow display the data type')
print(three_d_array.dtype)
