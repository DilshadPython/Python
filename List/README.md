### List: lists are Mutable can be change.
>>> car_list = ['Audi', 'BMW', 'Mercedes']
>>> # if we try to change the M in 2 elements in the list to lower case using index function \
... car_list[2] = 'mercedes' that doesn't work that is why we cal not mutable but we can use \
... lower() function to make all lowercase.

Python: python2.7
Python 2.7.10 (default, Feb 22 2019, 21:55:15) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> cars = ['Audi', 'BMW', 'VW']
>>> cars
['Audi', 'BMW', 'VW']
>>> cars[0] = 'audi'
>>> cars
['audi', 'BMW', 'VW']
>>> cars[0] = 'hello'
>>> cars
['hello', 'BMW', 'VW']

In python3.7 you can change the string in the list without using lower() function:
>>> car_list = ['Audi', 'BMW', 'Mercedes']
>>> car_list
['Audi', 'BMW', 'Mercedes']
>>> car_list[0] = 'audi'            
>>> car_list
['audi', 'BMW', 'Mercedes']
>>> car_list[1] = 'VW'
>>> car_list
['audi', 'VW', 'Mercedes']

### Sort

#### Help on method_descriptor:

sort(...)
    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
    	   key = sorting function


### reverse = False ==> Sort in ascending order
### reverse = True ==> Sort in descending order

#### 'in-place' Algorithm 
##### Does not create a secomd data structure
##### Modifies input/existing structure

### list.sort() changed the list
### Q: can we create a sorted copy?
### Q: how we sort a tuple
### A: for all above we use sorted() method