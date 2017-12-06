'''
Set is unordered collection of unique elements.

'''

a = {81, 41, 11, 77}
print(a)

print('Add 55: ')
a.add(55)
print(a)
print('---------######-----------')

print(' Add 105: ')
a.add(105)
print(a)
print('----------xxxxxx----------')

print('Add 55: ')
a.add(55)
print(a)
print('----------xxxxxx----------')

print('Update the set: ')
a.update([9, 0, -5, 4444])
print(a)
# There are two type of func remove element(of set
# 1. remove() methods
# 2. discard() methods
print('----------____________----------')
print('Removed 11 : ')
a.remove(11)
print(a)
print('----------+++++++++----------')

print('Discard -5: ')
a.discard(-5)
print(a)

print('Copied the set list to another file: ')
print('----------********----------')
j = a.copy()
print('j = ', j)