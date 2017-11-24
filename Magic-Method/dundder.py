'''
https://docs.python.org/3.5/reference/datamodel.html
Go to 3.3.7. Emulating numeric types
'''
print(int.__add__(33, 17))

print('\n###########\n')

print(float.__add__(21.098, 87.83))

print('\n###########\n')

print(str.__add__('A', 'B'))

print('\n###########\n')

print(float.__sub__(21.098, 87.83))

print('\n###########\n')

print(float.__mul__(21.098, 87.83))

print('\n###########\n')

print(int.__divmod__(221, 87))

print('\n###########\n')

print(len('Hellow world'))
# or
print('Hellow world'.__len__())
