'''
The comparasen between == and is in python
'''

names = ['Dilshad', 'Raffi', 'Tilly', 'Tom']

test = names

print('Test: ', test)

print('\n "is" expressions evaluate to True if two var point to the same object \n')

names is test

print('Names: ', names)

newlist = list(names)
print('Newlist: ', newlist)

print('\n "==" evaluate to True if the objects referred to by the var are equal \n')

print('That is correct: ', names == newlist)
print('names: ', names)

print('That is not true: ', names is newlist) 

print('Result', names)
