names = ['Tom', 'Chris', 'Julia', 'Rob', 'Claudio', 'Sarah', 'Amanda']
numbers = [1, 2, 3, 4, 5, 6, 7]

print('###########################')
for name in names:
    for index, num in enumerate(numbers):
        print(index, name, num)
