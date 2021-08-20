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
#
#