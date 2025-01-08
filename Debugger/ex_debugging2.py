
def add_num(num1, num2):
    sum = num1 + num2
    return sum

'''
third way to debug:
The next way to do debugging we import the file name to python shell
we create another def and called after if __name__ == '__main__'
 Debugger % python
Python 3.9.6 (default, Jun 29 2021, 06:20:32) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex_debugging2
>>> import pdb
>>> pdb.run('ex_debugging2.main()')
> <string>(1)<module>()->None
(Pdb) n
Enter number 1: 65
Enter number 2: 32
97
--Return--
> <string>(1)<module>()->None
'''

def main():
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    total = add_num(num1, num2)
    print(total)

if __name__ == '__main__':
    main()
