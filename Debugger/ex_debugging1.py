import pdb
def add_num(num1, num2):
    sum = num1 + num2
    return sum

'''
second way to debug:
da@Dilshads-MBP Debugger % python ex_debugging1.py
Enter number 1: 4
Enter number 2: 3
> /Users/da/Dev/Python/Debugger/ex_debugging1.py(10)<module>()
-> total = add_num(num1, num2)
(Pdb) n
> /Users/da/Dev/Python/Debugger/ex_debugging1.py(11)<module>()
-> print(total)
(Pdb) whatis total
<class 'int'>
'''
if __name__ == '__main__':
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    pdb.set_trace()
    total = add_num(num1, num2)
    print(total)