'''
If you using PyCharm there is a debug small icon next to run icon show the issues what is wrong
Down to the shell you have debug and Console
'''
def add_num(num1, num2):
    sum = num1 + num2
    return sum

'''
fourth way to debug:
"/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 53537 --file /Users/dilshadabdulla/Dev/Python/Debugger/ex_debugging3.py
Connected to pydev debugger (build 212.4746.96)
Enter number 1: >? 3
Enter number 2: >? 4
/Users/da/.virtualenvs/basicenv/bin/python "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py" --multiproc --qt-support=auto --client 127.0.0.1 --port 53528 --file /Users/dilshadabdulla/Dev/Python/Debugger/ex_debugging3.py
Connected to pydev debugger (build 212.4746.96)
Enter number 1: Enter number 2: 34
'''

def main():
    num1 = input('Enter number 1: ')
    num2 = input('Enter number 2: ')
    total = add_num(num1, num2)
    print(total)

if __name__ == '__main__':
    main()
