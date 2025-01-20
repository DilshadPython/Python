def main():
    number = int(input("Enter a number: "))
    print('Number square is ', square(number))

def square(number):
    return number * number

if __name__ == '__main__':
    main()