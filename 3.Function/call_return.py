def main():
    num = int(input('Enter a number, '))
    print('The sequre of num, ', square(num))
    num1 = int(input('Enter another num1, '))
    print('The power of num1, ', pow(num1, 3))


# to make it working we create another func named square
def square(n):
    return n * n


main()
