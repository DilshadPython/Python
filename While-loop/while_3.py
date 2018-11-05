print('Please enter a number that the reminder will be 0: ')

while True:
    response = input()
    if int(response) % 7 == 0:
        print('Well done 49 % 7 == 0 : ')
        break
    else:
        print('The number not remind 0 please continue.')
        continue
