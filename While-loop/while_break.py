total = 0
number = 0
count = 0
average = 0.0


while True:
	print('Enter a number: ')
	number = float(input())

	if number == -1:
		break

	total = total + number
	count += 1
	print('Total is : ' + str(total))

average = total / count
print('Average :', str(average))