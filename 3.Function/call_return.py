def main():
    num = int(input('Enter a number, '))
    print('The sequre of num, ', square(num))
    num1 = int(input('Enter second nummber, '))
    print('The power of second number is, ', pow(num1, 3))


# to make it working we create another func named square
def square(n):
    return n * n


main()
