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
print('Two dimienstions')
print(three_d_array)

print('\nNow try to show a shape:')
print(three_d_array.shape)

print('\nShow data-type:')
print(three_d_array.dtype)

tuple_list = (17, 9, 76, 1, 2, 3, 4, 17, 14, 5, 8, 54, 4, 12, 3, 17, 1, 9, 17)
new_array = np.array(tuple_list)
print(new_array)
# now we changing all

# In set all duplication will removed not display
print("\nIn set all duplication will removed not display")
set_list = {17, 9, 76, 1, 2, 3, 9, 4, 5, 8, 54, 4, 12, 3, 17, 1, 22}
myset = np.array(set_list)
print(myset)
