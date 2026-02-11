try:
    num = int(input("Enter a number: "))
    print(f'The number your enter is {num}')
except ValueError as e:
    print('You did not enter a number. You need to enter a number ', e)
