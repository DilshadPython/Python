from __future__ import division
import numpy as np


z = 5 / 2
print(z)

print()

f_array = np.array([[1, 16, 4, 30, 6, 10, 12],
                    [20, 5, 9, 18, 3, 7, 14]])

print(f_array)

print('\nMultiply each array to each other')
result = f_array * f_array

print(result)

print('\n============= sub =============')

sub = f_array[0] - f_array[1]
print(sub)

print('\n subscribe from itself')
sub = f_array - f_array
print(sub)

print('\n============ division =========')

test = 1 / f_array
print(test)

print('\n============ power ============')

my_power = f_array ** 3
print(my_power)
