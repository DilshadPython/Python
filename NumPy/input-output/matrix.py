import numpy as np


nums = np.array([[2,4,6,8,10], [3,6,9,12,15]])
print('Matrix: ', nums)

# delimiter = means saperate them by ,
text_file = np.savetxt('numstext.txt', nums, delimiter=',')
new_text = np.loadtxt('numstext.txt', delimiter=',')

print(new_text)

