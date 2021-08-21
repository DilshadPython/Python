# Python Debugger: 
	- Python is a built-in model help you to debug your codes example like print() use in the code
    - When you install python the debugger is installed pdb
	- Set break points in the code where you can:
		. Examine attribuites / variables
		. Step foward line by line
		. Show code as it executes

# Find all commands running with pdb()
- Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

# The most recent or used command is used with pdb are:
- next or type n
- step or type s
- continue or type c
  Example how to use:
- (Pdb) help next
n(ext)
        Continue execution until the next line in the current function
        is reached or it returns.

# Explain ex_debugging.py 
# To run the file python -m pdb ex_debugging.py
'''
Please read to this comments to understand
When we run this file the results is 34 instead of 7, why this happen?
Debugger % python -m pdb ex_debugging.py 
> /Users//Dev/Python/Debugger/ex_debugging.py(2)<module>()
-> def add_num(num1, num2):
(Pdb) 
Now we have to find out all commands we can use or rung with pdb by enter help in front of (pdb) help:
-   To debug we will start following:
(Pdb) help next
n(ext)
        Continue execution until the next line in the current function
        is reached or it returns.
-   After this we have to find out where the program started using (pdb) where:
(Pdb) where
  /usr/local/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/bdb.py(580)run()
-> exec(cmd, globals, locals)
  <string>(1)<module>()
> /Users/da/Dev/Python/Debugger/ex_debugging.py(2)<module>()
-> def add_num(num1, num2):
-   To see next step use n or next
(Pdb) next
> /Users/da/Dev/Python/Debugger/ex_debugging.py(11)<module>()
-> if __name__ == '__main__':
-   Just enter automatically use next or last command has been entered:
(Pdb) 
> /Users/ad/Dev/Python/Debugger/ex_debugging.py(12)<module>()
-> num1 = input('Enter number 1: ')
- Use help again
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb
-   Now use continue commands bring us to enter the numbers:
(Pdb) continue
Enter number 1: 3
Enter number 2: 4
34
The program finished and will be restarted
> /Users/da/Dev/Python/Debugger/ex_debugging.py(2)<module>()
-> def add_num(num1, num2):
(Pdb) n
> /Users/da/Dev/Python/Debugger/ex_debugging.py(54)<module>()
-> if __name__ == '__main__':
(Pdb) 
> /Users//Dev/Python/Debugger/ex_debugging.py(55)<module>()
-> num1 = input('Enter number 1: ')
(Pdb) n
Enter number 1: 3
> /Users//Dev/Python/Debugger/ex_debugging.py(56)<module>()
-> num2 = input('Enter number 2: ')
(Pdb) print(num1)
3
(Pdb) n
Enter number 2: 4
> /Users//Dev/Python/Debugger/ex_debugging.py(57)<module>()
-> result = add_num(num1, num2)
(Pdb) print(num2)
4
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) whatis num1
<class 'str'>
(Pdb) whatis num2
<class 'str'>
# Because we have not define what type of number enter automatically take as string
(Pdb) step
--Call--
> /Users/da/Dev/Python/Debugger/ex_debugging.py(2)add_num()
-> def add_num(num1, num2):
(Pdb) n
> /Users/da/Dev/Python/Debugger/ex_debugging.py(3)add_num()
-> sum = num1 + num2
(Pdb) n
> /Users/da/Dev/Python/Debugger/ex_debugging.py(4)add_num()
-> return sum
(Pdb) c
34
The program finished and will be restarted
> /Users/da/Dev/Python/Debugger/ex_debugging.py(2)<module>()
-> def add_num(num1, num2):
# The issue is the input not define what type to enter we have to add int in front of input to
# fixe the issues
we use break linenumber 122 to stop the script at the line of result then use whatis result and use q 
to exit from (pdp) shell
Debugger % python -m pdb ex_debugging.py
> /Users/dilshadabdulla/Dev/Python/Debugger/ex_debugging.py(2)<module>()
-> def add_num(num1, num2):
(Pdb) break 10
Breakpoint 1 at /Users/dilshadabdulla/Dev/Python/Debugger/ex_debugging.py:10
(Pdb) c
Enter number 1: 23
Enter number 2: 31
> /Users/dilshadabdulla/Dev/Python/Debugger/ex_debugging.py(10)<module>()
-> print(total)
(Pdb) whatis total
<class 'int'>

'''

def add_num(num1, num2):
    sum = num1 + num2
    return sum

if __name__ == '__main__':
    # num1 = input('Enter number 1: ') # before
    num1 = int(input('Enter number 1: ')) # after
    # num2 = input('Enter number 2: ') # before
    num2 = int(input('Enter number 2: ')) # after
    x = add_num(num1, num2)
    print(x)

# Use import pdb : stand for Python debugger

# This is a breakpoint to exame the code : pdb.set_trace() 