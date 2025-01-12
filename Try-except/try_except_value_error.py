try:
    num = int(input("Enter a number: "))
    print(f'The number your enter is {num}')
except ValueError:
    print('You did not enter a number. or you have not enter an integer')
