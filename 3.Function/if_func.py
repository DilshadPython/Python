
def main():
    num = int(input('Enter a number: '))
    if is_even(num):
        print('Even number')
    else:
        print('This is odd number')


def is_even(n):
    return(n % 2 == 0)

# or

def is_even(m):
    return True if m % 2 == 0 else False

main()
