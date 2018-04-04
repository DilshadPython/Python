import random 

# theindex 0  1	 2  3	4	5  6   7   8  9
numbers = [1, 5, 7, 2, 10, 17, 27, 39, 8, 11]

print('We show the index 4 in the above list: ')
print(numbers[4])

print()
print(numbers)
print()

# now we are update the index 3 which is number 2 changed 
numbers[3] = 88
print('We have updated index 3 which is number 2 changed to 88')
print(numbers)

print()
numbers[5] = 'Dilshad'
print(numbers)

print()
for num in numbers:
	print(num)

print()
print('We change the search in the list using range: ')
for num in range(len(numbers)):
	print(num)

print()
print('We change the search in the list using range but this time display the updated index 5: ')
for num in range(len(numbers)):
	print(numbers[num])

print()
print('We will display only 5 items until index 4: ')
print(numbers[0:4])


# print()
# print(numbers)
# print('How to randomise the Array: ')
# for num in numbers:
# 	num = random.random()
# 	print(num)
