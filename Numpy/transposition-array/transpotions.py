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

shape_array = np.arange(80).reshape((10,8))
print(shape_array)

print('\n')
print(shape_array.T)

print('\n')
# dot(a, b, out=None)¶
print('For 2-D arrays it is equivalent to matrix multiplication, and for 1-D\
		 arrays to inner product of vectors (without complex conjugation).\
		 For N dimensions it is a sum product over the last axis of a and the second-to-last of b:')
dot_array = np.dot(shape_array.T, shape_array)
print(dot_array)