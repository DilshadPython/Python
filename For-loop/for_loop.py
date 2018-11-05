names = ['Tom', 'Chris', 'Julia', 'Rob', 'Claudio', 'Sarah', 'Amanda']

for name in names:
    print(name)


print('###########################')
for name in names:
    if name == 'Rob':
        print('\n The name found')
        break
    print(name)


print('###########################')
for name in names:
    if name == 'Rob':
        print('\n - The name found\n')
        continue
    print(name)

numbers = [1, 2, 3, 4, 5, 6, 7]
print('###########################')
for name in names:
    for num in numbers:
        print(name, num)
