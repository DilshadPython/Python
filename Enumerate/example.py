def main():
    n = int(input('Enter a n: '))

    for i in range(n):
        print(fly(i))

def fly(n):
    return '*' * n

if __name__ == '__main__':
    main()