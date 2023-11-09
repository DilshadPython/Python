cars = ['Audi', 'Fiat', 'Alfa Romie', 'Porsh', 'Volvo']

for x in range(0, 5):
    if cars[x] == 'Porsh':
        print(f'The {cars[x]} already exists')
    else:
        print('Not found')

print('###########################')

for x in range(len(cars)):
    if cars[x] == 'Fiat':
        print(f'The {cars[x]} already exists')
    else:
        print('Not found')
