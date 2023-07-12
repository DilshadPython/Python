floors = 12

floor = input('Enter your floor number between 1 - 12 : ')

for floor in floors:
    num = int(floor) + 1
    if num == floor:
        print('You reached to your floor number, ', floor)
