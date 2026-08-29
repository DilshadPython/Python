while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input, the input is not integer")

print(f'You have entered {number}')