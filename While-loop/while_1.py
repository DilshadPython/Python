'''
True = 1
False = 0
'''

# keyword = str('exit')
while 1:
    print('Please enter between 1 - 10: ')
    name = input('\nEnter exit: ')
    if name == 1:
        # doing a loop until continue but it will get stop when user enter 1
        print('Correct')
        break
    else:
        print('\nThe number is not exit, please try again')
        continue
