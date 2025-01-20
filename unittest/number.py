def main():
    number = int(input("Enter a number: "))
    print('Number square is ', square(number))

def square(x):
    # for testing we change * to +
    return x + x

if __name__ == '__main__':
    main()