while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input, the input is not integer")
    else:
        break

print(f'You have entered {number}')