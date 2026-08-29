
for number in (2, 4, 6, 3, 7, 9, 1, 5, 8, 10, 15, 17, 21):
    print(number, end=' ')

print('\n#################################################')
# another way to go throw the name of list
numbers = (22, 14, 6, 3, 71, 9, 1, 5, 8, 18, 5, 17, 11)

for number in numbers:
    print(number, end=' ')

print('\n#################################################')

names = ('Paris', 'London', 'Berlin', 'Tokyo', 'Bruccel', 'Roma')
for name in names:
    print(name, end=' ')

print('\n#################################################')
total = 0
for number in (1, 2, 4, 6, 3, 7, 9, 1, 5, 8, 10, 15):
    print(number, end=' ')
    print()
    total = total + number

print('Total of all are:', total)

longestname = 0
for x in range(1, len(names)):
    if len(names[x]) > len(names[longestname]):
        longestname = x
print('The longest name of the city is :', names[longestname])
