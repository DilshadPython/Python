def main():
    x = input("Enter a x: ")
    print('The square is ', square(x))

def square(x):
    # for testing we change * to +
    return x * x

if __name__ == '__main__':
    main()