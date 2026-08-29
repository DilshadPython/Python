names = {'Alan': 23, 'Sara': 30, 'Tom': 28, 'Raechel': 27, 'Anja': 25}

print(names.keys())
print(names.values())

print('\n=========================================')
print('for keys in names:')
for key in names:
    print(key, end=' ')

print('\n=========================================\n')
print('for name in names.keys():')
for name in names.keys():
    print(name)

print('\n=========================================\n')
print('for name in names.values():')
for age in names.values():
    print(age, end=' ')

print('\n=========================================\n')
print('for name in names.keys()')
for key in names.keys():
    print(key, ' and his age is', names[key])
