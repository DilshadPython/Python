def main():
    n = int(input('Enter a n: '))

    for i in range(n):
        print(fly(i))


def fly(n):
    return ' <3 ' * n

if __name__ == '__main__':
    main()
