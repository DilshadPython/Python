def main():
    n = int(input('Enter a n: '))
    for x in range(n):
        print(fly(x))


def fly(n):
    flock = []
    for i in range(n):
        flock.append('<3' * i)
    return flock

if __name__ == '__main__':
    main()
