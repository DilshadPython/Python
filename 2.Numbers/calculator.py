print('Small calculation op means *, +, -, /, ^, //')


def main(num1=int(input("Enter num1: ")), op=input('Enter op: '), num2=int(input("Enter num2: "))):
    result = None
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '^':
        print(num1 ** num2)
    elif op == '%':
        print(num1 % num2)
    elif op == '//':
        print(num1 // num2)

if __name__ == '__main__':
    main()
