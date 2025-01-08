import numpy as np

# create 3 d array
txt = np.array([[['aa', 'ss'], ['oo', 'xx'], ['bb', 'uu']]])

print(txt)
print('\n#############')
# first list second ele aa
print(txt[0, 1, 1])

print('\n#############')
print(txt[0, 2, 1])

print('\n#############')

print(txt[:, 1, :])

print('\n#############\n')

txt[:, 1, :] = [['yy', 'tt']]
print(txt[:, 1, :])

alpha = np.array([[['aa', 'gg'], ['oo', 'ff']],
                  [['bb', 'mm'], ['cc', 'nn']],
                  [['dd', 'vv'], ['ee', 'hh']]])

print(alpha)
print('\n#############')

print(alpha[1, 1, 1])
print('\n#############')

print(alpha[2, 1, 0])