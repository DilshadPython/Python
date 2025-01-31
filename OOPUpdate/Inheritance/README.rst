https://docs.python.org/3/library/exceptions.html


Exception hierarchy

The class hierarchy for built-in exceptions is:

BaseException
  +── KeyboardInterrupt
  +── Exception
      +── ArithmeticError
      │    +── ZeroDivisionError
      +── AssertionError
      +── AttributeError
      +── BufferError
      +── EOFError
      +── ImportError
      │    +── ModuleNotFoundError
      +── LookupError
      │    +── KeyError
      +── MemoryError
      +── SyntaxError
      │    +── IndentationError
      +── ValueError

#####
In  cars.py we created a list of dictionary and made some difference for loops
first one display all list of dictionary without repeat any duplicated name
The other for loops display names except duplicate than models and years this is without using set()