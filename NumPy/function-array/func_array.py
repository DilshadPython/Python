# universal array functions
import numpy as np 
'''
numpy.exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, s
ubok=True[, signature, extobj]) = <ufunc 'exp'>¶
Calculate the exponential of all elements in the input array.

Parameters:	x : array_like
		Input values.
		out : ndarray, None, or tuple of ndarray and None, optional
		A location into which the result is stored. If provided, it must have a shape that the 
		inputs broadcast to. If not provided or None, a freshly-allocated array is returned. 
		A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

where : array_like, optional
	Values of True indicate to calculate the ufunc at that position, values of False indicate 
	to leave the value in the output alone.

	**kwargs
	For other keyword-only arguments, see the ufunc docs.
Returns: out : ndarray
	Output array, element-wise exponential of x.
'''

my_array = np.arange(24)
print(my_array)

print('\nSquare root')
new_array = np.sqrt(my_array)
print(new_array)

print('\nPower')
pow_array = np.exp(my_array)
print(pow_array)

## random
print('=======================================================================')
print('Randon')
x = np.random.randn(10)
print(x)

print('=======================================================================')
print('Randon')
y = np.random.randn(10)
print(y)

# Binary functions
print('\n')
result = np.add(x,y)
print(result)

print('\nMaximum')
maxim = np.maximum(x,y)
print(maxim)

print('\nMinmun')
mini = np.minimum(x,y)
print(mini)