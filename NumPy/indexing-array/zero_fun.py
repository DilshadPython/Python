import numpy as np

first_2_by_5 = np.zeros((2, 5))
print(first_2_by_5)

print()

second_7_by_3 = np.zeros((7, 3))
print(second_7_by_3)

print()
third_shape = np.zeros(((4, 4)))
print(third_shape)

print()
third_shape[:] = 5
print(third_shape)

print()
xx = np.zeros((2, 3, 4, 6))
print(xx)
