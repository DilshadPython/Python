# using int
https://docs.python.org/3/library/functions.html#int

the definition of int in the class
class int(x, base=10) this is the

The str in the class find in
https://docs.python.org/3/library/stdtypes.html#str

the definition of str in the class
class str(object="")

str.lower()
str.strip([chars])

using list https://docs.python.org/3/library/stdtypes.html#list

class list([iterable])

list.append(x)

using tuple https://docs.python.org/3/library/stdtypes.html#tuple
class tuple([iterable])

using dict https://docs.python.org/3/library/stdtypes.html#dict
class dict(**kwargs)


for more details look at all https://docs.python.org/3/library/stdtypes.html

py type.py
Numbers:
<class 'int'>
<class 'float'>
Booleans:
<class 'bool'>
<class 'bool'>
<class 'bool'>
None
<class 'NoneType'>
Strings:
<class 'str'>
Data Type in Python
<class 'list'>
<class 'list'>
<class 'tuple'>
<class 'tuple'>
<class 'dict'>
<class 'dict'>

# Class methods https://docs.python.org/3/library/stdtypes.html#methods
class C:
    def method(self):
        pass

@classmethod this class methods has not access to self args in the class but it knows what is in the class

when we use @classmethod we have to remove the __init__() and change all self in the class to cls look at this example
classmethods.py  for training purpose

 py clssmethods.py
This full name is Tony  is live in  London
/home/OOProgrammingH/Type$ py clssmethods.py
This full name is Tony  is live in  New York

