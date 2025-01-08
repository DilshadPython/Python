# What is the key feature of Python?
    1. Object-orinted
    2. Concise and simple
    3. Dynamically-typed
    4. Large community
    5. Free
    6. Interpreted, This is mean in python terminal you can compile your code directly.

# How many keywords are built-in in Python?
- 35 Keywords are in built-in
    [and , as, assert, break, class, continue, def, del, elif, else, except, exec, False, finally, for,
     from, global, if, import, in , is, lambda, None, nonlocal, not, or, pass, print, raise, return, True
     try, while, with, yield ]

# How long can an identifier be in Python?
- According python documentation can be any length but PEP 8 suggests maximum 79 characters  

# Is Python Case-sensitive?
- Yes its see examples:
  - >>> yourname = 'Tomy'
    >>> Yourname 
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'Yourname' is not defined    

# What is indices in List?
- books = ['Data Science', 'Biology', 'Chimiches', 'Python Tutorials', 'Django projects']
  - >>> books = ['Data Science', 'Biology', 'Chimiches', 'Python Tutorials', 'Django projects']
    >>> books[-2]
    'Python Tutorials'
  - Example of slicing:
    - >>> books[-5 : -2]
      ['Biology', 'Chimiches', 'Python Tutorials']
    >>> books[2 : 4]
      ['Chimiches', 'Python Tutorials']

# What is the Differentiate between lists and tuples?
- List is mutable where tuple is immutable (you can change index in the list but not in tuple)
  >>> books = ('Biology', 'Chimiches', 'Python Tutorials', 'Django projects', 'Java')
  >>> books
  ('Biology', 'Chimiches', 'Python Tutorials', 'Django projects', 'Java')
  >>> books[2] = 'Mathmatics' 
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
  >>> books = ['Biology', 'Chimiches', 'Python Tutorials', 'Django projects', 'Java']
  >>> books
  ['Biology', 'Chimiches', 'Python Tutorials', 'Django projects', 'Java']
  >>> books[2] = 'Mathmatics'
  >>> books
  ['Biology', 'Chimiches', 'Mathmatics', 'Django projects', 'Java']

# The is the three piller of OO in Python?
- Encapsulation
- Inheritance
- Polymorphism

# What makes Python object oriented?
- Encapsulation
- Abstracction
- Inheritance
- Polymorphism
- Data hiding

# How many types of objects Python support?
-    There are two types Mutable objects like[] List and Immutable object like Tupe()

# What is the different between single underscore _ and double underscroe __ in python?

# What is Genarator?

# What is Iterator?

# What is the difference between .pyc and .py file?

# How can you declare a multiple assignments in one statment?
- Option one:
  - >>> a, b, c, d = 3, 6, 11, 9
    >>> a
    3
    >>> b
    6
    >>> c
    11
    >>> d 
    9
- Option two:
- >>> a = b = c = 77
    >>> a
    77
    >>> b
    77
    >>> c
    77

# How many arguments can used in range() function?
- range() function can take up to 3 arguments:
  - Range with one argument:
    >>> list(range(7))
    [0, 1, 2, 3, 4, 5, 6]
    >>> tuple(range(8))
    (0, 1, 2, 3, 4, 5, 6, 7)
  - Range with two arguments: The first argument is where started the second is where finished.
    - >>> tuple(range(2, 10))
    (2, 3, 4, 5, 6, 7, 8, 9)
    >>> list(range(1, 10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
  - Range with three arguments: First argument start, second ended and the third is the step value.
    - >>> list(range(1, 10, 2))
   [1, 3, 5, 7, 9]
   >>> tuple(range(2, 10, 3))
   (2, 5, 8)

# What is PEP 8?

# How do you display firstname & surname of all university students, which data type more useful to use?
- The data type to use is dictionary here is some examples:
  - >>> stdn_names = {'fname': 'Thomas', 'sname': 'Andrew'}
  >>> print(stdn_names)
  {'fname': 'Thomas', 'sname': 'Andrew'}
  >>> print(stdn_names.keys(), ' = ', stdn_names.values())
  dict_keys(['fname', 'sname'])  =  dict_values(['Thomas', 'Andrew'])

# Create a list of number string convert to list of number as integer? 
- >>> numbers = ['2', '76', '14', '9', '25']
  >>> numbers
  ['2', '76', '14', '9', '25']
  >>> [int(x) for x in numbers]
  [2, 76, 14, 9, 25]

# What is swapcase() does in python?
- swapcase() is a method can swap upper and lower char in string example:
  - >>> full_name = 'Dilshad Abdulla'
  >>> full_name.swapcase()
  'dILSHAD aBDULLA'

# How to find out the values in the dictionary or how to test it?
- >>> stdn_names = {'fname': 'Thomas', 'sname': 'Andrew', 'fname': 'Julie', 'sname': 'Smith'}
  >>> 'sname' in stdn_names.values()
  False
  >>> 'Julie' in stdn_names.values()
  True

# What is the list Comprehension in Python?
- It's one line of codes use for loop and list example:
  - >>> [x for x in range(1, 21, 3)]
   [1, 4, 7, 10, 13, 16, 19]

# Python reserved keywords
  Flase,
  True,
  Class,
  return,
  is,
  in,
  finally,
  None,
  if,
  elif,
  else,
  for,
  lambda,
  continue,
  def,
  from,
  while,
  nonlocal,
  and,
  del,
  global,
  not,
  with,
  as,
  try,
  or,
  yield,
  assert,
  import,
  pass,
  break,
  except,
  raise

# INFO
  x = 4      Assignment statment
  x = x + 7  Assignment with expression

#
#
#
#
#
#
#
#
#
#
#
#
#
#