# first way to debug:

def add_num(num1, num2):
    sum = num1 + num2
    return sum

if __name__ == '__main__':
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    total = add_num(num1, num2)
    print(total)