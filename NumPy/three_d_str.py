import numpy as np


a = np.array([['a', 'b', 'c', 'd', 'e'],
				['ab', 'cd', 'ef','gh', 'ij'],
				['kl', 'mn', 'op', 'qr', 'st']])

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

print(a[0, 4]) 
print(a[1, 2]) 
print(a[2, 1])

print('###')
print(a[0, -1]) 
print(a[1, -3]) 
print(a[2, -4])

print('###')
print(a[1, -3]) 
print(a[0, -5]) 
print(a[2, -2])