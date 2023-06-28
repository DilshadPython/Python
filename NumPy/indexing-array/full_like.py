import numpy as np

a = np.array(([2,4,6,8,10], [1,3,5,7,9]))
xx = np.full_like(a.shape, 4)
print(xx)

print()
bb = np.full_like(a, 9)
print(bb)

print()
cc = np.full(a.shape, 9)
print(cc)