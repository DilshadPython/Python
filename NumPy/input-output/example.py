import numpy as np


nums = np.arange(8)
print('Before saved@ ', nums)

np.save('numssave', nums)

nums = np.arange(17)
print('Overwritten: ', nums)

print('\n')
bring_back = np.load('numssave.npy')
print('first file before save: ', bring_back)

nums = bring_back   
print(nums)

save_file = np.savez('raffi.npz', a=nums, b=bring_back)
archive_arr = np.load('raffi.npz')

print('A file: ', archive_arr['a'])
print('B file: ', archive_arr['b'])


