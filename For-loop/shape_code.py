rows = 8

for x in range(0, rows):
    for y in range(rows - 1, x, -1):
        print(y, '', end='')
    for i in range(x):
        print('  ', end='')
    for j in range(x + 1, rows):
        print(j, '', end='')
    print('\n')
