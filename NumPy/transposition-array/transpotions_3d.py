import numpy as np 
'''
Parameters:	
a : array_like
	First argument.

b : array_like
	Second argument.

out : ndarray, optional
	  Output argument. This must have the exact kind that would be returned if it was not used. 
	  In particular, it must have the right type, must be C-contiguous, and its dtype must be 
	  the dtype that would be returned for dot(a,b). This is a performance feature. Therefore, 
	  if these conditions are not met, an exception is raised, instead of attempting to be flexible.

Returns: output : ndarray
		Returns the dot product of a and b. If a and b are both scalars or both 1-D arrays then a
		scalar is returned; otherwise an array is returned. If out is given, then it is returned.

Raises:	ValueError
	If the last dimension of a is not the same size as the second-to-last dimension of b.
'''

shape_3d_array = np.arange(80).reshape((10, 4, 2))
print(shape_3d_array)

print('\n======')
print('All ')
print(shape_3d_array.transpose((1, 0, 2)))

print('\n')

my_array = np.array([[2,4,6]])
print(my_array)
print('======')
new_array = my_array.swapaxes(0,1)
print('New array:\n', new_array)
