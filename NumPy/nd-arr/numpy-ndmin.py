import numpy as np

num_list4 = np.array([22,  77,   'a','b', 'Hello', 3], ndmin = 4)
print(num_list4)

print('####' * 14)

num_list3 = np.array([22,  77,   'a','b', 'Hello', 3], ndmin = 3)
print(num_list3)

print('####' * 14)

num_list2 = np.array([22,  77,   'a','b', 'Hello', 3], ndmin = 2)
print(num_list2)

print('####' * 14)

num_list = np.array([22,  77,   'a','b', 'Hello', 3], ndmin = 1)
print(num_list)
