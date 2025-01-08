from itertools import product


def main():
    num = int(input('Enter a number, '))
    print('The sequre of num, ', square(num))
    num1 = int(input('Enter second nummber, '))
    print('The power of second number is, ', pow(num1, 3))
    num2 = int(input('Enter a third number, ', ))
    print('The power of num2 is, ', power(num2))


# to make it working we create another func named square
def square(n):
    return n * n

def power(n):
    return n ** 3


main()
