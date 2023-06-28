import numpy as np


print('=============================================')
print('arange([start,] stop[, step,], dtype=None)')
print(np.arange(5))

print('\n==================================================')
# start from 7
# stoped at 77
# steps by 3
print('Start from 7 and add 3 and so on until reach to 77')
text = np.arange(7, 77, 3)
print(text)

print('\n=======================================================')
print('start from 101, minuse 5 ending at 35')
decrease = np.arange(101, 35, -5)
print(decrease)
