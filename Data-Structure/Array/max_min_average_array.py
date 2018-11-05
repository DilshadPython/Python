# theindex 0  1	 2  3	4	5  6   7   8  9   10
numbers = [1, 5, 7, -2, 10, 17, 27, 39, 8, 11, -3]

print()
print('We will display all items except the last 3 index: ')
print(numbers[0:-3])


print()
print('We will search for the largest numbers, this is call liner search:')
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    elif num < minimum:
        minimum = num


print('The maximum number is: ', maximum)
print()
print('The minimum number is: ', minimum)
