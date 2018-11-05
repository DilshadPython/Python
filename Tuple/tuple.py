'''
Tupe is immutable can not been change
'''

tup = ('England', 24, 'USA', 'France', 24,
       'Germany', 'Spain', 24, -10, 'Italy', 16, 24)

print(tup)

print
print('Using index')
print('France is index: ', tup.index('France'))
print('Spain is index: ', tup.index('Spain'))
print('The value -10 is index: ', tup.index(-10))

print('################')
print
print('The number 24 has been repeated ', tup.count(24))
print('The France has been repeated ', tup.count('France'))
