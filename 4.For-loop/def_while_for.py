def main():
    value = get_me_out()
    myfunc(value)


def get_me_out():
    while True:
        n = int(input('Please enter a number: '))
        if n > 0:
            break
    return n

def myfunc(num):
    for _ in range(num):
        print(f'{_} Welcome to Python')

if __name__ == '__main__':
    main()
