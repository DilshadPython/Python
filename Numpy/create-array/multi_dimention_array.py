import numpy as np

multi = np.ones([10, 10])

print(multi)

print('=============================================')
empt = np.empty(5)

print(empt)

print('=============================================')
empt_two = np.empty([8, 8])
print(empt_two)

print('=============================================')
print('Identity matrix')
print(np.eye(5))


numpylib = dir(np) 
print(numpylib)