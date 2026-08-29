def main():
    myfunc(num=int(input('Please enter a number: ')))

def myfunc(num):
    for _ in range(num):
        print(f'{_} Welcome to Python')

if __name__ == '__main__':
    main()
