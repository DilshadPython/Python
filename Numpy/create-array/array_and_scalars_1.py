from __future__ import division
import numpy as np


z = 5 / 2
print(z)

print('==========================')

f_array = np.array([[1, 16, 4, 30, 6, 10, 12], [20, 5, 9, 18, 3, 7, 14]])

print(f_array)

print('Multiply each array to each other')
result = f_array * f_array

print(result)

print('==========================')

sub = f_array - f_array
print(sub)

print('==========================')

test = 1 / f_array
print(test)
print('==========================')

my_power = f_array ** 3
print(my_power)
