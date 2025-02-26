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

https://docs.python.org/3/howto/

using set in OOP https://docs.python.org/3/library/stdtypes.html#set

append() is used for a list where add() is used for a set
Using set in the list of dict but it take only thoes not are not duplicate in the name model and year but when we use zip() is only to collect all on one in this case each models of the car doesn't match the current car. Only for experiences how zip work.
