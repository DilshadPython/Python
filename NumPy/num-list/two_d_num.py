import numpy as np

a = np.array([[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]])

print(a)

# get shape
shape_a = a.shape
print(shape_a, ' << shape of a')
# get size
size_a = a.itemsize
print(size_a, ' << size of a')
# get ndim
ndim_a = a.ndim
print(ndim_a, ' << number of dimention of a')
# get dtype
type_a = a.dtype
print(type_a, ' << data-type of a')

# get total size using dtype
ntype_a = a.nbytes
print(ntype_a, ' << total size of a')

print(a[0, 4])  # first list colm 3 which is 10
print(a[1, 2])  # secnd list colm 2 which is 5
