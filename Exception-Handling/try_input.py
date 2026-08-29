num = input(' Please enter a number: ')
try:
    is_value = int(num)
except:
    is_value = -1

if is_value > 0:
    print('Correct number entered.')
else:
    print('You have not entered a number')
