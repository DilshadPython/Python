
num = input(' Please enter a number: ')

number = int(num)

if number % 2 == 0:
    print(' The number you entered is even')
elif number % 3 == 0 and number % 5 == 0:
    print(' The number you entered are also working with 3 and 5 is even')
else:
    print(' The number you enetered is odd.')
