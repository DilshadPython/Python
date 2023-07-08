print('Small calculation op means *, +, -, /, ^, //')


def call(num1=int(input("Enter num1: ")), op=input('Enter op: '), num2=int(input("Enter num2: "))):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    elif op == '^':
        result = num1 ** num2
    elif op == '%':
        result = num1 % num2
    elif op == '//':
        result = num1 // num2

    return print(result)


call()
