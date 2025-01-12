try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input, the input is not integer")
else:
    # if we don't use else put print in the begining on the new line display NameError
    print(f'You have entered {number}')